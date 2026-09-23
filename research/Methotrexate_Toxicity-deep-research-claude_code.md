---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-22T02:18:30.928467'
end_time: '2026-09-22T02:23:21.988310'
duration_seconds: 291.06
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Methotrexate Toxicity
  mondo_id: MONDO:0034212
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
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 17
  num_turns: 19
  total_cost_usd: 1.3882476000000001
  session_id: dc83c613-1fba-53b8-9741-f63fb2448a6e
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 57
reference_validation:
  total_references: 38
  verified: 38
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 38
  on_topic: 24
  validator_version: 0.2.1
term_validation:
  total_terms: 52
  verified: 46
  not_found: 0
  obsolete: 0
  unverifiable: 6
  confabulation_rate: 0.0
  labels_checked: 37
  labels_matching: 31
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0034212
    reported_labels:
    - MONDO
    ontology_label: methotrexate toxicity
  - term_id: HP:0001636
    reported_labels:
    - Myocarditis
    ontology_label: Tetralogy of Fallot
  - term_id: CL:0000075
    reported_labels:
    - "epithelial cell \u2014 intestinal/renal tubular"
    ontology_label: columnar/cuboidal epithelial cell
  - term_id: CL:0000097
    reported_labels:
    - "mast cell \u2014 not primary but relevant to mucosal injury context"
    ontology_label: mast cell
  labels_variant: 2
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Methotrexate Toxicity
- **MONDO ID:** MONDO:0034212 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Methotrexate Toxicity** covering all of the
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

I'll research this topic now, starting by loading the web search/fetch tools and running parallel searches across the key areas.

I have enough material now to compose a comprehensive report. Let me do a couple more targeted searches for HPO phenotype terms/ontology mapping and prevention/screening specifics before writing.

I have sufficient material to compile a thorough, well-cited report. Here it is:

# Methotrexate Toxicity — Comprehensive Research Report

## 1. Disease Information

