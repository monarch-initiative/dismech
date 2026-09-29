---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-18T11:56:03.145839'
end_time: '2026-09-18T12:00:21.036662'
duration_seconds: 257.89
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Scorpion Envenomation
  mondo_id: MONDO:0018755
  category: Injury
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
  num_turns: 25
  total_cost_usd: 1.6815448000000004
  session_id: dc83c613-1fba-53b8-9741-f63fb2448a6e
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 62
reference_validation:
  total_references: 47
  verified: 47
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 47
  on_topic: 27
  validator_version: 0.2.1
term_validation:
  total_terms: 45
  verified: 44
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 25
  labels_matching: 14
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0001649
    reported_labels:
    - 'Sympathetic predominance: tachycardia'
    ontology_label: Tachycardia
  - term_id: HP:0001662
    reported_labels:
    - 'Parasympathetic predominance: bradycardia'
    ontology_label: Bradycardia
  - term_id: CL:0011105
    reported_labels:
    - parasympathetic neuron
    ontology_label: dopamanergic interplexiform cell
  - term_id: UBERON:0001911
    reported_labels:
    - "skin of body \u2014 sting site, typically extremities"
    ontology_label: mammary gland
  labels_variant: 7
  obsolete_terms:
  - term_id: HP:0031297
    ontology_label: obsolete Coronary sinus atrial septal defect
    replaced_by: HP:0011643
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Scorpion Envenomation
- **MONDO ID:** MONDO:0018755 (if available)
- **Category:** Injury

## Research Objectives

Please provide a comprehensive research report on **Scorpion Envenomation** covering all of the
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

I now have comprehensive material across all sections. Let me compile the full research report.

# Scorpion Envenomation — Comprehensive Research Report

## 1. Disease Information

**Overview.** Scorpion envenomation is the clinical syndrome produced by injection of venom through the telson (stinger) of a scorpion, ranging from a trivial local sting to a life-threatening toxicological emergency dominated by autonomic "storm," neuromuscular hyperexcitability, and cardiopulmonary collapse. Of more than 2,900 described scorpion species, roughly 100 (nearly all in family Buthidae) are of medical significance (Medscape/eMedicine overview; PMC8158070 "Neurological and Systemic Manifestations of Severe Scorpion Envenomation"). It is classified by WHO among the neglected tropical diseases of high public-health relevance in endemic regions (PMC12170520, "Scorpionism: a neglected tropical disease with global public health implications," 2025).

**Key identifiers.**
- MONDO: MONDO:0018755 (scorpion envenomation; "has cause: scorpion sting")
- ICD-10-CM: T63.2 (Toxic effect of venom of scorpion), with subcodes T63.2X1– (accidental), T63.2X3– (assault), T63.2X4– (undetermined)
- MeSH: "Scorpion Stings" (D012620)
- Note: this is an **injury/toxicological** entry rather than a classical Mendelian or complex genetic disease — OMIM/Orphanet do not carry a disease record for it (consistent with the "Injury" category assigned to this stub).

**Synonyms/alternative names:** scorpionism, scorpion sting, scorpion stinging, scorpion poisoning, scorpion toxicosis (veterinary literature).

**Evidence basis.** Information is derived overwhelmingly from aggregated clinical/epidemiologic case series, hospital cohorts, and national poison-control/registry data (Mexico, Brazil, Iran, Tunisia, Morocco, India) rather than individual-patient EHR mining, supplemented by controlled clinical trials of antivenom and toxin-mechanism studies in animal/cell models.

