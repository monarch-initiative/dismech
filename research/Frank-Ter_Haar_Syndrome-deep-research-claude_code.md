---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-04T03:56:37.197445'
end_time: '2026-09-04T04:00:59.203279'
duration_seconds: 262.01
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Frank-Ter Haar Syndrome
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
  web_search_requests: 12
  num_turns: 26
  total_cost_usd: 1.3021753999999996
  session_id: cf062bef-21dd-529d-873d-1df1fa42d833
  stop_reason: end_turn
  assistant_text_blocks: 4
citation_count: 24
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 8
  validator_version: 0.2.1
term_validation:
  total_terms: 50
  verified: 48
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 30
  labels_matching: 20
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0000488
    reported_labels:
    - Macrocornea/megalocornea
    ontology_label: Retinopathy
  - term_id: CL:0007011
    reported_labels:
    - cephalic neural crest cell
    ontology_label: enteric neuron
  - term_id: UBERON:0001676
    reported_labels:
    - skull
    ontology_label: occipital bone
  - term_id: UBERON:0004437
    reported_labels:
    - skeletal system
    ontology_label: proximal epiphysis of middle phalanx of manual digit 3
  labels_variant: 6
  obsolete_terms:
  - term_id: HP:0410032
    ontology_label: obsolete Cleft of uvula
    replaced_by: HP:0000193
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Frank-Ter Haar Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Frank-Ter Haar Syndrome** covering all of the
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

I'll research Frank-Ter Haar Syndrome using web search tools now to compile a comprehensive, well-cited report.

Excellent data. Let me fetch a few more sources for completeness — the OMIM clinical synopsis, GARD, ClinGen curation, and additional recent literature/HPO terms.

I now have sufficient primary-source data across genetics, mechanism, animal/cellular models, and clinical case reports. Compiling the comprehensive report.

I have enough well-sourced material now to compile the full report.

# Frank–Ter Haar Syndrome (FTHS): Comprehensive Research Report

## 1. Disease Information

