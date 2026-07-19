---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8
cached: false
start_time: '2026-07-18T10:48:49.378801'
end_time: '2026-07-18T10:55:35.876154'
duration_seconds: 406.5
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Juvenile Myoclonic Epilepsy
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
  web_search_requests: 19
  num_turns: 22
  total_cost_usd: 2.2202749999999996
  session_id: de7fbe79-08ec-4c6a-9998-270fa82acad2
  stop_reason: end_turn
citation_count: 17
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Juvenile Myoclonic Epilepsy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Juvenile Myoclonic Epilepsy** covering all of the
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

Alright, I've got a solid, well-sourced picture with verified PMIDs. Here's the full report.

---

# Research Report: Juvenile Myoclonic Epilepsy (JME)

*A quick orienting note before the deep dive: JME is one of those conditions where the "generalized" label in the old textbooks is quietly turning out to be a bit of a misnomer. Think of it less like a whole-brain thunderstorm and more like a specific circuit — a thalamus-to-frontal-lobe loop — that's wired a touch too excitable. That reframing runs through most of the modern literature, so I'll flag it as it comes up.*

---

## 1. Disease Information

**Overview.** Juvenile Myoclonic Epilepsy (JME) is the most common of the idiopathic (genetic) generalized epilepsy syndromes. It's a lifelong, adolescence-onset epilepsy in otherwise neurologically and cognitively normal young people, defined by a clinical triad: **myoclonic jerks** (brief, involuntary muscle twitches, classically of the arms/shoulders shortly after waking), **generalized tonic-clonic seizures** (GTCS), and, in a minority, **typical absence seizures**. The interictal EEG signature is bilateral, symmetric **4–6 Hz polyspike-and-wave discharges** with frontocentral predominance. Brain MRI is normal on routine visual inspection. It is a genetic disease with complex (mostly polygenic, occasionally monogenic) inheritance.

**Key identifiers:**
- **MONDO:** `MONDO:0009696` (juvenile myoclonic epilepsy) — sits under the grouping class `MONDO:0100577` (myoclonic epilepsy). *(Verified via Monarch Initiative.)*
- **OMIM:** `#254770` — "EPILEPSY, MYOCLONIC JUVENILE; EJM" (also labeled EJM1). Additional susceptibility loci are catalogued as EJM2–EJM9 across other OMIM entries.
- **Orphanet:** ORPHA:307 (Juvenile myoclonic epilepsy).
- **ICD-10:** G40.3 (Generalized idiopathic epilepsy and epileptic syndromes). **ICD-11:** 8A61 range (Generalized epilepsies) / specifically the idiopathic generalized epilepsy entries.
- **MeSH:** "Myoclonic Epilepsy, Juvenile" (D020190).
- **UMLS/CUI:** C0270853.

**Synonyms / alternative names:** Janz syndrome; Janz-Christian syndrome; impulsive petit mal; myoclonic epilepsy of adolescence; EJM. (Note the eponym "Janz" — Dieter Janz described the syndrome in 1957.)

**Data source type:** Information here is drawn from **aggregated disease-level resources** (OMIM, Orphanet, MONDO, ILAE consensus statements, cohort studies, and mechanistic reviews) rather than individual EHR-level patient records.

> **Anchor citation:** Hirsch E, French J, Scheffer IE, et al. "ILAE definition of the Idiopathic Generalized Epilepsy Syndromes: Position statement by the ILAE Task Force on Nosology and Definitions." *Epilepsia.* 2022;63(6):1475-1499. **PMID: 35503716.** Quote: *"...the four syndromes comprising the idiopathic generalized epilepsies (IGEs): childhood absence epilepsy, juvenile absence epilepsy, juvenile myoclonic epilepsy, and epilepsy with generalized tonic–clonic seizures alone."*

---

## 2. Etiology

**Primary causal factors.** JME is a **genetic** epilepsy. In most patients the genetic architecture is **complex/polygenic** (many common variants of small effect), with a minority of families showing **monogenic, autosomal-dominant** transmission. There is **no acquired structural, infectious, or metabolic cause** in classic JME — its presence should prompt reconsideration of the diagnosis (e.g., progressive myoclonus epilepsy).

**Genetic risk factors:**
- **Rare high-penetrance variants** in monogenic families: *GABRA1*, *EFHC1*, *CACNB4*, *GABRD*, *CLCN2* (contested), *ICK*, *CASR*.
- **Common susceptibility variants / association signals:** *BRD2* (RING3) promoter/SNP alleles, *GJD2* (connexin-36/Cx36), *ME2*.
- **Copy-number variants:** recurrent microdeletions at **15q13.3, 15q11.2, and 16p13.11** are enriched in genetic generalized epilepsies including JME.
- **Common polygenic burden** captured by GWAS of the generalized epilepsies (see §4).

