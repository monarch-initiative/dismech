---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-07T23:00:34.665699'
end_time: '2026-09-07T23:04:37.793490'
duration_seconds: 243.13
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Diamond-Blackfan Anemia 14 with Mandibulofacial Dysostosis
  mondo_id: MONDO:0010493
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
  web_search_requests: 15
  num_turns: 20
  total_cost_usd: 1.2379292
  session_id: 8e6a3453-99e0-563b-8e2c-3bcb30d1c949
  stop_reason: end_turn
  assistant_text_blocks: 2
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 51
  verified: 47
  not_found: 0
  obsolete: 1
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 34
  labels_matching: 18
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: GO:0006974
    reported_labels:
    - "DNA damage response \u2014 for p53 axis, if used generically for nucleolar\
      \ stress signaling"
    ontology_label: DNA damage response
  - term_id: UBERON:0000453
    reported_labels:
    - jaw region
    ontology_label: decidua basalis
  - term_id: UBERON:0001676
    reported_labels:
    - mandible
    ontology_label: occipital bone
  - term_id: UBERON:0001703
    reported_labels:
    - upper jaw region/midface
    ontology_label: neurocranium
  - term_id: UBERON:0000151
    reported_labels:
    - pharyngeal arch
    ontology_label: pectoral fin
  labels_variant: 11
  obsolete_terms:
  - term_id: GO:0008565
    ontology_label: obsolete protein transporter activity
  unresolvable_prefixes:
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Diamond-Blackfan Anemia 14 with Mandibulofacial Dysostosis
- **MONDO ID:** MONDO:0010493 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Diamond-Blackfan Anemia 14 with Mandibulofacial Dysostosis** covering all of the
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

I'll research this rare disease using web search to ensure accurate, citable information.

I have sufficient primary-source material now. Compiling the comprehensive report.

# Diamond-Blackfan Anemia 14 with Mandibulofacial Dysostosis (DBA14) — Research Report

## 1. Disease Information

**Overview.** Diamond-Blackfan anemia 14 with mandibulofacial dysostosis (DBA14) is an extremely rare, X-linked form of Diamond-Blackfan anemia (DBA) — a congenital ribosomopathy characterized by pure red cell aplasia — occurring together with a Treacher-Collins/mandibulofacial-dysostosis-like craniofacial malformation spectrum (microtia, absent external auditory canals, micrognathia, cleft palate/midface hypoplasia). It is caused by hemizygous missense mutation of **TSR2** (TSR2 ribosome maturation factor), Xp11.22, and has to date been reported in a single kindred (two affected maternal first cousins) (PMID:24942156).

