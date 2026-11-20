---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-09T19:47:14.486807'
end_time: '2026-11-09T19:52:48.855434'
duration_seconds: 334.37
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Brunner Syndrome
  mondo_id: MONDO:0010379
  category: Mendelian
  causal_genes: MAOA
  omim_id: OMIM:300615
  synonyms: Brunner syndrome, X-linked recessive; antisocial behavior, X-linked recessive;
    monoamine oxidase A deficiency
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
  - claude-haiku-5-5
  - claude-opus-5-5
  num_turns: 20
  total_cost_usd: 1.3596085999999998
  session_id: 4768e34c-c70c-4a30-b28c-30f465344fed
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  assistant_text_blocks: 4
reference_validation:
  total_references: 37
  verified: 37
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 9
  quotes_valid: 7
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:40135540
  - PMID:1308352
  relevance_assessed: 37
  on_topic: 25
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 48
  verified: 48
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: HP:0002123
    reported_labels:
    - verify
    ontology_label: Generalized myoclonic seizure
  - term_id: HP:0001263
    reported_labels:
    - verify
    ontology_label: Global developmental delay
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Brunner Syndrome
- **MONDO ID:** MONDO:0010379 (if available)
- **Causal gene(s):** MAOA
- **OMIM:** OMIM:300615
- **Synonyms:** Brunner syndrome, X-linked recessive; antisocial behavior, X-linked recessive; monoamine oxidase A deficiency
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Brunner Syndrome** covering all of the
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

Pulling PubMed records for Brunner syndrome/MAOA deficiency to build the report.

Still gathering references (mouse models, contiguous deletions); then I'll write the report.

Last lookup: Palmer 2016 and van Rhijn 2022 details, then writing.

# Brunner Syndrome (MONDO:0010379): Research Report