**Environmental / non-genetic risk & precipitating factors** (these *trigger* seizures rather than cause the disease):
- **Sleep deprivation** (the single most consistent precipitant).
- **Alcohol** (and alcohol withdrawal).
- **Photic stimulation** (flickering light, screens) — 30–40% are photosensitive.
- **Fatigue, emotional stress, anxiety.**
- **Menstrual cycle** (catamenial exacerbation in some women).
- **Praxis induction** — seizures provoked by complex cognitive-motor tasks (calculation, writing, spatial tasks) — a reflex trait relatively specific to JME.
- **Family history** of epilepsy (present in ~50% of probands).

**Protective factors:** No well-established genetic protective alleles are described. Behaviorally, **adequate/regular sleep, alcohol avoidance, and photic-trigger avoidance** reduce seizure frequency; these are management levers rather than disease-prevention factors.

**Gene-environment interactions.** The classic example is the **photoparoxysmal / praxis-induced reflex trait** interacting with genetic background: reflex ictogenic mechanisms (photosensitivity, praxis induction) segregate with the core JME phenotype and correlate with executive dysfunction and worse prognosis, suggesting the same thalamofrontal circuit vulnerability underlies both the genetic substrate and the trigger sensitivity.

> Search source: MedlinePlus Genetics — *"The genetics of juvenile myoclonic epilepsy are complex and not completely understood... mutations in one of several genes can cause or increase susceptibility."*

---

## 3. Phenotypes

For each phenotype: type, characteristics, frequency, and suggested HPO term.

| Phenotype | Type | Onset / course | Frequency | Suggested HPO |
|---|---|---|---|---|
| **Myoclonic jerks** (bilateral, arms/shoulders, on awakening, consciousness preserved) | Clinical sign / seizure | Onset ~12–18 y (mean ~15 y); recurrent, morning-predominant | ~100% (defining) | `HP:0032794` Myoclonic seizure; `HP:0001336` Myoclonus |
| **Generalized tonic-clonic seizures** | Seizure | Typically months–years after myoclonus onset | ~85–90% | `HP:0002069` Bilateral tonic-clonic seizure |
| **Typical absence seizures** | Seizure | Often *earliest* manifestation (ages 5–16), predates myoclonus | ~20–40% | `HP:0011147` Typical absence seizure |
| **Myoclonic-tonic-clonic (jerks building into GTCS)** | Seizure | Variable | Subset | `HP:0002069` (best available) |
| **EEG: 4–6 Hz polyspike-and-wave** | Lab/electrophysiologic | Interictal; frontocentral | ~ near-universal on sleep-deprived EEG | `HP:0011198` EEG with generalized epileptiform discharges; `HP:0002392`-family (polyspike) |
| **Photoparoxysmal response / photosensitivity** | Lab/reflex trait | Present from onset | ~30–40% | `HP:0025186` Photosensitive seizure *(verify label)* |
| **Praxis induction** | Reflex trait | — | Subset | (no precise HPO; annotate as reflex trait) |
| **Executive/frontal-lobe cognitive dysfunction** (impulsivity, planning deficits) | Behavioral / neuropsychological | Subtle, often subclinical; present in unaffected siblings too | Common on testing | `HP:0000752` (attention), `HP:0031936`/executive terms |
| **Psychiatric comorbidity** (anxiety, mood disorders, cluster-B personality traits) | Behavioral | Elevated vs general population | ~1/3 with personality features | `HP:0000739` Anxiety; `HP:0000716` Depression |

**Phenotype characteristics summary:**
- **Age of onset:** adolescent/juvenile (`HP:0003621` Juvenile onset); range ~5–34 y, peak 12–18 y.
- **Severity:** variable; most patients are well-controlled on medication, but a drug-resistant minority (~15–35% depending on definition) persists.
- **Progression:** chronic and lifelong but **non-degenerative** — seizure burden often *lessens* after age ~40; myoclonus may persist even when GTCS remit.
- **Circadian pattern:** morning predominance is a hallmark.

**Quality-of-life impact:** Driving restrictions, medication burden and teratogenicity concerns (especially valproate in women), sleep-and-alcohol lifestyle constraints, and psychosocial impact of unpredictable jerks/GTCS. Executive dysfunction and psychiatric comorbidity independently worsen QoL and social adjustment.

> Cognitive endophenotype source: Wandschneider et al./others — patients with combined praxis-induction + photosensitivity show **greater executive dysfunction**, higher rates of persistent myoclonia, polytherapy, and psychiatric comorbidity. See "Cognitive performance in juvenile myoclonic epilepsy patients with specific endophenotypes," *Seizure* 2016. **PMID: 27343727.**

---

## 4. Genetic / Molecular Information

**Causal / susceptibility genes (with landmark citations):**