**Key identifiers:**
- **OMIM (phenotype):** #300946 — DIAMOND-BLACKFAN ANEMIA 14 WITH MANDIBULOFACIAL DYSOSTOSIS; DBA14
- **OMIM (gene):** *300945 — TSR2 RIBOSOME MATURATION FACTOR; TSR2
- **MedGen:** C4225422
- **MONDO:** MONDO:0010493
- **Gene:** TSR2, HGNC:25455 (aliases: DBA14, WGG1, DT1P1A10), Xp11.22
- **Sibling/allelic-spectrum entries:** DBA15 (OMIM #606164, RPS28-caused, autosomal), DBA10 (RPS26), all part of the broader "DBA with mandibulofacial dysostosis" phenotype cluster first delineated by Gripp et al. (PMID:24942156)
- DBA14 does not currently carry its own dedicated Orphanet number distinct from the general Diamond-Blackfan anemia entry (Orphanet ORPHA:124); it is catalogued there as a molecular subtype.

**Synonyms:** DBA with mandibulofacial dysostosis (TSR2-related); Diamond-Blackfan anemia, X-linked, with craniofacial anomalies.

**Evidence base:** Aggregated disease-level knowledge derived from a single published family report (two affected males, index case followed to age 24, cousin to age 16), supplemented by general Diamond-Blackfan anemia registry data (mostly RPS19/RPL5/RPL11/other-gene DBA) and by biochemical/structural studies of TSR2 protein function done in yeast, human cell, and in vitro biophysical systems — not from an EHR-scale cohort. Nearly everything specific to *this* entity (as opposed to DBA broadly) traces to one report.

---

## 2. Etiology

**Disease-causal factor.** A single hemizygous missense variant in TSR2: **c.191A>G, p.(Glu64Gly)** (E64G), located within the conserved "WGG domain" of the 191-amino-acid TSR2 protein. Segregation was consistent with X-linked inheritance — hemizygous in both affected males, heterozygous (carrier) in their mothers, who are sisters (PMID:24942156). In silico pathogenicity: PolyPhen-2 = 1.0 (probably damaging), SIFT = 0 (damaging), GERP = 5.91 (highly conserved position) (PMID:24942156).

**Genetic risk factors.** The only known causal factor is hemizygosity for this TSR2 missense allele; no other TSR2 variant has yet been reported to cause human disease. By analogy to other DBA genes, this is a haploinsufficiency/dominant-negative-type ribosomal-biogenesis lesion rather than a null allele — a fully null TSR2 allele is presumed embryonic lethal or far more severe, since TSR2 is essential for ribosome maturation (see Mechanism, below).

**Modifier/allelic-series context.** The craniofacial-plus-DBA phenotype is genetically heterogeneous: the same 2014 report that described the TSR2 family also identified two unrelated de novo **RPS28** c.1A>G mutations (translation start-codon loss) causing an overlapping phenotype (subsequently OMIM'd separately as DBA15, #606164), and noted that **RPS26** (DBA10) mutations can produce a similar craniofacial-DBA combination (PMID:24942156). This established that "DBA + mandibulofacial dysostosis" is a converging phenotype of at least three distinct small-subunit ribosome-biogenesis genes (TSR2, RPS26, RPS28) rather than a single-locus entity — an important lump/split consideration.

**Environmental/lifestyle risk factors.** None identified; this is a purely monogenic disorder with no known environmental, infectious, or lifestyle contribution to primary disease causation. (General DBA disease-modifying environmental factors — e.g., infection or drug exposure precipitating aplastic crises in any bone-marrow-failure syndrome — are theoretical extrapolations, not TSR2-specific data.)

**Protective factors.** None reported specific to TSR2. General DBA literature notes that a minority of patients experience spontaneous or steroid-induced remission, but no protective genetic modifier has been characterized for DBA14 specifically.

**Gene-environment interaction.** Not established for this entity.

---

## 3. Phenotypes

Data below are from the single reported kindred (PMID:24942156) unless otherwise noted; frequencies should be read as "observed in both/one of two reported patients," not population frequencies.

| Phenotype | Type | Onset | Notes | Suggested HP term |
|---|---|---|---|---|
| Macrocytic, normochromic anemia (DBA) | Laboratory/hematologic | Index case: diagnosed age 10 months | Steroid-responsive in the proband | HP:0001972 (Macrocytic anemia) / HP:0004840 (Chronic hemolytic anemia — not applicable; use HP:0005518 or general HP:0001903 Anemia with modifier) |
| Reticulocytopenia | Laboratory | Infancy | Classic DBA diagnostic criterion | HP:0001896 (Reticulocytopenia) |
| Elevated erythrocyte adenosine deaminase (eADA) | Laboratory biomarker | — | Cousin had DBA laboratory markers (elevated MCV, eADA, HbF) without overt anemia — a "silent"/subclinical DBA phenotype | HP:0025444 or note as biomarker (not a discrete HPO term; document via biochemical marker) |
| Elevated fetal hemoglobin (HbF) | Laboratory | — | Present in cousin without anemia | HP:0011903 (Increased hemoglobin F) |
| Bilateral microtia (grade 2, absent external auditory canal) | Structural/craniofacial | Congenital | Both affected males | HP:0009909 (Microtia) / HP:0000359 (Abnormal external auditory canal morphology) |
| Abnormal middle-ear structure | Structural | Congenital | Proband | HP:0008551 (Microtia) overlapping; HP:0000359 |
| Conductive hearing loss, hearing-aid dependent | Sensory | Congenital, persistent | Proband | HP:0000405 (Conductive hearing impairment) |
| Micrognathia | Structural/craniofacial | Congenital | Both patients | HP:0000347 (Micrognathia) |
| Midface hypoplasia | Structural/craniofacial | Congenital | Proband | HP:0011800 (Midface retrusion) |
| Downslanting palpebral fissures | Structural/craniofacial | Congenital | Proband | HP:0000494 (Downslanted palpebral fissures) |
| Sparse eyelashes, medial lower lid | Structural | Congenital | Proband | HP:0000653 (approx; consider HP:0000554-adjacent) |
| Cleft palate | Structural | Congenital | Cousin | HP:0000175 (Cleft palate) |
| Unilateral cryptorchidism | Structural/genitourinary | Congenital | Proband | HP:0000028 (Cryptorchidism) |

**Severity/progression:** The craniofacial malformations are static congenital anomalies (Treacher-Collins-like spectrum); the hematologic phenotype is variable within the family — from steroid-responsive transfusion-independent anemia (proband) to purely biochemical DBA markers without anemia (cousin), illustrating marked intrafamilial variable expressivity, a recognized feature of DBA broadly.

**Quality-of-life impact:** Conductive hearing loss and craniofacial dysmorphism carry the same functional burden documented generally for mandibulofacial dysostosis/Treacher Collins spectrum (speech/hearing-language development impact, psychosocial burden of facial difference); chronic anemia when present carries fatigue/growth burden typical of DBA. No DBA14-specific QoL instrument data exist; extrapolation from general DBA and Treacher Collins QoL literature is reasonable but should be flagged as extrapolated, not measured in this entity.

---

## 4. Genetic/Molecular Information

**Causal gene:** TSR2 (HGNC:25455; OMIM *300945; Xp11.22). Encodes a 191-amino-acid protein containing a conserved "WGG domain" (residues ~11–92) whose specific fold was historically "of unknown function" at the time of the 2014 report but has since been structurally characterized (see Mechanism).

**Pathogenic variant:**
- NM_058233 (representative transcript); **c.191A>G, p.Glu64Gly**
- Variant classification: reported as likely pathogenic/pathogenic on the basis of segregation, absence in controls, and in silico prediction (PolyPhen-2 1.0, SIFT 0, GERP 5.91) (PMID:24942156); functional validation later published (see below).
- Variant type: missense, hemizygous (X-linked)
- Zygosity/origin: germline, inherited (maternal carriers); not somatic
- Population frequency: not reported in gnomAD/ExAC at time of publication; effectively private to this family (no independent confirmatory family has been published as of current literature searches).

**Functional consequence — direct experimental confirmation.** The E64G substitution was functionally tested in a yeast complementation/humanized system: yeast expressing human TSR2^E64G showed strong growth impairment and defective 20S pre-rRNA processing (cytoplasmic accumulation of the ITS1-containing pre-rRNA reporter), directly demonstrating loss of TSR2's normal ribosome-maturation activity (PMID:24942156; mechanistic follow-up in PMID:30201955). Structural/biophysical work (PMID:30201955) subsequently showed that the DBA-linked TSR2 mutant is specifically **impaired in binding the eukaryotic-specific segment (ESS) of ribosomal protein eS26/RPS26** — the molecular interaction TSR2 normally uses to escort RPS26 — directly linking the E64G lesion to the RPS26-chaperone defect (see Mechanism §6).

**Modifier genes:** None specific to TSR2-DBA14 established. Broader DBA literature documents highly variable expressivity even for the same causal ribosomal-protein gene, attributed to unknown modifiers, but no locus has been mapped for TSR2 specifically.

**Epigenetic information:** Not reported for DBA14/TSR2. (General ribosomopathy literature discusses secondary transcriptional/translational stress-response reprogramming — e.g., ATF4 pathway dysregulation — rather than primary epigenetic lesions; see Mechanism.)

**Chromosomal abnormalities:** None reported; this is a single-nucleotide missense lesion, not a structural rearrangement.

---

## 5. Environmental Information

No environmental, toxic, occupational, or infectious contributing factors have been identified or are plausible as primary causes, given the clearly monogenic X-linked etiology. No lifestyle risk-factor literature exists specific to this entity. (As with other bone-marrow-failure syndromes, intercurrent infection could theoretically exacerbate cytopenia, but this is inferential, not documented for DBA14.)

---

## 6. Mechanism / Pathophysiology

### Causal chain (numbered, from lesion to phenotype)

1. Hemizygous **TSR2 c.191A>G (p.Glu64Gly)** disrupts the WGG-domain surface of the TSR2 escortin/chaperone protein (demonstrated functionally in a yeast complementation assay: PMID:24942156).
2. This **leads to** impaired binding between TSR2 and the eukaryotic-specific segment (ESS) of ribosomal protein eS26 (RPS26) — the interaction TSR2 normally uses (a) to escort cytoplasmic-imported RPS26 by disassembling the importin–RPS26 complex in a RanGTP-independent, non-canonical mechanism, and (b) to chaperone RPS26 incorporation into, and reversible release from, the nucleolar pre-40S particle (PMID:30201955; general TSR2/RPS26 mechanism reviewed via PMID for the "dual key lock" 40S-maturation step and the Tsr2–Rps26 chaperone-cycle biochemistry, e.g. eLife 2020/61254 and the 2021 Tsr2–Rps26 release/reincorporation study).
3. This **results in** defective 20S pre-rRNA processing / impaired 40S small-subunit maturation — directly shown as cytoplasmic accumulation of unprocessed pre-rRNA (Cy3-ITS1 reporter) in cells expressing the mutant (PMID:24942156). This step is analogous mechanistically to the RPS26-null and RPS28-null lesions found in the same family report, converging all three genes on the same terminal 40S-maturation checkpoint.
4. Impaired ribosome biogenesis **leads to** "nucleolar stress" — accumulation of free, unassembled ribosomal proteins that bind and inhibit HDM2 (MDM2), the negative regulator of p53, in the canonical DBA mechanism established for other ribosomal-protein genes (general DBA mechanism literature, e.g. PMID:21930148 and related). *This step is inferred by analogy to other DBA genes rather than directly demonstrated for TSR2-E64G specifically* — an important evidence-directness caveat.
5. p53 stabilization/activation, together with p53-independent pathways — notably loss of actively translated ATF4, a master regulator of the integrated stress response and of erythroid differentiation, shown across multiple DBA ribosomal-protein deficiencies — **leads to** cell-cycle arrest and/or apoptosis preferentially in erythroid progenitors, which have unusually high ribosome demand during rapid proliferation/differentiation (general ribosomopathy mechanism; PMC12096137, and PMID:21930148-class reviews). This explains the erythroid-lineage-selective bone-marrow failure (pure red cell aplasia) despite the ubiquitous requirement for ribosomes.
6. In parallel (branch point), defective ribosome biogenesis during embryonic/fetal craniofacial morphogenesis **leads to** apoptosis of neural-crest-derived cephalic/first- and second-branchial-arch precursor cells — the same convergent mechanism established for TCOF1-, POLR1C/POLR1D-, and other ribosomopathy-driven mandibulofacial dysostosis/Treacher Collins spectrum disorders, where correct "dosage" of ribosome-biogenesis machinery is specifically required for cephalic neural crest cell survival (general Treacher Collins mechanism literature). *This branch is inferred by mechanistic analogy — TSR2-specific neural-crest data do not exist* — producing the micrognathia, microtia, midface hypoplasia, and downslanting palpebral fissures.
7. The combined erythroid and craniofacial-neural-crest consequences of steps 5 and 6 **result in** the clinical DBA14 phenotype: congenital macrocytic anemia plus Treacher-Collins-like craniofacial malformation, occurring together because both tissue lineages are simultaneously vulnerable to the same underlying ribosome-biogenesis insult during development.

### Molecular pathways
Ribosome biogenesis / 40S small-subunit maturation pathway (pre-rRNA processing, KEGG "Ribosome biogenesis in eukaryotes"); downstream nucleolar-stress → p53 (MDM2/HDM2–p53 axis) and ATF4/integrated-stress-response pathways.

### Cellular processes
Impaired ribosomal protein assembly/nuclear import–export cycling (RanGTP-independent importin disassembly); apoptosis and cell-cycle arrest in erythroid progenitors; apoptosis of cranial neural crest cells.

### Protein dysfunction
TSR2 acts as a dual-function molecular chaperone ("escortin") for RPS26/eS26: (a) it recognizes the ESS segment of eS26 to trigger non-canonical disassembly of the importin:eS26 nuclear-import complex, and (b) it regulates reversible release and reincorporation of eS26 from mature 40S ribosomes under stress (redox/salt/pH), enabling a ribosome-mediated stress response. The E64G substitution impairs the ESS-binding interface, disabling both functions (PMID:30201955; bioRxiv/PMC8880767-class mechanistic follow-up work on Tsr2–Rps26 release/reincorporation biology).

### Tissue damage mechanisms
Selective failure of erythroid progenitor proliferation/survival (bone marrow); developmental (not degenerative) tissue-patterning failure in first/second branchial arch derivatives — mechanistically distinct from oxidative/ischemic damage models used elsewhere in the KB.

### Suggested ontology terms
- **GO (biological process):** GO:0042274 (ribosomal small subunit biogenesis), GO:0000462 (maturation of SSU-rRNA from tricistronic rRNA transcript), GO:0006446 (regulation of translational initiation — secondary), GO:0006974 (DNA damage response — for p53 axis, if used generically for nucleolar stress signaling), GO:0036503 (ERAD pathway — not applicable), GO:0043066 (negative regulation of apoptotic process — for the p53/MDM2 axis, inverted as appropriate)
- **GO (molecular function):** GO:0043022 (ribosome binding), GO:0008565 (protein transporter activity — for the importin-disassembly role)
- **CL (cell types):** CL:0000765 (erythroblast) / CL:0000038 (erythroid progenitor cell), CL:0000333 (migratory neural crest cell) / CL:0002321 (embryonic cell, cranial neural crest lineage)

---

## 7. Anatomical Structures Affected

**Organ level:**
- Primary: bone marrow (erythroid lineage — pure red cell aplasia); craniofacial skeleton and soft tissue (mandible, maxilla/midface, external and middle ear)
- Secondary: reproductive system (unilateral cryptorchidism in the proband) — plausibly a co-occurring neural-crest/genital-ridge developmental association rather than a direct ribosome-biogenesis erythroid mechanism
- Body systems: hematologic/immune (bone marrow), craniofacial/musculoskeletal, otologic/auditory, ophthalmologic (periorbital structures), genitourinary

**Tissue/cell level:**
- Erythroid progenitor cells in bone marrow (CL:0000765/CL:0000038)
- Cranial neural crest–derived mesenchyme forming first (mandibular) and second (hyoid) branchial/pharyngeal arch structures (CL:0000333)
- Middle/external ear structures (first and second arch derivatives)

**Subcellular level:**
- Nucleolus (site of pre-rRNA processing and TSR2/RPS26 pre-40S assembly) — GO:0005730 (nucleolus)
- Cytoplasm (site of late 40S maturation and TSR2-mediated RPS26 release/reincorporation cycling) — GO:0005737

**Localization (UBERON):** UBERON:0002371 (bone marrow), UBERON:0000453 (jaw region)/UBERON:0001676 (mandible), UBERON:0001703 (upper jaw region/midface), UBERON:0001846 (external auditory meatus), UBERON:0001846-adjacent middle ear structures, UBERON:0002190 (subcutaneous adipose — not relevant), UBERON:0000151 (pharyngeal arch)

**Lateralization:** Craniofacial anomalies were bilateral in both patients (microtia bilateral); cryptorchidism was unilateral in the proband.

---

## 8. Temporal Development

**Onset:** Craniofacial anomalies are present at birth (congenital, developmental origin in embryogenesis — first/second branchial arch patterning occurs in the first trimester). The hematologic phenotype in the reported proband was diagnosed at age 10 months, consistent with the general DBA pattern in which anemia is discovered within the first two years of life; diagnosis after age 4 is rare in classical DBA (general DBA epidemiology). The cousin's laboratory DBA markers (elevated MCV, eADA, HbF) were present without ever developing overt anemia — illustrating that TSR2-DBA14, like DBA generally, can present as a purely biochemical/subclinical hematologic phenotype.

**Progression:** The hematologic component in the index case was steroid-responsive; no long-term natural-history data (beyond follow-up to age 24) exist to characterize typical disease-course trajectory, remission likelihood, or transfusion dependence risk specific to TSR2-DBA14. Craniofacial anomalies are static structural malformations, not progressive.

**Pattern:** No relapsing-remitting pattern reported; anemia responded to corticosteroid treatment in the one treated patient and has remained controlled to at least age 24 per the report. No spontaneous-remission data specific to this gene are available.

---

## 9. Inheritance and Population

**Epidemiology.** DBA14 (TSR2-related) has been reported in exactly one family (two affected males) worldwide as of the primary literature search (PMID:24942156); no population-level prevalence/incidence estimate exists for this specific molecular subtype. For context, Diamond-Blackfan anemia overall has an estimated incidence of ~5–7 per 1,000,000 live births (roughly 1/150,000 in some European estimates), with TSR2 accounting for a vanishingly small fraction of the ~50–60% of DBA cases with an identified ribosomal-protein-pathway gene (RPS19 ~25% is the largest single contributor; RPL5, RPL11, RPS10, RPS17, RPS24, RPS26, RPL35A collectively contribute another ~25–35%; RPS28 and TSR2 are each represented by only one to a few families in the literature).

**Inheritance pattern:** X-linked (segregating as hemizygous-affected males, heterozygous unaffected/biochemically-marked carrier females in the one reported pedigree) (PMID:24942156). Suggested HP term for the mode of inheritance: HP:0001417 (X-linked inheritance); given only affected males and obligate-carrier transmitting females are reported, this reads as X-linked recessive-pattern segregation in the single pedigree, though with only two affected individuals formal recessive-vs-other X-linked distinction cannot be firmly established from this family alone.

**Penetrance/expressivity:** Marked variable expressivity within the one reported family — the proband had transfusion-requiring, steroid-responsive anemia plus a fuller craniofacial phenotype, while the cousin had only laboratory DBA markers (no anemia) with a somewhat different, still overlapping, craniofacial presentation (cleft palate rather than cryptorchidism, for example). This mirrors the well-documented variable expressivity seen across DBA generally, even for identical causal variants.

**Genetic anticipation:** Not applicable/not reported (not a repeat-expansion disorder).

**Germline mosaicism:** Not reported for this family.

**Founder effects / consanguinity:** Not applicable — the report describes an X-linked pedigree with maternal-cousin transmission, not a founder-population or consanguinity-driven case.

**Carrier frequency:** Unknown/not established (n=1 family; variant not seen in population databases at publication).

**Population demographics:** No ethnic, geographic, or sex-ratio data beyond the single reported (presumably North American, given the reporting center) family; as an X-linked disorder, males are hemizygously affected while carrier females may show attenuated/subclinical hematologic markers, consistent with typical X-linked recessive dynamics, though formal female-carrier phenotyping data are limited to the two reported obligate-carrier mothers.

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- Complete blood count showing macrocytic, normochromic anemia with reticulocytopenia and normal white cell/platelet counts (classical DBA diagnostic criterion)
- Bone marrow examination: normal cellularity with a selective paucity of erythroid precursors (classical DBA criterion)
- Erythrocyte adenosine deaminase (eADA) activity: elevated — a well-validated DBA biomarker with ~84% sensitivity, ~95% specificity, and ~91% positive/negative predictive value versus other inherited bone-marrow-failure syndromes (PMID:23252420-class literature); used here to identify the biochemically-affected but non-anemic cousin
- Fetal hemoglobin (HbF): elevated — supporting minor diagnostic criterion for DBA
- Craniofacial imaging (CT temporal bone for ear/middle-ear anatomy; standard clinical craniofacial exam) to characterize microtia/atresia, micrognathia, midface hypoplasia

**Genetic testing:**
- Given the phenotypic overlap between DBA and mandibulofacial dysostosis/Treacher Collins spectrum, the recommended approach is a combined ribosomal-protein-gene/ribosome-biogenesis-factor panel or exome sequencing including RPS19, RPL5, RPL11, RPS10, RPS17, RPS24, RPS26, RPL35A, RPS7, RPS29, RPL15, RPL26, TSR2, and RPS28, alongside classical mandibulofacial dysostosis genes (TCOF1, POLR1C, POLR1D, EFTUD2) when craniofacial features dominate — reflecting genetic heterogeneity of the combined phenotype (PMID:24942156 explicitly frames this as a diagnostic message: "DBA with mandibulofacial dysostosis is heterogeneous")
- Single-gene TSR2 Sanger sequencing is reasonable when family history/segregation suggests X-linked inheritance
- Chromosomal microarray/karyotype: not indicated as a primary test (this is a single-nucleotide missense disorder), but useful to exclude alternative structural causes of craniofacial anomaly + cytopenia phenotypes
- Carrier/segregation testing recommended for at-risk maternal relatives in an identified family, given the demonstrated carrier (heterozygous, biochemically-detectable-but-non-anemic) phenotype pattern

**Differential diagnosis:**
- Other DBA molecular subtypes with craniofacial features (RPS26/DBA10, RPS28/DBA15)
- Treacher Collins syndrome (TCOF1, POLR1C, POLR1D) without hematologic involvement
- Mandibulofacial dysostosis, Guion-Almeida type (EFTUD2), which includes microcephaly and esophageal atresia but not classically DBA-type anemia
- Other inherited bone marrow failure syndromes (Fanconi anemia, Shwachman-Diamond syndrome) — excluded via eADA pattern, HbF pattern, and absence of the syndrome-specific features (radial ray defects, pancreatic insufficiency, etc.)

**Screening:** No population or newborn screening program exists for this ultra-rare entity; screening in practice is limited to cascade testing of at-risk relatives once a proband is identified.

---

## 11. Outcome/Prognosis

No dedicated survival, mortality, or long-term outcome data exist for TSR2-DBA14 specifically (n=1 family, longest follow-up to age 24). By extrapolation from general DBA outcome data (not TSR2-specific):
- General DBA prognosis is favorable for the anemia itself with corticosteroid or transfusion management, but carries substantial treatment-related and disease-related long-term morbidity
- General DBA carries a markedly elevated lifetime cancer risk: myelodysplastic syndrome (a "few hundred-fold" increased relative risk in registry data) and acute myeloid leukemia, plus solid tumors — notably early-onset colorectal/gastrointestinal carcinoma and osteosarcoma — with a cumulative malignancy risk approaching 20% by age 40 in DBA Registry data (ASH/Blood registry literature)
- No TSR2-specific cancer-predisposition data exist; whether TSR2-DBA14 carries the same elevated malignancy risk as other DBA subtypes is an inferred extrapolation, not directly demonstrated, and should be flagged as such in any curated entry
- Craniofacial and hearing outcomes follow the general trajectory for mandibulofacial dysostosis/Treacher-Collins-spectrum disease: static structural anomaly amenable to surgical/audiologic management, with functional hearing loss requiring amplification (hearing aids were used in the reported proband)

---

## 12. Treatment

No TSR2-DBA14-specific treatment trial or outcome data exist; management follows general DBA and general mandibulofacial dysostosis/craniofacial-anomaly paradigms.

**Pharmacotherapy (hematologic):**
- Corticosteroids (e.g., prednisone) — first-line for DBA-associated anemia; the reported proband's anemia was explicitly steroid-responsive (PMID:24942156). NCIT term: NCIT:C15986 (Pharmacotherapy) with therapeutic_agent corticosteroid class (NCIT:C2322)
- Chronic red blood cell transfusion with iron chelation for steroid-refractory/intolerant cases (general DBA management, not documented as needed in this specific family)
- Danazol has been reported as an underutilized adjunct in general DBA management (PMC6636591-class literature) — not documented for this family specifically

**Advanced therapeutics:**
- Allogeneic hematopoietic stem cell transplantation (HSCT) — potentially curative for the hematologic component in steroid-refractory general DBA, though associated with significant transplant-related morbidity/mortality; gene therapy approaches are in early clinical development for DBA broadly but have not been reported for TSR2-DBA14. NCIT: NCIT:C15431 (Hematopoietic Cell Transplantation)

**Surgical/interventional (craniofacial):**
- Standard mandibulofacial dysostosis/craniofacial surgical management: ear reconstruction/atresia repair, orthognathic/mandibular distraction or reconstructive surgery for micrognathia, cleft palate repair (as needed in the cousin) — extrapolated from general Treacher Collins/MFD surgical management, not TSR2-DBA14-specific data. NCIT: NCIT:C15329 (Surgical Procedure), NCIT:C16186 (Orthopedic Surgical Procedure, if applicable to mandibular work)

**Supportive/rehabilitative:**
- Hearing aids for conductive hearing loss (used by the reported proband) — NCIT device-qualifier pattern (NCIT:C15302 Physical Therapy is not applicable; consider audiologic amplification device via qualifiers pattern, since NCIT has no direct "hearing aid usage" clinical-action term)
- Speech/language therapy for cleft-palate-associated speech impact (general MFD management, not documented specifically in this family)
- Genetic counseling for the family (NCIT:C15240)

**Experimental:** No registered clinical trials specific to TSR2-DBA14 were identified. General DBA trials (e.g., sotatercept, trifluoperazine — both identified in general DBA trial searches, NCT01464164 and NCT03966053) are not gene-subtype-specific and their applicability to TSR2-mediated disease is untested.

---

## 13. Prevention

No primary prevention is possible for this monogenic disorder beyond genetic counseling and reproductive options (carrier testing of at-risk female relatives, prenatal diagnosis, or preimplantation genetic testing once a familial TSR2 variant is identified) — standard for any X-linked Mendelian disorder, not TSR2-DBA14-specific literature. Secondary prevention centers on early recognition of the biochemical DBA phenotype (as demonstrated in the non-anemic cousin, identified via eADA/HbF/MCV screening) in at-risk relatives, enabling monitoring for later-onset anemia and enrollment in cancer surveillance protocols recommended generally for DBA (given the cancer-predisposition profile of DBA broadly). Tertiary prevention follows general DBA cancer-surveillance guidance (colonoscopy and other age-appropriate screening given elevated colorectal cancer and MDS/AML risk in DBA registries), extrapolated rather than demonstrated for this gene.

---

## 14. Other Species / Natural Disease

No naturally occurring TSR2-mutant disease has been reported in non-human species (companion animals, livestock, or wildlife); no OMIA entry exists for this gene-disease combination. TSR2 orthologs are broadly conserved across eukaryotes (yeast Tsr2 through human TSR2), reflecting the essential, deeply conserved nature of the ribosome-maturation function itself (see Model Organisms below) rather than any documented spontaneous veterinary phenotype.

---

## 15. Model Organisms

**Yeast (*Saccharomyces cerevisiae*) — functional/complementation model:** The pathogenicity of the human TSR2 E64G variant was directly demonstrated using a yeast humanized/complementation system: yeast strains expressing human TSR2^E64G in place of endogenous Tsr2 showed strong growth impairment and defective 20S pre-rRNA processing (cytoplasmic ITS1 reporter accumulation), providing direct functional evidence that this variant impairs TSR2's role in ribosome maturation (PMID:24942156). This is a gain of mechanistic insight but not a whole-organism disease model — it establishes molecular loss-of-function, not organismal phenocopy of anemia/craniofacial malformation.

**Yeast — structural/biochemical model of the Tsr2–Rps26 chaperone cycle:** NMR structural and cross-linking mass-spectrometry work (PMID:30201955) defined the Tsr2–eS26(ESS) binding interface in molecular detail and directly showed the DBA-linked mutant is selectively impaired in this interaction; subsequent biochemical work (2021, e.g. the Tsr2–Rps26 release/reincorporation stress-response study) further elaborated Tsr2's dual role in RPS26 nuclear escort and in reversible RPS26 disassembly from mature 40S ribosomes under oxidative/pH stress. These are molecular/biochemical models (recombinant protein, in vitro reconstitution), not organismal models, and their translational fidelity to human craniofacial and hematopoietic development is inferential.

**Mouse:** Tsr2 has an annotated mouse ortholog (MGI:1916749), but no published Tsr2-mutant or Tsr2-knockout mouse model recapitulating DBA-like anemia or craniofacial malformation was identified in this search. This is a genuine translational gap — unlike TCOF1 (Treacher Collins) and several other DBA genes (e.g., Rps19, Rpl11 mouse/zebrafish models), no whole-organism model exists to test whether the E64G lesion (or Tsr2 haploinsufficiency generally) reproduces the combined erythroid-failure-plus-craniofacial phenotype in vivo. This should be recorded as a `HUMAN_MODEL_MISMATCH`/knowledge-gap class finding if curated into dismech: evidence for the mechanism exists at the molecular/biochemical (yeast, in vitro) level, but organismal fidelity to the human phenotype (particularly the craniofacial neural-crest component) is unconfirmed in any animal model.

**Zebrafish:** No TSR2-specific zebrafish model was identified in this search, in contrast to other ribosomopathy genes (e.g., rps19, rpl11 morphants/mutants used extensively to model DBA hematopoietic phenotypes and to study neural-crest/craniofacial ribosomopathy convergence in zebrafish more generally).

---

## Summary of Key Citations

| Claim | PMID/Source |
|---|---|
| Original description of the TSR2 E64G family, RPS28/DBA15 discovery, DBA+MFD heterogeneity | PMID:24942156 (Gripp et al., *Am J Med Genet A*, 2014; full text PMC4149220) |
| Molecular/structural basis of Tsr2–eS26(ESS) interaction; DBA-linked mutant impaired in ESS binding | PMID:30201955 (*Nat Commun*, 2018) |
| eADA diagnostic performance in DBA | PMID:23252420 |
| DBA classical/supporting diagnostic criteria, general genetics/epidemiology | PMC6416817 (Diamond Blackfan Anemia: Genetics, Pathogenesis, Diagnosis and Treatment) |
| DBA cancer-predisposition/registry data (MDS, AML, colorectal cancer, osteosarcoma) | ASH/Blood registry literature (ashpublications.org/blood/article/128/22/333) |
| Nucleolar stress / p53 / ATF4 mechanism in DBA generally | PMID:21930148; PMC12096137 |
| Treacher Collins/mandibulofacial dysostosis neural-crest apoptosis mechanism (general, not TSR2-specific) | PMID:807232; PMID:3474899 |

**Explicit evidence-directness note:** Beyond the single foundational case report (PMID:24942156) and the follow-up molecular-mechanism paper on the E64G–ESS interaction (PMID:30201955), essentially all mechanistic (nucleolar stress/p53/ATF4), craniofacial-neural-crest, cancer-predisposition, and treatment-outcome content in this report is extrapolated by analogy from the broader Diamond-Blackfan anemia and Treacher Collins/mandibulofacial dysostosis literatures rather than demonstrated specifically for TSR2-DBA14. Any curation into dismech should carry `directness: INDIRECT` on evidence items sourced from this general-DBA/general-MFD literature rather than from the two TSR2-specific primary papers, and should flag the absence of any animal model as a structural knowledge gap rather than silently assuming mechanistic parity with better-studied DBA genes.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 51 |
| Resolved | 47 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 34 |
| Terms named correctly | 18 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 11 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `GO:0006974` (1 mention) - the report calls it "DNA damage response — for p53 axis, if used generically for nucleolar stress signaling"; GO calls it **DNA damage response**
- `UBERON:0000453` (1 mention) - the report calls it "jaw region"; UBERON calls it **decidua basalis**
- `UBERON:0001676` (1 mention) - the report calls it "mandible"; UBERON calls it **occipital bone**
- `UBERON:0001703` (1 mention) - the report calls it "upper jaw region/midface"; UBERON calls it **neurocranium**
- `UBERON:0000151` (1 mention) - the report calls it "pharyngeal arch"; UBERON calls it **pectoral fin**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0008565` (obsolete protein transporter activity) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0011903` (1 mention) - the report calls it "Increased hemoglobin F"; HP calls it **HbH hemoglobin**, and lists "Hemoglobin H" among its other names
- `GO:0000462` (1 mention) - the report calls it "maturation of SSU-rRNA from tricistronic rRNA transcript"; GO calls it **maturation of SSU-rRNA from tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA)**
- `GO:0006446` (1 mention) - the report calls it "regulation of translational initiation — secondary"; GO calls it **regulation of translational initiation**
- `GO:0036503` (1 mention) - the report calls it "ERAD pathway — not applicable"; GO calls it **ERAD pathway**
- `GO:0043066` (1 mention) - the report calls it "negative regulation of apoptotic process — for the p53/MDM2 axis, inverted as appropriate"; GO calls it **negative regulation of apoptotic process**
- `GO:0008565` (1 mention) - the report calls it "protein transporter activity — for the importin-disassembly role"; GO calls it **obsolete protein transporter activity**
- `CL:0002321` (1 mention) - the report calls it "embryonic cell, cranial neural crest lineage"; CL calls it **embryonic cell (metazoa)**
- `UBERON:0001846` (2 mentions) - the report calls it "external auditory meatus"; UBERON calls it **internal ear**
- `UBERON:0002190` (1 mention) - the report calls it "subcutaneous adipose — not relevant"; UBERON calls it **subcutaneous adipose tissue**
- `NCIT:C16186` (1 mention) - the report calls it "Orthopedic Surgical Procedure, if applicable to mandibular work"; NCIT calls it **Orthopedic Surgical Procedure**
- `NCIT:C15240` (1 mention) - the report calls it "Genetic counseling for the family"; NCIT calls it **Genetic Counseling**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.