**Overview.** Methotrexate (MTX) toxicity is a drug-induced condition arising from excess systemic or local exposure to methotrexate, an antifolate antimetabolite used at low doses for rheumatoid arthritis, psoriasis, inflammatory bowel disease, and ectopic pregnancy, and at intermediate-to-high doses for hematologic malignancies (acute lymphoblastic leukemia, primary CNS lymphoma, osteosarcoma) and as an abortifacient/antineoplastic agent. Toxicity is classified as a **complex, iatrogenic/pharmacogenomic disorder** rather than a single-gene Mendelian disease: the phenotype depends on dose, route (oral, IV, intrathecal), renal function, hydration status, third-space fluid accumulation, drug interactions, and inherited variation in folate-pathway and drug-transporter genes. It ranges from mild mucositis/cytopenia in low-dose chronic regimens to fulminant multiorgan failure after high-dose (HD-MTX) or intrathecal overdose. "It particularly affects the bone marrow, skin, liver, kidney, bone, lung, and brain" (MalaCards synthesis) ([MalaCards: Methotrexate Toxicity](https://www.malacards.org/card/methotrexate_toxicity)).

**Key identifiers:**
- **MONDO:** MONDO:0034212
- **Orphanet:** ORPHA:565782 ("Methotrexate toxicity") ([Orphanet](https://www.orpha.net/en/disease/detail/565782))
- **ICD-10-CM:** T45.1X1A (accidental poisoning by antineoplastic/immunosuppressive drugs, initial encounter), T45.1X5A (adverse effect), Y14 (poisoning by drug/medicament, unspecified intent) ([ICD10Data T45.1X1A](https://www.icd10data.com/ICD10CM/Codes/S00-T88/T36-T50/T45-/T45.1X1A), [T45.1X5A](https://www.icd10data.com/ICD10CM/Codes/S00-T88/T36-T50/T45-/T45.1X5A))
- **MeSH:** related to D008727 (Methotrexate) with adverse-effect qualifiers
- **Pharmacogenomic entries:** ClinVar carries MTHFR c.665C>T (p.Ala222Val, rs1801133) annotated for "methotrexate response – Toxicity" ([ClinVar RCV001847567.2](https://www.ncbi.nlm.nih.gov/clinvar/RCV001847567.2/))

**Synonyms:** methotrexate intoxication, methotrexate overdose, high-dose methotrexate (HD-MTX) delayed elimination/delayed methotrexate elimination (DME), methotrexate-induced pancytopenia, methotrexate-induced nephrotoxicity/crystal nephropathy, methotrexate-associated leukoencephalopathy.

**Data source note:** Understanding of this entity is derived from a mix of aggregated resources (FAERS pharmacovigilance database, national adverse-drug-reaction registries) and individual-patient sources (case reports/series, pediatric oncology cohort studies, single-center retrospective reviews) — there is no dedicated population disease registry, so most quantitative "risk factor" data come from oncology or rheumatology cohorts rather than population-representative EHR data.

---

## 2. Etiology

### Disease causal factors
Methotrexate toxicity is fundamentally **mechanistic/iatrogenic**: it results from methotrexate (or its metabolite 7-hydroxymethotrexate) accumulating to supratherapeutic intracellular or plasma concentrations, disproportionate to the intended therapeutic antifolate effect. It is not caused by an intrinsic disease process but by a mismatch between dose/route and the patient's capacity to distribute, metabolize, and excrete the drug.

### Risk factors

**Genetic risk factors (pharmacogenomic modifiers of clearance/toxicity, not causal mutations):**
- **SLCO1B1** (encodes OATP1B1, a hepatic uptake transporter) — the SNP **rs4149056** (c.521T>C) is the most replicated genome-wide hit for delayed MTX clearance; it was independently replicated in a genome-wide study of clearance and associated with higher serum MTX at 48/72 h and elimination delay ([Ramsey et al., ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0006497120421408); [Schulte 2021, Clin Transl Sci](https://ascpt.onlinelibrary.wiley.com/doi/10.1111/cts.12879)).
- **MTHFR** (methylenetetrahydrofolate reductase) — **rs1801133 (677C>T)**: T-allele carriers have significantly higher risk of hematopoietic toxicity vs. CC genotype; **rs1801131 (1298A>C)**: CC/AC genotypes show lower toxicity frequency than AA ([Frontiers in Oncology 2021](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2021.759805/full); [Sci Rep 2025](https://www.nature.com/articles/s41598-025-33039-x)).
- **ABCB1** (P-glycoprotein/MDR1, an efflux transporter that pumps MTX out of cells) — polymorphisms influence hematopoietic toxicity risk in adults with hematologic malignancies receiving HD-MTX ([PMC8739189](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8739189/)).
- **ATIC** (AICAR transformylase, rs2372536, 347C>G) — included in meta-analyses of MTX toxicity association, relevant because MTX polyglutamates inhibit ATIC, driving adenosine accumulation.
- A case report links **MTHFR polymorphism** combined with a drug interaction to severe hematologic toxicity after low-dose MTX for ectopic pregnancy, illustrating gene–drug interaction in a non-oncology setting ([PMC12528151](https://pmc.ncbi.nlm.nih.gov/articles/PMC12528151/)).
- Genotyping of **MTHFR 677C>T and/or ABCB1** pretreatment is proposed as a means to tailor HD-MTX dosing, though clinical adoption is not standardized.

**Environmental / clinical risk factors:**
- **Renal impairment / reduced GFR** — the single strongest determinant of MTX pharmacokinetics; MTX is cleared predominantly by renal excretion, and its own nephrotoxicity can self-perpetuate a vicious cycle of reduced clearance → higher levels → more nephrotoxicity ([PMC10642233](https://pmc.ncbi.nlm.nih.gov/articles/PMC10642233/)).
- **Dehydration / inadequate hydration and urine alkalinization** during HD-MTX.
- **Third-space fluid accumulation** (pleural effusion, ascites, edema) acts as a reservoir causing delayed/biphasic clearance and redistribution toxicity, including cases of encephalopathy from a loculated parapneumonic effusion and cardiotoxicity-associated pleural effusions recapturing MTX after apparent clearance ([CHEST 2024](https://journal.chestnet.org/article/S0012-3692(24)02991-X/fulltext); [PMC13417858](https://pmc.ncbi.nlm.nih.gov/articles/PMC13417858/)).
- **Drug–drug interactions**: NSAIDs (inhibit OAT-mediated renal tubular secretion), PPIs (compete for BCRP efflux transporter, reducing renal/biliary elimination), trimethoprim-sulfamethoxazole (dual DHFR inhibition + tubular secretion competition), penicillins, and other weak organic acids ([SPS NHS](https://sps.nhs.uk/articles/managing-interactions-with-methotrexate/); [PMC13235338](https://pmc.ncbi.nlm.nih.gov/articles/PMC13235338/)).
- **Advanced age, hypoalbuminemia, folate deficiency, dosing errors (daily instead of weekly dosing in low-dose regimens), infection, dialysis-dependence** — consistently identified across low-dose MTX pancytopenia cohorts ([ScienceDirect cohort of 28 patients](https://www.sciencedirect.com/science/article/abs/pii/S1568997214001712); [PMC13511332](https://pmc.ncbi.nlm.nih.gov/articles/PMC13511332/) — dialysis patients had ~1 in 3 risk of serious adverse event or death within 90 days of starting low-dose MTX).
- **Concurrent renal-toxic agents** and **extremes of urine pH** favoring MTX/7-OH-MTX crystallization.

**Protective factors:**
- **Folic acid supplementation** in chronic low-dose regimens: reduces GI adverse effects by ~9%, elevated LFTs by ~16%, and drug discontinuation by ~15%, without abrogating efficacy ([Medscape](https://www.medscape.com/viewarticle/588229); PubMed 15965822).
- **Leucovorin (folinic acid) rescue** after HD-MTX — see Treatment section.
- **Vigorous hyperhydration and urinary alkalinization (urine pH >7)** during HD-MTX — reduces crystal nephropathy risk by keeping MTX and 7-OH-MTX in solution.
- Possible **protective MTHFR genotypes** (e.g., 1298 CC/AC) associated with lower toxicity risk in some cohorts.

**Gene–environment interactions:** The clearest example is MTHFR/ABCB1/SLCO1B1 genotype combined with concurrent nephrotoxic or transporter-competing co-medications (NSAIDs, PPIs, trimethoprim) or with pre-existing renal impairment — genetic slow-clearance variants convert an otherwise tolerable interaction into severe or fatal toxicity, as demonstrated in the ectopic-pregnancy case report combining MTHFR variant status with a drug interaction ([PMC12528151](https://pmc.ncbi.nlm.nih.gov/articles/PMC12528151/)).

---

## 3. Phenotypes

Methotrexate toxicity is a **multi-system** toxidrome. Below, phenotypes are grouped by organ system with approximate onset timing, severity range, and suggested HPO terms.

| Phenotype | Type | Onset/Course | Frequency/Severity | Suggested HPO term |
|---|---|---|---|---|
| Pancytopenia / bone marrow suppression | Laboratory abnormality | Days after dose (low-dose chronic) or ~1–2 weeks (HD-MTX); can be delayed and prolonged | Most common manifestation of low-dose toxicity — reported in ~78.5% of low-dose toxicity cases in one series; mortality up to 25–44% in fatal cohorts, chiefly via sepsis | HP:0001876 (Pancytopenia) |
| Oral/GI mucositis, ulcerative stomatitis | Sign/symptom | Onset 3–7 days post HD-MTX; self-limited, <2 weeks | Very frequent (leading FAERS-reported reaction) | HP:0000164 (Abnormality of the oral cavity) / HP:0034754-like ulcerative stomatitis |
| Nausea, vomiting, diarrhea, abdominal distress | Symptom | Acute, dose-related | Common | HP:0002015 (Vomiting), HP:0002014 (Diarrhea) |
| Acute kidney injury / crystal nephropathy | Clinical sign/lab abnormality | Acute, within hours to days of HD-MTX | Central to delayed elimination cascade | HP:0001919 (Acute kidney injury) |
| Hepatotoxicity (acute transaminitis; chronic fibrosis/cirrhosis with prolonged low-dose use) | Laboratory abnormality / clinical sign | Acute: days; Chronic: after ≥2 years and cumulative dose ≥1.5 g | Acute reversible chemical hepatitis common; chronic fibrosis rarer but potentially fatal | HP:0002910 (Elevated hepatic transaminase), HP:0001394 (Hepatic fibrosis) |
| Pneumonitis / interstitial lung disease | Clinical sign | Variable, can be subacute | Incidence 0.3–14% across cohorts | HP:0006515 (Interstitial pneumonitis) |
| Leukoencephalopathy / stroke-like episodes / encephalopathy | Clinical sign, often on MRI | Acute-subacute (intrathecal or HD-MTX with CNS penetration; can mimic stroke) | Reported particularly in pediatric ALL and intrathecal overdose | HP:0002317 (Leukoencephalopathy) — see also mimicking HP:0001297 (Stroke) |
| Skin/mucosal toxicity (rash, mucocutaneous ulceration) | Physical sign | Days, can be severe in low-dose error cases | Reported with invasive secondary infection (e.g., mucormycosis) in severe cases | HP:0000988 (Skin rash) |
| Myocarditis / cardiotoxicity, transudative pleural effusion | Clinical sign | Case-report level, rare | Rare | HP:0001636 (Myocarditis) |
| Chemical conjunctivitis | Sign | Acute | Uncommon | HP:0000509 (Conjunctivitis) |
| Fever | Sign | Accompanies pancytopenia/sepsis | Common in severe presentations | HP:0001945 (Fever) |
| Bleeding/purpura (from thrombocytopenia) | Sign | Subacute | Seen in severe pancytopenia | HP:0000978 (Bruising susceptibility) |

**Quality-of-life impact:** Mucositis and GI symptoms substantially impair oral intake and daily function during acute episodes; pancytopenia-associated infection/sepsis is the dominant driver of morbidity and mortality; chronic hepatic fibrosis and pulmonary fibrosis (in long-term low-dose regimens) can produce lasting functional impairment. Neurotoxic leukoencephalopathy, when it occurs, can leave residual cognitive/motor deficits, particularly in pediatric ALL survivors, and diagnostic ambiguity with acute stroke can trigger inappropriate thrombolysis, itself a risk ([PMC10834224](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10834224/)).

---

## 4. Genetic/Molecular Information

Because methotrexate toxicity is not a monogenic disease, this section covers **pharmacogenomic modifiers** rather than disease-causing mutations.

- **Causal "gene"**: none in the Mendelian sense; the causal agent is the drug itself acting on its target enzyme, **DHFR** (dihydrofolate reductase, HGNC:2861), and downstream folate-pathway enzymes.
- **Modifier genes and variant detail:**
  - **MTHFR** (HGNC:7436) — rs1801133 (677C>T, p.Ala222Val) and rs1801131 (1298A>C, p.Glu429Ala); missense variants reducing enzyme activity and altering intracellular folate pools, modifying (not causing) toxicity risk. ClinVar records rs1801133 under "methotrexate response – Toxicity" ([ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/RCV001847567.2/)).
  - **SLCO1B1** (HGNC:10959) — rs4149056 (c.521T>C, p.Val174Ala), a missense variant reducing OATP1B1 hepatic uptake transporter function, associated with elevated 48h/72h MTX levels and elimination delay in genome-wide analyses ([ScienceDirect GWAS](https://www.sciencedirect.com/science/article/pii/S0006497120421408)).
  - **ABCB1/MDR1** (HGNC:40) — encodes P-glycoprotein efflux transporter; polymorphisms (e.g., in exons 21/26, commonly studied SNPs 1236C>T, 2677G>T/A, 3435C>T) modify hematopoietic toxicity risk.
  - **ATIC** (HGNC:794) — rs2372536 (347C>G); MTX polyglutamates directly inhibit the ATIC gene product, so variants here modulate the resulting adenosine surge implicated in toxicity/efficacy.
- **Allele frequency / population data:** Not systematically reported for this entity; MTHFR 677T allele frequency and SLCO1B1 521C allele frequency vary by ancestry and would be sourced from gnomAD/1000 Genomes for population context (not disease-specific).
- **Somatic vs. germline:** All pharmacogenomic variants relevant here are **germline**; toxicity is not driven by somatic mutation.
- **Functional consequences:** DHFR inhibition by MTX is the central molecular lesion (competitive, high-affinity inhibition blocking dihydrofolate → tetrahydrofolate conversion); polyglutamated MTX additionally inhibits **thymidylate synthase (TYMS)** and **AICAR transformylase (ATIC)**, and to a lesser extent other folate-dependent enzymes, compounding antifolate effects at high intracellular concentration.
- **Epigenetic information:** Not a primary driver of this entity; folate-pathway disruption itself affects **DNA methylation** capacity (via impaired S-adenosylmethionine regeneration, a downstream consequence of folate/homocysteine cycle disruption) — this is a *consequence* pathway rather than a causal epigenetic lesion, and is invoked in proposed mechanisms of MTX neurotoxicity (homocysteine/NMDA-receptor toxicity).
- **Chromosomal abnormalities:** Not applicable; this is a toxic/pharmacologic disorder rather than a structural genomic disease.

---

## 5. Environmental Information

- **Environmental/pharmacological factors**: The "environmental exposure" here is the drug itself and co-administered agents. Key interacting exposures:
  - **NSAIDs** — inhibit renal organic anion transporters (OAT), reducing MTX renal clearance, especially at high MTX doses ([SPS NHS](https://sps.nhs.uk/articles/managing-interactions-with-methotrexate/)).
  - **Proton pump inhibitors (PPIs)** — compete with MTX for BCRP efflux transporters, reducing renal and biliary elimination ([Pharmacy Times](https://www.pharmacytimes.com/view/methotrexate-and-proton-pump-inhibitors); [PMC13235338](https://pmc.ncbi.nlm.nih.gov/articles/PMC13235338/)).
  - **Trimethoprim-sulfamethoxazole** — additive DHFR inhibition plus tubular secretion competition, a well-documented cause of severe pancytopenia when combined with MTX.
  - **Penicillins and other weak organic acids** — compete for renal tubular secretion.
  - **Alcohol** — compounds hepatotoxicity risk in chronic low-dose regimens.
- **Lifestyle factors**: Poor oral hydration/fluid intake during HD-MTX cycles increases nephrotoxicity risk; adherence errors (e.g., inadvertent daily dosing instead of weekly dosing of low-dose oral MTX) are a well-recognized and preventable cause of severe/fatal toxicity.
- **Infectious agents**: Not a cause of the toxicity itself, but **secondary opportunistic infection** (bacterial sepsis, and rarely invasive fungal infection such as pulmonary mucormycosis) is a major downstream consequence of MTX-induced myelosuppression/mucosal barrier breakdown and a leading cause of death ([Frontiers case report — pulmonary mucormycosis after low-dose MTX toxicity](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2025.1704810/full)).

---

## 6. Mechanism / Pathophysiology

### Causal chain (ordered)

1. **Methotrexate (and active polyglutamated metabolites) enter cells** via reduced folate carrier/folate receptors and are retained intracellularly as **methotrexate polyglutamates (MTX-PG)**.
2. **MTX and MTX-PG competitively and with high affinity inhibit dihydrofolate reductase (DHFR)**, blocking the reduction of dihydrofolate (DHF) to tetrahydrofolate (THF) — *this is the primary, directly demonstrated molecular lesion* ([Frontiers/PMC synthesis](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2025.1704810/full)).
3. **THF depletion leads to** (a) impaired one-carbon transfer reactions required for **thymidylate synthesis** (via inhibited thymidylate synthase cofactor supply) and **purine synthesis** (via inhibited glycinamide ribonucleotide transformylase and **AICAR transformylase/ATIC**), and (b) impaired **methionine/homocysteine cycling** (via inhibited methionine synthase cofactor supply) — this branch point produces two downstream consequences.
4. **Branch A — impaired DNA/RNA synthesis** → **arrests cells in S-phase**, disproportionately affecting rapidly dividing tissues: bone marrow precursors, GI mucosal epithelium, hair follicles → this **leads to** myelosuppression (pancytopenia) and mucositis/enterocolitis (this is directly demonstrated in rodent models and human marrow/mucosal biopsies).
5. **Branch A also produces** locally elevated **oxidative stress (reactive oxygen species)**, which **leads to** apoptosis via caspase-3/caspase-8 activation and nitrosative stress in intestinal epithelium — demonstrated in rat intestinal mucositis models showing villus atrophy, crypt loss, and elevated cleaved caspase-3/8 ([Naunyn-Schmiedeberg's Arch Pharmacol 2024](https://pubmed.ncbi.nlm.nih.gov/38822868/); [PMC — Wnt/β-catenin enterocyte turnover rat model](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4222808/)).
6. **Branch B — ATIC inhibition** → accumulation of AICA-ribotide → **leads to increased extracellular adenosine release**, an anti-inflammatory but also neuro-vasoactive mediator implicated both in MTX's therapeutic anti-inflammatory action in rheumatoid arthritis and in **acute methotrexate-related encephalopathy** via adenosine-mediated vasodilation and cerebral edema (mechanism is **inferred from clinical/pharmacologic correlation, not fully demonstrated causally in humans**) ([Frontiers/BJP 2003](https://bpspubs.onlinelibrary.wiley.com/doi/10.1038/sj.bjp.0705054)).
7. **Branch B also causes** impaired remethylation of homocysteine → **elevated homocysteine**, which is proposed (inferred, not conclusively proven) to exert **direct endothelial toxicity and excitatory NMDA-receptor-mediated neurotoxicity**, contributing to white-matter injury and leukoencephalopathy ([Neurotoxic effects review, PMC11981439](https://pmc.ncbi.nlm.nih.gov/articles/PMC11981439/)).
8. **In parallel, independent of the folate-inhibition cascade — a pharmacokinetic branch**: MTX and its hepatic metabolite **7-hydroxymethotrexate (7-OH-MTX)** are renally excreted largely unchanged; at high concentrations and especially in acidic or low-volume urine, both **precipitate as crystals within renal tubular lumens**, causing **direct mechanical tubular obstruction** and **direct pharmacological/cytotoxic tubular cell injury** (S-phase arrest of tubular epithelial cells, plus 7-OH-MTX-induced oxidative stress and apoptosis in tubular cells) → this **leads to acute kidney injury/crystal nephropathy** ([NEJM correspondence](https://www.nejm.org/doi/full/10.1056/NEJMc1507547); [PMC9293278](https://ncbi.nlm.nih.gov/pmc/articles/PMC9293278); [Impact of MTX/7-OH-MTX on renal toxicity, PMC11739129](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11739129/)).
9. **Acute kidney injury then reduces renal MTX clearance**, which **feeds back** to raise systemic MTX exposure further — a self-amplifying vicious cycle that is the pathophysiologic core of "**delayed methotrexate elimination (DME)**," the syndrome underlying most severe/fatal HD-MTX toxicity.
10. Independently, **third-space fluid collections (pleural effusion, ascites)** act as a **redistribution reservoir**: MTX partitions into these compartments during the infusion/high-plasma-level phase and **releases back into the circulation later**, producing delayed or biphasic rebound toxicity even after apparent initial clearance — demonstrated in multiple case reports where thoracentesis/effusion drainage produced rapid clinical and biochemical improvement ([CHEST 2024](https://journal.chestnet.org/article/S0012-3692(24)02991-X/fulltext); [PMC13417858](https://pmc.ncbi.nlm.nih.gov/articles/PMC13417858/)).
11. The combined consequences of Branches A, B, and the renal/pharmacokinetic branch converge on the clinical syndrome: **pancytopenia + sepsis risk, mucositis, hepatotoxicity, pneumonitis, and (in CNS-exposed patients) leukoencephalopathy**, with **AKI-driven impaired clearance** determining overall severity and duration.

### Category detail

- **Molecular pathways**: One-carbon/folate metabolism (KEGG hsa00670), purine biosynthesis, pyrimidine (thymidylate) biosynthesis, methionine/homocysteine cycle.
- **Cellular processes**: Cell-cycle S-phase arrest; apoptosis (caspase-3/-8 dependent); oxidative/nitrosative stress; microglial activation and oligodendrocyte precursor depletion (proposed mechanism for demyelination in leukoencephalopathy) ([PMC11981439](https://pmc.ncbi.nlm.nih.gov/articles/PMC11981439/)).
- **Protein dysfunction**: DHFR is not structurally altered but is **pharmacologically inhibited** (competitive antagonism at the folate-binding site) — a functional rather than structural lesion.
- **Metabolic changes**: Reduced tetrahydrofolate pools; elevated homocysteine; accumulation of AICA-ribotide and extracellular adenosine; possible hyperammonemia in severe cases (via purine-cycle disruption, less well established).
- **Immune system involvement**: Adenosine-mediated immunosuppression is central to MTX's therapeutic anti-inflammatory action in RA but is mechanistically linked (via ROS generation in monocytoid/cytotoxic T-cell lines) to lymphocyte toxicity ([BJP 2003](https://bpspubs.onlinelibrary.wiley.com/doi/10.1038/sj.bjp.0705054)).
- **Tissue damage mechanisms**: Oxidative stress and apoptosis (GI mucosa); crystal-mediated tubular obstruction plus direct cytotoxicity (kidney); presumed blood-brain-barrier cumulative toxic injury (CNS).
- **Biochemical abnormalities**: DHFR inhibition; secondary thymidylate synthase and ATIC pathway disruption; hyperhomocysteinemia.
- **Molecular profiling**: Gut microbiota composition is significantly altered in a time-dependent manner following MTX administration in mouse models, implicating dysbiosis in GI toxicity ([PubMed 30049384](https://pubmed.ncbi.nlm.nih.gov/30049384/)).
- **Suggested ontology terms**: GO:0004146 (dihydrofolate reductase activity), GO:0006281 (DNA repair)/GO:0006260 (DNA replication) for S-phase arrest context, GO:0006915 (apoptotic process), GO:0034599 (cellular response to oxidative stress), GO:0006144 (purine nucleobase metabolic process); CL:0000075 (epithelial cell — intestinal/renal tubular), CL:0000097 (mast cell — not primary but relevant to mucosal injury context), CL:0000451 (dendritic cell)/CL:0000542 (lymphocyte) for immune involvement.

---

## 7. Anatomical Structures Affected

- **Organ level (primary)**: Bone marrow (hematopoietic suppression), gastrointestinal tract (mucosal ulceration/mucositis), kidney (crystal nephropathy/AKI), liver (hepatocellular injury/fibrosis), lung (pneumonitis/interstitial lung disease), central nervous system (leukoencephalopathy, encephalopathy). Secondary involvement: skin/mucous membranes (rash, ulceration), heart (rare myocarditis/pericardial-pleural effusion), eye (chemical conjunctivitis).
- **Body systems**: Hematologic, digestive, renal/urinary, hepatic, respiratory, nervous, integumentary — essentially a multisystem toxidrome. UBERON terms: UBERON:0002371 (bone marrow), UBERON:0001007 (digestive system), UBERON:0002113 (kidney), UBERON:0002107 (liver), UBERON:0002048 (lung), UBERON:0000955 (brain), especially UBERON:0002316 (white matter of central nervous system) for leukoencephalopathy.
- **Tissue/cell level**: Bone marrow hematopoietic progenitor cells; small intestinal crypt/villus enterocytes (villus atrophy, crypt loss documented in rat models); renal proximal tubular epithelial cells; hepatocytes; alveolar epithelium/interstitium; oligodendrocytes and microglia in CNS white matter. Cell Ontology: CL:0000015 (hematopoietic stem cell), CL:0000584 (enterocyte), CL:1000838 (kidney proximal convoluted tubule epithelial cell), CL:0000182 (hepatocyte), CL:0000128 (oligodendrocyte), CL:0000129 (microglial cell).
- **Subcellular level**: Nucleus (DNA/RNA synthesis blockade); mitochondria (implicated in oxidative-stress-driven apoptosis). GO Cellular Component: GO:0005634 (nucleus), GO:0005739 (mitochondrion).
- **Localization**: Renal toxicity is typically bilateral (both kidneys via systemic circulation); CNS leukoencephalopathy is often bilateral, periventricular/deep white matter — imaging pattern that can mimic bilateral acute ischemic stroke, prompting inappropriate thrombolysis in reported cases ([PMC10834224](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10834224/)).

---

## 8. Temporal Development

- **Onset**: Depends entirely on regimen. Low-dose weekly oral/SC MTX toxicity (e.g., in RA) is typically **insidious/subacute**, emerging over weeks to months, often precipitated by an acute trigger (dosing error, new interacting drug, intercurrent renal impairment). HD-MTX toxicity is **acute**, unfolding over hours to days after infusion, with mucositis at day 3–7 and nephrotoxicity/pancytopenia nadir around day 7–14.
- **Progression**: Follows a **dose-and-clearance-dependent course** rather than fixed disease stages. "Delayed methotrexate elimination" is the operative staging concept: normal clearance vs. mild/moderate delay (managed with leucovorin dose escalation) vs. severe delay with organ dysfunction (requiring glucarpidase). Progression rate is variable — rapid deterioration is possible with renal injury feedback loops or third-space redistribution.
- **Course pattern**: Generally **self-limited and reversible** with prompt supportive care/rescue therapy in most cases (mucositis "usually...lasts less than 2 weeks"); can be **relapsing/biphasic** when third-space fluid redistributes drug back into circulation after apparent clearance, or when a second high-dose cycle is given without addressing the prior cause of delayed clearance. Chronic hepatotoxicity/pulmonary fibrosis from long-term low-dose regimens follows an **indolent, cumulative-dose-dependent** course over years.
- **Remission**: Spontaneous resolution occurs once the drug is cleared/inactivated (endogenously or via glucarpidase) and marrow/mucosal/renal recovery proceeds; treatment-induced remission via leucovorin rescue and, when needed, glucarpidase.
- **Critical periods/windows for intervention**: Leucovorin rescue must begin within 24–48 hours of MTX administration (or within 24 hours of completing an infusion) to be maximally effective, and continues until MTX level falls below 0.1 µM ([BJCP review](https://bpspubs.onlinelibrary.wiley.com/doi/10.1111/bcp.16096)). Glucarpidase is most effective when given promptly once severe toxicity/AKI with markedly elevated MTX levels is recognized, reducing plasma MTX by ≥97% within 15 minutes ([FDA approval summary via PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8756618/)).

---

## 9. Inheritance and Population

- **Epidemiology**: No single population-wide prevalence/incidence figure exists because this is a treatment-emergent toxicity, not an independent disease with fixed population prevalence; incidence is reported per exposed cohort:
  - Interstitial lung disease/pneumonitis: 0.3–14% of MTX-exposed patients depending on cohort and dose.
  - Pancytopenia is the dominant manifestation of low-dose toxicity, detected in ~78.5% of cases in one low-dose toxicity case series (n=28) ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1568997214001712)).
  - FAERS pharmacovigilance analysis (2004–2024) captured 130,818 MTX-related adverse event reports, with females representing 64.2% of reporters and adults 18–64.9 years the most frequent age group ([Frontiers in Immunology 2025](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2025.1586361/full)).
  - Among dialysis patients newly started on low-dose MTX, approximately **1 in 3 experienced a serious adverse event or death within 90 days** ([PMC13511332](https://pmc.ncbi.nlm.nih.gov/articles/PMC13511332/)).
  - Mortality in major MTX-toxicity cohorts: reported figures range from ~12.9% (27/31 discharged, 4 died) to markedly higher (25–44%) in specifically pancytopenia-driven low-dose toxicity series, chiefly from sepsis.
- **Inheritance pattern**: Not applicable in the Mendelian sense — this is an acquired, drug-induced condition modulated by common pharmacogenomic variants (MTHFR, SLCO1B1, ABCB1) inherited in the general population as ordinary polymorphisms rather than disease alleles. No single-gene inheritance pattern, penetrance, expressivity, anticipation, mosaicism, or founder-effect concept applies directly, though the modifying alleles themselves (e.g., MTHFR 677T) have population-specific allele frequencies (higher in some European and East Asian populations) that could stratify risk.
- **Population demographics**: Affected populations mirror the populations receiving MTX therapeutically: RA/psoriasis/IBD patients (predominantly adult, female-skewed given RA epidemiology), pediatric and young-adult ALL/lymphoma patients (HD-MTX protocols), and dialysis/renal-impaired patients (disproportionately high-risk subgroup). No distinct geographic endemicity; distribution follows MTX prescribing patterns globally.
- **Sex ratio**: FAERS data show a notable female predominance among adverse-event reporters (64.2%), likely reflecting the female predominance of rheumatoid arthritis rather than a sex-specific toxicity mechanism.
- **Age distribution**: Bimodal in practice — pediatric/young-adult oncology patients receiving HD-MTX, and adult/elderly patients on chronic low-dose regimens (with elderly ≥65 years patients also showing increased risk of drug hypersensitivity per the FAERS analysis).

---

## 10. Diagnostics

**Laboratory tests:**
- **Serum/plasma MTX concentration** via immunoassay or LC-MS/MS, monitored at defined intervals (commonly 24/48/72 hours) post-HD-MTX to guide leucovorin dosing and trigger escalation of care ([JALM 2025](https://academic.oup.com/jalm/article/11/2/320/8439372)). LOINC-coded methotrexate serum level assays exist for this purpose.
- **Complete blood count** (for pancytopenia/myelosuppression), **liver function tests** (AST/ALT/bilirubin), **serum creatinine/BUN and eGFR** (renal function and monitoring for AKI), **urine pH** (to confirm alkalinization adequacy).
- **Critical assay caveat**: after glucarpidase administration, a non-toxic MTX metabolite (DAMPA) **cross-reacts with standard immunoassays**, producing artifactually elevated apparent MTX levels; **LC-MS/MS is required** for accurate post-glucarpidase monitoring ([PubMed 29994985](https://pubmed.ncbi.nlm.nih.gov/29994985/); [Pediatr Blood Cancer 2024](https://onlinelibrary.wiley.com/doi/10.1002/pbc.30831)).
- **Biomarkers**: Homocysteine level (proposed neurotoxicity correlate); no FDA-qualified specific biomarker panel beyond MTX level itself and standard organ-function labs.

**Imaging**: Brain MRI (T2/FLAIR/diffusion-weighted imaging) for suspected leukoencephalopathy — shows restricted diffusion in white matter that can mimic acute ischemic stroke ([Ann Child Neurol 2024](https://www.annchildneurol.org/upload/pdf/acn-2024-00507.pdf); [PMC10834224](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10834224/)); chest radiograph/CT for pneumonitis; abdominal imaging to detect ascites/effusions as third-space reservoirs before HD-MTX.

**Functional/electrophysiologic tests**: EEG may show nonspecific slowing in MTX encephalopathy; nerve conduction studies have been explored for MTX-related peripheral/central neurotoxicity diagnostic challenges ([PMC12269288](https://pmc.ncbi.nlm.nih.gov/articles/PMC12269288/)).

**Genetic testing**: Not part of routine standard-of-care diagnosis of toxicity itself, but pretreatment **MTHFR 677C>T / 1298A>C**, **SLCO1B1 rs4149056**, and **ABCB1** genotyping have been proposed (research/selected-center use) to risk-stratify patients before HD-MTX, particularly in hematologic malignancy protocols.

**Clinical criteria**: No formal DSM/ICD diagnostic algorithm exists beyond recognizing the clinical/laboratory toxidrome (cytopenia, mucositis, rising creatinine, elevated MTX level) in the context of known exposure. Diagnosis is fundamentally exposure-based (poisoning/adverse-effect coding under ICD-10 T45.1).

**Differential diagnosis**: For pancytopenia — other drug-induced marrow suppression, aplastic anemia, myelodysplastic syndrome (a reported longer-term hematologic sequela of chronic low-dose MTX, per a 2025 case report of therapy-related MDS ([Oxford Med Case Reports](https://academic.oup.com/omcr/article/2025/11/omaf253/8343280))); for AKI — other nephrotoxic drug exposures, tumor lysis syndrome; for leukoencephalopathy — acute ischemic stroke (a well-documented diagnostic pitfall leading to inappropriate thrombolysis), PRES, other toxic/metabolic leukoencephalopathies.

**Screening**: Baseline CBC, renal function, liver function, and (in women of reproductive age) pregnancy testing before initiating MTX at any dose; ongoing periodic CBC/LFT/renal monitoring throughout chronic low-dose therapy is the principal "screening" strategy for evolving toxicity ([AAFP guide to monitoring methotrexate](https://www.aafp.org/afp/2000/1001/p1607)).

---

## 11. Outcome / Prognosis

- **Mortality**: Highly variable by setting. In severe low-dose MTX-induced pancytopenia cohorts, mortality has been reported as high as 25–44%, almost always due to sepsis/infection in the setting of neutropenia. In a broader major-toxicity cohort, 4/31 patients (12.9%) died. Dialysis patients starting low-dose MTX had markedly elevated 90-day risk of serious adverse events or death (~1 in 3) compared with hydroxychloroquine comparators.
- **Morbidity/functional outcomes**: Most acute toxicity (mucositis, cytopenia, mild-moderate AKI) is reversible with prompt supportive care; chronic hepatic fibrosis/cirrhosis and pulmonary fibrosis from long-term low-dose therapy can cause lasting organ impairment. CNS leukoencephalopathy may leave residual neurocognitive deficits, particularly relevant in pediatric ALL survivors.
- **Complications**: Secondary bacterial sepsis (leading cause of death in pancytopenic patients), invasive fungal infection (e.g., pulmonary mucormycosis reported after severe low-dose toxicity), myelodysplastic syndrome as a longer-term hematologic sequela, and diagnostic/iatrogenic complications such as inappropriate thrombolytic therapy given for MTX-leukoencephalopathy misdiagnosed as stroke.
- **Recovery potential**: Excellent with early recognition and appropriate rescue therapy (leucovorin ± glucarpidase, dialysis for severe renal failure); recovery potential drops sharply once profound, prolonged pancytopenia with sepsis or severe multiorgan AKI supervenes.
- **Prognostic factors**: **WBC count at hospital admission** has been identified as the most important prognostic factor for survival in low-dose MTX pancytopenia; degree/duration of renal impairment and time-to-initiation of rescue therapy (leucovorin/glucarpidase) are key prognostic determinants in HD-MTX toxicity; presence of third-space fluid collections predicts a more protracted/relapsing course.

---

## 12. Treatment

### Pharmacotherapy / rescue agents
- **Leucovorin (folinic acid) rescue** — the mainstay. Provides a reduced folate (tetrahydrofolate precursor) that bypasses the DHFR block. Standard HD-MTX rescue dosing: **10–25 mg/m² IV or IM every 6 hours for 72 hours**; in renal compromise, higher dosing (**150 mg/m² every 3 hours**) is used. For overdose/unknown MTX level: **up to 100 mg/m² IV**. Must begin within 24–48 hours of MTX start (or ≤24 hours after infusion completion) and continue until MTX level <0.1 µM ([J Clin Pharm Ther review](https://onlinelibrary.wiley.com/doi/abs/10.1111/jcpt.13739); [BJCP 2025](https://bpspubs.onlinelibrary.wiley.com/doi/10.1111/bcp.16096)). Caution: excessive leucovorin can reduce MTX's antitumor efficacy; repeated high-dose calcium folinate can cause **hypercalcemia**.
- **Glucarpidase (carboxypeptidase G2)** — recombinant bacterial enzyme, **FDA-approved 2012**, cleaves ~99% of circulating MTX to inactive metabolites (DAMPA and glutamate) within 15 minutes; FDA-recommended dose **≥50 U/kg**, reducing plasma MTX by ≥97% ([PMC8756618](https://pmc.ncbi.nlm.nih.gov/articles/PMC8756618/)). Indicated for HD-MTX patients with markedly elevated MTX and/or renal impairment refractory to hydration/alkalinization/leucovorin. Leucovorin should not be given within 2 hours before or after glucarpidase (leucovorin is also a glucarpidase substrate). NCIT: **NCIT:C1872**-style specific-agent binding pattern; glucarpidase itself would bind to an NCIT drug/agent term (e.g., analogous to therapeutic_agent slot) under `treatment_term` NCIT:C15986 (Pharmacotherapy) with `therapeutic_agent` for glucarpidase and separately for leucovorin/folinic acid.
- **NCIT clinical-intervention terms** applicable: NCIT:C15986 (Pharmacotherapy) as the treatment_term for both leucovorin and glucarpidase administration; NCIT:C49236 (Therapeutic Procedure) may apply to hyperhydration/alkalinization protocols.

### Supportive and procedural measures
- **Aggressive IV hyperhydration** and **urinary alkalinization** (target urine pH ≥7) to maintain MTX/7-OH-MTX solubility and prevent crystal nephropathy — foundational to all HD-MTX protocols ([European consensus, PMC11446969](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11446969/); [Middle East consensus 2025](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2025.1660937/full)).
- **Drainage of third-space fluid collections** (thoracentesis/chest tube for pleural effusion, paracentesis for ascites) before HD-MTX administration when feasible, and emergently if delayed clearance/redistribution toxicity is identified — demonstrated to rapidly improve MTX kinetics and clinical status in case reports.
- **Renal replacement therapy** (high-flux hemodialysis, sometimes combined with high-dose folinic acid) for severe AKI with markedly elevated MTX refractory to other measures ([PMC3636355](https://pmc.ncbi.nlm.nih.gov/articles/PMC3636355/)).
- **Discontinuation of interacting drugs** (NSAIDs, PPIs, trimethoprim-sulfamethoxazole) is a critical, low-tech but essential intervention.
- **Pegylated G-CSF** and supportive transfusion for severe myelosuppression ([J Cancer Detect Diagn Res 2024 case report](https://journals.lww.com/cddr/fulltext/2024/08020/acute_methotrexate_toxicity_managed_with.12.aspx)).

### Experimental / investigational
- Routine low-dose glucarpidase following HD-MTX in adult CNS lymphoma patients has been studied as a preventive strategy in a phase I open-label multi-center study ([PMC8756618](https://pmc.ncbi.nlm.nih.gov/articles/PMC8756618/)).
- Preclinical/animal-model protective strategies for MTX-induced intestinal mucositis include mesenchymal stem cells plus glutathione, lutein, butyrate, and olmesartan, targeting oxidative stress and inflammatory pathways ([PMC13358174](https://pmc.ncbi.nlm.nih.gov/articles/PMC13358174/); [PMC3765170](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3765170/); [PMC8617074](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8617074/); [PMC4273993](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4273993/)) — these are model-organism/in-vitro findings, not yet standard clinical practice.

### Treatment algorithm (escalation logic)
1. Baseline risk stratification (renal function, third-space fluid, drug list review) before HD-MTX.
2. Hyperhydration + urinary alkalinization throughout infusion.
3. Scheduled leucovorin rescue starting per protocol timing.
4. Serum MTX level monitoring at defined intervals (e.g., 24/48/72 h) with leucovorin dose escalation if levels exceed nomogram thresholds.
5. If MTX remains markedly elevated despite hydration/alkalinization/leucovorin, or AKI develops → **glucarpidase**, with leucovorin timing adjusted around dosing, and switch to LC-MS/MS for subsequent MTX monitoring.
6. Dialysis for refractory severe renal failure.
7. Supportive care (transfusion, G-CSF, antimicrobial prophylaxis/treatment) for cytopenia-related complications.

---

## 13. Prevention

- **Primary prevention**: Careful patient selection (avoid MTX or use extreme caution in renal impairment — MTX is contraindicated at creatinine clearance <50 mL/min per common guidance), pre-treatment drug reconciliation to avoid NSAID/PPI/trimethoprim co-prescription, correct dosing education (especially preventing inadvertent daily dosing of weekly low-dose oral regimens — a recurrent, preventable cause of severe toxicity), and drainage of pre-existing third-space fluid collections before HD-MTX.
- **Secondary prevention (early detection)**: Scheduled CBC, renal function, and liver function monitoring throughout MTX therapy (baseline plus periodic monitoring per AAFP/rheumatology guidance); serum MTX level monitoring at fixed intervals during HD-MTX; prompt recognition of early mucositis/cytopenia signs to trigger dose modification or rescue escalation.
- **Tertiary prevention**: Leucovorin rescue and glucarpidase administration to prevent progression to organ failure once toxicity is identified; drainage of accumulating effusions to prevent relapse.
- **Folic acid supplementation** in chronic low-dose regimens reduces incidence of GI adverse effects, LFT elevation, and treatment discontinuation, though no consensus dosing regimen exists ([Medscape](https://www.medscape.com/viewarticle/588229)).
- **Genetic/risk stratification**: Pretreatment MTHFR/ABCB1/SLCO1B1 genotyping has been proposed as a personalized-prevention strategy in HD-MTX oncology protocols, though not yet part of standard guidelines.
- **Public health / systems-level**: Standardized institutional protocols (structured risk stratification for delayed elimination, standardized monitoring intervals, pharmacokinetically guided leucovorin dose adjustment, and criteria for early glucarpidase use) were the focus of 2024–2025 regional consensus statements (Middle East and European consensus groups), reflecting an active area of guideline development ([Frontiers in Oncology 2025](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2025.1660937/full); [European consensus, PMC11446969](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11446969/)).
- **Counseling**: Patient education regarding weekly (not daily) dosing for low-dose oral regimens, avoidance of alcohol and interacting OTC medications (NSAIDs), and prompt reporting of mucositis/fever/bruising.

---

## 14. Other Species / Natural Disease

Methotrexate toxicity is not a naturally occurring disease in animals but is extensively **induced experimentally**; it is also encountered clinically in veterinary oncology when MTX or related antifolates are used therapeutically in companion animals, though this is not well represented in the search results retrieved. No OMIA entry or spontaneous veterinary disease model was identified in this search; the "natural disease" concept does not apply here (this is a pharmacologic/toxic disorder, not a genetic disease with cross-species natural occurrence). Orthologous relevance is instead expressed through the conservation of the DHFR/folate pathway across mammals, which is why rodent models faithfully reproduce human-relevant intestinal, renal, and marrow toxicity (see Model Organisms below). No zoonotic or transmission relevance applies, as this is a drug toxicity, not an infectious or heritable disease.

---

## 15. Model Organisms

- **Model types**: Predominantly **rodent (rat and mouse) induced-toxicity models**; no established knockout/transgenic genetic models specific to this toxicity (since it is drug-induced, not gene-driven), though DHFR and folate-pathway gene knockouts/hypomorphs in mice have been used in related folate-biology research.
- **Specific model systems**:
  - **Rat intestinal mucositis model**: intraperitoneal MTX injection (a commonly cited regimen is ~10 mg/kg IP every 3 days for 3 doses, or single higher-dose regimens) reproducibly induces villus atrophy, crypt loss, and decreased crypt cell proliferation, maximal around day 3–5 post-injection, with recovery mediated by HGF/c-Met upregulation ([PMC2374397](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2374397/); [PMC4222808](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4222808/)).
  - **Mouse models of GI toxicity and gut microbiota disruption**: demonstrate time-dependent alteration of gut microbial diversity and immune/macrophage response following MTX administration ([PubMed 30049384](https://pubmed.ncbi.nlm.nih.gov/30049384/)).
  - **Rat nitrosative-stress small intestinal injury model** ([Arch Toxicol 2008](https://link.springer.com/article/10.1007/s00204-008-0287-9)).
  - **IEC-6 rat intestinal epithelial cell line** (in vitro) used to study ROS-mediated apoptosis and protective agents such as lutein ([PMC3765170](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3765170/)).
  - **Osteosarcoma cell lines** used to study MTX resistance mechanisms via ROS/p53-mediated apoptosis modulated by estrogen-related receptor alpha ([PMC4055217](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4055217/)) — relevant to efficacy/resistance rather than toxicity per se, but mechanistically overlapping.
  - **Rabbit model** for MTX-ketoprofen (NSAID) pharmacokinetic interaction studies, directly modeling the human drug-interaction toxicity risk ([PMC1971536](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1971536/)).
- **Phenotype recapitulation**: Rodent models faithfully reproduce human intestinal mucositis (villus atrophy, crypt apoptosis) and renal/hepatic oxidative injury, and are used to test protective/mitigating agents (mesenchymal stem cells + glutathione, Daikenchuto herbal formula, butyrate, olmesartan). They do not fully recapitulate the human leukoencephalopathy phenotype, and CNS-toxicity mechanisms remain comparatively less modeled.
- **Model limitations**: Acute high-bolus IP dosing regimens in rodents do not perfectly mirror the pharmacokinetics of human HD-MTX infusion protocols with leucovorin rescue, and species differences in folate metabolism and renal handling of MTX/7-OH-MTX limit direct extrapolation, particularly for nephrotoxicity thresholds and third-space redistribution kinetics.
- **Research applications**: These models are primarily used to test **GI-mucositis mitigation strategies** (probiotics/microbiota modulation, antioxidants, growth factors) and to dissect the ROS/apoptosis/inflammatory signaling underlying mucosal and renal injury, informing candidate adjunctive therapies (none yet FDA-approved beyond leucovorin/glucarpidase).

---

## Summary of Suggested Ontology Terms for KB Curation

| Category | Examples |
|---|---|
| HP | HP:0001876 (Pancytopenia), HP:0001919 (Acute kidney injury), HP:0002910 (Elevated hepatic transaminase), HP:0006515 (Interstitial pneumonitis), HP:0002317 (Leukoencephalopathy), HP:0000164 (oral cavity abnormality/mucositis), HP:0001945 (Fever) |
| GO (BP) | GO:0006281/GO:0006260 (DNA synthesis/replication context), GO:0006915 (apoptotic process), GO:0034599 (cellular response to oxidative stress), GO:0006144 (purine nucleobase metabolic process) |
| GO (MF) | GO:0004146 (dihydrofolate reductase activity) |
| CL | CL:0000015 (hematopoietic stem cell), CL:0000584 (enterocyte), CL:1000838 (proximal tubule epithelial cell), CL:0000182 (hepatocyte), CL:0000128 (oligodendrocyte) |
| UBERON | UBERON:0002371 (bone marrow), UBERON:0002113 (kidney), UBERON:0002107 (liver), UBERON:0002048 (lung), UBERON:0002316 (CNS white matter) |
| CHEBI | CHEBI:44185 (methotrexate), folinic acid/leucovorin (CHEBI term for calcium folinate) |
| HGNC | DHFR (HGNC:2861), MTHFR (HGNC:7436), SLCO1B1 (HGNC:10959), ABCB1 (HGNC:40), ATIC (HGNC:794) |
| NCIT | NCIT:C15986 (Pharmacotherapy) for leucovorin/glucarpidase treatment_term |
| MONDO | MONDO:0034212 |

---

### Sources

- [Navigating methotrexate toxicity: folinic acid and glucarpidase (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/pmid/38889902)
- [Navigating methotrexate toxicity (BJCP/Wiley, 2025)](https://bpspubs.onlinelibrary.wiley.com/doi/10.1111/bcp.16096)
- [Neurotoxic effects of methotrexate: literature review (PMC11981439)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11981439/)
- [Factors influencing delayed clearance of HD-MTX in pediatric/AYA oncology (PMC10642233)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10642233/)
- [Genome-wide study of methotrexate clearance replicates SLCO1B1 (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S0006497120421408)
- [Effect of SLCO1B1 Polymorphisms on HD-MTX Clearance (Clin Transl Sci 2021)](https://ascpt.onlinelibrary.wiley.com/doi/10.1111/cts.12879)
- [Genetic polymorphisms and renal toxicity in Thai patients receiving HD-MTX (Sci Rep 2024)](https://www.nature.com/articles/s41598-024-60334-w)
- [Consensus on managing delayed methotrexate elimination: Middle East (Frontiers Oncology 2025)](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2025.1660937/full)
- [European consensus recommendation on delayed methotrexate elimination (PMC11446969)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11446969/)
- [Glucarpidase efficacy unaffected by concurrent folinic acid (PMC13156163)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13156163/)
- [Routine low-dose glucarpidase in CNS lymphoma, phase I (PMC8756618)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8756618/)
- [Acute methotrexate-induced crystal nephropathy (NEJM)](https://www.nejm.org/doi/full/10.1056/NEJMc1507547)
- [Crystalline nephropathy with HD-MTX in primary CNS lymphoma (PMC9293278)](https://ncbi.nlm.nih.gov/pmc/articles/PMC9293278)
- [Impact of MTX and 7-OH-MTX exposure on renal toxicity in pediatric NHL (PMC11739129)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11739129/)
- [Effect of ABCB1 and MTHFR polymorphisms on MTX-related toxicities (PMC8739189)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8739189/)
- [MTHFR and ABCB1 polymorphisms and toxicity in hematological malignancies (Sci Rep 2025)](https://www.nature.com/articles/s41598-025-33039-x)
- [Severe hematologic toxicity after low-dose MTX in ectopic pregnancy: MTHFR polymorphism (PMC12528151)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12528151/)
- [Clinical characteristics and risk factors for low-dose MTX toxicity: cohort of 28 patients (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S1568997214001712)
- [A Rapidly Fatal Case of Low-Dose Methotrexate Toxicity (PMC6020544)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6020544/)
- [Risk of Serious Adverse Events and Death with Low-Dose MTX vs. Hydroxychloroquine in Dialysis (PMC13511332)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13511332/)
- [Adverse drug reactions related to methotrexate: FAERS 2004–2024 (Frontiers Immunology 2025)](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2025.1586361/full)
- [Therapy-related myelodysplastic syndrome after low-dose MTX (Oxford Med Case Reports 2025)](https://academic.oup.com/omcr/article/2025/11/omaf253/8343280)
- [MalaCards: Methotrexate Toxicity](https://www.malacards.org/card/methotrexate_toxicity)
- [Orphanet: Methotrexate toxicity (ORPHA:565782)](https://www.orpha.net/en/disease/detail/565782)
- [ClinVar RCV001847567.2 — MTHFR c.665C>T and methotrexate toxicity](https://www.ncbi.nlm.nih.gov/clinvar/RCV001847567.2/)
- [ICD-10-CM T45.1X1A](https://www.icd10data.com/ICD10CM/Codes/S00-T88/T36-T50/T45-/T45.1X1A) / [T45.1X5A](https://www.icd10data.com/ICD10CM/Codes/S00-T88/T36-T50/T45-/T45.1X5A)
- [Managing interactions with methotrexate (SPS/NHS)](https://sps.nhs.uk/articles/managing-interactions-with-methotrexate/)
- [Methotrexate toxicity due to dispensing error and PPI interaction (PMC13235338)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13235338/)
- [Molecular mechanisms underlying methotrexate-induced intestinal injury (PubMed 38822868)](https://pubmed.ncbi.nlm.nih.gov/38822868/)
- [The anti-inflammatory actions of methotrexate and ROS (BJP 2003)](https://bpspubs.onlinelibrary.wiley.com/doi/10.1038/sj.bjp.0705054)
- [Role of Wnt/β-catenin in enterocyte turnover during MTX-induced mucositis, rat (PMC4222808)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4222808/)
- [Increased HGF/c-met during recovery from MTX-induced mucositis, rat (PMC2374397)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2374397/)
- [Induction/amelioration of MTX GI toxicity: immune response and gut microbiota (PubMed 30049384)](https://pubmed.ncbi.nlm.nih.gov/30049384/)
- [Encephalopathy from delayed MTX clearance due to loculated pleural effusion (CHEST 2024)](https://journal.chestnet.org/article/S0012-3692(24)02991-X/fulltext)
- [Third-space entrapment of methotrexate in anthracycline-induced cardiomyopathy (PMC13417858)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13417858/)
- [Leucovorin (folinic acid) rescue for HD-MTX: a review (J Clin Pharm Ther 2022)](https://onlinelibrary.wiley.com/doi/abs/10.1111/jcpt.13739)
- [Multi-site validation of FDA-cleared automated MTX immunoassay (JALM 2025)](https://academic.oup.com/jalm/article/11/2/320/8439372)
- [TDM of methotrexate necessary after glucarpidase administration (PubMed 29994985)](https://pubmed.ncbi.nlm.nih.gov/29994985/)
- [Methotrexate level discrepancy post-glucarpidase, pediatric case series (Pediatr Blood Cancer 2024)](https://onlinelibrary.wiley.com/doi/10.1002/pbc.30831)
- [Does folic acid reduce the toxicity of methotrexate? (Medscape)](https://www.medscape.com/viewarticle/588229)
- [A Family Physician's Guide to Monitoring Methotrexate (AAFP)](https://www.aafp.org/afp/2000/1001/p1607)
- [Methotrexate-induced leukoencephalopathy mimicking acute ischemic stroke, thrombolysis (PMC10834224)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10834224/)
- [Methotrexate-induced neurotoxicity: neurophysiological testing (PMC12269288)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12269288/)
- [Rare case of low-dose MTX toxicity with invasive pulmonary mucormycosis (Frontiers Pharmacology 2025)](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2025.1704810/full)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 38 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 38 |
| On topic | 24 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 52 |
| Resolved | 46 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 6 |
| Terms whose name was checked | 37 |
| Terms named correctly | 31 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0034212` (2 mentions) - the report calls it "MONDO"; MONDO calls it **methotrexate toxicity**
- `HP:0001636` (1 mention) - the report calls it "Myocarditis"; HP calls it **Tetralogy of Fallot**
- `CL:0000075` (1 mention) - the report calls it "epithelial cell — intestinal/renal tubular"; CL calls it **columnar/cuboidal epithelial cell**
- `CL:0000097` (1 mention) - the report calls it "mast cell — not primary but relevant to mucosal injury context"; CL calls it **mast cell**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0002316` (2 mentions) - the report calls it "white matter of central nervous system"; UBERON calls it **white matter**, and lists "white matter of neuraxis" among its other names
- `CL:0000015` (2 mentions) - the report calls it "hematopoietic stem cell"; CL calls it **male germ cell**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.