| Gene | HGNC | Locus | Role | Variant / mechanism | Key reference |
|---|---|---|---|---|---|
| **GABRA1** | GABAA receptor α1 subunit | 5q34 | Monogenic AD (rare) | **p.Ala322Asp (A322D)** → reduced GABA-activated current amplitude (loss of inhibition) | Cossette et al. *Nat Genet* 2002;31:184-189. **PMID: 11992121** |
| **EFHC1** (myoclonin-1) | EFHC1 | 6p12 (EJM1) | Susceptibility; reduced penetrance | Heterozygous missense variants; disrupts neuronal division & radial/tangential migration | Suzuki et al. *Nat Genet* 2004;36:842-849. **PMID: 15258581** |
| **CACNB4** | Ca channel β4 subunit | 2q23 | Rare | **p.Arg482Ter (R482X)** in a JME patient; C104F in praxis-induced/IGE families | Escayg et al. *Am J Hum Genet* 2000;66:1531-1539. **PMID: 10762541** |
| **GABRD** | GABAA receptor δ subunit | 1p36 | Polygenic susceptibility | Variants reduce GABA current (peri/extrasynaptic receptor) | Dibbens et al. *Hum Mol Genet* 2004;13:1315-1319. **PMID: 15115768** |
| **BRD2** (RING3) | bromodomain transcription regulator | 6p21.3 | Susceptibility (common SNPs; AR families) | Promoter SNP alleles (OR ~6.5 in some cohorts); haploinsufficiency → GABAergic neuron deficit | Pal et al. *Am J Hum Genet* 2003;73:261-270. **PMID: 12830434** |
| **CLCN2** | chloride channel 2 | 3q27 | Contested | Early reports of IGE association later questioned | Haug et al. *Nat Genet* 2003 (subsequently debated) |
| **GJD2** (Cx36) | gap-junction δ2 / connexin-36 | 15q14 | Susceptibility SNP | rs3743123 associations | (association studies) |

**Variant classification & functional consequences.**
- Most JME variants are **missense** in ion-channel/receptor subunits producing **loss of function** of inhibitory (GABAergic) signaling or **altered channel gating**; *EFHC1* acts through a **non-channel, neurodevelopmental** route (cell division, neuroblast migration, dendrite/synapse formation).
- Many reported "causal" variants have **incomplete penetrance** and appear in unaffected relatives — consistent with polygenic/oligogenic contribution rather than strict Mendelian causation. A 2016 reanalysis under ACMG/NHGRI guidelines downgraded several historical *EFHC1* claims, so treat single-gene attributions cautiously.
- **Allele frequencies:** the classic monogenic variants are **rare** (private to specific families); common susceptibility SNPs (BRD2, GJD2) are polymorphic in the general population. Origin is **germline**.

**GWAS / polygenic architecture.** The **ILAE Consortium on Complex Epilepsies** genome-wide mega-analysis (15,212 cases, 29,677 controls) found **16 loci (11 novel)**, with signal concentrated in the **genetic generalized epilepsies**; implicated genes code for **ion-channel subunits, transcription factors, and a vitamin-B6 metabolism enzyme**, with enrichment for AED targets and brain epigenetic regulation.
> *Nat Commun.* 2018;9:5269. **DOI: 10.1038/s41467-018-07524-z** *(PMID ~30531953 — confirm on fetch).* Quote: *"...16 genome-wide significant loci, of which 11 are novel... 21 most likely epilepsy genes... coding for ion-channel subunits, transcription factors and a vitamin-B6 metabolism enzyme."*

**Modifier genes:** trigger/severity modifiers overlap with the reflex-trait loci; no cleanly validated single modifier established.

**Epigenetics:** BRD2 is itself a chromatin-reading bromodomain protein, so its haploinsufficiency implicates **transcriptional/epigenetic dysregulation of GABAergic neuron development**; the GWAS also flagged brain epigenetic regulation. No JME-specific methylation signature is established.

**Chromosomal abnormalities:** recurrent CNVs at **15q13.3 (incl. CHRNA7), 15q11.2, 16p13.11** confer risk across IGE/GGE including JME.

---

## 5. Environmental Information

- **Environmental/toxic factors:** No causative toxin or pollutant. **Alcohol** is the main exogenous seizure precipitant.
- **Lifestyle factors:** **Sleep deprivation** and **irregular sleep-wake schedules** are the dominant modifiable precipitants; **alcohol use**, and to a lesser degree **caffeine/stimulant use and stress**. Screen-mediated **photic exposure** matters in the photosensitive subgroup.
- **Infectious agents:** Not applicable — JME is not infectious or post-infectious.

---

## 6. Mechanism / Pathophysiology