**Overview.** Frank–Ter Haar syndrome (FTHS; also called Ter Haar syndrome, or "Frank–ter Haar syndrome") is a rare autosomal recessive multisystem developmental disorder first delineated as a possible autosomal-recessive variant of Melnick–Needles syndrome by ter Haar et al. in three Dutch siblings, and separately by Frank et al. It is characterized by a distinctive craniofacial gestalt (brachycephaly, wide fontanels, prominent forehead, hypertelorism, prominent/bulging eyes, full cheeks, small chin), ocular anomalies (macrocornea/megalocornea with or without congenital glaucoma), skeletal dysplasia (bowing of long bones, flexion deformities of fingers/brachydactyly, prominent coccyx), congenital heart defects, and variable developmental delay ([Orphanet](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=137834); [OMIM #249420](https://omim.org/entry/249420); [GARD/NIH](https://rarediseases.info.nih.gov/diseases/5138/frank-ter-haar-syndrome)).

**Key identifiers:**
- **OMIM:** #249420 (phenotype), *613293 (SH3PXD2B gene)
- **MONDO:** MONDO:0009579
- **Orphanet:** ORPHA 137834
- **Disease Ontology:** DOID:0111789
- **GTR/ClinVar condition:** C1855305
- **Synonyms:** Ter Haar syndrome; Frank–ter Haar syndrome; Borrone dermato-cardio-skeletal syndrome (allelic — see below); FTHS

**Evidence basis.** The knowledge for this disease is derived almost entirely from **aggregated disease-level resources** — case reports and small case series (typically single families or 1–3 affected sibs, often consanguineous), plus two mechanistic model-organism/cell-line studies. There is no large clinical cohort, registry, or EHR-derived dataset. As of the most recent literature reviews, **~40 patients with a clinical diagnosis of FTHS have been reported worldwide, with molecularly confirmed SH3PXD2B mutations in only ~20** ([ScienceDirect literature review, 2019](https://www.sciencedirect.com/science/article/abs/pii/S1769721219306731); summarized via [PMC8872394](https://pmc.ncbi.nlm.nih.gov/articles/PMC8872394/)); other secondary sources cite a lower figure of ~24 reported cases ([FDNA resource center](https://fdna.com/health/resource-center/frank-ter-haar-syndrome-fths/)). This makes FTHS an ultra-rare condition with no formal population prevalence estimate.

---

## 2. Etiology

**Primary cause — genetic.** FTHS is caused by **biallelic (homozygous or compound heterozygous) loss-of-function mutations in *SH3PXD2B*** (5q35.1), encoding the podosomal adaptor protein **TKS4** (Tyrosine kinase substrate with four SH3 domains) ([OMIM #249420](https://omim.org/entry/249420); [Mao et al. 2010, *Am J Hum Genet*/ScienceDirect](https://www.sciencedirect.com/science/article/pii/S000292971000011X)). The original Dutch families were found to be homozygous for a **1-bp insertion (147insT)** in SH3PXD2B, with unaffected parents as heterozygous carriers, and immunoblotting confirmed loss of TKS4 protein — establishing a loss-of-function mechanism.

**Risk factors:**
- **Genetic:** Biallelic pathogenic *SH3PXD2B* variants are necessary and sufficient; **consanguinity** is a major risk factor, as most reported families are consanguineous, consistent with autosomal recessive transmission and founder/identical-by-descent alleles ([multiple consanguineous case reports](https://www.sciencedirect.com/science/article/abs/pii/S1769721219306731); [Saudi family WES report, PMC11214900](https://pmc.ncbi.nlm.nih.gov/articles/PMC11214900/)).
- **No established environmental, infectious, or lifestyle risk factors** — this is a purely monogenic Mendelian disorder; no gene–environment interaction data exist.
- **Protective factors:** None reported at the genetic or environmental level; there is no known modifier locus or protective allele documented in the literature.

**Population genetics:** SH3PXD2B pathogenic variants are extremely rare in population databases. For example, the missense variant c.127C>T (p.R43W), identified in an affected individual, has an overall gnomAD allele frequency of only ~0.001% (3/248,004 alleles), with the highest sub-population frequency (~0.006%) in African-ancestry alleles — consistent with a disease too rare and too deleterious to accumulate meaningfully in the general population.

---

## 3. Phenotypes

FTHS presents as a recognizable multi-system pattern. Onset is **congenital** for the craniofacial/ocular/skeletal features; developmental delay and hearing issues become apparent in infancy/childhood. Severity is **variable** even within families, and phenotypic overlap with Borrone dermato-cardio-skeletal syndrome exists (see Genetics section).

| Phenotype | HPO term (suggested) | Frequency/notes |
|---|---|---|
| Brachycephaly | HP:0000248 | Core diagnostic feature |
| Wide/large fontanels | HP:0000239 | Core diagnostic feature |
| Prominent forehead | HP:0011220 | Core diagnostic feature |
| Hypertelorism | HP:0000316 | Core diagnostic feature |
| Prominent/bulging eyes (proptosis) | HP:0000520 / HP:0000271 | Core diagnostic feature |
| Macrocornea/megalocornea | HP:0000488 | Hallmark; present with or without glaucoma |
| Congenital glaucoma | HP:0008007 | Variable; documented via trabeculotomy case reports ([Springer/UT Health San Antonio](https://scholars.uthscsa.edu/en/publications/congenital-glaucoma-as-an-ophthalmic-manifestation-of-frank-ter-h/)) |
| Full cheeks | HP:0000293 | Core diagnostic feature |
| Micrognathia/small chin | HP:0000347 | Core diagnostic feature |
| Protruding, simple ears | HP:0009748 | Diagnostic sign |
| Prominent coccyx | HP:0410032 (or free text) | Diagnostic sign; coccygeal skin folds also reported |
| Bowing of long bones | HP:0006487 | Skeletal dysplasia |
| Flexion deformity of fingers / brachydactyly | HP:0001284 / HP:0001156 | Skeletal |
| Kyphoscoliosis | HP:0002751 | Skeletal |
| Congenital heart defects (ASD, VSD, PDA, coarctation/interrupted aortic arch, mitral valve prolapse/cleft, aortic regurgitation) | HP:0030680 (generic), plus specific terms (HP:0001631 ASD, HP:0001629 VSD, HP:0001643 PDA) | Present in a substantial subset; documented in multiple case reports incl. a 2024 cardiac-surgery case ([PMC11895790](https://pmc.ncbi.nlm.nih.gov/articles/PMC11895790/)) and the Saudi WES family (cardiomegaly, double pulmonary trunk) |
| Developmental delay / cognitive disability | HP:0001263 / HP:0100543 | Variable — present in some, absent in others |
| Hearing impairment | HP:0000365 | Reported specifically in the mouse model and in some patients; not universally documented in humans |
| Craniosynostosis (sagittal) | HP:0011330 | Reported as an **expansion of the phenotypic spectrum** in a 2012 case series of 3 siblings, associated with raised intracranial pressure requiring calvarial expansion surgery in 2 of 3 ([PMC3532175](https://pmc.ncbi.nlm.nih.gov/articles/PMC3532175/)) |
| Lymphedema, Class III malocclusion, anterior open bite | — | Additional findings noted in the same craniosynostosis case series, expanding the phenotype |
| Clubfoot | HP:0001762 | Presenting feature in the Saudi family (initially misdiagnosed as isolated clubfoot before WES) |

**Important phenotypic variability note:** the 2012 sibling case series notably found **no megalocornea or glaucoma** despite confirmed SH3PXD2B involvement — a departure from "hallmark" features seen in earlier reports, underscoring that ocular findings, while classic, are not obligate ([PMC3532175](https://pmc.ncbi.nlm.nih.gov/articles/PMC3532175/)).

**Quality of life impact:** Not formally studied with QOL instruments (no EQ-5D/SF-36 data identified). Qualitatively, morbidity stems from congenital heart disease (may require cardiac surgery), congenital glaucoma (risk of vision loss without early trabeculotomy), craniosynostosis/raised ICP (may require neurosurgical intervention), and skeletal deformity affecting mobility.

---

## 4. Genetic/Molecular Information

**Causal gene:** ***SH3PXD2B*** (HGNC:29242; OMIM *613293), chromosome 5q35.1, encoding **TKS4** (Tyrosine kinase substrate with 4 SH3 domains).

**Protein structure:** TKS4 contains an N-terminal **PX (Phox homology) domain** and **four SH3 domains**, plus several proline-rich motifs. The PX domain is essential for membrane localization via phospholipid binding; SH3 domains mediate protein–protein interactions ([PMC8872394](https://pmc.ncbi.nlm.nih.gov/articles/PMC8872394/)).

**Reported variant spectrum** (compiled across ~20 molecularly confirmed cases; [PMC8872394](https://pmc.ncbi.nlm.nih.gov/articles/PMC8872394/)):
- **Frameshift/truncating:** original Dutch founder variant 147insT (1-bp insertion); c.578delG; c.969delG (p.Arg324fs, in ClinVar as [RCV000000212](https://www.ncbi.nlm.nih.gov/clinvar/RCV000000212/))
- **Nonsense:** c.250C>T (p.R84*)
- **Missense:** c.280C>G (p.Arg94Gly) — localizes to the PX domain, predicted to disrupt phospholipid binding; c.127C>T (p.R43W)
- **Splice-site:** c.76-2A>C; c.401+1G>A (ClinVar [RCV000201206](https://www.ncbi.nlm.nih.gov/clinvar/RCV000201206/))
- **Large structural deletions:** complete exon 13 deletion; a 12,583-bp deletion; a 7,625-bp deletion affecting exon 13 (in the craniosynostosis sibship, [PMC3532175](https://pmc.ncbi.nlm.nih.gov/articles/PMC3532175/))
- A novel homozygous missense variant **c.280C>G (p.R94G)**, absent from population databases and predicted damaging, was identified by unbiased/hypothesis-free WES reanalysis in a Saudi family initially referred for isolated clubfoot ([PMC11214900](https://pmc.ncbi.nlm.nih.gov/articles/PMC11214900/)).

**Variant classification:** All reported disease variants are classified **pathogenic/likely pathogenic** under a loss-of-function mechanism (nonsense-mediated decay or protein truncation/domain disruption); population allele frequencies in gnomAD are consistent with recessive-disease-causing rarity (e.g., c.127C>T at ~0.001% overall).

**Inheritance mechanism:** Loss-of-function — immunoblotting in the original Dutch pedigree showed **absent TKS4 protein** in affected homozygotes, and parental carriers were unaffected heterozygotes, consistent with simple autosomal recessive haploinsufficiency-tolerant/complete loss mechanism.

**Allelic disorder — Borrone dermato-cardio-skeletal syndrome (BDCS):** *SH3PXD2B* mutations also cause **Borrone dermato-cardio-skeletal syndrome**, a severe progressive disorder with coarse facies, thick skin, acne conglobata, vertebral abnormalities, and mitral valve prolapse. Genetic analysis demonstrated that **a proportion of BDCS and FTHS cases are allelic**, i.e., caused by mutations in the same gene, suggesting these were originally described as distinct syndromes but represent a phenotypic continuum from a single locus ([Wilson et al., *Eur J Hum Genet*, PubMed 24105366](https://pubmed.ncbi.nlm.nih.gov/24105366/); [Nature EJHG](https://www.nature.com/articles/ejhg2013229)). Loss-of-function mutations in SH3PXD2B were shown to underlie **7 of 13 families** studied with an FTHS clinical diagnosis, implying **genetic heterogeneity** — some clinically diagnosed FTHS families do not have identifiable SH3PXD2B mutations, raising the possibility of an unidentified second locus or phenocopies.

**Historical misclassification:** ter Haar's original description proposed this as a possible **autosomal recessive form of Melnick–Needles syndrome** (an X-linked skeletal dysplasia caused by *FLNA* mutations) due to overlapping craniofacial/skeletal gestalt — this is now understood to be a distinct, genetically unrelated entity ([PMC3532175](https://pmc.ncbi.nlm.nih.gov/articles/PMC3532175/); [BMC Med Genet](https://link.springer.com/article/10.1186/1471-2350-13-104)).

**Epigenetics/chromosomal abnormalities:** No epigenetic (DNA methylation/histone) studies or chromosomal aneuploidy/translocation associations have been reported for FTHS; the disease is exclusively linked to point mutations/small indels/exonic deletions in *SH3PXD2B*.

---

## 5. Environmental Information

No environmental, toxin, infectious, or lifestyle contributing factors have been identified or studied for FTHS — it is a purely monogenic disorder. No literature addresses gene–environment interaction, teratogen exposure, or infectious triggers.

---

## 6. Mechanism / Pathophysiology

**Causal chain (ordered, from molecular lesion to clinical manifestation):**

1. Biallelic loss-of-function mutation in *SH3PXD2B* → **absence or truncation of the TKS4 adaptor protein** (demonstrated by immunoblot in the founder Dutch family) ([OMIM #249420](https://omim.org/entry/249420)).
2. Loss of TKS4 → **disrupted PX-domain-mediated membrane phospholipid binding** and loss of the SH3-domain protein-interaction scaffold → **failure of Tks4–EGF receptor (EGFR) signaling complex formation**; in wild-type cells, EGF induces Tks4 tyrosine phosphorylation and translocation to the plasma membrane via a PI3K-dependent step, which is abolished when Tks4 is absent or its PX domain is disrupted ([PMC8872394](https://pmc.ncbi.nlm.nih.gov/articles/PMC8872394/)).
3. Disrupted EGFR/Tks4 signaling → **impaired formation of podosomes and invadopodia** (actin-rich, matrix-degrading membrane protrusions) — demonstrated directly: Tks4-silenced cells show markedly inhibited migration in Boyden-chamber assays and **"fewer and structurally aberrant podosomes"** compared to wild-type ([Sharma et al./Buschman et al., cited in PMC8872394](https://pmc.ncbi.nlm.nih.gov/articles/PMC8872394/); [Sh3Pxd2bnee−/− mouse study, *Development* 2026, PMC12912270](https://pmc.ncbi.nlm.nih.gov/articles/PMC12912270/)).
4. Impaired podosome-dependent **cell migration and pericellular matrix remodeling** → this is specifically detrimental to **neural crest-derived cell lineages**, which require high migratory capacity during craniofacial and cardiac development. The 2026 mouse model shows **"impaired migration of the cephalic neural crest cell lineage"** and decreased proliferation/migration of osteoblasts and dura mater cells, both in vitro and in vivo during calvarial healing.
5. Failure of neural-crest-dependent tissue morphogenesis → **(branch A) craniofacial dysmorphogenesis**: disorganized sagittal suture patterning, hypomineralization, and failure of the posterofrontal suture to undergo normal endochondral ossification/closure, producing the brachycephaly/wide-fontanel/prominent-forehead gestalt and, in a subset, **sagittal craniosynostosis with raised intracranial pressure** (documented clinically requiring calvarial expansion surgery) ([PMC12912270](https://pmc.ncbi.nlm.nih.gov/articles/PMC12912270/); [PMC3532175](https://pmc.ncbi.nlm.nih.gov/articles/PMC3532175/)).
6. **(branch B) Skeletal dysplasia**: at the cellular level, loss of TKS4 impairs mesenchymal stem cell (MSC) differentiation toward osteogenic lineages — a human Tks4-knockout embryonic stem cell (hESC) model shows **reduced expression of mesodermal and osteogenic marker genes (including GATA4 and goosecoid)** during MSC differentiation, directly linking TKS4 loss to the bowing of long bones, brachydactyly, and skeletal dysplasia seen clinically ([PMC9369304](https://pmc.ncbi.nlm.nih.gov/articles/PMC9369304/)).
7. **(branch B, continued)** In the same hESC model, knockout MSCs exhibit a **partial epithelial-mesenchymal transition (EMT) phenotype** (altered E-cadherin/Snail1 expression, "increased matrix degrading ability") without full EMT marker activation (Vimentin/Fibronectin unchanged) — suggesting TKS4 loss selectively perturbs, rather than globally activates, EMT-associated pathways during skeletogenesis.
8. **(branch C) Ocular anomalies**: megalocornea and congenital glaucoma are attributed to abnormal neural-crest-derived anterior-segment mesenchyme development (periocular mesenchyme is neural-crest derived), though the precise cellular mechanism for glaucoma (e.g., trabecular meshwork dysgenesis) has not been directly studied at the molecular level in FTHS — this step is **inferred by analogy to the neural-crest mechanism established for craniofacial defects**, not directly demonstrated.
9. **(branch D) Cardiac anomalies**: septal defects (ASD/VSD), PDA, coarctation/interrupted aortic arch, and mitral valve abnormalities are consistent with **cardiac neural crest and endocardial cushion contributions to septation and valvulogenesis**, both processes dependent on directed cell migration — again **largely inferred from the neural-crest paradigm** rather than FTHS-specific cardiac tissue studies, though the *Sh3Pxd2b*-null mouse (from the original 2010 characterization) directly showed cardiovascular abnormalities corresponding to human FTHS features.
10. Downstream of the craniofacial/skeletal/neural-crest developmental defect, transcriptomic analysis (bulk RNA-seq) of mutant mouse skulls reveals **downregulation of ribosome biogenesis genes**, including SNORD (small nucleolar RNA) genes and nuclear-encoded 5S rRNA, with reduced small RNA/microRNA content — a newly identified (2026) downstream molecular signature whose causal relationship to the skeletal phenotype (upstream driver vs. downstream consequence of reduced proliferation) is **not yet resolved**.

**Molecular pathways:** EGFR signaling (Tks4 as an EGFR-proximal signaling adaptor); PI3K-dependent membrane translocation of Tks4; actin cytoskeleton remodeling (podosome/invadopodia assembly) — GO term suggestions: **GO:0002102 (podosome)**, **GO:0031252 (cell leading edge)**, **GO:0030335 (positive regulation of cell migration)**, **GO:0007173 (epidermal growth factor receptor signaling pathway)**, **GO:0001501 (skeletal system development)**, **GO:0014032 (neural crest cell development)**.

**Cell types involved:** neural crest-derived mesenchyme, osteoblasts, dura mater cells, mesenchymal stem cells (MSCs) — Cell Ontology suggestions: **CL:0000058 (chondroblast)**/relevant osteoblast lineage terms **CL:0000062 (osteoblast)**, **CL:0000134 (mesenchymal stem cell)**, **CL:0007011 (cephalic neural crest cell)**.

**Model system caveats:** The mouse skull-focused study did not directly assess ocular or cardiac phenotypes, so the neural-crest mechanism for those organ systems remains **an extrapolation from the craniofacial findings and the shared developmental cell lineage**, not a directly demonstrated mechanism within a single unifying study.

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** Cranium/skull (sutures, calvaria), facial skeleton, eyes (cornea, anterior segment, optic structures via glaucoma), heart (septa, valves, great vessels), axial/appendicular skeleton (long bones, spine, coccyx, digits). **Secondary:** brain (via raised intracranial pressure from craniosynostosis), ears (external ear shape; hearing apparatus in the mouse model).
- **Body systems:** skeletal, cardiovascular, ocular/visual, craniofacial, and (variably) nervous system (developmental delay, ICP-related complications).
- **Tissue/cell level:** cranial neural crest-derived mesenchyme (Uberon: cranial neural crest, UBERON:0002418 relevant structures), osteoblastic bone-forming tissue, corneal/anterior-segment mesenchymal tissue, cardiac septal and valvular mesenchyme.
- **Subcellular level:** plasma membrane (podosome/invadopodia formation sites; GO Cellular Component **GO:0002102 podosome**), cytoplasm-to-membrane translocation machinery for Tks4.
- **Localization:** Bilateral/symmetric craniofacial and ocular involvement typical; cardiac lesions vary by case (septal defects, valve, great-vessel anomalies) without a stereotyped laterality pattern.

Suggested UBERON terms: UBERON:0001676 (skull), UBERON:0000970 (eye), UBERON:0000948 (heart), UBERON:0004437 (skeletal system), UBERON:0001456 (face).

---

## 8. Temporal Development

- **Onset:** **Congenital** for craniofacial dysmorphism, ocular anomalies, skeletal features, and (when present) congenital heart defects — all apparent at birth or in early infancy. Developmental delay, hearing impairment, and orthodontic/malocclusion issues become evident in **early childhood**.
- **Progression:** Predominantly a **stable, non-progressive developmental malformation syndrome** rather than a degenerative disease — the craniofacial/skeletal features reflect a fixed developmental error rather than ongoing tissue destruction. However, **untreated congenital glaucoma is progressive** (risk of vision loss), and **craniosynostosis with raised ICP is progressive** if uncorrected, requiring surgical intervention (documented calvarial expansion in 2 of 3 siblings in one series).
- **Disease course:** Chronic and lifelong; no spontaneous remission reported. No formal staging system exists (this is a congenital malformation syndrome, not a staged disease like cancer).
- **Critical periods:** Prenatal/early postnatal period is critical for craniofacial suture and cardiac septation development (per the neural-crest mechanism); early childhood is the critical window for detecting and surgically treating congenital glaucoma and craniosynostosis-associated raised ICP before permanent visual or neurological damage occurs.

---

## 9. Inheritance and Population

- **Epidemiology:** No formal prevalence/incidence rate has been calculated (too rare for epidemiological registries). The disease is characterized as **ultra-rare**, with **approximately 40 clinically diagnosed cases and ~20 molecularly confirmed cases reported in the world literature** as of recent reviews ([ScienceDirect 2019 literature review](https://www.sciencedirect.com/science/article/abs/pii/S1769721219306731); [PMC8872394](https://pmc.ncbi.nlm.nih.gov/articles/PMC8872394/)); some secondary aggregator sources cite ~24 total reported cases.
- **Inheritance pattern:** **Autosomal recessive** ([OMIM #249420](https://omim.org/entry/249420)).
- **Penetrance:** Appears complete for the core craniofacial/skeletal gestalt among biallelic mutation carriers, though **expressivity is markedly variable** — e.g., megalocornea/glaucoma present in most originally reported families but absent in the sibship reported with craniosynostosis, and developmental delay/cognitive involvement present in some patients but not others.
- **Genetic anticipation:** Not reported/applicable (no repeat-expansion mechanism).
- **Germline mosaicism:** Not specifically documented in the literature reviewed.
- **Founder effects:** The original Dutch families share the 147insT founder variant; this and other family-specific variants (e.g., in Saudi and Iranian families) suggest **regional/consanguinity-driven founder or identical-by-descent alleles** rather than a single global founder mutation.
- **Consanguinity:** A major contributing factor — the majority of reported families (Dutch, Saudi, Iranian, and others) are consanguineous, consistent with autosomal recessive segregation of rare alleles.
- **Carrier frequency:** Not established at a population level given the extreme rarity; gnomAD-derived data on individual variants (e.g., c.127C>T at ~0.001% overall, ~0.006% in African-ancestry alleles) suggest very low carrier frequencies for any single allele, consistent with private/family-specific mutations rather than a common carrier variant.
- **Population demographics:** No specific ethnic predisposition has been established beyond the observation that reported cases cluster in consanguineous populations (Dutch founder family, Saudi Arabian, Iranian families, and others), which likely reflects ascertainment via consanguinity rather than true differential susceptibility.
- **Sex ratio:** No skewed sex ratio reported (consistent with autosomal, non-sex-linked inheritance).

---

## 10. Diagnostics

- **Clinical diagnosis:** Based on recognition of the characteristic craniofacial-ocular-skeletal-cardiac gestalt (brachycephaly, wide fontanels, hypertelorism, macrocornea ± glaucoma, full cheeks, small chin, protruding ears, prominent coccyx, long-bone bowing, finger flexion deformities, congenital heart defects).
- **Genetic testing:**
  - **Single-gene sequence analysis of *SH3PXD2B*** (all coding exons) is commercially available and is the definitive diagnostic test (e.g., listed in NCBI GTR for both postnatal and prenatal testing) ([GTR test listing](https://www.ncbi.nlm.nih.gov/gtr/tests/584144.1/)).
  - **Whole exome sequencing (WES)** has proven valuable, especially in atypical presentations — e.g., a family initially referred for isolated bilateral clubfoot was correctly diagnosed with FTHS only after an "unbiased, hypothesis-free" WES reanalysis identified the SH3PXD2B variant, prompting re-examination and clinical reclassification ([PMC11214900](https://pmc.ncbi.nlm.nih.gov/articles/PMC11214900/)); similarly, exome sequencing identified two novel SH3PXD2B mutations in another report ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S037811191730519X)).
  - Given genetic heterogeneity (only 7/13 clinically diagnosed families in one study had identifiable SH3PXD2B mutations), a **negative single-gene test does not exclude the clinical diagnosis**, and broader panel/exome testing may be warranted.
- **Imaging:** Skeletal survey/radiographs for long-bone bowing, brachydactyly, and spinal changes (kyphoscoliosis); cranial imaging (CT/MRI) for craniosynostosis and assessment of raised intracranial pressure; echocardiography for congenital heart defects (essential pre-surgical workup, as illustrated in the anesthesia case report).
- **Ophthalmologic exam:** Slit-lamp/tonometry for megalocornea and glaucoma screening; documented management includes bilateral trabeculotomy for congenital glaucoma with elevated IOP and buphthalmos.
- **Differential diagnosis:** Historically confused with **Melnick–Needles syndrome** (X-linked, *FLNA*-related skeletodysplasia) due to overlapping craniofacial/skeletal features — ter Haar's original 1982 report proposed FTHS as a possible autosomal recessive variant of Melnick–Needles syndrome before the distinct genetic basis (SH3PXD2B) was established. FTHS and **Borrone dermato-cardio-skeletal syndrome** are allelic and clinically overlapping, requiring consideration as a phenotypic spectrum rather than fully distinct entities.
- **Screening:** No population-level newborn or carrier screening program exists given the extreme rarity; genetic counseling for consanguineous families with an index case is the primary risk-stratification approach, with prenatal testing available once a familial variant is identified (per GTR prenatal test listing).

---

## 11. Outcome/Prognosis

- **Survival/mortality:** No systematic survival statistics exist. Morbidity/mortality risk is driven primarily by **congenital heart disease severity** (e.g., coarctation/interrupted aortic arch, VSD/ASD requiring surgical correction) and **complications of congenital glaucoma or raised intracranial pressure from craniosynostosis** if untreated. One case report explicitly notes a **deceased sibling** in the context of severe cardiac complications, though comprehensive mortality data are lacking ([PMC8872394](https://pmc.ncbi.nlm.nih.gov/articles/PMC8872394/) discussion of the index Saudi patient family).
- **Morbidity:** Variable developmental delay/cognitive impairment; skeletal deformity may affect mobility; vision impairment risk from glaucoma if not surgically managed early; neurological risk from raised ICP if craniosynostosis is not surgically corrected.
- **Complications documented in case reports:** cardiac conduction abnormalities post-surgery (a documented case had transient "type 2 cardiac block" post-VSD/ASD repair, resolving with a brief PCICU stay); difficult airway/intubation due to micrognathia and craniofacial anomalies, requiring specialized anesthetic planning for surgery.
- **Prognostic factors:** Presence and severity of congenital heart disease and craniosynostosis/raised ICP are the most clinically significant modifiers of outcome; no molecular/biomarker-based prognostic indicators have been established.
- **Recovery potential:** With appropriate surgical management (cardiac repair, glaucoma surgery, calvarial expansion), reported outcomes in case reports have generally been favorable in the short term (e.g., successful discharge after cardiac surgery), though long-term functional/cognitive outcome data are not systematically reported.

---

## 12. Treatment

There is **no disease-modifying or curative treatment** for FTHS — management is entirely **symptomatic/organ-specific**, addressing each system's manifestations as they arise.

- **Ophthalmologic (congenital glaucoma):** **Trabeculotomy** has been used successfully — one reported patient underwent uneventful bilateral trabeculotomy for congenital glaucoma with buphthalmos, mild corneal edema, and elevated IOP; marked bilateral anterior iris insertion was noted intraoperatively ([Springer/UT Health San Antonio report](https://scholars.uthscsa.edu/en/publications/congenital-glaucoma-as-an-ophthalmic-manifestation-of-frank-ter-h/)). NCIT suggestion: **NCIT:C15329** (Surgical Procedure) for the intervention broadly; a more specific glaucoma-surgery NCIT term should be sought if available.
- **Cardiac (congenital heart defects):** **Surgical repair** (sternotomy, cardiopulmonary bypass) for septal defects — a 2024/2025 case report details successful **ASD and VSD repair with mitral valve cleft repair** in a 3-year-old with FTHS, using careful pre-operative planning for a **suspected difficult airway** (craniosynostosis, micrognathia, prominent forehead, hypertelorism, anteverted nostrils) ([PMC11895790](https://pmc.ncbi.nlm.nih.gov/articles/PMC11895790/)). Difficult-airway equipment (laryngeal masks, fiberoptic bronchoscope) was prepared; induction with sevoflurane, successful direct laryngoscopy and intubation (4.5 ETT), maintenance with fentanyl/midazolam/cisatracurium, and intraoperative monitoring via cerebral oximetry and transesophageal echocardiography. Post-operatively the patient developed transient type 2 heart block, managed during a 5-day PCICU stay, and was discharged in normal sinus rhythm. NCIT: **NCIT:C15329** (Surgical Procedure)/cardiac surgical repair terms.
- **Craniofacial/neurosurgical:** **Calvarial expansion surgery** for craniosynostosis-associated raised intracranial pressure (performed in 2 of 3 siblings in one case series) ([PMC3532175](https://pmc.ncbi.nlm.nih.gov/articles/PMC3532175/)). NCIT: **NCIT:C15329** (Surgical Procedure).
- **Orthopedic/dental:** Management of skeletal deformities (bowing, brachydactyly) and dental/orthodontic issues (Class III malocclusion, anterior open bite) as needed — no FTHS-specific surgical protocol has been published; standard orthopedic and orthodontic approaches are used. NCIT: **NCIT:C16186** (Orthopedic Surgical Procedure).
- **Supportive/developmental care:** Developmental surveillance and early intervention/therapy services for developmental delay, as clinically indicated (no FTHS-specific rehabilitation protocol reported). NCIT: **NCIT:C15302** (Physical Therapy), **NCIT:C15240** (Genetic Counseling).
- **No pharmacotherapy, gene therapy, cell therapy, or targeted/precision-medicine approaches** have been reported or are in clinical trials for FTHS — a search of ClinicalTrials.gov and the literature returned no registered interventional trials specific to this condition, consistent with its ultra-rarity.
- **Anesthesia considerations** are a recurring and clinically important theme in the literature given the difficult-airway anatomy (micrognathia, craniofacial anomalies) combined with frequent need for cardiac surgery — this represents a key practical management point for any FTHS patient requiring general anesthesia.

---

## 13. Prevention

- **Primary prevention:** Not applicable in the traditional sense (monogenic recessive disorder) — the only "primary prevention" avenue is **genetic counseling and reproductive planning** for known carrier couples (e.g., consanguineous couples with a prior affected child), including discussion of **preimplantation genetic diagnosis (PGD)** or **prenatal diagnosis** once the familial pathogenic variant is known (prenatal SH3PXD2B sequencing is commercially available per GTR).
- **Secondary prevention:** Early diagnosis (ideally via prenatal or early postnatal genetic testing in at-risk families) enables **early ophthalmologic screening for glaucoma** and **early cardiac evaluation**, both of which can prevent irreversible complications (vision loss, cardiac decompensation) if intervention is timely.
- **Tertiary prevention:** Surveillance for craniosynostosis-related raised intracranial pressure with prompt calvarial surgery to prevent neurological sequelae; ongoing cardiology follow-up post-surgical repair to monitor for conduction abnormalities.
- **Genetic counseling:** Essential for consanguineous families or those with a prior affected child, given the ~25% recurrence risk in each pregnancy under autosomal recessive inheritance once carrier status is confirmed.
- **No immunization, public health, or population screening program** exists or is applicable given the extreme rarity of this disorder.

---

## 14. Other Species / Natural Disease

- No naturally occurring FTHS-like disease has been reported in companion animals or wildlife (no OMIA entries identified in this research).
- **Orthologous gene:** Mouse *Sh3Pxd2b* (chromosome 11) — used extensively in engineered/spontaneous mutant models (see below). NCBI Gene/ortholog relationship is well established between human SH3PXD2B and mouse Sh3Pxd2b.
- **Taxonomy:** Homo sapiens (NCBITaxon:9606) for the human disease; Mus musculus (NCBITaxon:10090) for the principal animal model.

---

## 15. Model Organisms

**Mouse model — *Sh3Pxd2bnee−/−*:** A **spontaneous single-base-pair deletion in the last exon** of *Sh3pxd2b* on mouse chromosome 11 produces the "nee" (naked ear/eye, per typical mouse mutant nomenclature conventions — exact allele name as reported) mutant. Published in *Development*, February 2026 ([PMC12912270](https://pmc.ncbi.nlm.nih.gov/articles/PMC12912270/); [journals.biologists.com](https://journals.biologists.com/dev/article/153/2/dev204631/370535/The-Sh3Pxd2bnee-mouse-reveals-developmental)):
- **Phenotype recapitulation:** Homozygous nee/nee mice show **runted growth, craniofacial and skeletal abnormalities, ocular anterior segment dysgenesis, and hearing impairment** — closely paralleling the human FTHS phenotype across the craniofacial, skeletal, ocular, and audiologic domains. Specific findings include shortened noses, domed skulls, widened fontanels, disorganized/hypomineralized sagittal suture, and failure of posterofrontal suture endochondral ossification/closure.
- **Mechanistic insights:** The causative mutation produces a frameshift truncation affecting the TKS4 SH3 domains; mutant cells form fewer/structurally aberrant podosomes; osteoblasts and dura mater cells show decreased proliferation; cephalic neural crest cell migration is impaired both in vitro and in vivo (calvarial defect healing assay). Bulk RNA-seq revealed downregulation of ribosome biogenesis genes (SNORD genes, 5S rRNA) as a novel downstream transcriptomic signature.
- **Limitations:** This study was **skull/craniofacial-focused**; ocular and cardiac phenotypes, though present per the phenotype summary, were not mechanistically dissected in this particular paper (an earlier, original 2010 mouse characterization by Mao et al. established the cardiovascular and ocular correspondence to human FTHS).
- Earlier engineered *Sh3pxd2b*-null mice (2010, Mao et al.) similarly displayed skeletal, ocular, and cardiovascular abnormalities corresponding to FTHS.

**Human cell-based model — Tks4-KO HUES9 hESC line:** Published August 2022, *International Journal of Molecular Sciences* ([PMC9369304](https://pmc.ncbi.nlm.nih.gov/articles/PMC9369304/)):
- CRISPR/Cas9-generated homozygous and heterozygous Tks4-knockout clones in the HUES9 human embryonic stem cell line.
- Knockout cells **retained pluripotency and normal morphology/proliferation** as undifferentiated stem cells.
- Upon **directed differentiation to mesenchymal stem cells (MSCs)**, knockout cells showed **impaired osteogenic maturation** — reduced expression of mesodermal/osteogenic markers including **GATA4 and goosecoid** — directly relevant to the skeletal phenotype of FTHS.
- A **partial EMT phenotype** was observed (altered E-cadherin/Snail1, increased matrix-degrading capacity) without full EMT marker activation (Vimentin/Fibronectin unchanged), suggesting selective pathway disruption.
- The authors propose that **TKS4 loss disrupts cell lineage differentiation and maturation** during development, providing a tractable human cellular system for dissecting FTHS pathogenesis — a first-in-class disease model for this ultra-rare disorder, since no patient-derived iPSC lines have yet been reported.

**Model limitations overall:** No single model system captures the full multi-organ FTHS phenotype (craniofacial + skeletal + ocular + cardiac + auditory) with mechanistic depth in one study; the mouse model is strong for craniofacial/skeletal/neural-crest mechanism but under-characterized for cardiac/ocular pathogenesis at the molecular level, and the hESC model captures osteogenic differentiation defects but does not model whole-organism morphogenesis.

---

## Summary Table: Key Evidence Sources

| Claim | Source type | Citation |
|---|---|---|
| Gene/OMIM/phenotype definition | Structured database | [OMIM #249420](https://omim.org/entry/249420); [OMIM *613293](https://www.omim.org/entry/613293) |
| Orphanet epidemiology/clinical description | Structured database | [Orphanet 137834](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=137834) |
| Original founder mutation & LOF mechanism | Primary literature (human clinical) | Mao et al., *Am J Hum Genet* 2010 ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S000292971000011X)) |
| Allelism with Borrone syndrome | Primary literature (human clinical) | Wilson et al., *Eur J Hum Genet* 2013 ([PubMed 24105366](https://pubmed.ncbi.nlm.nih.gov/24105366/)) |
| Craniosynostosis/ICP phenotype expansion | Primary literature (human clinical case series) | [PMC3532175](https://pmc.ncbi.nlm.nih.gov/articles/PMC3532175/) |
| Congenital glaucoma/trabeculotomy | Primary literature (human clinical case report) | [Springer/UT Health San Antonio](https://scholars.uthscsa.edu/en/publications/congenital-glaucoma-as-an-ophthalmic-manifestation-of-frank-ter-h/) |
| Cardiac surgery/anesthesia case (2024–25) | Primary literature (human clinical case report) | [PMC11895790](https://pmc.ncbi.nlm.nih.gov/articles/PMC11895790/) |
| WES diagnosis, Saudi family | Primary literature (human clinical case report) | [PMC11214900](https://pmc.ncbi.nlm.nih.gov/articles/PMC11214900/) |
| Comprehensive mutation review & mechanism | Primary literature (review) | [PMC8872394](https://pmc.ncbi.nlm.nih.gov/articles/PMC8872394/) |
| Mouse model mechanism (2026) | Model organism (mouse) | [PMC12912270](https://pmc.ncbi.nlm.nih.gov/articles/PMC12912270/), *Development* Feb 2026 |
| hESC model mechanism (2022) | In vitro (human cell line) | [PMC9369304](https://pmc.ncbi.nlm.nih.gov/articles/PMC9369304/) |

**Evidence-type distribution:** Human clinical (case reports/series) dominate the phenotypic and diagnostic literature; molecular mechanism relies on a mix of human clinical genetics (variant identification), in vitro cell biology (podosome/EGFR signaling assays, hESC differentiation), and model organism data (mouse). No computational/in silico modeling studies specific to FTHS pathogenesis were identified beyond standard variant-effect prediction tools used in individual case reports.

Sources:
- [OMIM #249420 — FRANK-TER HAAR SYNDROME](https://omim.org/entry/249420)
- [OMIM *613293 — SH3PXD2B](https://www.omim.org/entry/613293)
- [Orphanet — Frank-Ter Haar syndrome](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=137834)
- [Disruption of the Podosome Adaptor Protein TKS4 (SH3PXD2B) Causes FTHS — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S000292971000011X)
- [Mutations in SH3PXD2B cause Borrone dermato-cardio-skeletal syndrome — PubMed](https://pubmed.ncbi.nlm.nih.gov/24105366/)
- [Mutations in SH3PXD2B cause Borrone dermato-cardio-skeletal syndrome — Nature EJHG](https://www.nature.com/articles/ejhg2013229)
- [A severe case of Frank-ter Haar syndrome and literature review — ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1769721219306731)
- [Frank-ter Haar syndrome associated with sagittal craniosynostosis and raised ICP — PMC3532175](https://pmc.ncbi.nlm.nih.gov/articles/PMC3532175/)
- [Congenital glaucoma as an ophthalmic manifestation of Frank–Ter Haar syndrome](https://scholars.uthscsa.edu/en/publications/congenital-glaucoma-as-an-ophthalmic-manifestation-of-frank-ter-h/)
- [Anesthesia and Airway Management in a Child with FTHS Undergoing Cardiac Surgery — PMC11895790](https://pmc.ncbi.nlm.nih.gov/articles/PMC11895790/)
- [Whole exome sequencing enables correct diagnosis of FTHS in a Saudi family — PMC11214900](https://pmc.ncbi.nlm.nih.gov/articles/PMC11214900/)
- [The Role of the Disrupted Podosome Adaptor Protein (SH3PXD2B) in Frank–Ter Haar Syndrome — PMC8872394](https://pmc.ncbi.nlm.nih.gov/articles/PMC8872394/)
- [The Sh3Pxd2bnee−/− mouse reveals developmental features of Frank-ter Haar syndrome — PMC12912270](https://pmc.ncbi.nlm.nih.gov/articles/PMC12912270/)
- [A Novel Cell-Based Model: Tks4-KO Human Embryonic Stem Cell Line — PMC9369304](https://pmc.ncbi.nlm.nih.gov/articles/PMC9369304/)
- [Frank-Ter Haar syndrome — GARD/NIH](https://rarediseases.info.nih.gov/diseases/5138/frank-ter-haar-syndrome)
- [Frank-Ter Haar syndrome — MalaCards](https://www.malacards.org/card/frank_ter_haar_syndrome_2)
- [Frank-Ter Haar syndrome Disease Ontology Browser — DOID:0111789](https://www.informatics.jax.org/disease/DOID:0111789)
- [NM_001017995.3(SH3PXD2B):c.969del AND FTHS — ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/RCV000000212/)
- [NM_001017995.3(SH3PXD2B):c.401+1G>A AND FTHS — ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/RCV000201206/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 50 |
| Resolved | 48 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 30 |
| Terms named correctly | 20 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000488` (1 mention) - the report calls it "Macrocornea/megalocornea"; HP calls it **Retinopathy**
- `CL:0007011` (1 mention) - the report calls it "cephalic neural crest cell"; CL calls it **enteric neuron**
- `UBERON:0001676` (1 mention) - the report calls it "skull"; UBERON calls it **occipital bone**
- `UBERON:0004437` (1 mention) - the report calls it "skeletal system"; UBERON calls it **proximal epiphysis of middle phalanx of manual digit 3**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0410032` (obsolete Cleft of uvula) (1 mention) - replaced by `HP:0000193`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000239` (1 mention) - the report calls it "Wide/large fontanels"; HP calls it **Large fontanelles**, and lists "Large fontanels" among its other names
- `HP:0008007` (1 mention) - the report calls it "Congenital glaucoma"; HP calls it **Primary congenital glaucoma**
- `HP:0000347` (1 mention) - the report calls it "Micrognathia/small chin"; HP calls it **Micrognathia**
- `HP:0009748` (1 mention) - the report calls it "Protruding, simple ears"; HP calls it **Large earlobe**, and lists "Prominent ear lobes" among its other names
- `HP:0011330` (1 mention) - the report calls it "Craniosynostosis (sagittal)"; HP calls it **Metopic synostosis**, and lists "Metopic craniosynostosis" among its other names
- `NCBITaxon:9606` (1 mention) - the report calls it "Taxonomy:** Homo sapiens"; NCBITaxon calls it **Homo sapiens**