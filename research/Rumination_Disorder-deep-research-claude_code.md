---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-29T22:11:55.518894'
end_time: '2026-07-29T22:17:48.004224'
duration_seconds: 352.49
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Rumination Disorder
  mondo_id: ''
  category: Psychiatric
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
  web_search_requests: 19
  num_turns: 19
  total_cost_usd: 1.697897
  session_id: 574ce21a-bc93-5c7c-a2f0-f74643218baf
  stop_reason: end_turn
citation_count: 38
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Rumination Disorder
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Rumination Disorder** covering all of the
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

# Rumination Disorder / Rumination Syndrome — Comprehensive Research Report

## 1. Disease Information

### Overview
Rumination disorder (synonymous in the literature with "rumination syndrome" and historically "merycism") is a disorder of gut–brain interaction/functional gastroduodenal disorder characterized by the **effortless, painless, repeated regurgitation of recently ingested food** into the mouth, occurring shortly after eating (typically within 10–15 minutes, ranging from immediately to up to 2 hours postprandially), where the regurgitated material is recognizable, undigested, and initially palatable, and is then re-chewed, re-swallowed, or expectorated. It is **not preceded by retching or nausea**, distinguishing it fundamentally from vomiting. The condition spans the lifespan — described separately in infants, in individuals with intellectual/developmental disabilities, and in otherwise cognitively normal adolescents and adults — with distinct proposed etiologic models for each group (NCBI StatPearls, NBK576404; Wikipedia "Rumination syndrome").

The mechanism is now understood as a learned/acquired motor behavior: a voluntary (though usually unconscious/unperceived) contraction of the abdominal wall and thoracic musculature raises intragastric pressure above lower esophageal sphincter (LES) pressure, in the context of transient LES/upper esophageal sphincter relaxation, producing retrograde flow of gastric contents — essentially "an unintentionally acquired habit, possibly a learned adaptation of the belch reflex" (StatPearls NBK576404).

Because the manifest behavior (regurgitation of food) overlaps with both **eating disorders** and **gastrointestinal motility disorders**, rumination is classified in *two entirely separate diagnostic systems* with different emphases:
- **DSM-5 / DSM-5-TR**: classified among Feeding and Eating Disorders (code 307.53).
- **Rome IV**: classified as a Functional Gastroduodenal Disorder (an entirely separate nosologic tradition, emphasizing the motility mechanism over psychiatric framing).

### Key Identifiers
| System | Code / ID | Notes |
|---|---|---|
| **ICD-10-CM** | F98.21 | Rumination disorder of infancy and childhood |
| **ICD-10-CM** | F50.84 | Rumination disorder (adults; added in ICD-10-CM update aligning with DSM-5-TR) |
| **ICD-10** | P92.1 | Regurgitation and rumination of newborn (perinatal) |
| **ICD-11** | **6B85** | Rumination-regurgitation disorder (Mental, Behavioural or Neurodevelopmental Disorders chapter; requires developmental age ≥2 years, regurgitation ≥ several times/week for ≥ several weeks) |
| **ICD-11** | **DD90.6** | Adult rumination syndrome (Digestive System Diseases chapter — the Rome IV/gastroenterology-tradition entity) |
| **DSM-5 / DSM-5-TR** | 307.53 | Rumination Disorder |
| **Rome IV** | — | Functional gastroduodenal disorder; separate child/adolescent and adult criteria sets |
| **MONDO** | *A MONDO term for "rumination syndrome" appears in general searches (frequently cited informally as MONDO:0001301), but this identifier could not be independently confirmed against the authoritative MONDO OBO record in this research pass — it should be verified with `runoak -i sqlite:obo:mondo info <ID> -O obo` before use in curation, per dismech's anti-hallucination policy.* | Needs OAK verification |
| **OMIM** | None identified | Rumination disorder is not a monogenic/Mendelian condition and does not have a dedicated OMIM phenotype MIM number; it is not indexed as a single-gene disorder. |
| **MeSH** | (Not independently confirmed in this pass — MeSH heading likely "Rumination Syndrome"; verify before citing.) | |

Note the **important dual coding** in ICD-11: **6B85** (mental/behavioral chapter — "rumination-regurgitation disorder," developmentally framed, ≥2 years) and **DD90.6** (digestive-disease chapter — "adult rumination syndrome," Rome-IV-aligned). This dual placement mirrors the DSM-5-vs-Rome-IV split and should be preserved as two related but distinct classification anchors rather than merged into one.

### Synonyms
- Rumination syndrome
- Merycism / mericism (from Latin *ruminare*, "to chew the cud"; term also historically used in animal physiology)
- Rumination disorder of infancy and childhood
- Adult rumination syndrome
- Psychogenic rumination (older, less-preferred term)

### Data Provenance
Nearly all available evidence is **aggregated disease-level clinical literature**: case series, cohort studies from tertiary motility centers (e.g., Mayo Clinic, Rome Foundation cohorts), and a small number of population/school-based surveys and epidemiologic studies (e.g., the Rome Foundation Global Epidemiology Study). There is **no individual-patient EHR-scale registry** specific to rumination syndrome analogous to cancer or rare-disease registries; most quantitative estimates (prevalence, weight loss %, treatment response rates) derive from single-center case series of tens to low hundreds of patients, which should be treated as suggestive rather than population-representative.

---

## 2. Etiology

### Disease Causal Factors
There is **no known single cause**; rumination syndrome is best understood as a **learned, largely subconscious motor/behavioral adaptation** rather than a primary structural, infectious, or classically "genetic" disease. As Wikipedia's synthesis states plainly: *"The cause of rumination syndrome is unknown."* The dominant mechanistic model (see Section 6) is behavioral-motor: voluntary abdominal-wall contraction paired with LES relaxation, which becomes an unconsciously reinforced habit.

Three broadly distinct etiologic narratives exist across the age spectrum:

1. **Infants (typical onset 3–12 months)**: hypothesized links to **caregiver under-stimulation, emotional neglect, or disrupted maternal–infant bonding/attachment** — described historically as arising from "a certain deprivation of relations with the mother… or a disturbance in the child's relationship with the mother," with the behavior serving a self-soothing/self-stimulatory function. It has also been described in neonatal intensive care settings, where efforts toward parent–infant bonding have made the presentation rare (Vulgaris Medical; StatPearls).
2. **Individuals with intellectual/developmental disabilities**: proposed as **self-stimulatory behavior** arising from a mismatch of environmental stimulation (over- or under-stimulation), occurring at markedly elevated rates in institutionalized populations.
3. **Cognitively normal adolescents/adults**: proposed **habit/behavioral-learning models**, sometimes triggered by an antecedent illness, surgery, psychological trauma/stress, or a prior history of self-induced vomiting (bulimia nervosa) that becomes an involuntary conditioned reflex; also described following stressful life events (family bereavement, concussion) or medication changes (Wikipedia; StatPearls).