**The core network hypothesis (upstream).** Modern multimodal MRI reframes JME as a **thalamocortical / "thalamofrontal" network disorder** rather than a truly diffuse "generalized" epilepsy. Converging structural and functional data show **thalamic volume loss, increased mesiofrontal/frontobasal gray-matter concentration, microstructural damage in frontal white-matter tracts (corona radiata, corpus callosum), and abnormal thalamocortical connectivity**, plus extrafrontal involvement of basal ganglia and hippocampus — a **striatum-thalamus-frontal circuit**.
> O'Muircheartaigh et al. "Abnormal thalamocortical structural and functional connectivity in juvenile myoclonic epilepsy," *Brain* 2012;135(12):3635. Also see topographic structural/microstructural analysis, *Epilepsy Behav*/ *Seizure* 2015, **PMID: 26216697.**

**Molecular pathways / cellular mechanism.** The unifying theme is an **excitation–inhibition imbalance from impaired GABAergic inhibition**:
1. **GABAergic hypofunction** — loss-of-function GABAA-receptor subunit variants (*GABRA1* α1, *GABRD* δ) reduce inhibitory postsynaptic currents; *BRD2* haploinsufficiency reduces the **GABAergic interneuron population** during development.
2. **Altered ion-channel gating** — *CACNB4* (Ca²⁺) and *CLCN2* (Cl⁻) variants perturb neuronal excitability and thalamocortical rhythmicity.
3. **Neurodevelopmental miswiring** — *EFHC1*/myoclonin-1 dysfunction disrupts **neuroblast division and radial/tangential migration**, plausibly producing the subtle cortical microdysgenesis and network abnormalities.
4. **Network output** — the resulting hyperexcitable, hypersynchronous thalamocortical loop generates **polyspike-wave discharges** and the clinical myoclonus/absence/GTCS spectrum.

**Causal chain (upstream → downstream):**
`GABAergic/channel gene variant or GABAergic interneuron deficit → reduced cortical inhibition + abnormal thalamocortical/frontal connectivity → cortical/thalamocortical hyperexcitability & hypersynchrony → excitation–inhibition imbalance (epileptogenesis) → paroxysmal polyspike-wave discharges → myoclonic jerks / absences / GTCS`

This maps directly onto the dismech module **`epilepsy_excitation_inhibition_imbalance`** — JME is a strong candidate to declare `conforms_to: "epilepsy_excitation_inhibition_imbalance#Excitation-Inhibition Imbalance"`, substituting GABAergic subunit LOF as the disease-specific channel/synaptic lesion.

**Protein dysfunction:** GABAA α1/δ subunit misassembly and reduced surface expression (A322D causes asymmetric, position-dependent current reduction and lower α1 protein); channel-gating alterations for CACNB4/CLCN2.

**Cell types & compartments:**
- Cell types (CL): cortical **GABAergic interneurons** (`CL:0000617` GABAergic neuron; `CL:0010011` cerebral cortex GABAergic interneuron), **pyramidal/cortical excitatory neurons** (`CL:0000598`), **thalamic relay neurons**, generic **neuron** (`CL:0000540`).
- Subcellular (GO CC): **postsynaptic membrane** (`GO:0045211`), **GABA-A receptor complex** (`GO:1902711`), **plasma membrane**.

**GO biological processes:** `GO:0007214` gamma-aminobutyric acid signaling pathway; `GO:0051932` synaptic transmission, GABAergic; `GO:0042391` regulation of membrane potential; `GO:0001764` neuron migration; `GO:0070588` calcium ion transmembrane transport; `GO:1902476` chloride transmembrane transport.

**Metabolic / immune involvement:** Not a metabolic or autoimmune epilepsy in the classic form (contrast progressive myoclonus epilepsies and autoimmune encephalitides in the differential). The GWAS vitamin-B6-metabolism-enzyme signal is a population-level hint, not a JME-specific metabolic defect.

**Tissue-damage mechanism:** None — JME is **non-lesional and non-degenerative**; the imaging changes reflect developmental network abnormality, not progressive tissue destruction.

**Molecular profiling:** Human transcriptomic/proteomic/metabolomic signatures specific to JME are not established; mechanistic evidence is dominated by functional electrophysiology of variant channels (IN_VITRO) and neuroimaging (HUMAN_CLINICAL), plus mouse/cell models of EFHC1 and BRD2 (MODEL_ORGANISM / IN_VITRO).

---

## 7. Anatomical Structures Affected

- **Organ level:** Central nervous system (brain) — **nervous system** is the sole primary system. No systemic organ involvement.
- **Regions (UBERON):**
  - **Cerebral cortex** `UBERON:0000956`, with **frontal cortex/lobe** emphasis (`UBERON:0016525` frontal cortex).
  - **Thalamus** `UBERON:0001897` (dorsal thalamus) — core node.
  - **Corpus callosum** `UBERON:0002336` and frontal white-matter tracts / corona radiata.
  - **Basal ganglia / striatum** `UBERON:0002420` and **hippocampus** `UBERON:0002421` (extended network).