Sources: [Scorpion Envenomation – Medscape](https://emedicine.medscape.com/article/168230-overview) · [Neurological and Systemic Manifestations of Severe Scorpion Envenomation – PMC8158070](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8158070/) · [Scorpionism: a neglected tropical disease – PMC12170520](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12170520/) · [scorpion envenomation – Wikidata Q55788313](https://www.wikidata.org/wiki/Q55788313) · [ICD-10 T63.2X1A – icd10data.com](https://www.icd10data.com/ICD10CM/Codes/S00-T88/T51-T65/T63/T63.2-/T63.2X1A)

---

## 2. Etiology

**Disease causal factor:** direct envenomation — injection of a complex peptide/protein venom through the scorpion telson. This is a mechanistic/toxicological (not genetic) etiology; there is no host causal gene. All "risk factors" below are risk factors for **exposure** or for **severity of envenomation**, not for genetic disease susceptibility per se.

**Genetic risk/modifier factors (host side):** None established as disease-causing loci. The closest analogues in the literature are (a) age-dependent physiologic vulnerability (smaller body mass, immature autonomic/cardiovascular reserve in children) rather than a genotype, and (b) individual "sensitivity to venom" invoked qualitatively by Ministry of Health severity models without a defined genetic marker (PMC10615126, "Moderate or severe scorpion sting: identification of risk factors").

**Environmental/exposure risk factors:**
- **Geography** — seven historically recognized high-risk regions: North Saharan Africa, Sahelian Africa, southern Africa, Near/Middle East, South India, Mexico, and northern South America/Amazon basin east of the Andes, covering an estimated 2.3 billion people at risk (Chippaux & Goyffon 2008, PMID:18579104, *Acta Tropica* 107:71-79).
- **Occupation** — farming, agricultural labor, firewood collection, animal husbandry (handling ducks/hens), and rural residence.
- **Housing quality** — thatched roofs, cracks/crevices in walls and floors that harbor scorpions; sleeping on the floor without a bed net.
- **Age** — children under 15, and especially under 5–10 years, are disproportionately at risk of severe/fatal envenomation because of lower body mass amplifying effective venom dose per kg (multiple sources below).
- **Sting location** — stings on the torso, head, or neck (closer to central circulation) predict faster systemic absorption and greater severity than distal-limb stings.
- **Time-to-treatment** — delay >3 hours between sting and antivenom/hospital care is an independent severity predictor.
- **Climate/behavior** — scorpion activity (and sting incidence) rises with warm-season nocturnal foraging.

**Protective factors (environmental):** footwear use, bed nets suspended below thatched roofs, sealing of household cracks/crevices, shaking out shoes/bedding before use, improved rural healthcare access enabling rapid antivenom administration, and community education/awareness campaigns.

**Gene–environment interactions:** not characterized in the literature as a formal GxE model; the closest is pharmacogenomic variability in individual antivenom/catecholamine response, which remains unstudied at a population-genetic level.

Sources: [Epidemiology of scorpionism: a global appraisal – PMID:18579104](https://pubmed.ncbi.nlm.nih.gov/18579104/) · [Scorpionism at the human–environment interface – PMC13006650](https://pmc.ncbi.nlm.nih.gov/articles/PMC13006650/) · [Moderate or severe scorpion sting: risk factors – PMC10615126](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10615126/) · [DHMOSH UN Guidance for Prevention/Management of Scorpion Stings](https://operationalsupport.un.org/sites/default/files/2026-01/DHMOSH%20Guidance%20for%20the%20Prevention%20and%20Management%20of%20Scorpion%20Stings%20-%20English.pdf)

---

## 3. Phenotypes

### Local phenotypes (signs)
- **Local pain/paresthesia at sting site** — nearly universal, immediate, often severe and out of proportion to visible findings for buthid stings (HP:0012531 Pain / HP:0040218 Paresthesia). Onset: immediate. Frequency: ~99–100% for most species.
- **Erythema, edema, tenderness** (HP:0010783 Erythema) — mild local envenomation category, estimated ~68.6% of cases.
- **Skin necrosis / bullae / ulceration** — characteristic of cytotoxic species (*Hemiscorpius lepturus*), classically delayed and initially **painless**, evolving over days (HP:0031297 Skin ulcer). PMID:9679690 "Cutaneous manifestations of the Hemiscorpius lepturus sting."

### Systemic/autonomic phenotypes
- **Autonomic "storm"** — mixed sympathetic and parasympathetic hyperactivity: tachycardia, hypertension, diaphoresis, hypersalivation, lacrimation, vomiting (cholinergic "SLUDGE" pattern) followed often by a later parasympathetic/hypotensive phase.
  - Sympathetic predominance: tachycardia (HP:0001649), hypertension (HP:0000822), hyperthermia (HP:0001945), pulmonary edema (HP:0100598).
  - Parasympathetic predominance: bradycardia (HP:0001662), hypotension (HP:0002615), sialorrhea/hypersalivation (HP:0002307), lacrimation, priapism (HP:0030731) — reported as a Grade II severity feature in children, pathogenically linked to acetylcholine-driven parasympathetic activation.
- **Cardiotoxicity** — arrhythmia, myocarditis, cardiogenic shock, congestive heart failure; onset can be within 2 hours of the sting. Reported mortality in confirmed scorpion myocarditis ≈7.3% (PLOS NTD systematic review, PMID:37018229).
- **Pulmonary edema/respiratory failure** — leading proximate cause of death; occurs with or without hemoptysis in 7–32% of respiratory cases; mechanism combines direct toxin-induced increased pulmonary vascular permeability with catecholamine-driven afterload/hypoxia.
- **Neuromuscular hyperexcitability** — fasciculations, tremor, opsoclonus/roving eye movements, trismus, dysarthria, cranial-nerve hyperactivity (HP:0001336 Myoclonus, HP:0002378 Fasciculations).
- **Gastrointestinal** — nausea, vomiting, abdominal pain, hypersalivation, and **acute pancreatitis** — hyperamylasemia in ~80% of a case series, elevated immunoreactive cationic trypsin in 93% of pediatric cases after *Leiurus quinquestriatus* stings (PMID:2028471).
- **Endocrine/metabolic** — stress hyperglycemia mediated by catecholamine/counter-regulatory hormone release, correlating with severity (recent 2025/2026 cohort, PMC12974955).
- **Hematologic/renal (cytotoxic species, e.g., *Hemiscorpius lepturus*)** — intravascular hemolysis, disseminated intravascular coagulation, acquired ADAMTS13 deficiency, hemolytic-uremic syndrome, acute kidney injury (PMID:23893367; PMC2813541; PMC11872030).
- **Neurological complications (rare)** — ischemic and hemorrhagic stroke, seizures, altered consciousness/coma (systematic review, PMC11403367).
- **Local mechanical/traumatic sequelae** — massive tissue defect reconstruction case reports for severe cytotoxic necrosis.

### Phenotype characteristics
- **Onset:** typically minutes (local pain, autonomic symptoms); systemic/cardiopulmonary complications generally manifest within 1–6 hours, occasionally up to 24 hours.
- **Severity/frequency by grade** (commonly used 3–4 tier systems):
  - Mild (Grade I): local pain ± paresthesia only — most common (~68.6% in one classification).
  - Moderate (Grade II/III): ascending local signs, mild systemic signs, sweating, vomiting, tachycardia/tachypnea, hypertension, cranial-nerve involvement, twitching (~26.8%).
  - Severe (Grade IV): profuse vomiting/sweating/salivation, seizures, coma, bradycardia, heart failure, severe pulmonary edema, shock — life-threatening.
- **Progression:** typically rapid (hours) rather than chronic; most survivors resolve within 24–48 hours with or without antivenom.
- **Quality of life:** acute, self-limited in the majority; severe cases can leave residual organ dysfunction (renal, cardiac) or, rarely, neurological deficits after stroke. Formal EQ-5D/SF-36 data specific to scorpion envenomation are not established in the literature reviewed.

Sources: [Scorpion Envenomation Clinical Presentation – Medscape](https://emedicine.medscape.com/article/168230-clinical) · [Classification of clinical consequences of scorpion stings: consensus development](https://www.sciencedirect.com/science/article/abs/pii/S0035920311000617) · [Neurological and Systemic Manifestations – PMC8158070](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8158070/) · [Scorpion envenomation-associated myocarditis: systematic review – PMID:37018229](https://pubmed.ncbi.nlm.nih.gov/37018229/) · [Acute pancreatitis following Leiurus quinquestriatus envenomation – PMID:2028471](https://pubmed.ncbi.nlm.nih.gov/2028471/) · [Predictive value of admission blood glucose – PMC12974955](https://pmc.ncbi.nlm.nih.gov/articles/PMC12974955/) · [Stroke as a rare complication of scorpion stings – PMC11403367](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11403367/) · [ADAMTS13 deficiency after hemolysis – PMID:23893367](https://pubmed.ncbi.nlm.nih.gov/23893367/) · [Cutaneous manifestations of Hemiscorpius lepturus sting – PMID:9679690](https://pubmed.ncbi.nlm.nih.gov/9679690/) · [Scorpion Envenomation with Delayed Ischemic Priapism – AJTMH](https://www.ajtmh.org/abstract/journals/tpmd/111/4/article-p911.xml)

---

## 4. Genetic/Molecular Information

Scorpion envenomation has **no human causal gene** — it is toxin-mediated, not a Mendelian disease. The relevant "genetic/molecular" content is the **venom toxin** side:

**Venom toxin classes (the causal molecular agents):**
- **Long-chain neurotoxins acting on voltage-gated Na⁺ channels (Nav):**
  - **α-NaTx (α-scorpion toxins, receptor site 3):** bind the voltage-sensing domain IV (VSD4) of Nav channels and **inhibit fast inactivation**, prolonging Na⁺ current and depolarization. Structural work (cryo-EM, 3.5 Å) resolved a eukaryotic Nav channel in complex with the lethal α-toxin AaH2, showing it wedges into VSD4 and traps a deactivated gating-charge state ("Structural basis of α-scorpion toxin action on Nav channels," *Science*, DOI:10.1126/science.aav8573; PNAS PMID for site mapping: PMC3696675 "Modular Organization of α-Toxins").
  - **β-NaTx (β-scorpion toxins, receptor site 4):** bind the S3b–S4 voltage-sensor paddle of domain II and **shift voltage-dependence of activation to more hyperpolarized potentials**, lowering the threshold for channel opening and causing repetitive/spontaneous firing (Rockefeller *J Gen Physiol* review of excitatory/depressant β-toxin modes).
  - Net physiological effect: massive, uncontrolled presynaptic neurotransmitter release (acetylcholine at parasympathetic terminals; norepinephrine/epinephrine at sympathetic terminals and adrenal medulla), producing the autonomic storm.
- **K⁺ channel toxins (KTx, α/β/γ/κ families):** block Kv channels, further prolonging depolarization and neurotransmitter release; e.g., α-KTx4.9 from *Tityus fasciolatus*.
- **Bradykinin-potentiating peptides (BPPs) and natriuretic-like/hypotensin peptides** (e.g., *Tityus serrulatus* Hypotensins, TsHpt) — contribute to vascular tone changes.
- **Enzymes:** hyaluronidase (spreading factor), metalloproteinases, phospholipases.
- **Cytolytic/hemolytic toxins** (notably *Hemiscorpius lepturus*): lysophospholipase D and related lytic enzymes causing cell-membrane lysis, hemolysis, and tissue necrosis — mechanistically distinct from the neurotoxic Buthidae venoms.

**Nomenclature note for dismech curation:** because there is no host causal gene, this section is best modeled via **CHEBI** (venom peptide/small-molecule mediators — e.g., acetylcholine CHEBI:15355, epinephrine CHEBI:33568, norepinephrine CHEBI:33569, prostaglandin E2 CHEBI:15551) and **GO molecular function/biological process** terms rather than HGNC gene bindings. The Nav1.x / Kv channel *targets* in the human host can be annotated with HGNC gene symbols where the specific isoform is documented (e.g., SCN9A/Nav1.7 hgnc:10598, SCN4A/Nav1.4 hgnc:10593) — the referenced study "CeII8/CeII9" toxins are isoform-selective for Nav1.7 vs Nav1.4 (PMID:20600228).

**Allele frequency / somatic-germline / ACMG classification:** not applicable — this is not a variant-based disease.

**Modifier genes:** none established; host channel isoform expression pattern (which Nav/Kv subtypes are expressed at a given synapse) determines tissue-specific toxin effect but is not itself a "modifier gene" in the ACMG sense.

**Epigenetics/chromosomal abnormalities:** not applicable.

Sources: [Structural basis of α-scorpion toxin action on Nav channels – Science](https://www.science.org/doi/10.1126/science.aav8573) · [Modular Organization of α-Toxins – PMC3696675](https://ncbi.nlm.nih.gov/pmc/articles/PMC3696675) · [Scorpion β-toxin interference with NaV channel voltage sensor – J Gen Physiol](https://rupress.org/jgp/article/139/4/305/43010/) · [Mapping the receptor site for α-scorpion toxins – PNAS](https://www.pnas.org/doi/10.1073/pnas.1112320108) · [CeII8/CeII9 Nav1.7/Nav1.4-selective toxins – PMID:20600228](https://pubmed.ncbi.nlm.nih.gov/20600228/) · [Novel components of Tityus serrulatus venom – transcriptomic approach](https://ouci.dntb.gov.ua/en/works/lmxaKaD4/) · [Tityus serrulatus Hypotensins](https://www.sciencedirect.com/science/article/abs/pii/S0006291X08007936) · [Purification of neurotoxic peptides from Hemiscorpius lepturus – PMC7211352](https://pmc.ncbi.nlm.nih.gov/articles/PMC7211352/)

---

## 5. Environmental Information

**Environmental factor = the disease trigger itself:** scorpion envenomation is, by definition, an environmentally/mechanically caused injury (ECTO/exposure framing: exposure to scorpion venom via sting). There are no separate "contributing" environmental toxins in the classic sense, though secondary environmental modifiers include:
- **Ambient temperature/season** — scorpion activity and human outdoor/nocturnal exposure both increase in hot months, raising sting incidence.
- **Housing construction materials** (thatch, mud-brick with crevices) enabling scorpion cohabitation with humans.
- **Rural/agricultural occupational exposure** (see Etiology above).

**Lifestyle factors:** going barefoot, sleeping on the floor, not shaking out shoes/clothing before use, storing firewood/rubble near dwellings.

**Infectious agents:** not applicable — scorpion envenomation is not infectious, though secondary wound infection of necrotic cytotoxic lesions (e.g., from *Hemiscorpius*) can occur as a complication, not an etiologic agent.

Sources: [Scorpionism at the human–environment interface – PMC13006650](https://pmc.ncbi.nlm.nih.gov/articles/PMC13006650/) · [DHMOSH UN Guidance](https://operationalsupport.un.org/sites/default/files/2026-01/DHMOSH%20Guidance%20for%20the%20Prevention%20and%20Management%20of%20Scorpion%20Stings%20-%20English.pdf)

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Venom injection** via telson delivers a mixture of Na⁺-channel toxins (α-NaTx, β-NaTx), K⁺-channel toxins, phospholipases/hyaluronidase, and (in cytotoxic species) lytic enzymes into subcutaneous tissue → **leads to** local nociceptor activation (intense pain) and, for neurotoxic Buthidae venoms, rapid systemic absorption.
2. α-NaTx binds Nav channel VSD4 and blocks fast inactivation; β-NaTx binds Nav channel domain II voltage sensor and lowers the activation threshold → **leads to** prolonged Na⁺ influx and repetitive, uncontrolled action-potential firing at peripheral and autonomic nerve terminals (demonstrated structurally for AaH2-Nav complex, *Science* 2019).
3. Repetitive firing at **sympathetic** postganglionic terminals and the **adrenal medulla** → **results in** massive release of norepinephrine and epinephrine ("catecholamine storm") → tachycardia, hypertension, diaphoresis, hyperglycemia (via counter-regulatory hormone release), and increased myocardial oxygen demand.
4. Simultaneous repetitive firing at **parasympathetic (cholinergic)** terminals → **results in** acetylcholine release → bradycardia (in the later/mixed phase), hypersalivation, lacrimation, gastric hypermotility, priapism.
5. Catecholamine excess → **leads to** (a) direct catecholamine-induced myocardial injury ("adrenergic/toxic myocarditis," inflammatory infiltrate), and (b) increased myocardial O₂ demand with relative coronary hypoperfusion → myocardial ischemia — three convergent mechanisms proposed for cardiac dysfunction: adrenergic myocarditis, toxic (direct venom) myocarditis, and ischemia (PLOS NTD systematic review, PMID:37018229).
6. In parallel, venom (and the host inflammatory response to it) triggers **IL-1 receptor signaling** → **induces** prostaglandin E2 (PGE2) production → PGE2 **drives** excessive acetylcholine release at the heart via vagal efferents → **causes** acetylcholine-mediated cardiac dysfunction, heart failure, and death in a validated mouse model; IL-1R deficiency, dexamethasone, atropine, or vagotomy each abolish this pathway and prevent mortality (Nature Communications 2020, PMID/PMC7595177 — direct mechanistic/causal evidence, MODEL_ORGANISM).
7. A parallel IL-1R→nitric-oxide pathway in the pancreas has been shown to **control** hyperglycemia after envenomation (PMC7150851), linking the inflammatory cascade to the metabolic phenotype described in Section 3.
8. Direct toxin action plus catecholamine/cytokine-driven increases in pulmonary vascular permeability → **leads to** noncardiogenic-plus-cardiogenic pulmonary edema, the dominant proximate cause of death, sometimes with hemoptysis.
9. Combined cardiogenic (myocarditis/arrhythmia) and pulmonary (edema, hypoxia) failure → **results in** cardiogenic/cardiopulmonary shock, the terminal common pathway in fatal cases, typically within the first hours to ~24 hours after the sting.
10. **Branch — cytotoxic (non-neurotoxic) venoms (e.g., *Hemiscorpius lepturus*):** lysophospholipase D and other lytic enzymes directly lyse cell membranes at the sting site and systemically → **leads to** local dermonecrosis (initially painless) plus intravascular hemolysis, complement/coagulation activation, acquired ADAMTS13 deficiency (with autoantibody formation) → **results in** disseminated intravascular coagulation, thrombotic microangiopathy, and hemolytic-uremic syndrome with acute kidney injury — a mechanistically distinct downstream chain from the Nav/Kv-driven autonomic-storm pathway above.
11. **Branch — pancreatic injury:** autonomic hyperstimulation (direct cholinergic/adrenergic overactivity on acinar cells) plus possible direct venom enzymatic effects → **leads to** acute pancreatitis (elevated amylase/trypsinogen), contributing to abdominal pain/vomiting.
12. **Branch — neurological:** severe hypertensive surges and coagulopathy (in cytotoxic envenomation) can precipitate hemorrhagic or ischemic stroke; direct venom neuroexcitatory action can produce seizures independent of stroke.

### Detail by mechanistic category
- **Molecular pathways:** Nav/Kv channel gating cascades (not classical signaling pathways like Wnt/MAPK); downstream, IL-1R→cyclooxygenase→PGE2→muscarinic acetylcholine signaling constitutes a defined, experimentally verified pathway (Nature Comm 2020).
- **Cellular processes:** exocytotic neurotransmitter release (GO:0007269 neurotransmission), sympathetic/parasympathetic neuron activation, cardiomyocyte injury/apoptosis-necrosis, inflammatory cytokine release, complement activation, erythrocyte lysis (cytotoxic venoms).
- **Protein dysfunction:** the "dysfunction" is imposed on host ion channels by toxin binding (gain-of-function-like persistent activation), not intrinsic host protein misfolding.
- **Immune involvement:** IL-1β/IL-1R–PGE2 axis is central and causally demonstrated; correlational human data link IL-1β and malondialdehyde (oxidative stress marker) to cardiac/pancreatic complication risk (PMC12670810).
- **Tissue damage mechanisms:** catecholamine-induced myocardial injury, hypoxic/ischemic injury from pulmonary edema, direct cytolysis (Hemiscorpius), oxidative stress (elevated MDA).
- **Advanced/omics data:** proteomic/transcriptomic venom-gland profiling (e.g., *Tityus obscurus* and *T. serrulatus*, PMID:29561852) has catalogued the toxin repertoire (Na/K channel toxins as the dominant "toxin core," alongside metalloproteinases and hyaluronidases) but there is no reported single-cell or spatial transcriptomic human host-response dataset specific to scorpion envenomation.

**Suggested GO terms:** GO:0086010 (membrane depolarization during action potential), GO:0001508 (action potential), GO:0007268 (chemical synaptic transmission), GO:0043473 (pigmentation — n/a), GO:0034405 (response to fluid shear stress — n/a), GO:0006954 (inflammatory response), GO:0019233 (sensory perception of pain), GO:0001516 (prostaglandin biosynthetic process), GO:0007613 (memory — n/a). **Suggested CL terms:** CL:0000101 (sensory neuron), CL:0011103 (sympathetic neuron), CL:0011105 (parasympathetic neuron), CL:0000746 (cardiac muscle cell), CL:0000232 (erythrocyte, for hemolytic branch), CL:0000583 (alveolar macrophage — inflammatory branch).

Sources: [Interleukin-1 receptor-induced PGE2 production controls acetylcholine-mediated cardiac dysfunction and mortality – Nat Commun, PMC7595177](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7595177/) · [IL-1R-induced NO production in the pancreas controls hyperglycemia – PMC7150851](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7150851/) · [Scorpion envenomation-associated myocarditis: systematic review – PMID:37018229 / PLOS NTD](https://journals.plos.org/plosntds/article?id=10.1371%2Fjournal.pntd.0011219) · [Cardiovascular dysfunction following severe scorpion envenomation: mechanisms – PMID:15687982](https://pubmed.ncbi.nlm.nih.gov/15687982/) · [Structural basis of α-scorpion toxin action on Nav channels – Science](https://www.science.org/doi/10.1126/science.aav8573) · [Scorpion β-toxin interference with NaV channel voltage sensor – JGP](https://rupress.org/jgp/article/139/4/305/43010/) · [IL-1β/MDA correlation with cardiac and pancreatic complications – PMC12670810](https://pmc.ncbi.nlm.nih.gov/articles/PMC12670810/) · [Proteomic/transcriptomic venom gland profiles – PMID:29561852](https://pubmed.ncbi.nlm.nih.gov/29561852/) · [High frequency of acquired ADAMTS13 deficiency – PMID:23893367](https://pubmed.ncbi.nlm.nih.gov/23893367/)

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** skin/subcutis (sting site), autonomic nervous system, heart, lungs.
- **Secondary:** pancreas (pancreatitis), kidneys (AKI, especially cytotoxic species), brain (stroke, seizures — rare), eyes (periocular sting → corneal ulceration case report), genital vasculature (priapism).
- **Body systems:** cardiovascular, respiratory, nervous (peripheral autonomic + central), endocrine/metabolic, hematologic (cytotoxic species), integumentary.

**Tissue/cell level:** peripheral sensory and autonomic (sympathetic and parasympathetic) neurons and nerve terminals; cardiomyocytes; pulmonary capillary endothelium (increased permeability); pancreatic acinar cells; renal tubular/glomerular endothelium (thrombotic microangiopathy in cytotoxic envenomation); erythrocytes (hemolysis).

**Subcellular level:** plasma-membrane voltage-gated Na⁺ and K⁺ channels (site of primary toxin action; GO Cellular Component: GO:0005248 voltage-gated sodium channel activity is a molecular function, GO:0034706 sodium channel complex is the CC term); synaptic vesicles (neurotransmitter exocytosis); mitochondria (secondary oxidative-stress injury).

**Localization (UBERON):** UBERON:0000948 (heart), UBERON:0002048 (lung), UBERON:0001264 (pancreas), UBERON:0002113 (kidney), UBERON:0001911 (skin of body — sting site, typically extremities), UBERON:0001021 (nerve), UBERON:0000375 (autonomic nerve — sympathetic/parasympathetic subdivisions).

**Lateralization:** local sting effects are unilateral/focal at the sting site; systemic effects are bilateral/generalized.

Sources: [Cardiac involvement in scorpion envenomation: review](https://www.ijconline.id/index.php/ijc/article/view/1710) · [Corneal ulceration following periocular scorpion sting – PMC11199440](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11199440/) · [Acute kidney injury and pancreatitis due to scorpion sting](https://www.scielo.br/j/rimtsp/a/rZvfqJgs37hLrCCmBsjGnhG/)

---

## 8. Temporal Development

**Onset:** acute, occurring at any age but disproportionately in children; local pain is immediate, systemic/autonomic signs typically within 15 minutes to a few hours, cardiopulmonary complications typically within 1–24 hours.

**Progression:** most cases are **self-limited** over 24–48 hours (mild/moderate); severe envenomation can progress rapidly (hours) to cardiogenic shock, pulmonary edema, or death, particularly in young children with delayed treatment. There is no chronic/relapsing course analogous to a genetic disease, though rare chronic-relapsing pancreatitis has been reported as a late sequela in one case report from Trinidad (PMID:8687203).

**Disease course pattern:** acute, generally monophasic; biphasic autonomic pattern (early sympathetic surge, later parasympathetic/cholinergic phase) is well described clinically.

**Critical period for intervention:** the first several hours after the sting — antivenom is most effective when given early (systematic review/meta-analysis: antivenom reverses the clinical syndrome faster than no treatment; PMID:28390429), and IL-1R/PGE2 pathway blockade (dexamethasone) has been proposed for administration "very early after envenomation, even before antiserum" based on the mouse mechanistic model (PMC7595177).

Sources: [Management of scorpion envenoming: systematic review and meta-analysis – PMID:28390429](https://pubmed.ncbi.nlm.nih.gov/28390429/) · [Chronic relapsing pancreatitis from scorpion sting – PMID:8687203](https://pubmed.ncbi.nlm.nih.gov/8687203/) · [Interleukin-1 receptor-induced PGE2 – PMC7595177](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7595177/)

---

## 9. Inheritance and Population

**Not a genetic/heritable disease** — no inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, or carrier frequency applies.

**Epidemiology:**
- **Global incidence:** estimates range from ~1.2 million (Chippaux & Goyffon 2008, PMID:18579104) to ~1.5 million scorpion stings annually.
- **Global mortality:** >3,000 deaths/year (Chippaux/Goyffon original estimate: >3,250 deaths, 0.27% case fatality across the seven at-risk regions); scorpion envenomation is described as the second leading cause of death from venomous animals after snakebite.
- **Regional burden:** the MENA region accounts for ~42% of the global sting burden and roughly half of related mortality. High-burden countries: Mexico, Brazil, Iran, Algeria, Morocco, Tunisia, India.
- **Age distribution:** children <15 years (especially <5–10 years) bear disproportionate morbidity/mortality.
- **Sex ratio:** not sharply skewed in most series, though occupational exposure patterns can shift regional sex ratios (e.g., higher male exposure in agricultural work).
- **Geographic variant distribution:** species-specific — *Centruroides sculpturatus* (Sonoran Desert bark scorpion) in the US Southwest/Mexico; *Androctonus australis* (North Africa, probably the most lethal species worldwide) and *Leiurus quinquestriatus* in North Africa/Middle East; *Mesobuthus tamulus* (Indian red scorpion) on the Indian subcontinent; *Tityus serrulatus*, *T. bahiensis*, *T. obscurus*, *T. silvestris* (Brazil/French Guiana/Amazon); *Hemiscorpius lepturus* (Iran, cytotoxic syndrome).

Sources: [Epidemiology of scorpionism: a global appraisal – PMID:18579104](https://pubmed.ncbi.nlm.nih.gov/18579104/) · [Scorpionism: neglected tropical disease – PMC12170520](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12170520/) · [Assessing the burden of Scorpionism in NW Iran – PMC12286322](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12286322/) · [Epidemiological patterns in Ecuador – PMC11951006](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11951006/) · [Distribution, biology, and management of medically relevant bark scorpions – Oxford J Integ Pest Mgmt](https://academic.oup.com/jipm/article/17/1/pmag029/8724371)

---

## 10. Diagnostics

**Clinical diagnosis:** history of sting/scorpion sighting plus characteristic local pain and, in moderate-severe cases, autonomic/neuromuscular signs; diagnosis is predominantly clinical, not laboratory-based, for triage.

**Laboratory tests:**
- CBC (leukocytosis common), amylase/lipase (pancreatitis screening), glucose (hyperglycemia, prognostic), creatine kinase (rhabdomyolysis), renal function tests.
- **Cardiac biomarkers:** troponin I shows limited discrimination between mild-moderate and severe groups in pediatric cohorts; **NT-proBNP/proBNP is a more sensitive early predictor of pediatric cardiotoxicity**, significantly elevated in severe cases at admission and at 12–24 hours (PMID:33994108; PMID:33094659). Emerging biomarkers sST2 and FABP-3 show association with LV dysfunction (sensitivity 92.3%) in a recent (2025) study ("New biomarkers in scorpion stings," PMID:39842516).
- Coagulation studies, LDH, haptoglobin, ADAMTS13 activity, and Coombs testing for suspected *Hemiscorpius*-type hemolytic/DIC presentations.

**Imaging:** chest X-ray (pulmonary edema pattern), echocardiography (LV dysfunction, wall-motion abnormalities including takotsubo-like patterns; PMID:26135709 "Scorpion envenomation cardiomyopathy: a promising model for takotsubo syndrome"), cranial CT/MRI when stroke is suspected.

**Electrophysiology:** ECG for arrhythmia/ischemia surveillance (ST-T changes, QT prolongation reported); EEG if seizures.

**Genetic testing:** not applicable — no genetic test exists or is indicated for this condition.

**Histopathology/biopsy:** autopsy series document myocarditis (lymphocytic/catecholaminergic pattern), pulmonary edema, and occasionally pancreatic necrosis in fatal cases (PMC7551928, "Autopsy Findings in Case of Fatal Scorpion Sting: A Systematic Review").

**Clinical severity/diagnostic criteria:** several regionally validated classification systems (3-tier mild/moderate/severe; 4-grade systems incorporating local pain → systemic neuromuscular signs → cardiopulmonary collapse); a "Scorpion Envenomation: ICU Transfer Prediction Score" has recently been proposed (PMC13331192).

**Differential diagnosis:** other envenomations (spider bite, snakebite), acute abdomen/pancreatitis of other cause, myocardial infarction, sepsis, thyroid storm, pheochromocytoma crisis (given catecholamine excess phenotype), organophosphate poisoning (cholinergic overlap).

**Screening:** no population screening applicable; this is an acute injury, not a condition amenable to newborn/carrier screening.

Sources: [The Role of ProBNP on Prognosis in Scorpion Stings – PMID:33994108](https://pubmed.ncbi.nlm.nih.gov/33994108/) · [NT-proBNP as early predictor of pediatric cardiotoxicity – PMID:33094659](https://pubmed.ncbi.nlm.nih.gov/33094659/) · [New biomarkers in scorpion stings – PMID:39842516](https://pubmed.ncbi.nlm.nih.gov/39842516/) · [Scorpion envenomation cardiomyopathy: a takotsubo model – PMID:26135709](https://pubmed.ncbi.nlm.nih.gov/26135709/) · [Autopsy findings in fatal scorpion sting – PMC7551928](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7551928/) · [Scorpion Envenomation: ICU Transfer Prediction Score – PMC13331192](https://pmc.ncbi.nlm.nih.gov/articles/PMC13331192/) · [Diagnostic value of GPX4, IL-13, periostin, thiol/disulfide balance – PMC12629928](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12629928/)

---

## 11. Outcome/Prognosis

**Mortality:** overall case-fatality low (~0.27% globally per Chippaux/Goyffon), but far higher in untreated severe pediatric cases in endemic low-resource settings; confirmed myocarditis cases carry ~7.3% mortality. Pediatric ICU cohorts (e.g., Qena Governorate, Egypt) have specifically studied predictors of in-hospital mortality (PMC6779185).

**Morbidity:** most survivors recover fully within 24–72 hours; severe cases may have prolonged ICU stays (mechanical ventilation required in ~35% of severe respiratory-failure cases in one series) and, rarely, residual renal impairment (post-AKI, especially cytotoxic *Hemiscorpius* cases) or neurological deficits post-stroke.

**Complications:** cardiogenic shock, pulmonary edema, myocarditis/heart failure, acute pancreatitis, AKI/HUS (cytotoxic species), DIC, stroke (rare), priapism, secondary wound infection/necrosis.

**Recovery potential:** generally excellent with prompt supportive care ± antivenom; echocardiographic LV dysfunction (including takotsubo-pattern cardiomyopathy) is typically reversible over days to weeks.

**Prognostic factors:** young age (<5–10 years), delayed time-to-treatment (>3 hours), sting on torso/head/neck, elevated NT-proBNP/sST2/FABP-3, hyperglycemia at admission, species (e.g., *Androctonus australis*, *Tityus serrulatus*, *Centruroides* spp., *Leiurus quinquestriatus* associated with higher lethality than most other genera).

Sources: [Scorpion envenomation-associated myocarditis: systematic review – PMID:37018229](https://pubmed.ncbi.nlm.nih.gov/37018229/) · [Predictors for Mortality in Children, Qena Governorate, Egypt – PMC6779185](https://pmc.ncbi.nlm.nih.gov/articles/PMC6779185/) · [Predictive value of admission blood glucose – PMC12974955](https://pmc.ncbi.nlm.nih.gov/articles/PMC12974955/)

---

## 12. Treatment

**Pharmacotherapy — antivenom (specific antidote):**
- **Species-specific F(ab′)₂ equine antivenom** is first-line for moderate-severe envenomation by medically significant species. Systematic review/meta-analysis of controlled trials (PMID:28390429; PMC5385045) found antivenom against *Centruroides* effective in reversing the clinical syndrome faster than no antivenom (322 participants across 3 trials).
- **Anascorp® (Centruroides [Scorpion] Immune F(ab′)₂, equine)** — FDA-approved August 4, 2011, the first US-approved scorpion antivenom (orphan drug, priority review). Pivotal RCT (Boyer et al., *NEJM* 2009, DOI:10.1056/NEJMoa0808455): 100% resolution of clinical syndrome within 4 hours vs. 14.3% with placebo in 15 pediatric ICU patients with clinically significant *Centruroides* envenomation.
- **Monovalent antivenom against *Mesobuthus tamulus*** (India) combined with prazosin resolves symptoms faster than prazosin alone (mean difference ≈12.6 hours faster).

**Adjunctive/symptomatic pharmacotherapy:**
- **Prazosin** (selective α1-adrenergic antagonist, CHEBI:8364) — counteracts catecholamine-mediated vasoconstriction/peripheral ischemia; established add-on for *M. tamulus* stings; NCIT: C15986 (Pharmacotherapy) as treatment action term, therapeutic_agent CHEBI:8364.
- **Dobutamine** (β1-agonist inotrope) — for myocardial depression/cardiogenic shock, typical infusion 5–10 µg/kg/min (PMID:32428515, "Dobutamine in the treatment of severe scorpion envenoming").
- **Atropine** — for symptomatic bradycardia/excess cholinergic effects (mechanistically supported by the IL-1R/PGE2/acetylcholine pathway study, PMC7595177, where atropine or vagotomy abolished mortality in the mouse model).
- **Corticosteroids (dexamethasone)** — proposed as very-early adjunct based on the same mechanistic model, to blunt IL-1R-driven PGE2/acetylcholine cascade; also explored in a 2024 review of "Immunosuppressive therapies in scorpion envenomation."
- **Levosimendan** — case-report-level evidence for acute heart failure with renal impairment post-severe envenomation (PMC12360093).
- **Diuretics, nitroglycerin, digoxin** — used adjunctively for pulmonary edema/heart failure management per clinical judgement.
- **Analgesics/local anesthetics** — for local pain management in mild cases (most stings require only this).

**Advanced therapeutics under development:**
- **Nanobody (VHH, camelid single-domain antibody)-based antivenoms** — smaller (15 kDa vs. ~100 kDa for F(ab′)₂), better tissue penetration; a camelid antibody candidate against *Hemiscorpius lepturus* venom has been described (PMC5395729), and recombinant scorpion-antivenom production in *E. coli* is an active area (2023 review, Appl Microbiol Biotechnol, DOI:10.1007/s00253-023-12578-1).
- **scFv/VHH recombinant fragments** targeting Na⁺-channel neurotoxins are the focus of most recent pharmaceutical-development work, aiming to reduce serum-sickness risk associated with equine antivenoms.

**Surgical/interventional:** generally not indicated except for debridement/reconstruction of severe necrotic wounds from cytotoxic species (e.g., *Hemiscorpius* neck-defect reconstruction case report) or dialysis for AKI/HUS.

**Supportive/critical care:** cardiac monitoring, mechanical ventilation for respiratory failure (required in ~35% of severe cases in one cohort), ICU admission for grade III/IV envenomation, fluid/electrolyte management, glycemic monitoring.

**Treatment algorithm:** graded, severity-stratified — Grade I/mild: local care + analgesia; Grade II/moderate: antivenom ± prazosin, close monitoring; Grade III/IV/severe: antivenom + ICU-level supportive care (dobutamine, mechanical ventilation, atropine/steroids as adjuncts).

**Experimental/clinical trials:** NCT01599936 (Anascorp pediatric open-label trial), NCT01336660 (equine F(ab′)₂ trial, Morocco), NCT00753064 (AScVS and/or prazosin), NCT00696683 (natural history study), NCT00624078 (Anascorp treatment protocol).

Sources: [Antivenom for Critically Ill Children with Neurotoxicity from Scorpion Stings – NEJM](https://www.nejm.org/doi/full/10.1056/NEJMoa0808455) · [Management of scorpion envenoming: systematic review/meta-analysis – PMID:28390429](https://pubmed.ncbi.nlm.nih.gov/28390429/) · [Dobutamine in the treatment of severe scorpion envenoming – PMID:32428515](https://pubmed.ncbi.nlm.nih.gov/32428515/) · [Emerging options for the management of scorpion stings – PMC3401053](https://pmc.ncbi.nlm.nih.gov/articles/PMC3401053/) · [A camelid antibody candidate against Hemiscorpius lepturus – PMC5395729](https://pmc.ncbi.nlm.nih.gov/articles/PMC5395729/) · [Production of recombinant scorpion antivenoms in E. coli – Appl Microbiol Biotechnol 2023](https://link.springer.com/article/10.1007/s00253-023-12578-1) · [Immunosuppressive therapies in scorpion envenomation – Frontiers Toxicol 2024](https://www.frontiersin.org/journals/toxicology/articles/10.3389/ftox.2024.1503055/full) · [Intravenous Levosimendan case report – PMC12360093](https://pmc.ncbi.nlm.nih.gov/articles/PMC12360093/) · [FDA Anascorp label](https://www.fda.gov/media/81093/download)

---

## 13. Prevention

**Primary prevention:**
- Footwear use outdoors/at night; shaking out shoes, clothing, and bedding before use.
- Bed nets suspended beneath thatched or gapped roofing to prevent scorpions falling onto sleepers.
- Sealing cracks/crevices in walls, floors, and foundations; removing woodpiles/rubble near dwellings; general household decluttering.
- Community/occupational education campaigns for farmers, laborers, and rural residents (identified as most vulnerable groups).

**Secondary prevention:** rapid recognition and healthcare-seeking behavior; training of rural/peripheral healthcare workers in clinical recognition and immediate management, since time-to-treatment >3 hours independently predicts severity.

**Tertiary prevention:** ICU protocols to prevent/limit complications (mechanical ventilation readiness, cardiac monitoring, dialysis access for AKI) in endemic-region referral centers.

**Immunization:** no vaccine exists or is in development for scorpion envenomation (unlike some snake-antivenom vaccine research programs).

**Screening/risk stratification:** clinical severity-grading systems (Section 10) function as triage/risk-stratification tools rather than population screening.

**Genetic counseling:** not applicable.

**Public health/environmental interventions:** vector (scorpion) control around dwellings, improved housing construction standards, national/regional scorpion-sting surveillance and reporting systems (as increasingly implemented in Mexico, Iran, Ecuador).

Sources: [Scorpionism at the human–environment interface – eco-epidemiological synthesis – PMC13006650](https://pmc.ncbi.nlm.nih.gov/articles/PMC13006650/) · [DHMOSH UN Guidance for the Prevention and Management of Scorpion Stings](https://operationalsupport.un.org/sites/default/files/2026-01/DHMOSH%20Guidance%20for%20the%20Prevention%20and%20Management%20of%20Scorpion%20Stings%20-%20English.pdf) · [Scorpionism: neglected tropical disease with global public health implications – PMC12170520](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12170520/)

---

## 14. Other Species / Natural Disease

**Veterinary relevance:** scorpion envenomation is a recognized cause of acute illness in domestic animals, especially dogs and cats in endemic regions.
- A case report of a *Tityus bahiensis* sting in a small-breed dog documented pain, aggressiveness, tachypnea, tachycardia, and local erythema, resolving within 24 hours of supportive treatment (Brazil, ScienceDirect/SciELO case report).
- A retrospective study of 11 dogs and 1 cat with scorpionism in Manizales, Colombia (2009–2018) found no fatalities; two severe and five moderate cases, with local pain and limb lameness as the primary presenting signs (PMID:31563524).
- Death in animals, as in humans, occurs via cardiocirculatory failure and pulmonary edema.
- Corneal ulceration following periocular scorpion sting has been reported (case report context; primarily human but illustrates ocular local-toxicity mechanism relevant across species) — PMC11199440.

**Comparative biology:** the Nav/Kv channel toxin mechanism is broadly conserved across mammals (and indeed across the arthropod prey targeted by these toxins in nature), which is why rodent (mouse, rat, guinea pig) and canine/feline models recapitulate core neuroexcitatory and cardiovascular phenotypes, though species-specific LD50 differences are substantial (e.g., toxicity of *Buthus tamulus* venom varies by age and species — LD50 in mice 7.2±1.35 vs. adult rats/guinea pigs 1.14±0.08, PMID:8146875).

**Zoonotic potential:** not applicable — scorpion envenomation is an injury, not a transmissible/zoonotic infectious disease.

Sources: [Envenomation by scorpion in dog: case report](https://www.scielo.br/j/jvatitd/a/BrMjdK9tkFyjGvRxNBr9DKn/) · [Retrospective study of scorpionism in 11 dogs and a cat, Colombia – PMID:31563524](https://pubmed.ncbi.nlm.nih.gov/31563524/) · [Toxicity of scorpion (Buthus tamulus) venom: age/species influence – PMID:8146875](https://pubmed.ncbi.nlm.nih.gov/8146875/) · [Merck Veterinary Manual: Spider and Scorpion Bites/Stings to Animals](https://www.merckvetmanual.com/toxicology/bites-and-stings-from-spiders-scorpions-and-insects/spider-and-scorpion-bites-and-stings-to-animals)

---

## 15. Model Organisms

**Rodent (mouse/rat) models** are the dominant experimental system:
- **Mechanistic causal model:** the IL-1R–PGE2–acetylcholine cardiac-dysfunction pathway was established in a **mouse envenomation model**, with genetic (IL-1R-knockout) and pharmacologic (dexamethasone, atropine, vagotomy) interventions each abolishing mortality — a high-fidelity, causally interrogable model of the human cardiotoxic phenotype (PMC7595177, *Nat Commun* 2020).
- **Hyperglycemia model:** a parallel mouse model demonstrated an IL-1R–nitric oxide pancreatic pathway controlling venom-induced hyperglycemia (PMC7150851).
- **LD50/toxicity models:** intraperitoneal or intracisternal venom injection in mice is the standard lethality assay across many species' venoms (e.g., *Leiurus quinquestriatus* IP LD50 ≈0.25–0.50 mg/kg; *Hemiscorpius lepturus* LD50 ≈177 µg/mouse); species- and age-dependent toxicity has been demonstrated across mice, rats, and guinea pigs (PMID:8146875).
- **Electrophysiology models:** mouse phrenic nerve–hemidiaphragm and sciatic nerve preparations are used to study venom-induced neurotoxicity at the neuromuscular junction (e.g., *Odontobuthus doriae* venom studies, PMC3813362).
- **Cardiomyopathy model:** rat/experimental models of scorpion-envenomation cardiomyopathy have been proposed as a naturally occurring analog of human takotsubo (stress) cardiomyopathy (PMID:26135709), offering a translational bridge for catecholamine-cardiotoxicity research generally.
- **Histopathology models:** *Hemiscorpius lepturus* venom injected in mice reproduces the cytotoxic/hemolytic/nephrotoxic phenotype seen in human envenomation, supporting model validity for the cytotoxic-species branch of pathophysiology.

**Model recapitulation vs. limitations:** rodent models robustly recapitulate the acute autonomic/cardiotoxic and cytotoxic (Hemiscorpius) phenotypes and have been directly used to establish causal mechanism (not merely correlation) for the IL-1R/PGE2/acetylcholine pathway — an unusually strong (`RECAPITULATES`-grade) evidentiary link for a toxin-mediated syndrome. Limitations include species-dependent LD50/sensitivity differences (rodents vs. primates/humans) and the absence of validated large-animal or iPSC-cardiomyocyte models specific to this condition in the literature surveyed.

**Model databases:** no dedicated MGI/IMPC genetic-knockout resource exists for "scorpion envenomation" per se (it is an induced/pharmacologic model, not a genetic strain), but IL1R1-knockout mice (a standard IMPC/MGI-catalogued line) are the specific genetic tool used in the causal cardiotoxicity study above.

Sources: [Interleukin-1 receptor-induced PGE2 production – PMC7595177](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7595177/) · [IL-1R-induced NO production in the pancreas – PMC7150851](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7150851/) · [Scorpion envenomation cardiomyopathy: takotsubo model – PMID:26135709](https://pubmed.ncbi.nlm.nih.gov/26135709/) · [Toxicity of scorpion venom influenced by age/species – PMID:8146875](https://pubmed.ncbi.nlm.nih.gov/8146875/) · [Effects of Odontobuthus doriae venom on mouse sciatic nerve – PMC3813362](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3813362/) · [Histopathological changes induced by Hemiscorpius lepturus venom in mice](https://www.sciencedirect.com/science/article/abs/pii/S0041010111003862)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 47 |
| Resolved | 47 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 47 |
| On topic | 27 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 45 |
| Resolved | 44 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 25 |
| Terms named correctly | 14 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001649` (1 mention) - the report calls it "Sympathetic predominance: tachycardia"; HP calls it **Tachycardia**
- `HP:0001662` (1 mention) - the report calls it "Parasympathetic predominance: bradycardia"; HP calls it **Bradycardia**
- `CL:0011105` (1 mention) - the report calls it "parasympathetic neuron"; CL calls it **dopamanergic interplexiform cell**
- `UBERON:0001911` (1 mention) - the report calls it "skin of body — sting site, typically extremities"; UBERON calls it **mammary gland**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0031297` (obsolete Coronary sinus atrial septal defect) (1 mention) - replaced by `HP:0011643`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0018755` (1 mention) - the report calls it "scorpion envenomation; "has cause: scorpion sting"; MONDO calls it **scorpion envenomation**
- `GO:0043473` (1 mention) - the report calls it "pigmentation — n/a"; GO calls it **pigmentation**
- `GO:0034405` (1 mention) - the report calls it "response to fluid shear stress — n/a"; GO calls it **response to fluid shear stress**
- `GO:0007613` (1 mention) - the report calls it "memory — n/a"; GO calls it **memory**
- `CL:0000232` (1 mention) - the report calls it "erythrocyte, for hemolytic branch"; CL calls it **erythrocyte**
- `CL:0000583` (1 mention) - the report calls it "alveolar macrophage — inflammatory branch"; CL calls it **alveolar macrophage**
- `UBERON:0000375` (1 mention) - the report calls it "autonomic nerve — sympathetic/parasympathetic subdivisions"; UBERON calls it **mandibular nerve**, and lists "trigeminal nerve mandibular division" among its other names