### Risk Factors

**Genetic risk factors**: No causal or susceptibility variant, locus, or Mendelian mechanism has been established for rumination syndrome/disorder specifically. Wikipedia notes "little evidence concerning the impact of hereditary influence," though isolated case reports describe clustering within families — insufficient to establish heritability.

> **Critical distinction to avoid Named-Entity/construct confusion:** A body of behavioral-genetics literature exists on heritability of "**rumination**" as a *psychological/cognitive construct* — repetitive, passive, negative self-focused thinking associated with depression (the RRS "Ruminative Response Scale" literature). Twin studies report ~24–41% heritability for this cognitive rumination trait (Moksnes et al.; PMC4111768), and a GWAS (Eszlari et al., *Transl Psychiatry* 2019, PMC6423133) found gene-level (not genome-wide-significant SNP-level) associations with ***KCTD12*** and miR-383-binding genes, plus candidate-gene signals at *KCNJ6* (GIRK2), *CREB1*, and *BDNF*. **This is a different disease/construct than the GI rumination-regurgitation disorder** covered in this report (repetitive negative *thought* vs. repetitive food *regurgitation*) — the two share only the English word "rumination." These genetic findings should **not** be cited as genetic evidence for Rumination Disorder/rumination syndrome; doing so would be a textbook Named Entity Confusion error. No comparable GWAS/twin heritability data exist for the GI condition.

**Environmental / demographic risk factors**:
- **Sex**: adult prevalence skews female (Rome Global Epidemiology Study: 54.5% female vs. 45.5% male); pediatric/school-based samples show more even sex distribution.
- **Age**: bimodal — infant onset (3–12 months) and adolescent/adult onset; adult mean age of onset ~44.5 years per the Rome Global study, though clinical case series more often describe adolescent presentation (mean ~12.9 years, with a female-later/male-earlier onset split: males 11.0±0.8 years vs. females 13.8±0.5 years).
- **Comorbid psychiatric disease**: strongly associated. In a case–control analysis, 83.3% of rumination syndrome patients had a psychiatric diagnosis (vs. controls), with anxiety (37.5%), depression (29.2%), OCD (8.3%), PTSD (8.3%), and bipolar disorder (4.2%) represented; psychiatric disorder was an independent predictor (adjusted OR = 4.47) (PubMed 33988353).
- **Comorbid eating disorder**: 37.5% of rumination patients had a history of an eating disorder (anorexia nervosa 12.5%, bulimia nervosa 16.7%), an independent predictor with adjusted OR = 16.4 (PubMed 33988353) — the strongest risk factor identified in that cohort.
- **Institutionalization / intellectual disability**: markedly increases risk (see epidemiology below).
- **History of trauma/abuse**: cited in up to ~33% of cases in some case series (StatPearls).
- **Higher BMI**: associated with adult rumination syndrome in meta-analytic characterization.
- **Concurrent GERD** (secondary rumination pathway — see mechanism section).

### Protective Factors
No specific genetic or pharmacologic protective factor is established. The clearest "protective" intervention is environmental/behavioral: for infant rumination linked to neglect, **increased caregiver responsiveness, holding, and nurturing** reduces/resolves the behavior (a mother-substitute caregiving intervention is a described historical treatment), and improved NICU bonding practices have made infant rumination syndrome rare in that setting.

### Gene–Environment Interactions
No specific gene–environment interaction has been characterized for the GI disorder. The pathophysiologic model instead emphasizes a **behavior–environment interaction**: an underlying capacity for voluntary/learnable control of intra-abdominal pressure and sphincter tone (present in everyone, and exploited deliberately by professional "regurgitators"/some competitive eaters) becomes pathologically and involuntarily reinforced under specific psychosocial conditions (neglect, stress, post-illness state, eating-disorder history), analogous to how the LES/belch reflex can be voluntarily co-opted and then become an unconscious habit.

---

## 3. Phenotypes

| Phenotype | Type | Frequency (where reported) | Suggested HP term* |
|---|---|---|---|
| Regurgitation of recently ingested, undigested, recognizable food, effortless, within ~10–15 min (up to ~1–2 h) of a meal | Symptom / cardinal feature | Present by definition (100%) | HP:0002020 Regurgitation *(verify label match via OAK before use)* |
| Absence of retching/nausea preceding regurgitation | Clinical sign (defining/negative criterion) | By definition | — (absence-of-feature; may use negation modifier on HP:0002013 Vomiting) |
| Abdominal pain | Symptom | ~38% (Wikipedia synthesis of case series) | HP:0002027 Abdominal pain |
| Weight loss | Physical sign | ~40–42% adults; 17–43% in pediatric cohorts (mean ~9.6 kg in one series) | HP:0001824 Weight loss |
| Reduced fecal output / constipation | Symptom | ~21% | HP:0002019 Constipation |
| Nausea (independent of regurgitation episodes) | Symptom | ~17% | HP:0002018 Nausea |
| Diarrhea | Symptom | ~8% | HP:0002014 Diarrhea |
| Bloating | Symptom | ~4% | HP:0030760 Abdominal bloating (verify) |
| Dental erosion / caries, halitosis | Physical sign | Reported more in pediatric/refractory cases; ~3–7% in some series | HP:0006486 Dental fracture / consider HP:0000670 Dental caries or a dedicated "dental erosion" term (verify best match) |
| Failure to thrive / malnutrition (esp. pediatric) | Physical sign | Minority; more common with diagnostic delay or comorbid eating disorder | HP:0001508 Failure to thrive |
| Electrolyte disturbance | Laboratory abnormality | Uncommon unless refractory/comorbid eating disorder | HP:0011036 Abnormal electrolyte level (or specific ion term) |
| School/work absenteeism, social withdrawal | Behavioral/functional impact | Frequently described qualitatively | (Functional/QoL descriptor rather than HPO term) |
| Comorbid anxiety | Behavioral | 37.5% in one case-control cohort | HP:0000739 Anxiety |
| Comorbid depression | Behavioral | 29.2% | HP:0000716 Depressivity |

*HP term suggestions are first-pass candidates based on typical HPO coverage for these common clinical concepts; **each must be independently verified via OAK (`runoak -i sqlite:obo:hp info <ID> -O obo`)** for exact label match before use in a dismech entry, consistent with project anti-hallucination policy — none were independently confirmed against the live HPO database in this research pass.