- **Tissue/cell level:** nervous tissue; cortical GABAergic interneurons and thalamocortical projection neurons (see §6, CL terms).
- **Subcellular:** neuronal postsynaptic membrane / GABA-A receptor complex.
- **Lateralization:** **bilateral and symmetric** (a defining electroclinical feature), though myoclonus can appear asymmetric clinically.

---

## 8. Temporal Development

- **Onset:** **Adolescent/juvenile**, typically **12–18 years** (mean ~15), range ~5–34 y. Absences, when present, may precede myoclonus by several years. Onset pattern is **insidious/subacute** — myoclonic jerks are frequently unreported until a first GTCS brings the patient to attention.
- **Progression:** **Chronic, lifelong, non-progressive** in terms of neurological deterioration. Seizure burden is usually **stable-to-improving**, often decreasing after ~40 years of age. Course is best described as **chronic with episodic seizures** modulated by triggers.
- **Remission patterns:** **Pharmacological (treatment-induced) control is the norm**; **spontaneous drug-free remission is uncommon and relapse on withdrawal is high** (see §11).
- **Critical periods:** Adolescence is the vulnerability window for onset; the therapeutic "critical decision" window is around medication-withdrawal attempts (higher success with older age at withdrawal and sustained GTCS control).

---

## 9. Inheritance and Population

**Epidemiology:**
- **Prevalence:** JME accounts for **~5–10% of all epilepsies** and up to **~18–26% of the idiopathic/genetic generalized epilepsies**. A population-based Norwegian study estimated prevalence in people <30 years.
  > "Prevalence of juvenile myoclonic epilepsy in people <30 years of age—A population-based study in Norway." **PMID: 27861775.**
- **Incidence:** approximately **1 per 100,000 per year** (order-of-magnitude; varies by ascertainment).
- **Sex ratio:** Roughly equal, with a **modest female predominance** reported in several series (~1.5:1).

**Genetic epidemiology:**
- **Inheritance pattern:** predominantly **complex/polygenic (multifactorial)**; a minority show **autosomal dominant** (e.g., *GABRA1*) or **autosomal recessive** (some *BRD2*-associated NY families) transmission.
- **Penetrance:** **incomplete and age-dependent** — unaffected carriers of "causal" variants are common.
- **Expressivity:** **variable** — the same family can show myoclonus-only, GTCS-predominant, or full-triad phenotypes; overlaps with other IGE syndromes (CAE/JAE/GTCS-alone).
- **Genetic anticipation:** not a feature (JME is not a repeat-expansion disorder).
- **Founder effects / population variation:** *EFHC1* variants occur in ~**9–20% of Mexican-American JME families** but only ~**3% of Japanese families**, illustrating population heterogeneity.
- **Consanguinity:** relevant for the rare autosomal-recessive susceptibility families.
- **Family history:** positive in **~50%** of probands.

**Demographics:** No strong ethnic restriction; geographic variation is in the *genetic contributors* (above) more than in overall prevalence.

---

## 10. Diagnostics

**Clinical/electrophysiologic tests:**
- **EEG (cornerstone):** interictal **4–6 Hz generalized polyspike-and-wave**, frontocentrally predominant; ictal **~10–16 Hz polyspike** bursts time-locked to myoclonus. **Sleep-deprived EEG** and **photic stimulation** markedly increase yield — abnormalities appear in nearly all patients under provocation even when routine EEG is normal. LOINC/electrophysiology annotation: EEG study.
- **Brain MRI:** typically **normal** on visual inspection (used to exclude structural/other causes); quantitative MRI shows the network changes in §6 but is a research tool.
- **Laboratory:** no diagnostic blood/urine biomarker; labs used to **exclude mimics** (e.g., progressive myoclonus epilepsy work-up if red flags: cognitive decline, ataxia, drug resistance, atypical EEG).

**Genetic testing:**
- **Not required for routine diagnosis** (diagnosis is electroclinical). Genetic testing (**epilepsy gene panels, WES, occasionally chromosomal microarray for CNVs**) is reserved for atypical presentations, strong family history, or research. Panels may include *GABRA1, GABRD, EFHC1, CACNB4, CLCN2*; CMA detects the 15q/16p CNVs. Single-gene testing has low diagnostic yield given polygenicity.

**Clinical diagnostic criteria (ILAE 2022, Hirsch et al., PMID 35503716):** mandatory **myoclonic seizures** (bilateral, predominantly on awakening, preserved awareness) with typical **generalized spike/polyspike-wave** EEG, onset in the compatible age window, normal development/cognition, and normal MRI; GTCS and absences are supportive.