**Causal gene: *MAOA*** (monoamine oxidase A; HGNC `hgnc:6833`; Xp11.3; OMIM gene \*309850; disease OMIM #300615). Brunner syndrome is an X-linked recessive inborn error of monoamine metabolism. Hemizygous loss-of-function variants in *MAOA* remove MAO-A enzyme activity. The result is borderline-to-mild intellectual disability, episodic impulsive or aggressive behaviour, and a characteristic pattern of biogenic amine biomarkers.

**Notes on the evidence:**
- The quoted phrases below came from a summarising fetch of the PubMed abstracts, not a byte-exact download. Verify each with `just fetch-reference PMID:…` and `just count-verified-snippets` before using it as a `snippet`.
- `kb/disorders/Brunner_Syndrome.yaml` already exists as an 8-line skeleton: name, creation date, category and a MONDO:0010379 binding.
- Ontology CURIEs marked ✔ were checked against this repo's `cache/*/terms.csv`. Unmarked CURIEs need a lookup before you bind them.

---

## 1. Disease Information

- **Overview.** The disorder was first described in 1993 in a large Dutch kindred. Affected males had "a new form of X-linked nondysmorphic mild mental retardation" with prominent behavioural disturbance (PMID:8503438). The syndrome "was associated with a complete and selective deficiency of enzymatic activity of monoamine oxidase A (MAOA)" (PMID:8211186).
- **Identifiers:**
  - MONDO:0010379
  - OMIM #300615; gene *MAOA* \*309850
  - Orphanet "Monoamine oxidase A deficiency" (verify the ORPHA code: `just fetch-reference ORPHA:<code>`)
  - MeSH: there is no specific descriptor; it falls under "Monoamine Oxidase" plus "Intellectual Disability, X-linked" (verify)
  - ICD-10/ICD-11: no specific code; it sits under other disorders of amino-acid/neurotransmitter metabolism (verify)
- **Synonyms:** Brunner syndrome; MAOA deficiency; monoamine oxidase A deficiency; antisocial behavior, X-linked recessive; "X-linked borderline mental retardation with prominent behavioral disturbance".
- **Data provenance.** The literature is case reports and family studies, about a dozen families. The registry-level data come from the iNTD neurotransmitter registry (PMID:34245036; PMID:33443316). No EHR cohort exists.

## 2. Etiology

- **Causal factors.** Germline hemizygous loss-of-function variants in *MAOA*. Reported variant classes are:
  - nonsense: p.Gln296\* in exon 8 of the original kindred, historically called "C936T" (PMID:8211186; PMID:11378857)
  - frameshift: p.Ser251Lysfs\*2 (PMID:25807999)
  - missense: p.Cys266Phe (PMID:24169519); p.Arg45Trp (PMID:25807999); p.Glu137Gly (PMID:37750385); p.Thr408Met (PMID:39450862)
  - splice-site, with intron 8 retention leading to a premature stop codon (PMID:42511567)
- **Population screening.** The original nonsense variant was not found in a population sample of aggressive men (PMID:11378857). An early review asked whether MAO-A deficiency is "highly uncommon" in high-risk populations (PMID:9564605).
- **Genetic risk and modifiers.** No established modifier genes. Adjacent *MAOB* loss makes the phenotype more severe (see §4). The common promoter uVNTR ("MAOA-L") polymorphism is a separate susceptibility topic and is **not** Brunner syndrome. Do not conflate the two. The best-known paper on it is the GxE study of genotype × childhood maltreatment → antisocial outcome (Caspi 2002, PMID:12161658; review PMID:29881923).
- **Environment and GxE in Brunner families.** Piton et al. reported that in the p.C266F family, "Two maternal uncles carry the mutation and have severe ID, with a history of maltreatment in early childhood." The authors suggested that gene–environment interaction contributes to variable expressivity (PMID:24169519). This is a suggestion, not a demonstrated mechanism.
- **Dietary triggers (inferred).** Dietary tyramine and serotonergic or sympathomimetic drugs are plausible triggers of the episodic symptoms, by analogy with MAO-inhibitor pharmacology. Palmer et al. recommend dietary modification and avoiding drugs contraindicated with MAO inhibitors (PMID:25807999).
- **Protective factors.** None documented.

## 3. Phenotypes

Frequencies are qualitative because there are fewer than about 30 reported hemizygous males.

| Phenotype | HPO (✔ = cached) | Onset / course | Frequency | Key PMIDs |
|---|---|---|---|---|
| Borderline or mild intellectual disability | HP:0006889 ✔ Borderline ID; HP:0001256 ✔ Mild ID | Childhood, stable | Nearly all males | 8503438, 25807999 |
| Severe ID (some families, sometimes alongside adverse environment) | HP:0010864 ✔ | Childhood | Occasional | 24169519 |
| Impulsive or explosive aggression, often episodic | HP:0000718 ✔ Aggressive behavior; HP:0100710 ✔ Impulsivity | Childhood/adolescence, episodic | Frequent | 8211186, 25807999 |
| Antisocial or disinhibited acts (arson, attempted rape, exhibitionism in the original kindred) | HP:0000734 ✔ Disinhibition; HP:0012433 ✔ Abnormal social behavior | Adolescence/adult | Original kindred | 8211186 |
| Autistic features | HP:0000729 ✔ | Childhood | Several cases | 24169519, 37750385 |
| ADHD or attention deficit | HP:0007018 ✔; HP:0000736 ✔ | Childhood | Frequent | 25807999, 39450862 |
| Obsessive or repetitive behaviour | HP:0031432 ✔; HP:0000722 ✔ | Childhood | Some | 25807999 |
| Self-injurious behaviour | HP:0100716 ✔ | Childhood | "Commonly observed" in the iNTD registry | 24169519, 34245036 |
| Sleep disturbance; REM sleep behaviour disorder | HP:0002360 ✔; HP:5200291 ✔ | Adult (RBD at 46 y, nightmares for 15 y) | Case report | 37750385, 38881510 |
| Episodic flushing, headache, diarrhoea ("serotonergic" episodes) | HP:0031284 ✔; HP:0002315 ✔; HP:0002014 ✔ | Episodic | One family, plus a carrier mother | 25807999 |
| Palpitations, abdominal pain or bloating (carrier mother) | HP:0001962 Palpitations (verify) | Episodic | Case report | 37750385 |
| Myoclonic epilepsy (child) | HP:0002123 (verify) | Childhood | Single case | 37750385 |
| Developmental delay | HP:0001263 (verify) | Infancy | Paediatric cases | 37750385 |
| Brain MRI pattern of post-infantile-onset neuronal disease | — | — | One MAOA case of 70 patients | 33443316 |

**Heterozygous females** are usually unaffected. Some carriers have episodic symptoms or mild ID; Family 2's carrier mother had normal intelligence but episodic symptoms (PMID:25807999; PMID:37750385).

**Quality of life.** Registry data show that patients with primary monoamine disorders "had lower IQ scores" (mean IQ 58) and reduced HRQoL (PMID:34245036). There are no Brunner-specific EQ-5D or SF-36 data.

**Laboratory abnormalities** are covered in §10.

## 4. Genetic / Molecular Information

- **Gene.** *MAOA*, `hgnc:6833` ✔. It encodes a flavin (FAD)-dependent enzyme in the outer mitochondrial membrane. The enzyme oxidatively deaminates serotonin, norepinephrine, dopamine and tyramine.
- **Variants:**
  - p.Gln296\*: exon 8 nonsense, PMID:8211186
  - p.Ser251Lysfs\*2: PMID:25807999
  - p.Arg45Trp: PMID:25807999
  - c.797_798delinsTT, p.Cys266Phe: PMID:24169519. The missense variant "decreases MAOA enzymatic activity, leading to abnormal levels of urinary monoamines."
  - c.410A>G, p.Glu137Gly: PMID:37750385
  - p.Thr408Met: PMID:39450862
  - a splice-site variant causing intron 8 retention: PMID:42511567
  - p.Glu446Lys: modelled computationally (PMID:36536002)
  - Check ClinVar for current ACMG classifications. Most published variants are reported as pathogenic or likely pathogenic, with functional or biochemical support.
- **Functional consequence.** Loss of function (LOF/amorph). Multiscale simulations predict that R45W causes "a 6000-fold slowdown of enzymatic function" and that E446K reduces activity about 450-fold. The authors call both "practically equivalent to a gene knockout" (PMID:36536002; COMPUTATIONAL; follow-up PMID:40135540).
- **Origin.** Germline, usually maternally inherited. There is one reported case with no family history (PMID:42511567).
- **Allele frequency.** Hemizygous LOF alleles are essentially absent from gnomAD males (check gnomAD).
- **Chromosomal abnormalities (contiguous-gene differential):**
  - Xp11.3 deletions removing *MAOA* + *MAOB* ± *NDP* cause a more severe phenotype.
  - With Norrie disease (*NDP*), there is undetectable MAO-A and MAO-B activity; the authors note that "a marked deficiency of MAO activity is compatible with life" (PMID:2483108; PMID:1308352).
  - *MAOA/MAOB*-only deletions (240 kb and about 800 kb) cause severe developmental delay, intermittent hypotonia, stereotyped hand movements, attacks of sudden atonia and "extremely elevated" CSF serotonin (PMID:20485326; PMID:23414621).
  - Isolated *MAOB* deletion causes no behavioural or cognitive phenotype: "MAO-A is considerably more important than MAO-B" (PMID:8613523).
- **Epigenetics.** MAOA promoter methylation is linked to impulsivity in the general population (PMID:37507512). This is not established for Brunner syndrome.

## 5. Environmental Information

- No causal environmental agent and no infectious aetiology.
- Two modifiers are plausible:
  - early-life maltreatment (PMID:24169519; and the hypomorphic-mouse × early-life-stress data in PMID:30738037)
  - dietary tyramine or amine load (PMID:25807999)

## 6. Mechanism / Pathophysiology

**Causal chain:**

1. A hemizygous *MAOA* LOF variant (nonsense, frameshift, splice or missense) **leads to** absent or near-absent MAO-A catalytic activity (GO:0097621 monoamine oxidase activity, needs verifying) in the outer mitochondrial membrane (GO:0005741 ✔). This is demonstrated in fibroblasts and patient cells and modelled in silico (PMID:8211186; PMID:24169519; PMID:36536002).
2. Loss of oxidative deamination **results in** failure of serotonin catabolism (GO:0042429, verify), norepinephrine catabolism and dopamine catabolism (GO:0042420 ✔). Substrates accumulate: serotonin (CHEBI:28790 ✔), noradrenaline (CHEBI:33569 ✔), dopamine (CHEBI:18243 ✔) and tyramine. Deaminated products are depleted: 5-HIAA, VMA, MHPG and HVA (CHEBI:545959 ✔). O-methylated products are shunted up: normetanephrine and 3-methoxytyramine. This is demonstrated in human urine and serum (PMID:8503438; PMID:9564603; PMID:25807999).
3. **Branch A, systemic:** raised circulating serotonin and amines **lead to** episodic "serotonergic" symptoms such as flushing, headache, diarrhoea and palpitations. Symptomatic individuals "had particularly high serotonin levels" (PMID:25807999). This step is partly inferred (correlation, plus reversal with treatment).
4. **Branch B, CNS developmental:** excess serotonin during development **leads to** altered cortical and serotonergic circuit maturation. In *Maoa*-knockout pups, brain "serotonin concentrations were increased up to ninefold" (PMID:7792602; MODEL_ORGANISM). Pharmacological reversal by a serotonin-synthesis inhibitor (PMID:7792602) implies a critical developmental window. In humans this is inferred.
5. **Branch C, synaptic:** in patient iPSC-derived dopaminergic neurons (CL:0000700 ✔), MAOA loss **leads to** upregulated GRIN2A/GRIN2B and NMDAR hyperfunction. This **results in** reduced synaptic density but "hyperactive network activity". CRISPR correction restored these features to control levels (PMID:34923109; IN_VITRO).
6. Altered serotonergic (CL:0000850 ✔), noradrenergic and dopaminergic signalling in prefrontal, amygdala and hippocampal circuits **leads to** impulsive aggression, deficits in social and executive function, and cognitive impairment. Supporting evidence:
   - Mouse knockouts show increased intermale aggression (PMID:7792602; PMID:18418249).
   - Hypomorphic mice show social deficits and perseveration "without overt aggression", which shows that residual activity changes the phenotype (PMID:21832987).
   - Lower 5-HTT expression is a downstream adaptation (PMID:24882701).
   - The human link is inferred from the mouse data plus clinical correlation.
7. Additional MAOB loss, in contiguous deletions, **leads to** further loss of compensation and a severe phenotype with hypotonia and atonic attacks (PMID:20485326; PMID:23414621).

**Supporting detail:**
- **Immune involvement.** Not part of the human disease. Hematopoietic *Maoa* deficiency worsens EAE in female mice (PMID:42454033), and one autoantibody-profiling study looked at MAOA-deficient ASD patients (PMID:40620708). Both are exploratory.
- **Cerebellum.** Hypomorphic mice show cerebellar disorganisation (PMID:22971542).
- **Respiratory regulation.** Neonatal *Maoa*-KO mice show noradrenergic respiratory changes (PMID:12672546).
- **Omics.** No transcriptomic, proteomic or single-cell datasets are specific to the disease. The iPSC study is the main molecular profiling.

## 7. Anatomical Structures

- **Primary site:** brain (UBERON:0000955 ✔). Implicated regions are the prefrontal cortex/neocortex (UBERON:0001950 ✔), amygdala, hippocampus, brainstem raphe (UBERON:0002298 ✔), hypothalamus (UBERON:0001898 ✔) and cerebellum (UBERON:0002037 ✔; mouse).
- **Peripheral sites:** gut and enterochromaffin serotonin (diarrhoea); vasculature (flushing); platelets (CL:0000233 ✔). Platelet MAO-B is normal in isolated MAOA deficiency, which is a diagnostic discriminator (PMID:8503438).
- **Cell types:** serotonergic neurons CL:0000850 ✔; dopaminergic neurons CL:0000700 ✔; neurons CL:0000540 ✔; astrocytes CL:0000127 ✔ (MAO-B-rich; compensation).
- **Subcellular:** mitochondrial outer membrane GO:0005741 ✔.
- **Lateralisation:** not applicable.

## 8. Temporal Development

- **Onset:** congenital biochemical defect. Developmental delay or ID appears in childhood. Behavioural episodes become prominent in childhood or adolescence.
- **Course:** lifelong and non-progressive for cognition. Behaviour is episodic and fluctuating; Palmer et al. call it "paroxysmal" (PMID:25807999).
- **Age range of reports:** symptoms are described from age 5 (PMID:37750385) to the 40s (PMID:38881510). There is no natural-history study.
- **Remission:** treatment-induced biochemical and partial behavioural improvement (PMID:25807999; PMID:37750385).
- **Critical periods:** developmental serotonin excess in mouse pups (PMID:7792602). Early-life stress interacts with hypomorphic alleles (PMID:30738037).

## 9. Inheritance and Population

- **Inheritance:** X-linked recessive (HP:0001419 ✔). Linkage gave a maximal multipoint lod score of 3.69 at MAOA in Xp11.23–11.4 (PMID:8503438).
- **Penetrance:** apparently complete for the biochemical defect in hemizygous males.
- **Expressivity:** variable within and between families, from borderline ID with placid behaviour to severe ID with aggression (PMID:24169519; PMID:25807999; PMID:39450862).
- **Carrier females:** usually unaffected; occasionally show episodic symptoms or mild ID.
- **Not reported:** anticipation, founder effects and germline mosaicism.
- **Epidemiology:** ultra-rare, fewer than about 15 families published. Suggested prevalence class `CASES_IN_LITERATURE` / `ULTRA_RARE`.
- **Demographics:** almost exclusively males. Reported families come from the Netherlands, France, Australia, Italy, Turkey and Japan (deletion cases).

## 10. Diagnostics

- **Biochemistry (key screening):**
  - Random urine normetanephrine/VMA or normetanephrine/MHPG ratios: "MAO-A deficiency can be reliably diagnosed by measuring the ratio of normetanephrine…". The abnormality was "faithfully present in every one of 12 independent samples" (PMID:9564603).
  - Other urine findings: raised normetanephrine, 3-methoxytyramine and tyramine; low 5-HIAA, VMA and HVA.
  - Serum serotonin is high (PMID:25807999). Raised plasma or CSF serotonin occurs in deletions (PMID:23414621).
  - Recommended screen: serum/urine metanephrines and serotonin (PMID:25807999).
  - LC-MS/MS profiling of tryptophan/tyrosine metabolism is available (PMID:26818237).
  - Possible LOINC codes: urine normetanephrine and serum serotonin. Seed them via `just loinc-seed-cache`.
- **Enzyme assay:** MAO-A activity in cultured fibroblasts. Platelet MAO-B is normal in point-mutation cases and absent in *MAOA/MAOB* deletions.
- **Genetic testing:**
  - Single-gene *MAOA* sequencing, or an X-linked ID panel, or exome/genome sequencing (PMID:24169519 targeted X-exome; PMID:37750385 WES; PMID:42511567 clinical exome).
  - CMA for Xp11.3 deletions.
  - RNA studies to confirm splice variants (PMID:42511567).
  - Carrier testing of the mother.
- **Imaging:** MRI is usually normal or non-specific (PMID:33443316).
- **Differential diagnosis:**
  - *MAOA/MAOB* contiguous deletion ± Norrie disease (more severe; ocular findings with *NDP*)
  - other X-linked ID syndromes
  - aromatic L-amino acid decarboxylase deficiency and other iNTD disorders (opposite biomarker pattern)
  - carcinoid/neuroendocrine tumour (raised serotonin)
  - pheochromocytoma (raised metanephrines; MAOA deficiency is a false-positive risk)
  - idiopathic ADHD, ASD or conduct disorder
- **Screening:** none at population level. Cascade carrier testing in affected families.

## 11. Outcome / Prognosis

- Life expectancy appears normal. There are no mortality data.
- Morbidity comes from lifelong ID and behavioural episodes. The original kindred had legal and social consequences (PMID:8211186).
- **Perioperative risk:** an anaesthesia case in combined MAO-A/B deficiency managed propofol/sugammadex "without any appreciable clinical signs of fatal arrhythmias". This implies a theoretical risk of sympathomimetic or serotonergic crisis (PMID:32504152).
- **Prognostic factor:** serotonin level correlates with symptoms (PMID:25807999).

## 12. Treatment

There is no approved disease-specific therapy. The evidence is case-level only.

| Treatment | NCIT action (✔) | Agent | Evidence |
|---|---|---|---|
| Serotonin reuptake inhibitor plus dietary modification | NCIT:C15986 Pharmacotherapy ✔ + NCIT:C15447 Dietary Intervention ✔ | SSRI, e.g. fluoxetine CHEBI:5118 ✔ (the agent in the mouse studies; check which agent was used in humans) | Biochemistry reversed, "serotonergic" symptoms fell and behaviour improved (PMID:25807999); partial response in a mother (PMID:37750385); mouse rescue of aggression and social deficits with acute fluoxetine (PMID:24882701) |
| Serotonin antagonist and reuptake inhibitor (SARI) | NCIT:C15986 ✔ | trazodone class CHEBI:9654 ✔ (confirm the drug named in the paper) | Improved social behaviour and sleep in one patient; off-label (PMID:42511567) |
| Clonazepam for REM sleep behaviour disorder | NCIT:C15986 ✔ | clonazepam CHEBI:3756 ✔ | "significant reduction" of RBD symptoms (PMID:38881510) |
| Low-amine (tyramine) diet | NCIT:C15447 ✔ | — | Recommended (PMID:25807999) |
| Avoid MAOI-contraindicated drugs (sympathomimetics, serotonergic combinations); anaesthetic precautions | NCIT:C15747 Supportive Care ✔ | — | PMID:25807999; PMID:32504152 |
| Behavioural or psychiatric support; special education | NCIT:C15747 ✔ | — | Standard of care |
| Genetic counselling | NCIT:C15240 ✔ | — | X-linked recessive risk |

- **Caution:** an SSRI raises synaptic serotonin even though serotonin is already elevated. The rationale is to reduce platelet and peripheral serotonin and to normalise 5-HTT-dependent signalling. Palmer et al. advise "cautious" use (PMID:25807999).
- **Experimental:** no gene therapy or clinical trials (none found on ClinicalTrials.gov). An NMDAR-directed approach is only suggested by the iPSC data (PMID:34923109).
- **Pharmacogenomics:** not established.

## 13. Prevention

- Primary prevention: carrier testing, prenatal diagnosis or PGD for known familial variants, and genetic counselling.
- Tertiary prevention: diet, avoiding drug interactions, an anaesthesia alert, early behavioural intervention, and minimising early-life adversity. The last of these is inferred from GxE data (PMID:24169519; PMID:30738037).
- No vaccine and no public-health measures apply.

## 14. Other Species

- No naturally occurring animal disease is documented (check OMIA).
- *MAOA* is conserved across vertebrates.
- Rhesus macaque MAOA promoter polymorphism × prenatal iron deficiency affects behaviour (PMID:22340208; PMID:24402517). This is a polymorphism model, not a null allele.

## 15. Model Organisms

| Model | Genotype | Recapitulation | Limitations | PMID |
|---|---|---|---|---|
| *Maoa* KO mouse (Tg8, IFN-β transgene insertion) | null | Pup brain serotonin up to 9×; adult male aggression; pup phenotype reversed by inhibiting serotonin synthesis | Insertional allele; mouse aggression ≠ human impulsive aggression | 7792602 |
| *Maoa*^A863T mouse | spontaneous exon-8 nonsense allele (human-like) | No MAO-A activity; intruder-directed aggression | Locomotor activity differs from Tg8 | 18418249 |
| MAO-A^Neo hypomorphic mouse | low residual activity | Social deficits and perseveration without aggression; cerebellar changes; GxE with early-life stress | Models hypomorphic, not null, alleles | 21832987, 22971542, 30738037, 37080337 |
| Pharmacological rescue | fluoxetine in KO and Neo mice | Aggression and social deficits rescued | Acute dosing only | 24882701 |
| Patient iPSC-derived dopaminergic neurons with isogenic CRISPR correction | 3 patient variants | Reduced synapses; NMDAR hyperfunction; network hyperactivity; corrected by gene repair | Only one neuron type; no circuit context | 34923109 |
| In silico QM/MM | R45W, E446K | Mechanistic rate loss | COMPUTATIONAL | 36536002, 40135540 |

Resources: MGI (*Maoa*), IMPC, MMRRC.

---

## Key References

| PMID | Citation |
|---|---|
| 8211186 | Brunner HG et al. Science 1993: point mutation in MAOA |
| 8503438 | Brunner HG et al. Am J Hum Genet 1993: phenotype, linkage, monoamines |
| 8862875 | Brunner HG. Ciba Found Symp 1996: perspectives |
| 9564603 | Abeling NG et al. 1998: urine ratio diagnosis |
| 24169519 | Piton A et al. Eur J Hum Genet 2014: p.C266F |
| 25807999 | Palmer EE et al. Clin Genet 2016: p.S251Kfs\*2, p.R45W, SRI and diet therapy |
| 37750385 | Minniti ML et al. Am J Med Genet A 2024: p.E137G |
| 39450862 | Ünsel-Bolat G et al. 2024: p.T408M |
| 42511567 | Gravagno E et al. Int J Mol Sci 2026: splice variant, SARI |
| 38881510 | Cesari E et al. J Clin Sleep Med 2024: RBD |
| 34923109 | van Rhijn JR et al. Neurobiol Dis 2022: iPSC dopaminergic neurons, NMDAR |
| 36536002 | Prah A et al. Sci Rep 2022: simulation of R45W and E446K |
| 7792602 | Cases O et al. Science 1995: KO mouse |
| 18418249 | Scott AL et al. Neuroreport 2008: A863T mouse |
| 21832987 | Bortolato M et al. Neuropsychopharmacology 2011: hypomorphic mouse |
| 24882701 | Godar SC et al. J Psychiatr Res 2014: fluoxetine rescue |
| 29748850 | Bortolato M et al. 2018: review |
| 2483108; 20485326; 23414621 | Contiguous MAOA/MAOB deletions |
| 8613523 | Lenders JW et al. J Clin Invest 1996: MAOB deficiency phenotype |
| 34245036; 33443316 | iNTD registry: IQ/HRQoL and MRI |
| 32504152 | Hoshijima H et al. 2020: anaesthesia |
| 11378857 | Mejia JM et al. 2001: no C936T in a population sample |
| 12161658 | Caspi A et al. 2002: uVNTR GxE; susceptibility, not Brunner syndrome |

**Still unconfirmed:**
- the Orphanet, MeSH and ICD codes
- these CURIEs: GO:0097621, GO:0042429, HP:0001962, HP:0002123, HP:0001263 and `hgnc:6834` (MAOB)
- the exact SSRI agent used in the Palmer and Minniti cases

Resolve each with `runoak` or `just fetch-reference` before binding.

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 37 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 9 |
| Quoted claims found in source | 7 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 37 |
| On topic | 25 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:40135540` *(abstract only)*: "practically equivalent to a gene knockout"
  - closest text in source: "We found that the C266F mutation causes an approximately 18,000-fold slowdown of enzymatic function, which is equivalent to a MAOA gene knockout"
- `PMID:1308352` *(abstract only)*: "a marked deficiency of MAO activity is compatible with life"
  - closest text in source: "The propositus' mother met diagnostic criteria for "chronic hypomania and schizotypal features." The propositus' MAO activity was undetectable and the female heterozygotes had reduced levels comparable to patients receiving MAO inhibiting antidepressants"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 48 |
| Resolved | 48 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002123` (2 mentions) - the report calls it "verify"; HP calls it **Generalized myoclonic seizure**
- `HP:0001263` (2 mentions) - the report calls it "verify"; HP calls it **Global developmental delay**