### Phenotype Characteristics
- **Onset**: Trimodal by age group — infancy (3–12 months), childhood/adolescence (mean ~12.9 years in adolescent case series), and adulthood (mean ~44.5 years in the Rome Global Epidemiology cohort). Onset can also be triggered acutely by an illness, surgery, or stressful event in previously asymptomatic adolescents/adults.
- **Severity**: Variable — ranges from occasional, minimally impairing regurgitation to disabling, near-constant regurgitation causing marked weight loss, malnutrition (occasionally requiring enteral/jejunostomy feeding), and severe psychosocial impairment (school absenteeism).
- **Progression/course**: Chronic once established; the StatPearls source states prognosis in children/adolescents is "benign, although symptoms may persist for years." Diagnostic delay is characteristic and substantial: average **21–77 months** to diagnosis by one estimate, or "an average of five physicians over 2.75 years" by another (Wikipedia, citing case-series data) — reflecting frequent misdiagnosis as GERD, cyclic vomiting, gastroparesis, or an eating disorder.
- **Frequency among affected individuals**: Not a population-frequency concept for a single condition, but note: rumination syndrome itself as a "phenotype of a phenotype" — its prevalence is presented in Section 9.

### Quality-of-Life Impact
Regurgitation-associated social embarrassment leads to **school and work absenteeism**, social withdrawal/avoidance of eating in public, and secondary **anxiety and depressive symptomatology**. Weight loss and diagnostic-odyssey frustration compound psychosocial burden. No disease-specific validated QoL instrument was identified in this pass (searches did not surface an EQ-5D/SF-36 rumination-syndrome-specific substudy); general GI-QoL and psychiatric comorbidity scales are used in the literature instead.

---

## 4. Genetic/Molecular Information

**There is no established monogenic cause, no ClinVar/HGMD pathogenic variant catalog, no defined causal gene, and no OMIM phenotype entry for rumination disorder/syndrome.** This is fundamentally a learned behavioral-motor disorder of the gut-brain axis, not a Mendelian or classically "genetic" disease in the dismech schema sense.