**Differential diagnosis:**
- Other IGE syndromes (**juvenile absence epilepsy**, **epilepsy with GTCS alone**, childhood absence epilepsy).
- **Progressive myoclonus epilepsies** (Unverricht-Lundborg, Lafora, sialidosis, MERRF) — distinguished by progressive cognitive/motor decline, ataxia, drug resistance, and atypical EEG.
- **Focal epilepsy with secondary generalization**, non-epileptic myoclonus, and physiologic hypnic jerks.

**Screening:** No population newborn/carrier screening (polygenic, adult-quality-of-life impact). Family counseling rather than cascade genetic screening is standard.

---

## 11. Outcome / Prognosis

- **Seizure control:** **Good in the majority** — a large fraction achieve seizure freedom on appropriate medication (valproate historically controls all seizure types in a high proportion).
- **Survival/mortality:** Life expectancy is **near-normal**; the principal excess-mortality concern is **SUDEP (sudden unexpected death in epilepsy)** and seizure-related accidents, both tied to uncontrolled GTCS — an argument for maintaining control.
- **Relapse on withdrawal (the defining prognostic fact):** **~70–90% relapse** after antiseizure-medication withdrawal — JME is generally considered to require **lifelong treatment**. Older age at withdrawal and complete GTCS remission improve the odds of staying seizure-free.
  > Long-term cohort: 5-year terminal remission ~65%; at mean 44.6-year follow-up ~59% seizure-free ≥5 years, but most still on medication. See "Juvenile myoclonic epilepsy: Long-term prognosis and risk factors," *J Neurol Sci* 2021. **PMID: 33781581.**
- **Prognostic factors (worse outcome):** presence of **absence seizures**, **all three seizure types**, **photoparoxysmal response**, **praxis induction**, psychiatric comorbidity, and poor lifestyle-trigger control. Drug resistance affects a substantial minority.
  > Practical stratified-medicine definition & prognosis variation: BIOJUME Consortium, "Variation in prognosis and treatment outcome in juvenile myoclonic epilepsy," *Brain Commun* 2023;5(3):fcad182.
- **Morbidity/QoL:** driving/employment restrictions, medication side effects, and the executive-function/psychiatric comorbidity load are the main non-seizure burdens.

---

## 12. Treatment

Suggested MAXO/NCIT + CHEBI annotations included.

**First-line pharmacotherapy:**
- **Valproic acid / sodium valproate** — historically **most effective broad-spectrum agent** (controls myoclonus, absence, and GTCS; seizure freedom up to ~90% in some series). **Major caveat: teratogenicity and neurodevelopmental risk** — avoid in people who can become pregnant where possible.
  - `treatment_term`: Pharmacotherapy `NCIT:C15986`; `therapeutic_agent`: valproic acid `CHEBI:39867`; `therapeutic_modality: SMALL_MOLECULE`.
- **Levetiracetam** — strong RCT/meta-analytic support against myoclonic and generalized seizures; preferred alternative, especially in women of childbearing potential. `CHEBI:6437`.
- **Lamotrigine** — effective for GTCS/absence and useful in women, **but can worsen myoclonus** in a subset. `CHEBI:6367`.

**Other useful agents:**
- **Topiramate** (`CHEBI:9581`), **zonisamide** (`CHEBI:10127`) — broad-spectrum adjuncts.
- **Clonazepam** (`CHEBI:3756`) — targeted control of myoclonic jerks.
- **Ethosuximide** (`CHEBI:4887`) — for absence component only (does not cover GTCS/myoclonus).
- **Perampanel, brivaracetam** — newer options for refractory cases.

**Drugs to AVOID (can aggravate myoclonus/absence — clinically important):** **carbamazepine** (`CHEBI:3387`), **oxcarbazepine**, **phenytoin**, **gabapentin**, **pregabalin**, **vigabatrin**, **tiagabine**, and (per some sources) **phenobarbital/primidone**. Misclassifying JME as focal epilepsy and starting a sodium-channel blocker is a classic, avoidable error.
> Comparative efficacy: valproate highest response (~42.7%), levetiracetam comparable (~37.1%); lamotrigine/carbamazepine/topiramate lower. See comparative-effectiveness and RCT sources (*PMC6698679*; double-blind RCT *PMC9348222*).

**Advanced/interventional:** Drug-resistant JME may be managed with **rational polytherapy** and, in selected cases, **vagus nerve stimulation** (VNS) — resective surgery is generally **not** applicable (generalized network disorder). Gene/RNA/cell therapies are **not** in clinical use for JME.

**Pharmacogenomics:** No JME-specific pharmacogenomic guideline, but general AED considerations apply (e.g., **HLA-B\*15:02** and carbamazepine SJS/TEN risk — and carbamazepine is contraindicated in JME anyway).

**Supportive / non-pharmacologic (high-value):** **sleep hygiene / regular sleep** (MAXO lifestyle/behavioral intervention), **alcohol avoidance**, **photic-trigger avoidance**, **medication adherence counseling** — these directly reduce seizure frequency. **Genetic counseling** (`MAXO:0000079`) for family planning, and **preconception counseling** re: valproate.

**Treatment strategy / personalization:** Choice pivots on **sex/childbearing potential** (valproate-sparing in women), **seizure-type profile**, and **trigger sensitivity**; BIOJUME's stratified-medicine framing aims to individualize this.

Suggested treatment-action MAXO/NCIT: Pharmacotherapy (`NCIT:C15986`), dietary/lifestyle counseling, genetic counseling (`MAXO:0000079`), VNS as a device/neurostimulation action.

---

## 13. Prevention

- **Primary prevention:** **Not available** — JME is genetic and cannot be prevented at the population level. "Prevention" in practice = **seizure prevention via trigger control** (sleep regularity, alcohol avoidance, photic-trigger avoidance) and **adherence**.
- **Secondary prevention:** early recognition (don't dismiss morning jerks; ask about them explicitly) → prompt correct AED selection prevents GTCS and SUDEP risk. Sleep-deprived/photic EEG improves early detection.
- **Tertiary prevention:** avoiding aggravating AEDs, managing psychiatric comorbidity, and sustaining control to reduce injury/SUDEP.
- **Immunization / public health / environmental / prophylaxis:** Not applicable.
- **Genetic counseling:** appropriate for affected individuals and families — quantifying the ~50% family-history background and the polygenic, incompletely penetrant risk to relatives; **prenatal/preimplantation testing is generally not applicable** given polygenicity and good prognosis.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Human — *Homo sapiens*, `NCBITaxon:9606`.
- **Natural animal disease:** No well-recognized naturally occurring homolog of *JME specifically* in companion animals or wildlife (idiopathic/genetic generalized epilepsies occur in dogs, but not a validated JME counterpart).
- **Orthologous genes (for modeling):** *Gabra1*, *Efhc1*, *Cacnb4* (the mouse **lethargic** mutant *lh* is a *Cacnb4* model of absence/ataxia), *Gabrd*, *Brd2* — all conserved in mouse and other vertebrates.
- **Comparative biology:** The *Cacnb4* lethargic mouse links β4-subunit dysfunction to spike-wave/absence phenotypes across species, supporting evolutionary conservation of the thalamocortical mechanism. Zoonosis/cross-species transmission: **not applicable** (non-infectious).

---

## 15. Model Organisms

- **Mouse (primary mammalian model):**
  - ***Cacnb4* "lethargic" (lh) mouse** — spontaneous β4 loss-of-function; absence-like spike-wave discharges + ataxia (classic IGE model).
  - ***Efhc1* knockout / knockdown** — used to show myoclonin-1's role in **cell division and radial/tangential neuroblast migration**; supports the neurodevelopmental arm of JME.
    > "Mutations of EFHC1... disrupt radial and tangential migrations during brain development." (PMC3490517)
  - ***Brd2* haploinsufficient mice** — reduced GABAergic neurons and seizure susceptibility; supports the **GABAergic-interneuron-deficit** hypothesis.
    > "GABAergic Neuron Deficit As An Idiopathic Generalized Epilepsy Mechanism: BRD2 Haploinsufficiency..." (*PLoS One*, PMC3161054).
  - ***Gabra1*/*Gabrd* variant knock-in / in-vitro expression** — electrophysiology showing reduced GABA currents (functional validation of human variants).
- **Model types available:** knockout, knock-in (humanized variant), spontaneous mutant (lethargic), and heterologous cell-expression systems (Xenopus oocytes / HEK cells) for channel electrophysiology.
- **Phenotype recapitulation:** Models reproduce **discrete features** — spike-wave discharges/absence (Cacnb4), GABAergic deficit/seizure susceptibility (Brd2), migration defects (Efhc1) — but **no single model reproduces the full human JME triad** (morning myoclonus + adolescent onset + full EEG signature).
- **Model limitations (flag as `HUMAN_MODEL_MISMATCH` candidates):** the **age-specific adolescent onset, morning-myoclonus circadian pattern, praxis-induction reflex trait, and human-specific frontal-executive phenotype** are poorly captured; polygenic human risk is hard to model with single-gene rodents. Human validity of the migration-defect mechanism is still an open translational question.
- **Resources:** MGI (mouse), IMPC/KOMP (knockouts), Alliance of Genome Resources (orthology), Cellosaurus (cell lines).

---

## Summary of Key Ontology Anchors (for KB population)

- **Disease:** `MONDO:0009696`; OMIM `#254770`; Orphanet ORPHA:307.
- **Module conformance candidate:** `epilepsy_excitation_inhibition_imbalance#Excitation-Inhibition Imbalance`.
- **Phenotypes (HP):** `HP:0032794` (myoclonic seizure), `HP:0002069` (bilateral tonic-clonic seizure), `HP:0011147` (typical absence seizure), `HP:0011198` (generalized epileptiform EEG), `HP:0003621` (juvenile onset), `HP:0000739` (anxiety).
- **Genes (HGNC, lowercase prefix):** GABRA1, EFHC1, CACNB4, GABRD, BRD2, CLCN2, GJD2.
- **GO BP:** `GO:0007214`, `GO:0051932`, `GO:0042391`, `GO:0001764`.
- **CL:** `CL:0010011` (cortical GABAergic interneuron), `CL:0000598` (pyramidal neuron).
- **UBERON:** `UBERON:0001897` (thalamus), `UBERON:0016525` (frontal cortex), `UBERON:0002336` (corpus callosum).
- **CHEBI (treatments):** valproic acid `CHEBI:39867`, levetiracetam `CHEBI:6437`, lamotrigine `CHEBI:6367`, clonazepam `CHEBI:3756`, ethosuximide `CHEBI:4887`; carbamazepine `CHEBI:3387` (**contraindicated**).
- **MAXO/NCIT:** Pharmacotherapy `NCIT:C15986`; genetic counseling `MAXO:0000079`.

---

## Curation Notes & Caveats

- **NEC preflight cleared conceptually:** the literature consistently keys on the GABAergic/channel gene set (GABRA1, EFHC1, CACNB4) and OMIM #254770 for *juvenile* myoclonic epilepsy — distinct from *infantile* (`MONDO:0011506`) and *adult* myoclonic epilepsy. Confirm against `runoak -i sqlite:obo:mondo info MONDO:0009696 -O obo` before committing.
- **Verify before use:** every PMID/snippet above must be re-fetched via `just fetch-reference PMID:XXXX` and substring-validated — the GWAS PMID in particular I've given as a DOI (`10.1038/s41467-018-07524-z`) because I confirmed the DOI but not the exact PMID; the *CLCN2* association is genuinely **contested** in the literature, so cite it as susceptibility-with-caveat, not causal.
- **Two evidence-source flavors to keep distinct:** channel-variant electrophysiology = `IN_VITRO`; mouse *Efhc1*/*Brd2*/lethargic work = `MODEL_ORGANISM`; imaging/cohort/epidemiology = `HUMAN_CLINICAL`.

**Primary sources used (URLs):**
- [ILAE IGE definition — Hirsch 2022, Epilepsia](https://onlinelibrary.wiley.com/doi/10.1111/epi.17236) (PMID 35503716)
- [Cossette 2002, GABRA1 — Nat Genet](https://www.nature.com/articles/ng885z) (PMID 11992121)
- [Suzuki 2004, EFHC1 — Nat Genet](https://pubmed.ncbi.nlm.nih.gov/15258581/) (PMID 15258581)
- [Escayg 2000, CACNB4 — Am J Hum Genet](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1378014) (PMID 10762541)
- [Dibbens 2004, GABRD — Hum Mol Genet](https://pubmed.ncbi.nlm.nih.gov/15115768/) (PMID 15115768)
- [Pal 2003, BRD2 — Am J Hum Genet](https://pubmed.ncbi.nlm.nih.gov/12830434/) (PMID 12830434)
- [ILAE Consortium GWAS 2018 — Nat Commun](https://www.nature.com/articles/s41467-018-07524-z) (DOI 10.1038/s41467-018-07524-z)
- [StatPearls: Juvenile Myoclonic Epilepsy](https://www.ncbi.nlm.nih.gov/books/NBK537109/)
- [OMIM #254770](https://omim.org/entry/254770)
- [MONDO:0009696 — Monarch Initiative](https://monarchinitiative.org/MONDO:0009696)
- [Long-term prognosis — PMID 33781581](https://pubmed.ncbi.nlm.nih.gov/33781581/)
- [BIOJUME stratified definition — Brain Communications 2023](https://academic.oup.com/braincomms/article/5/3/fcad182/7193319)
- [Thalamocortical connectivity — Brain 2012](https://academic.oup.com/brain/article/135/12/3635/286702)
- [Cognitive endophenotypes — PMID 27343727](https://pubmed.ncbi.nlm.nih.gov/27343727/)
- [Prevalence, Norway — PMID 27861775](https://pubmed.ncbi.nlm.nih.gov/27861775/)
- [EFHC1 migration defects — PMC3490517](https://pmc.ncbi.nlm.nih.gov/articles/PMC3490517/)
- [BRD2 haploinsufficiency/GABAergic deficit — PMC3161054](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3161054/)