- **Causal genes**: None identified.
- **Pathogenic variants**: None identified; not applicable.
- **Modifier genes**: None specifically validated for the GI disorder. (As emphasized above, the *KCTD12*/miR-383/*KCNJ6*/*CREB1*/*BDNF* genetic-association literature pertains to the **psychological rumination/depressive-thinking construct**, not this condition — do not conflate.)
- **Epigenetic information**: None identified specific to rumination syndrome.
- **Chromosomal abnormalities**: None identified as causal; rumination behavior is *secondarily* over-represented in populations with chromosomal/neurodevelopmental conditions causing intellectual disability (e.g., trisomy 21, fragile X, and other syndromic ID), but this reflects the general enrichment of self-stimulatory/self-injurious behaviors in intellectual disability rather than a rumination-specific chromosomal etiology.

**Curatorial implication for dismech**: this entry will likely have a very sparse/absent `genetic:` block, and should explicitly note (in `notes` or discussion) that this is a behaviorally/psychosocially mediated condition rather than force-fitting genetic annotation. If any digenic/oligogenic or single-gene claims are later found in more targeted searches, they should be treated with high NEC suspicion given how easily "rumination" the cognitive construct is confused with "rumination" the GI disorder in literature search.

---

## 5. Environmental Information

- **Environmental/psychosocial factors**: caregiver neglect or under/over-stimulation (infants); institutionalization (intellectual disability); psychological trauma, abuse history, stressful life events, recent illness or surgery, and medication changes (adolescents/adults).
- **Lifestyle factors**: no established association with smoking, diet composition, alcohol, or exercise as primary causal/risk factors (as distinct from the *behavior itself*, which is diet-triggered — i.e., meal ingestion is the physiologic trigger for each episode, not a lifestyle risk factor for disease onset).
- **Infectious agents**: none implicated.

---

## 6. Mechanism / Pathophysiology

### Causal Chain (Primary/Idiopathic Rumination)
1. **Trigger**: Ingestion of a meal → gastric distension.
2. **Voluntary (but typically unperceived/subconscious) coordinated abdominothoracic maneuver**: simultaneous **contraction of the intercostal and upper abdominal wall muscles** (external oblique, upper rectus abdominis) together with a **thoracic "suction" maneuver and relaxation of the crural diaphragm**. This raises **intragastric pressure** — objectively documented at **>30 mmHg on combined high-resolution manometry with impedance (HRIM)** — occurring in a coordinated fashion rather than as isolated straining.
3. **Reversal of the normal esophagogastric pressure gradient**: the elevated intragastric pressure now exceeds LES pressure; concurrently, there is **relaxation of the upper esophageal sphincter** (and proposed relaxation of the gastric fundus/diaphragm), producing in effect a transient common cavity between stomach and oropharynx.
4. **Retrograde flow / regurgitation**: gastric contents flow passively up the esophagus into the mouth, where they are re-chewed, re-swallowed, or expectorated.
5. **Cessation**: episodes typically stop once the refluxed material becomes acidic/bilious in taste (proposed to act as an aversive stop signal), or with sleep/distraction/environmental engagement.

Manometric/electrophysiologic correlates: gastroduodenal manometry historically demonstrated characteristic **"R" (rumination) waves** attributed to abrupt intra-abdominal pressure spikes; **abdominal wall EMG** shows activation of the abdominal-wall musculature time-locked to episodes; modern **combined esophageal HRIM with impedance** is considered the objective/gold-standard confirmatory test, showing reflux events reaching the proximal esophagus tightly coupled to an abdominal pressure rise >30 mmHg (adults; ~25 mmHg proposed threshold in children) (Absah et al., *Neurogastroenterol Motil* 2017, PMID cited via Wiley DOI 10.1111/nmo.12954; also PMC6034670, PubMed 24366235/38385686).

### "Secondary" Rumination (GERD-Associated Pathway)
A distinct proposed subtype: pre-existing gastroesophageal reflux episodes trigger a **learned/reflexive abdominal straining response**, effectively "hijacking" a physiologic reflux event into a rumination episode. This subgroup is mechanistically and therapeutically relevant because it may respond differently (e.g., possibly better candidates for anti-reflux surgery) than primary/idiopathic rumination.

### Proposed Contributing/Associated Findings
- **Delayed gastric emptying** in a subset of patients.
- **Increased gastric mechanosensory perception** (visceral hypersensitivity).
- **Duodenal/gastric antral eosinophilia and mast cell infiltration**, and increased intraepithelial lymphocytes reported in small histopathologic comparison studies — suggesting a possible low-grade inflammatory/immune component, though causality and specificity remain unestablished (StatPearls NBK576404).
- **Autonomic/vagal tone**: contrary to some hypotheses, controlled studies found rumination-syndrome patients do **not** show decreased postprandial vagal tone versus controls; cardiac vagal tone assessment (via ECG-derived indices) is being explored as a marker of gastric discomfort/pain perception rather than as a primary causal autonomic lesion (Fitzke/Hoshikawa et al., UCL working paper; PubMed 32383546; "The autonomic phenotype of rumination," PubMed 19272312). Diaphragmatic breathing's therapeutic benefit is **not mediated by changes in vagal tone**, per at least one mechanistic study (Halland et al., *Neurogastroenterol Motil* 2016) — its benefit is attributed instead to providing a **competing voluntary motor pattern** that displaces the acquired, largely unperceived abdominothoracic contraction sequence.

### Cell Types / Biological Processes (for GO/CL annotation, tentative)
This is predominantly a **systems-level neuromuscular/behavioral mechanism** rather than a discrete cellular pathology, so GO/CL annotation is necessarily coarse:
- Smooth muscle of the lower esophageal sphincter (relevant anatomic structure, not a defined "cell type" lesion) — relaxation/tone dysregulation.
- Skeletal muscle: intercostal muscles, external oblique, rectus abdominis, crural diaphragm — voluntary contraction driving the pressure gradient reversal.
- Possible antral/duodenal eosinophil and mast cell involvement (immune cell types) in a subset, of uncertain mechanistic significance — candidate CL terms: eosinophil (CL:0000771), mast cell (CL:0000097), if curating this histopathology finding.
- Vagal/parasympathetic autonomic circuitry — implicated in visceral perception/discomfort signaling rather than motor execution per current evidence.

**Biological process framing (tentative GO candidates, to be OAK-verified)**: "regulation of gastric emptying," "esophageal smooth muscle relaxation," "belch reflex," "regurgitation" — HPO/GO do not have precise 1:1 process terms for "rumination behavior" itself; this is a case where the mechanism is best captured in `pathophysiology` free text plus modeled causal-edge nodes (gastric distension → abdominal wall contraction → LES/UES relaxation → pressure gradient reversal → regurgitation) rather than forced into narrow GO leaf terms.

### Molecular Profiling / Advanced Technologies
No transcriptomic, proteomic, metabolomic, single-cell, or spatial-omics dataset specific to rumination syndrome was identified in this research pass. This is consistent with the condition's characterization as a functional/behavioral motility disorder rather than a molecularly profiled disease entity — a notable "gap" relative to sections 6's omics sub-bullets in the template.

---

## 7. Anatomical Structures Affected

- **Organ level (primary)**: Stomach (fundus — pressure generation), lower esophageal sphincter, upper esophageal sphincter, esophagus (retrograde conduit), diaphragm (crural portion — relaxation permits pressure transmission), abdominal wall musculature (external oblique, rectus abdominis), intercostal muscles (thoracic component of the maneuver).
- **Secondary/complication-related organs**: Oral cavity/teeth (dental erosion from repeated acid exposure), possibly duodenum (eosinophilia reported in a subset).
- **Body systems involved**: Digestive system (primary); musculoskeletal system (voluntary muscles executing the maneuver); autonomic nervous system (vagal/parasympathetic signaling implicated in discomfort perception, not primary motor mechanism); psychiatric/behavioral system (learned habit, comorbid anxiety/depression).
- **Suggested UBERON terms** (tentative, to be OAK-verified): UBERON:0000945 stomach; UBERON:0004907 lower esophageal sphincter; UBERON:0001043 esophagus; UBERON:0001087 diaphragm; UBERON:0001416 external oblique muscle (verify exact ID); UBERON:0002378 rectus abdominis (verify).
- **Tissue/cell level**: Smooth muscle of the esophagogastric junction; striated/skeletal muscle of the abdominal wall and diaphragm; possibly gastric antral/duodenal mucosal eosinophils and mast cells (histopathologic finding in a subset).
- **Subcellular level**: Not applicable/not characterized — no subcellular lesion (e.g., organelle dysfunction) is described in the literature; this is a systems/organ-level functional disorder.
- **Lateralization**: Not applicable (midline, bilateral musculature involved symmetrically).

---

## 8. Temporal Development

### Onset
- **Infantile form**: onset typically **3–12 months of age**.
- **Pediatric/adolescent form**: mean onset ~12.9 years in one adolescent case series (males 11.0±0.8 years; females 13.8±0.5 years) — i.e., earlier onset in males, later in females within the adolescent-onset subgroup.
- **Adult form**: mean age at onset **44.5 years** in the Rome Foundation Global Epidemiology Study (i.e., a distinct, later-onset adult population separate from those whose disorder began in adolescence and persisted).
- **Onset pattern**: Typically insidious in infants/those with intellectual disability; in adolescents/adults can be **acute**, often triggered by an identifiable antecedent (illness, surgery, psychological stressor).

### Progression
- **Disease course pattern**: Chronic once established, without formal "staging" system (unlike oncologic or infectious diseases). No AJCC/WHO staging scheme applies.
- **Progression rate**: Variable; can wax and wane with psychosocial stress.
- **Disease duration**: Can be self-limited in infants (most recover within about one year, particularly with improved caregiving) but tends toward **chronic, multi-year persistence** if untreated in adolescents/adults, compounded by the characteristic multi-year diagnostic delay (21–77 months, or "5 physicians over 2.75 years").
- **Remission**: Achievable with behavioral treatment — a 12-month follow-up study of 47 adolescents found continued symptomatic improvement, with **symptom cessation for ≥6 months in 20%** of patients after intensive behavioral treatment; a separate 54-adolescent cohort followed for 10 months found diaphragmatic breathing + supportive therapy produced **56% substantial improvement and complete symptom cessation in an additional ~30%**.
- **Critical periods for intervention**: Early diagnosis (avoiding the characteristic multi-year delay) is emphasized throughout the literature as key to preventing secondary complications (weight loss, malnutrition, dental damage, psychosocial harm) and unnecessary invasive testing/treatment for presumed GERD or cyclic vomiting.

---

## 9. Inheritance and Population

### Epidemiology
- **General adult population prevalence**: **3.1%** (Rome Foundation Global Epidemiology Study), with 54.5% female / 45.5% male among cases and mean onset age 44.5 years.
- **Infants/toddlers (0–3 years)**: pooled prevalence **~2.9%**.
- **Children**: pooled prevalence **~0.1%**.
- **Adolescents**: pooled prevalence **~1.1%**; one school-based survey of 10–16-year-olds in Sri Lanka found **5.1%** prevalence (boys 5.1%, girls 5.0% — essentially equal by sex in that cohort) (PMC3538663).
- **Individuals with intellectual disability**: markedly elevated — reported in **6–10% of infants with developmental delay** and **8–10% of institutionalized adults with intellectual disability**, with rates up to ~10% among institutionalized populations specifically.
- **General/normal-intelligence population true prevalence is likely underestimated**, because affected individuals often do not seek care or are misdiagnosed (as GERD, cyclic vomiting, or an eating disorder) for years.

### Inheritance Pattern
**Not a Mendelian/single-gene disorder** — no defined inheritance pattern (AD/AR/X-linked/mitochondrial) applies. Any familial clustering reported in isolated case reports likely reflects shared environmental/behavioral-learning factors (e.g., modeling within a household, shared psychosocial stressors) rather than genetic transmission; "little evidence concerning the impact of hereditary influence" (Wikipedia synthesis). Penetrance, expressivity, anticipation, germline mosaicism, founder effects, and carrier frequency are **not applicable** concepts for this condition.

### Population Demographics
- **Sex ratio**: Female predominance in adult-onset disease (Rome Global study: ~55:45 F:M); more balanced in pediatric/school-based samples.
- **Geographic distribution**: No endemic geographic pattern identified; case series and school surveys span North America, Europe, and South Asia (e.g., Sri Lanka) without described regional clustering beyond study-site availability/ascertainment.
- **Age distribution**: Bimodal/trimodal as above (infant, adolescent, adult-onset subgroups), likely representing at least partially distinct clinical entities sharing a final common regurgitation phenotype rather than one uniform age-of-onset disease.

---

## 10. Diagnostics

### Clinical Criteria

**Rome IV (adults)** — all of the following:
1. Regurgitation of food into the mouth occurring at least 2–3 times weekly (some summaries state "at least 2-3 times monthly" — sources vary; the widely cited Rome IV wording requires "repeated regurgitation... occurring within minutes of ingesting a meal," present for the last 3 months with symptom onset ≥6 months prior).
2. Regurgitation is **not preceded by retching**.
Supportive: material is recognizable food with a pleasant/non-acidic initial taste; symptoms cease when the material becomes acidic; heartburn is absent unless concurrent GERD.

**Rome IV pediatric (neonate/toddler, ≥2 months of age)**: repetitive abdominal/diaphragmatic/tongue-muscle contractions with effortless regurgitation, **plus 3 or more** of: onset age 3–8 months; unresponsive to standard GERD therapy; unaccompanied by signs of distress; does not occur during sleep or during active social interaction with caregivers.

**Rome IV pediatric (children/adolescents, ≥2 months)**: repeated regurgitation/rechewing/expulsion beginning soon after meal ingestion; not occurring during sleep; not preceded by retching.

**DSM-5 / DSM-5-TR**: repeated regurgitation for ≥1 month, occurring after feeding, with rechewing/reswallowing/expectorating; occurring several times weekly (usually daily); **absence of retching, nausea, disgust, or associated GI illness**; not attributable to a medical condition (GERD, pyloric stenosis) or exclusively during the course of anorexia nervosa, bulimia nervosa, binge-eating disorder, or ARFID; if occurring alongside another mental disorder or medical condition, must be severe enough to warrant independent clinical attention.

**ICD-11 (6B85, rumination-regurgitation disorder)**: regurgitation behavior that is frequent (≥ several times per week) and sustained (≥ several weeks); diagnosed only at developmental age ≥2 years.

### Clinical Tests / Objective Confirmation
- **Combined esophageal high-resolution manometry with impedance (HRIM)** is the **objective gold-standard confirmatory test** when clinical diagnosis is uncertain: diagnostic pattern = reflux events reaching the proximal esophagus tightly time-coupled with an **abdominal pressure rise >30 mmHg (adults)** / **~25 mmHg proposed in children**, with near-simultaneous esophageal pressure rise, and (per one detailed criterion set) a gastro-esophageal sphincteric pressure gradient of ~2 mmHg immediately preceding the episode (Kessing et al., "Objective manometric criteria for the rumination syndrome," PubMed 24366235; Absah et al. 2017 review, DOI 10.1111/nmo.12954; Puoti et al. 2024, pediatric HRIM validation, PubMed 38385686).
- **Abdominal wall EMG**: demonstrates time-locked activation of abdominal-wall musculature with episodes.
- **Gastroduodenal manometry**: historically used, shows characteristic "R waves."
- **Upper endoscopy / cross-sectional imaging (e.g., CT enterography)**: used to **exclude** mechanical obstruction, achalasia, or other structural disease — not diagnostic of rumination itself.
- **Gastric emptying study, esophageal pH monitoring**: not required for diagnosis but used selectively to exclude/characterize concurrent GERD or gastroparesis, and notably, **~20% of patients labeled "PPI-non-responsive GERD" show a rumination pattern on testing** — an important diagnostic-overlap statistic.
- **Basic labs**: electrolytes to screen for complications of frequent regurgitation (uncommon unless a concurrent eating disorder is present).
- **Eating-disorder screening**: essential given the high rate of comorbid anorexia/bulimia nervosa (see Section 2).

### Genetic Testing
**Not applicable** — no genetic test, panel, WGS/WES indication, karyotype, microarray, or repeat-expansion assay is relevant to diagnosing rumination disorder/syndrome, since it is not a genetically defined condition.

### Differential Diagnosis
| Condition | Key Distinguishing Feature |
|---|---|
| **Vomiting / gastroparesis** | Gastroparesis vomiting is intermittent, preceded by nausea/retching, occurs late postprandially (hours), and vomitus is no longer recognizable as recently ingested food (may be old/partially digested); rumination regurgitation is immediate, effortless, and the food is fresh/recognizable. |
| **Cyclic vomiting syndrome** | Discrete, stereotyped vomiting episodes with symptom-free intervals; lacks the immediate-postprandial, retching-free character of rumination. |
| **Achalasia** | Patients typically stop eating once regurgitation begins and do not habitually re-swallow the regurgitated material — a key behavioral distinguishing feature from rumination, in which re-chewing/re-swallowing is characteristic. |
| **GERD** | Rumination lacks the sour/acidic taste and heartburn typical of reflux (until late in the episode when regurgitant becomes acidic); ~20% of PPI-refractory "GERD" patients actually have rumination on HRIM testing. |
| **Bulimia nervosa** | The most common misdiagnosis/confounder — regurgitation in rumination is **involuntary/reflexive**, whereas bulimic purging is **intentional, self-induced vomiting**, often associated with body-image concerns and preceded by binge eating; the two can also co-occur (16.7% of rumination patients had bulimia nervosa history in one cohort). |
| **Functional dyspepsia, esophagogastric junction outflow obstruction, aerophagia, belching disorders** | Distinguished by symptom timing, character, and (where needed) manometric/impedance findings. |

### Screening
No population-level screening program exists (this is not a condition amenable to newborn/carrier/genetic screening); "screening" in practice consists of maintaining clinical suspicion — particularly in patients labeled "PPI-refractory GERD," in institutionalized individuals with intellectual disability, and in adolescents/young adults with unexplained weight loss and postprandial regurgitation — to shorten the characteristically long diagnostic delay.

---

## 11. Outcome / Prognosis

- **Survival/mortality**: No literature indicates increased mortality or reduced survival associated with rumination disorder/syndrome; it is not a lethal condition per se, though severe untreated cases can cause serious malnutrition.
- **Morbidity/function**: Chief morbidity is **psychosocial** (school/work absenteeism, social avoidance, anxiety, depression) and **nutritional** (weight loss in up to ~40% of adult cohorts and 17–43% of pediatric cohorts, occasionally severe enough to require enteral nutrition).
- **Disease course**: Considered a **reversible, acquired habit** rather than a fixed structural lesion — the condition responds well to targeted behavioral intervention in the majority of patients. StatPearls: prognosis in children/adolescents is "benign, although symptoms may persist for years" without treatment.
- **Complications**:
  - Weight loss/malnutrition (more common with prolonged diagnostic delay or comorbid eating disorder).
  - Electrolyte disturbance (uncommon, mainly in refractory/comorbid-eating-disorder cases).
  - Dental erosion and caries (more prominent in pediatric and refractory cases).
  - Need for nutritional support: in one retrospective cohort of 133 underweight rumination patients, **23 required jejunostomy tube placement**, maintained on average **16 weeks**, associated with a mean weight gain of **38.8 pounds**, supporting weight restoration and enabling engagement in behavioral therapy.
  - Psychosocial complications: anxiety, depression, somatization, social withdrawal.
- **Prognostic factors**: Response to diaphragmatic breathing/behavioral therapy is a strong positive prognostic indicator. A **prior history of bulimia nervosa is associated with reduced treatment response** to standard behavioral approaches (Wikipedia, citing PubMed source [9]/[14]). Longer diagnostic delay is associated with greater nutritional/psychosocial morbidity by the time treatment begins.
- **Longitudinal outcome data**: A 2018 study of 47 adolescents followed for 12 months after intensive behavioral treatment found continued improvement, with **symptom cessation ≥6 months in 20%**, along with discontinuation of supplemental nutrition, reduced somatic symptom burden, and improved quality of life.

---

## 12. Treatment

### First-Line: Behavioral Therapy
- **Diaphragmatic breathing** is the universally recommended **first-line therapy** across pediatric and adult guidelines. Technique: seated, one hand on chest and one on abdomen; breathe so only the abdominal hand moves; inhale through the nose over 4–6 seconds, hold 2–3 seconds, exhale slowly through pursed lips; performed proactively after meals or at the first sensation/urge to regurgitate. Mechanistically, it works by **substituting a competing, voluntary motor pattern for the acquired, largely unperceived abdominothoracic contraction sequence** — notably, its benefit is **not mediated via changes in cardiac vagal tone** (Halland et al. 2016).
- **Biofeedback-assisted training**: uses visual/instrumented feedback (surface EMG or HRIM tracing) to help patients learn to suppress the postprandial rise in gastric/intra-abdominal pressure. A randomized trial found biofeedback produced a **74±6% reduction in rumination events** (from 29±6 to 7±2 daily episodes) versus ~1±14% with sham treatment.
- Behavioral modification overall is reported to **eliminate the behavior in up to 66%** of patients and **reduce frequency by up to 55%** in others (StatPearls synthesis); a separate adolescent cohort (n=54, 10-month follow-up) found diaphragmatic breathing + supportive therapy produced substantial improvement in 56% and complete cessation in an additional ~30%.
- Adjuncts: general relaxation training, cognitive-behavioral therapy (especially where anxiety/depression/OCD/PTSD comorbidity is present), habit-reversal training, and gum-chewing as a behavioral adjunct.
- **Suggested MAXO terms** (tentative — verify via OAK before curating): `MAXO:0000011` physical therapy (not an exact fit — diaphragmatic breathing training is closer to a specific respiratory/behavioral retraining technique without an obvious precise MAXO leaf term; consider `MAXO:0000077` behavioral counseling or a biofeedback-specific term if one exists), and a general **behavioral/psychotherapy** MAXO/NCIT term for CBT.

### Pharmacotherapy (Reserved for Behavior-Therapy-Refractory Cases)
- **Baclofen** (GABA-B agonist): **10 mg three times daily**, shown in a double-blind, placebo-controlled crossover RCT to reduce transient LES relaxations and improve patient-reported rumination symptoms, with **symptomatic improvement in 63% of treated patients**. Main limitation: sedation/drowsiness. `treatment_term`: NCIT:C15986 Pharmacotherapy; `therapeutic_agent`: baclofen (CHEBI ID to be verified, e.g., CHEBI:2972 — confirm via OAK).
- **Buspirone**: supported by extrapolation from functional dyspepsia data (improves gastric fundic relaxation); expert opinion supports a trial in refractory rumination, but no rumination-syndrome-specific RCT was identified.
- **Proton pump inhibitors and other standard antireflux medications**: explicitly noted to have "little or no effect" on primary rumination — an important negative finding, useful for distinguishing rumination from GERD in a treatment-response sense.

### Nutritional Support
- Careful assessment of nutritional status is essential given typical diagnostic delay.
- **Jejunostomy (J-tube) feeding** for underweight/malnourished patients unable to progress with behavioral therapy alone — in one cohort, 23/133 underweight patients required J-tube placement (mean duration 16 weeks), with mean weight gain of 38.8 lb, facilitating subsequent behavioral therapy engagement.

### Surgical/Interventional (Investigational; Not Recommended as Standard)
- **Nissen fundoplication**: case series show mixed results — some patients (e.g., 5 cases in one series) responded well; a separate 12-patient series found upper GI symptoms *worsened* in 9/12 patients. Considered potentially more rational for **"secondary" rumination** (GERD-triggered rumination) than for primary/idiopathic rumination. Current consensus: role remains investigational/uncertain, and "avoidance of surgery as a therapy for rumination syndrome is recommended" in the absence of controlled data.
- **Subtotal gastrectomy with Roux-en-Y reconstruction**: reported as a "last resort" in a single refractory case with concurrent delayed gastric emptying, with >85% symptom resolution over 6 months and improved BMI/QoL — a single case report, not generalizable.

### Experimental / Emerging
No dedicated ClinicalTrials.gov-registered pharmacologic trials beyond the baclofen crossover study and the NHRA "Role of Vagal Tone in Rumination Syndrome" study (NCT03912636, mechanistic, not a treatment trial) were identified; a behavioral-therapy trial (NCT05232097, "Behavioral Therapy in Patients With Rumination") is registered, focused on optimizing/validating behavioral intervention delivery rather than a novel therapeutic agent.

### Treatment Strategy / Algorithm
1. Confirm diagnosis clinically (Rome IV/DSM-5), consider HRIM if uncertain or if ruling out GERD/gastroparesis.
2. Educate and reassure (benign, learned-behavior framing); screen for and address comorbid eating disorder/psychiatric disease.
3. First-line: diaphragmatic breathing ± biofeedback, delivered with structured behavioral/CBT support.
4. Assess and address nutritional status; enteral (jejunostomy) feeding if significant malnutrition impedes behavioral engagement.
5. Refractory to behavioral therapy → trial of baclofen (consider buspirone as an alternative).
6. Surgery (fundoplication, subtotal gastrectomy) reserved as an investigational last resort in carefully selected refractory cases, particularly those with a "secondary"/GERD-driven mechanism or concurrent gastric emptying disorder.

---

## 13. Prevention

- **Primary prevention**: For infantile rumination linked to neglect/under-stimulation, promoting **responsive, nurturing caregiving** (including formal caregiver training and, historically, use of a temporary substitute caregiver to model appropriate soothing/feeding responses) is the described preventive/therapeutic approach; improved NICU bonding practices are credited with making infant rumination rare in that setting.
- **Secondary prevention (early detection)**: The single most emphasized "preventive" measure in the literature is **reducing diagnostic delay** — maintaining clinical suspicion for rumination in patients labeled treatment-refractory GERD, cyclic vomiting, or eating disorder, thereby avoiding years of unnecessary/invasive testing and ineffective treatment (PPIs) and initiating effective behavioral therapy sooner, which limits secondary malnutrition/psychosocial harm.
- **Tertiary prevention**: Behavioral therapy adherence and nutritional monitoring to prevent complications (dental erosion, malnutrition) in patients with established disease; integrated multidisciplinary care (gastroenterology + behavioral health + dietetics ± pharmacy) to prevent relapse and complication accrual.
- **Immunization**: Not applicable.
- **Genetic/carrier screening, preimplantation testing**: Not applicable (non-genetic condition).
- **Behavioral interventions**: Central to prevention/management — see diaphragmatic breathing/biofeedback above.
- **Genetic counseling**: Not applicable.
- **Public health/environmental interventions**: Not a notifiable or environmentally-driven condition; no public-health-level intervention (sanitation, vector control) is relevant.
- **Prophylaxis (medication)**: No prophylactic medication regimen is established; baclofen is used therapeutically once symptomatic, not prophylactically.

---

## 14. Other Species / Natural Disease

This section requires an important conceptual clarification: **"rumination" as normal ruminant digestive physiology is an entirely distinct phenomenon from the human disease "rumination syndrome/disorder"** and the two should not be conflated in a mechanism module.

- **Ruminant "rumination" (physiological, not pathological)**: In ruminants (cattle, sheep, goats, giraffes — a large clade within Artiodactyla with a four-chambered stomach), rumination is a **normal, essential digestive process**: reticular contraction plus relaxation of the distal esophageal sphincter allows a bolus of fermented "cud" to be carried by reverse peristalsis into the mouth for re-chewing/re-insalivation before re-swallowing, aiding fibrous-plant-material digestion. This is physiologic, not disease, and is actively used as an animal-health/reproduction monitoring signal in veterinary/livestock science (e.g., automated "rumination time" sensors in dairy cattle correlate with health and reproductive status; PMC11398270, PMC8547861).
- **Non-ruminant animals with a pathological/atypical rumination-like behavior** (more analogous to the human disorder):
  - **Great apes/other primates**: involuntary regurgitation-and-reingestion behavior has been documented in **gorillas** and other non-human primates, often studied as an abnormal repetitive/self-directed behavior in captivity (a behavioral-welfare concern, sometimes linked to environmental impoverishment — conceptually parallel to the caregiver-neglect/under-stimulation model proposed for human infants and institutionalized individuals with intellectual disability).
  - **Kangaroos**: exhibit regurgitation, re-mastication, and re-swallowing behavior also termed "merycism" in that context, but described as less predictable/rhythmic than true ruminant physiology and not essential to their digestion.
  - **Companion/zoo animals**: a case report describes a **multimodal treatment approach for "rumination syndrome" in a California sea lion (*Zalophus californianus*)** (PMC12562190) — a genuinely veterinary-clinical (pathological, non-digestive-physiology) presentation, the closest documented naturally-occurring veterinary analog to the human disorder identified in this search.
- **Taxonomy note**: no NCBI Taxon-specific "affected species" list beyond the above exists in a systematic disease-registry sense; OMIA (Online Mendelian Inheritance in Animals) was not found to carry a dedicated entry, consistent with this not being a genetically defined condition in any species.
- **Zoonotic potential**: Not applicable — this is a behavioral/motility condition, not a transmissible disease.

**Curatorial recommendation**: if modeling this in dismech, keep the human disorder's `pathophysiology` chain strictly separate from ruminant digestive physiology (which is not a disease at all in that context) and, if desired, note the sea-lion/primate veterinary parallels only as a brief comparative note rather than a "natural disease in other species" `has_subtypes`-style model, since evidence density there is minimal (single case reports).

---

## 15. Model Organisms

**No dedicated genetic model organism (mouse knockout, zebrafish, Drosophila, C. elegans, yeast) exists for rumination disorder/syndrome**, consistent with its non-genetic, behaviorally-mediated pathophysiology. This is an important and notable gap relative to most dismech entries.

The closest experimental analogs identified are **not disease models but mechanistic/physiological probes of the shared gastric-distension → visceral-perception pathway**:
- **Intragastric balloon distension studies** (both in animal models, e.g., awake-rat visceral-manipulation neuroimaging paradigms — bioRxiv 2024.09.17.613477 — and in human fMRI studies) show that experimenter-controlled gastric distension is temporally coincident with cerebral blood flow changes in the cerebellum, insula, and anterior cingulate gyrus, with **overlapping activation patterns between animal gastric-distension paradigms and human intragastric-balloon fMRI studies** — relevant to understanding gastric mechanosensation/visceral perception generally, but these are models of **visceral sensory processing**, not of the rumination behavior/motor sequence itself.
- **Historical human "auto-experimentation"**: the 19th-century physiologist Dr. Charles-Édouard Brown-Séquard is described as having experimentally induced a personal rumination habit while testing gastric-acid responses using swallowed string-tied sponges, eventually developing habitual reflex regurgitation of meals — an early (non-systematic) human self-experiment rather than a formal model system, but historically notable.
- **Veterinary case reports** (sea lion, above) function as isolated clinical analogs rather than controlled experimental models.

**Applications/limitations**: Because no genetic or induced-lesion animal model recapitulates the human behavioral syndrome, essentially all pathophysiologic and treatment-mechanism knowledge in this field derives from **human clinical physiology studies** (manometry/impedance, EMG, cardiac vagal tone measurement) rather than model-organism experimentation. Any future "model" claims for this condition would need scrutiny for **HUMAN_MODEL_MISMATCH**-type validity concerns given the essentially human-behavioral nature of the disorder.

---

## Summary of Key Evidence Gaps (for Curation Planning)

1. **No confirmed MONDO ID, no OMIM entry** — needs direct OAK/Monarch lookup before curating `disease_term`/`mappings`.
2. **No verified HPO term IDs** in this pass — all suggested HP terms above are first-pass candidates requiring OAK confirmation.
3. **No genetic etiology** — `genetic:` block should likely be omitted or explicitly annotated as not-applicable; strong NEC risk if genetic-rumination (cognitive/depressive construct) literature is mistakenly cited.
4. **No animal/cellular disease model** — `model_organisms` section will be essentially empty beyond noting the absence and the tangential gastric-distension neuroimaging literature.
5. Quantitative statistics (prevalence, weight-loss %, treatment response rates) derive mostly from **single-center case series**, not population-representative registries — should be flagged as such in evidence `notes`/`explanation` fields.
6. Distinguish carefully in curation between the **two ICD-11 codes** (6B85 mental/behavioral vs. DD90.6 digestive-disease) and the **DSM-5 vs. Rome IV** classification traditions, which frame the same clinical phenomenon differently and carry different comorbidity/exclusion criteria.

## Sources

- [Rumination Disorder - StatPearls - NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK576404/)
- [Rumination syndrome - Wikipedia](https://en.wikipedia.org/wiki/Rumination_syndrome)
- [Review article: the pathophysiology, differential diagnosis and management of rumination syndrome - PubMed](https://pubmed.ncbi.nlm.nih.gov/21303399/)
- [Rumination syndrome: pathophysiology, diagnosis, and treatment - Absah et al., Neurogastroenterology & Motility 2017](https://onlinelibrary.wiley.com/doi/10.1111/nmo.12954)
- [Current state of rumination syndrome - Diseases of the Esophagus](https://academic.oup.com/dote/article/37/9/doae041/7671046) / [PubMed](https://pubmed.ncbi.nlm.nih.gov/38741462/)
- [Diagnosis and Treatment of Rumination Syndrome - Clinical Gastroenterology and Hepatology](https://www.cghjournal.org/article/S1542-3565(18)30602-5/fulltext)
- [The role of high-resolution impedance manometry to identify rumination syndrome in children with unexplained foregut symptoms - PubMed](https://pubmed.ncbi.nlm.nih.gov/38385686/)
- [Objective manometric criteria for the rumination syndrome - PubMed](https://pubmed.ncbi.nlm.nih.gov/24366235/)
- [Rumination Syndrome: Unknown Pathology Easy to Diagnose With High-resolution Impedance Manometry - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6034670/)
- [Role of Vagal Tone in Rumination Syndrome - ClinicalTrials.gov (NCT03912636)](https://clinicaltrials.gov/study/NCT03912636)
- [Rumination syndrome: Assessment of vagal tone during... - PubMed](https://pubmed.ncbi.nlm.nih.gov/32383546/)
- [The autonomic phenotype of rumination - PubMed](https://pubmed.ncbi.nlm.nih.gov/19272312/)
- [Diaphragmatic breathing for rumination syndrome: efficacy and mechanisms of action - Halland et al., Neurogastroenterology & Motility 2016](https://onlinelibrary.wiley.com/doi/abs/10.1111/nmo.12737)
- [Rumination syndrome: when to suspect and how to treat - PubMed](https://pubmed.ncbi.nlm.nih.gov/31116102/)
- [Rumination syndrome in children and adolescents: a school survey assessing prevalence and symptomatology - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3538663/)
- [Prevalence of pica and rumination behaviours in adults... - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9220787/)
- [Eating and Psychiatric Disorders Are Independent Risk Factors for Rumination Syndrome - PubMed](https://pubmed.ncbi.nlm.nih.gov/33988353/)
- [Eating Disorders and Other Psychiatric Disorders May Increase Risk for Rumination Syndrome - Gastroenterology Advisor](https://www.gastroenterologyadvisor.com/news/eating-disorders-psychiatric-disorders-increased-risk-rumination-syndrome/)
- [ICD-11 Criteria for Rumination-Regurgitation Disorder (6B85)](https://www.mrcpsych.uk/2022/05/icd-11-criteria-for-rumination.html)
- [DD90.6 Adult rumination syndrome - ICD-11 MMS](https://www.findacode.com/icd-11/code-55732315.html)
- [6B85 Rumination-regurgitation disorder - ICD-11 MMS](https://www.findacode.com/icd-11/code-1205760590.html)
- [2025 ICD-10-CM Diagnosis Code F98.21](https://www.icd10data.com/ICD10CM/Codes/F01-F99/F90-F98/F98-/F98.21)
- [Subtotal Gastrectomy as "Last Resort" Consideration in the Management of Refractory Rumination Syndrome - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5040524/) / [PubMed](https://pubmed.ncbi.nlm.nih.gov/27785277/)
- [Is Nissen Fundoplication Surgery Efficacious for the... - ACG Journal](https://journals.lww.com/ajg/fulltext/2015/10001/is_nissen_fundoplication_surgery_efficacious_for.1719.aspx)
- [Belching Disorders and Rumination Syndrome: A Literature Review - Digestion (Karger)](https://karger.com/dig/article/105/1/18/864318/Belching-Disorders-and-Rumination-Syndrome-A)
- [Rumination disorder - Symptoms, Causes and Treatments - Vulgaris Médical](https://www.vulgaris-medical.com/en/encyclopedie-medicale/merycisme)
- [Genome-wide association analysis reveals KCTD12 and miR-383-binding genes in the background of rumination - Translational Psychiatry](https://www.nature.com/articles/s41398-019-0454-1)
- [Genetic and environmental influences on rumination and its covariation with depression - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4111768/) / [PubMed](https://pubmed.ncbi.nlm.nih.gov/24499019/)
- [A Multimodal Approach to Treatment and Management of Rumination Syndrome in a California Sea Lion (Zalophus californianus) - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12562190/)
- [Rumen Physiology and Rumination - Colorado State University](https://vivo.colostate.edu/hbooks/pathphys/digestion/herbivores/rumination.html)
- [A New Approach to Recording Rumination Behavior in Dairy Cows - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11398270/)
- [Using rumination time to manage health and reproduction in dairy cattle: a review - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8547861/)
- [Neuroimaging model of visceral manipulation in awake rat - bioRxiv](https://www.biorxiv.org/content/10.1101/2024.09.17.613477.full.pdf)
- [Rumination syndrome: Critical review - Gastroenterología y Hepatología (English Edition)](https://www.elsevier.es/en-revista-gastroenterologia-hepatologia-english-edition--382-articulo-rumination-syndrome-critical-review-S2444382422000189)
- [Rumination Syndrome - Mayo Clinic Proceedings](https://www.mayoclinicproceedings.org/article/S0025-6196(11)63571-4/fulltext)