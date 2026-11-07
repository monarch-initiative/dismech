---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-30T07:51:20.458789'
end_time: '2026-10-30T08:38:15.170420'
duration_seconds: 2814.71
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Congenital Myopathy 28 With Rigid Spine
  mondo_id: MONDO:0980756
  category: Mendelian
  causal_genes: HMGCS1
  omim_id: OMIM:621433
  synonyms: not recorded
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 5
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 6
  quotes_valid: 6
  relevance_assessed: 8
  on_topic: 6
  validator_version: 0.4.0
term_validation:
  total_terms: 40
  verified: 37
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 4
  labels_variant: 2
  obsolete_terms:
  - term_id: GO:0010142
    ontology_label: obsolete farnesyl diphosphate biosynthetic process, mevalonate
      pathway
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Congenital_Myopathy_28_With_Rigid_Spine-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Congenital_Myopathy_28_With_Rigid_Spine-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Myopathy 28 With Rigid Spine
- **MONDO ID:** MONDO:0980756 (if available)
- **Causal gene(s):** HMGCS1
- **OMIM:** OMIM:621433
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Congenital Myopathy 28 With Rigid Spine** covering all of the
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

# Congenital Myopathy 28 With Rigid Spine (CMYO28) — Comprehensive Disease Report

**MONDO:** MONDO:0980756 · **OMIM phenotype:** 621433 · **Causal gene:** **HMGCS1** (3-hydroxy-3-methylglutaryl-CoA synthase 1; cytosolic) · **Category:** Mendelian, autosomal recessive

> **Causal gene stated up front:** This report concerns the disease caused by biallelic variants in **HMGCS1** (HGNC:5007; NCBI Gene 3157; chromosome 5p12; gene alias **CMYO28**), the first committed enzyme of the cytosolic **mevalonate pathway**. It is *not* the SELENON-related rigid spine muscular dystrophy (RSMD1), with which it overlaps clinically. The near-totality of disease-specific knowledge derives from a single defining study: **Dofash et al., *Brain* 2025;148(5):1707–1722 (PMID: 39531736)**. Where a section has no disease-specific evidence, this is stated explicitly and inferences are drawn from mevalonate-pathway biology and the closely related HMGCR/GGPS1 myopathies.

---

## 1. Disease Information

**Overview.** Congenital Myopathy 28 with Rigid Spine (CMYO28) is a rare, childhood-onset recessive myopathy belonging to the "rigid spine syndrome" clinical group. It is characterized by slowly progressive or non-progressive **spinal rigidity (cervical and dorso-lumbar), scoliosis, axial/limb contractures, hypotonia, and respiratory insufficiency**, with variably elevated creatine kinase (CK). It was defined in 2025 as the newest recognized mevalonate-pathway myopathy. Rigid spine syndrome as a group is "a rare childhood-onset myopathy characterized by slowly progressive or non-progressive scoliosis, neck and spine contractures, hypotonia and respiratory insufficiency" (PMID: 39531736); most such cases are caused by SELENON, and HMGCS1 explains a subset of previously unsolved cases.

**Key identifiers.**
- **OMIM phenotype:** 621433 (Congenital Myopathy 28 With Rigid Spine, CMYO28)
- **Gene OMIM:** HMGCS1 — 142940
- **MONDO:** MONDO:0980756
- **HGNC:** HMGCS1, HGNC:5007; **NCBI Gene:** 3157; **Ensembl:** ENSG00000112972; **UniProt:** Q01581 (HMCS1_HUMAN)
- **ICD-11:** best mapped to 8C70 (Primary disorders of muscles / congenital myopathies); **ICD-10:** G71.2 (congenital myopathies) — no CMYO28-specific code exists.
- **MeSH:** no specific descriptor; closest umbrella terms are "Myopathies, Structural, Congenital" (D020914) and "Muscular Diseases."
- **Orphanet:** no dedicated ORPHA code yet (disease defined 2024–2025); phenotypically within the "rigid spine syndrome" / congenital myopathy groups.

**Synonyms / alternative names.** CMYO28; HMGCS1-related rigid spine myopathy; HMGCS1-related rigid spine syndrome; mevalonate-pathway rigid spine myopathy. Gene aliases: HMGCS, HMG-CoA synthase 1 (soluble/cytosolic).

**Information source type.** Aggregated from **individual patient reports** (5 patients from 4 unrelated families) combined with in vitro recombinant-protein biochemistry and a zebrafish disease model — i.e., primary-literature case-level data, not population registries or EHR aggregation.

---

## 2. Etiology

**Primary cause (genetic).** Biallelic (autosomal recessive) variants in **HMGCS1**. "In five patients from four unrelated families, we identified biallelic variants in HMGCS1 ... six missense variants and one frameshift variant distributed throughout HMGCS1" (PMID: 39531736). HMGCS1 catalyzes condensation of acetyl-CoA + acetoacetyl-CoA → HMG-CoA, the first committed, cytosolic step of the mevalonate pathway that produces cholesterol and non-sterol isoprenoids (dolichol, ubiquinone/CoQ10, farnesyl- and geranylgeranyl-pyrophosphate for protein prenylation).

**Genetic risk factors.** The disease is monogenic/Mendelian: the only established risk factor is inheriting **two** pathogenic/hypomorphic HMGCS1 alleles. Heterozygous carriers are unaffected. No susceptibility loci or modifier genes have been formally identified. Mechanistically, variants in **downstream** mevalonate-pathway enzymes act as candidate phenocopy/comparator loci: "biallelic hypomorphic variants in downstream enzymes including HMGCR and GGPS1 are associated with muscular dystrophy resembling our cohort's presentation" (PMID: 39531736).

**Environmental / acquired modifiers.** Not causal, but clinically important as **triggers of deterioration**: "The clinical course worsened with intercurrent disease or certain drugs in some patients; one patient died from respiratory failure following infection" (PMID: 39531736). By mechanistic inference, **statins** (HMG-CoA reductase inhibitors) and other mevalonate-pathway–suppressing drugs are expected to be deleterious, since statins alone cause myopathy by inhibiting the immediately downstream enzyme HMGCR (PMID: 36745799, 37167966). Age, sex, occupational, and lifestyle risk factors are not established.

**Protective factors.** No genetic protective alleles described. Mechanistically, **mevalonic acid supplementation** is protective in the zebrafish model (see §12) — bypassing the deficient enzymatic step restores downstream flux.

**Gene–environment interaction.** Strongly suggested: a partially functional (hypomorphic) mevalonate pathway is **decompensated by metabolic stress** (infection, fever, catabolic illness) and by pathway-inhibiting drugs, precipitating respiratory crises. This is an inferred gene × environment interaction based on the clinical course description, not a formally quantified interaction.

---

## 3. Phenotypes

Frequencies below are the **curated HPO disease annotations for MONDO:0980756** (Monarch/HPOA, derived from the PMID 39531736 cohort), which give explicit percentages. Phenotype type and HPO terms are given; obligate (100%) features are the diagnostic core.

| Phenotype | Type | Frequency | Characteristics | HPO term |
|---|---|---|---|---|
| **Spinal rigidity (cervical + dorso-lumbar)** | Clinical sign / contracture | **100%** | Childhood onset; slowly/non-progressive; defining feature | **HP:0003306** (Spinal rigidity) |
| **Scoliosis** | Physical manifestation | **100%** | Childhood onset; may progress | **HP:0002650** (Scoliosis) |
| **Elevated creatine kinase** | Laboratory abnormality | **100%** (variably elevated level) | "Creatine kinase levels were variably elevated" | **HP:0003236** (Elevated circulating creatine kinase activity) |
| **Fatty replacement of skeletal muscle** | Imaging/pathology | **100%** | Muscle MRI/biopsy fatty infiltration | **HP:0012548** (Fatty replacement of skeletal muscle) |
| **Reduced forced vital capacity / respiratory insufficiency** | Functional / clinical sign | **100%** (reduced FVC) | Restrictive; diaphragmatic weakness; cause of death in 1 patient | **HP:0032341** (Reduced forced vital capacity); HP:0002093 (Respiratory insufficiency) |
| **Rimmed vacuoles (muscle biopsy)** | Pathology | **100%** | Plus oxidative-enzyme-stain irregularities, occasional internal nuclei | **HP:0003805** (Rimmed vacuoles); HP:0003687 (Centrally nucleated fibers) |
| **Scapular winging** | Clinical sign | **80%** | Axial/scapular girdle involvement | **HP:0003691** (Scapular winging) |
| **Proximal muscle weakness** | Clinical sign | **80%** | Limb-girdle component | **HP:0003701** (Proximal muscle weakness) |
| **Distal muscle weakness** | Clinical sign | **60%** | | **HP:0002460** (Distal muscle weakness) |
| **High/narrow palate** | Physical manifestation | **40%** | Dysmorphic/secondary to weakness | **HP:0000218** (High palate) |
| **Bulbar palsy** | Clinical sign | **20%** | Bulbar weakness | **HP:0001283** (Bulbar palsy) |
| **Hypotonia** | Clinical sign | characteristic of group (congenital) | Often early | **HP:0001252** (Hypotonia) |
| **Clinical worsening with illness/drugs; risk of death** | Course modifier | some | Respiratory decompensation; 1 death | HP:0002878 (Respiratory failure) |

**Explicitly absent / discriminating negatives (0% in annotations):** facial muscle weakness (HP:0030319), ptosis (HP:0000508), **reduced left-ventricular ejection fraction (HP:0012664) — i.e., no primary cardiomyopathy**, and myositis (HP:0100614). Sparing of face, eyelids and heart helps distinguish CMYO28 from other congenital myopathies.

**Onset:** childhood-onset (congenital myopathy group); **severity:** moderate–severe and **variable**; **progression:** slowly progressive or non-progressive baseline with **episodic decompensation** during intercurrent illness.

**Quality-of-life impact.** Not directly measured in the HMGCS1 cohort. By close analogy to SELENON-related rigid spine myopathy, expect impaired QoL with pain, problematic fatigue, restricted mobility/standing-transfers, and respiratory burden: SELENON-RM "Questionnaires revealed impaired quality of life, pain and problematic fatigue" and diaphragm/respiratory function "was impaired in all patients" (PMID: 37807786). (Evidence: analogous disease, not HMGCS1-specific.)

---

## 4. Genetic / Molecular Information

**Causal gene.** HMGCS1 (OMIM 142940; HGNC:5007; Gene 3157), 12 exons on 5p12 (GRCh38 NC_000005.10:~43,287,469–43,313,411, minus strand). Protein: **cytoplasmic hydroxymethylglutaryl-CoA synthase**, **520 aa**, **EC 2.3.3.10**, functions as a **homodimer**; UniProt **Q01581**; crystal structure **PDB 2P8U**; domains Pfam **PF01154** (HMG_CoA_synt_N) + **PF08540** (HMG_CoA_synt_C), InterPro IPR013528/IPR013746/IPR010122 (thiolase-like fold IPR016039); subcellular location **cytoplasm** (UniProt). Canonical transcript NM_001098272 / NM_002130. Function (UniProt): "Catalyzes the condensation of acetyl-CoA with acetoacetyl-CoA to form HMG-CoA, which is converted by HMG-CoA reductase (HMGCR) into mevalonate, a precursor for cholesterol synthesis."

**Pathogenic variants (from PMID: 39531736; HGVS confirmed against ClinVar, transcript NM_001098272).**
- **Seven variants total:** six missense + one frameshift, distributed throughout the gene (no single hotspot).
- **Specific alleles (HGVS):** **c.209T>C (p.Met70Thr)**, **c.803G>C (p.Cys268Ser)**, **c.890G>T (p.Gly297Val)**, **c.1289G>A (p.Arg430Lys)**, **p.Ser447Pro**, **p.Gln29Leu** (six missense), and **c.344_345del (p.Ser115fs)** (frameshift). In ClinVar, p.Gly297Val, p.Arg430Lys and p.Ser115fs are classified **Pathogenic**; p.Met70Thr and p.Cys268Ser show "conflicting classifications" (reflecting their recent, 2025 disease association).
- **Functionally characterized missense variants:** **p.Ser447Pro, p.Gln29Leu, p.Met70Thr, p.Cys268Ser** (recombinant-protein and zebrafish-rescue assays).
- **Variant type/class:** predominantly **missense**; one **frameshift** (predicted truncating/LoF).
- **Functional consequence:** **hypomorphic / partial loss of function** — "these missense variants in HMGCS1 act through a hypomorphic mechanism." All four tested mutants retained dimerization; 3/4 had reduced thermal stability; 2/4 showed subtle enzymatic-activity changes; all four showed reduced function in zebrafish rescue. Biallelic complete LoF is presumed non-viable (HMGCS1 is essential; see zebrafish lethality), so disease genotypes are hypomorphic.
- **ACMG/AMP classification:** reported as disease-causing with functional support (PS3/PM-level evidence); several alleles curated **Pathogenic** in ClinVar, others still "conflicting/VUS" pending wider recognition.
- **Allele frequency / population constraint:** disease alleles are rare/very low frequency in gnomAD. **HMGCS1 is extremely loss-of-function intolerant: gnomAD pLI = 0.99999, LOEUF (oe_lof upper 90% CI) = 0.30 (point o/e 0.17), LoF Z = 5.08, missense Z = 5.15** — strong population depletion of both LoF and missense alleles, consistent with essentiality and with viable disease requiring residual-function (hypomorphic) genotypes.
- **Origin:** **germline**, biallelic. No somatic involvement (not a neoplastic disease).

**Modifier genes.** None established. Downstream pathway load (HMGCR, GGPS1, FDPS, etc.) is a plausible modifier space but untested.

**Epigenetics / chromosomal abnormalities.** No disease-specific methylation, histone, or large structural/cytogenetic findings reported. Not a copy-number/aneuploidy disorder.

---

## 5. Environmental Information

- **Environmental/chemical factors:** No causal environmental agent. **Drugs that inhibit the mevalonate pathway (statins; possibly bisphosphonates/aminobisphosphonates acting on FDPS; antifungal/other mevalonate-suppressing agents) are expected to aggravate disease** by mechanistic analogy to statin myopathy and to the reported "certain drugs" worsening the course (PMID: 39531736). CHEBI terms: statins (CHEBI:87631), mevalonic acid (CHEBI:25350), cholesterol (CHEBI:16113), ubiquinone (CHEBI:16389).
- **Lifestyle factors:** No established diet/smoking/exercise risk. Catabolic stress and dehydration during illness plausibly worsen the metabolic myopathy.
- **Infectious agents:** None causal, but **intercurrent infection is a documented precipitant of fatal respiratory decompensation** (PMID: 39531736).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic hypomorphic HMGCS1 variants** (missense ± frameshift) **lead to** reduced thermal stability and modestly reduced catalytic activity of the cytosolic HMG-CoA synthase homodimer (demonstrated in vitro). *[Demonstrated: recombinant protein assays.]*
2. This **results in** decreased synthesis of **HMG-CoA**, the first committed intermediate of the mevalonate pathway. *[Inferred from enzyme function; HMGCS1 catalyzes acetyl-CoA + acetoacetyl-CoA → HMG-CoA.]*
3. Reduced HMG-CoA **leads to** reduced flux to **mevalonate** and thence to all downstream isoprenoids — **cholesterol, dolichol, ubiquinone (CoQ10), and farnesyl-/geranylgeranyl-pyrophosphate (FPP/GGPP)**. *[Inferred from pathway position; supported by rescue with exogenous mevalonic acid.]*
4. **Branch A — defective protein prenylation:** reduced GGPP/FPP **leads to** impaired prenylation of small GTPases (e.g., Rab/Rho), paralleling GGPS1-related muscular dystrophy, where loss of geranylgeranyl-PP causes dystrophic muscle, **delayed sarcolemmal membrane repair** in patient myogenic cells, and enlarged mitochondria/autophagic material (PMID 32403198). *[Inferred for HMGCS1; demonstrated for the downstream enzyme GGPS1.]*
5. **Branch B — membrane/sterol and CoQ deficits:** reduced cholesterol/dolichol/ubiquinone **leads to** membrane and mitochondrial/oxidative dysfunction in muscle, consistent with biopsy "irregularities in oxidative enzyme staining" and rimmed vacuoles. *[Partly demonstrated (biopsy); mechanism inferred.]*
6. These deficits **result in** myofiber dysfunction/degeneration and impaired regeneration in **axial (paraspinal, cervical) and diaphragmatic muscle**, producing **spinal rigidity, scoliosis, contractures, and respiratory insufficiency**. *[Demonstrated clinically/histologically; cell-biological link inferred.]*
7. Under **metabolic stress (infection, catabolic illness) or pathway-inhibiting drugs**, the already marginal mevalonate flux **decompensates**, **leading to** acute respiratory failure and, in one patient, **death**. *[Demonstrated clinically.]*
8. In the zebrafish model, loss of Hmgcs1 **leads to** immobility by 2 dpf and death by day 3; **supplying mevalonic acid bypasses step 2–3 and reduces phenotype severity**, closing the causal loop. *[Demonstrated in animal model.]*

### Checklist detail
- **Molecular pathways:** Mevalonate / isoprenoid / cholesterol biosynthesis (KEGG hsa00900 "Terpenoid backbone biosynthesis"; Reactome R-HSA-191273 "Cholesterol biosynthesis"). GO:0019287 (isopentenyl diphosphate biosynthetic process, mevalonate pathway); GO:0010142 (farnesyl diphosphate biosynthetic process); GO:0006695 (cholesterol biosynthetic process).
- **Cellular processes:** oxidative metabolism/mitochondrial function (biopsy oxidative-stain irregularities), autophagic/vacuolar pathology (rimmed vacuoles), impaired muscle regeneration (inferred).
- **Protein dysfunction:** hypomorphic HMGCS1 — reduced thermostability, subtle activity loss, **dimerization preserved** (not a dominant-negative/aggregation mechanism). Enzyme activity: GO:0004421 (hydroxymethylglutaryl-CoA synthase activity).
- **Metabolic changes:** reduced endogenous cholesterol and non-sterol isoprenoid (dolichol, CoQ, prenyl-PP) synthesis in muscle.
- **Immune involvement:** none established (distinct from anti-HMGCR *immune-mediated* necrotizing myopathy, which is autoantibody-driven and unrelated).
- **Tissue damage:** myofiber degeneration with internal nuclei, rimmed vacuoles, oxidative-enzyme irregularity.
- **Biochemical abnormality:** partial HMG-CoA synthase deficiency (EC 2.3.3.10).
- **Molecular profiling:** no transcriptomic/proteomic/metabolomic patient datasets published yet; proteomics expertise (Stroud lab) contributed to functional work. **Functional genomics/model:** zebrafish *hmgcs1* mutant (lethal, mevalonate-rescuable).
- **Cell types:** skeletal myofibers (**CL:0000188** skeletal muscle cell), satellite cells (**CL:0000594**) plausibly involved in impaired regeneration.

---

## 7. Anatomical Structures Affected

- **Primary organ/system:** **skeletal muscle**, musculoskeletal and respiratory systems. Axial muscles — paraspinal/cervical (**UBERON:0001134** skeletal muscle tissue; UBERON:0001774 neck muscle) — and the **diaphragm (UBERON:0001103)**.
- **Secondary involvement:** spine/vertebral column (**UBERON:0001130**) → scoliosis and rigidity; **lungs (UBERON:0002048)** / respiratory function secondarily (restrictive respiratory failure); possible secondary **right-heart/pulmonary-hypertension** burden (reported in the analogous SELENON-RM group, PMID: 35868898 — not confirmed in HMGCS1).
- **Tissue level:** striated muscle tissue; myopathic changes on biopsy.
- **Cell level:** skeletal myofibers (CL:0000188); satellite/muscle stem cells (CL:0000594) by inference.
- **Subcellular (GO Cellular Component):** **cytosol (GO:0005829)** — site of HMGCS1 and the mevalonate pathway; secondary **mitochondrial (GO:0005739)** oxidative-enzyme abnormalities; **endoplasmic reticulum (GO:0005783)** (downstream cholesterol/dolichol synthesis); autophagic **vacuoles** (rimmed vacuoles).
- **Localization/lateralization:** **bilateral, axial-predominant** (cervical and dorso-lumbar spine, diaphragm); scoliosis introduces a lateralized curvature but the muscle disease is symmetric.

---

## 8. Temporal Development

- **Onset:** **childhood-onset / congenital myopathy** spectrum; rigid spine syndrome is "childhood-onset" (PMID: 39531736). Onset pattern **insidious/chronic** with early hypotonia.
- **Progression:** **slowly progressive or non-progressive** scoliosis/rigidity baseline, with superimposed **episodic acute decompensation** during intercurrent illness or drug exposure.
- **Course:** chronic, lifelong; respiratory function tends to decline; **critical vulnerability windows = intercurrent infections and exposure to mevalonate-inhibiting drugs.**
- **Remission:** no spontaneous remission; mevalonic acid supplementation is a candidate disease-modifying (not curative) intervention (animal data only).
- **Critical period for intervention:** restoring mevalonate flux (supplementation) and aggressive respiratory/infection management during catabolic illness.

---

## 9. Inheritance and Population

- **Inheritance:** **autosomal recessive** (biallelic). Consistent across 4 unrelated families.
- **Penetrance/expressivity:** apparently high penetrance for biallelic genotypes; **variable expressivity** (CK variable; severity ranges to early death). Formal penetrance estimates not available (n=5).
- **Carrier frequency / founder effects:** not established; individual disease variants are rare/very low frequency in gnomAD, and HMGCS1 is strongly LoF- and missense-constrained (pLI≈1.0, LOEUF 0.30), so biallelic null carriers are essentially absent. No founder haplotype reported (families unrelated, geographically diverse — Australia, Spain, Italy, France, Japan, USA contributing centers).
- **Epidemiology:** **ultra-rare**; only 5 patients reported worldwide at description. No prevalence/incidence estimates; no dedicated registry.
- **Demographics:** no sex predilection established (recessive, small n); multi-ethnic (European, Japanese, and others represented through contributing centers). Age distribution: pediatric onset, into adulthood.
- **Anticipation / germline mosaicism:** not applicable / not reported (not a repeat-expansion disorder).
- **Consanguinity:** biallelic recessive; some families may be consanguineous (typical for homozygous hypomorphic genotypes), though specific consanguinity details are not extractable here.

---

## 10. Diagnostics

- **Laboratory:** serum **creatine kinase** — variably elevated (HP:0003236; LOINC 2157-6, Creatine kinase [serum]). No validated disease-specific circulating biomarker yet; a metabolite signature (low mevalonate/isoprenoid intermediates) is a plausible but unproven biomarker.
- **Muscle biopsy / histopathology:** irregular **oxidative enzyme (NADH/SDH/COX) staining**, occasional **internal (central) nuclei**, and **rimmed vacuoles** — nonspecific myopathic/dystrophic changes (PMID: 39531736). (SNOMED: myopathy, muscle biopsy abnormal.)
- **Imaging:** spine radiographs/MRI for scoliosis and rigidity; muscle MRI/ultrasound expected to show axial/paraspinal involvement (by analogy to SELENON-RM, which shows symmetric increased echogenicity; PMID: 37807786). RadLex: scoliosis, muscle atrophy.
- **Functional/respiratory testing:** pulmonary function tests with emphasis on **diaphragm function** (restrictive pattern; nocturnal hypoventilation surveillance), as in SELENON-RM (PMID: 37807786). Cardiac surveillance (ECG/echo) advisable given secondary pulmonary-hypertension risk in the rigid-spine group (PMID: 35868898).
- **Genetic testing (diagnostic gold standard):** **exome or genome sequencing** identified the variants (PMID: 39531736). Recommended approach: WES/WGS or a **congenital myopathy / rigid-spine gene panel** that now should **include HMGCS1** alongside SELENON, and consider HMGCR and GGPS1. Single-gene HMGCS1 testing is reasonable when phenotype is classic and panel negative. CMA/karyotype/FISH/mtDNA/repeat-expansion testing are **not** indicated (point-mutation recessive disorder).
- **Clinical criteria / differential diagnosis:** diagnose rigid spine myopathy clinically (early spinal rigidity + scoliosis + respiratory insufficiency + relative preservation of ambulation), then confirm genetically. **Differentials:** SELENON (SEPN1)-related rigid spine muscular dystrophy (RSMD1) — most common cause; collagen VI–related (Ullrich/Bethlem); LMNA-related; FHL1; multiminicore/RYR1; HMGCR- and GGPS1-related muscular dystrophies (same pathway); and **immune-mediated anti-HMGCR necrotizing myopathy** (serologic, treatable, mechanistically distinct from HMGCS1).
- **Screening:** no newborn screening. **Cascade/carrier testing** in families; prenatal/preimplantation testing possible once biallelic variants are known.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** potentially fatal — **"one patient died from respiratory failure following infection"** (PMID: 39531736). No cohort survival statistics (n=5).
- **Morbidity/function:** chronic restrictive respiratory impairment, scoliosis, contractures, and reduced mobility drive disability; likely need for respiratory support (NIV) and orthopedic/scoliosis management over time (by analogy to SELENON-RM).
- **Disease course:** chronic progressive with acute decompensations; recovery potential limited without disease-modifying therapy.
- **Prognostic factors:** severity of respiratory/diaphragmatic involvement; frequency of intercurrent illness; exposure to mevalonate-inhibiting drugs; (hypothesized) degree of residual HMGCS1 function by genotype.
- **Prognostic biomarkers:** none validated; CK is nonspecific.

---

## 12. Treatment

**No approved disease-specific therapy exists.** Management is currently supportive, with one mechanistically rational candidate therapy from animal data.

- **Candidate disease-modifying therapy — mevalonic acid supplementation:** "we demonstrate the potential for mevalonic acid supplementation to reduce phenotypic severity in mutant zebrafish" (PMID: 39531736). Rationale: exogenous **mevalonate (CHEBI:25350)** bypasses the deficient HMGCS1 step, restoring downstream isoprenoid/sterol synthesis. Human efficacy/safety untested. (NCIT: dietary supplement / metabolic replacement therapy.)
- **Avoid pathway inhibitors:** **statins and other mevalonate-pathway–suppressing drugs should be avoided** (drugs worsened the course; statins alone cause myopathy via the downstream HMGCR step — PMID: 36745799, 37167966). Pharmacogenomic-style caution: genotype (biallelic HMGCS1) should flag statin contraindication.
- **Supportive/rehabilitative (standard for rigid-spine congenital myopathy):**
  - **Respiratory care:** surveillance PFTs, nocturnal non-invasive ventilation, aggressive management of chest infections, vaccination against respiratory pathogens (NCIT: Respiratory Therapy; Mechanical Ventilation).
  - **Orthopedic:** scoliosis monitoring, bracing, and spinal fusion surgery when indicated (NCIT: Spinal Fusion).
  - **Physiotherapy/OT:** contracture prevention, stretching, mobility aids; nutrition support during catabolic illness.
- **Advanced therapeutics (gene/RNA/cell therapy):** none in development reported; because the mechanism is hypomorphic LoF, **gene replacement or metabolic bypass** are conceptually attractive future directions.
- **Experimental/clinical trials:** none registered specifically for HMGCS1 disease as of the 2025 description.
- **Combination/personalized strategy:** personalized approach = confirm biallelic HMGCS1 genotype → avoid mevalonate inhibitors → standard respiratory/orthopedic supportive care → consider mevalonate supplementation under research/compassionate framework.

---

## 13. Prevention

- **Primary prevention:** not applicable to a germline Mendelian disease at the population level; **avoid mevalonate-pathway–inhibiting drugs** in known patients (prevents iatrogenic worsening).
- **Secondary prevention:** early genetic diagnosis via panel/exome in rigid-spine phenotypes; proactive **respiratory surveillance** and prompt infection treatment to prevent fatal decompensation.
- **Tertiary prevention:** NIV, scoliosis surgery, contracture management to prevent complications.
- **Genetic counseling:** autosomal recessive — 25% recurrence risk for carrier couples; offer **carrier/cascade testing** and **prenatal/preimplantation genetic testing** once familial variants are defined (NSGC/ACMG framework).
- **Immunization/public health/environmental:** routine vaccination (influenza, pneumococcus, RSV where applicable) is prudent given infection-triggered deterioration; no vector/sanitation dimension.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** HMGCS1 is **deeply conserved**. Human (NCBI Taxon 9606) gene 3157. Orthologs: mouse *Hmgcs1* (NCBI Gene 208715; Taxon 10090), zebrafish *hmgcs1* (Taxon 7955), Drosophila and yeast (ERG13) homologs exist (mevalonate pathway is ancient/essential).
- **Natural disease in other species:** no naturally occurring HMGCS1 myopathy catalogued in OMIA for companion/livestock species to date. Zebrafish *hmgcs1* loss-of-function (the historical *stachel* mutant) is a known developmental-lethal model.
- **Comparative biology:** the lethality of complete loss across species underscores the essentiality of the mevalonate pathway, explaining why only **hypomorphic** biallelic human genotypes are viable and disease-causing. Evolutionary conservation of the pathway supports cross-species mechanistic translation.
- **Zoonosis/transmission:** not applicable (non-infectious genetic disease).

---

## 15. Model Organisms

- **Primary model — zebrafish (*Danio rerio*; Taxon 7955):** *hmgcs1* mutant. Phenotype: **immobile by 2 dpf, dead by day 3 post-fertilisation**; rescued by wild-type **HMGCS1 mRNA**. Used for **variant functional validation** (S447P, Q29L, M70T, C268S all showed reduced rescue vs wild-type) and **therapeutic proof-of-concept** (mevalonic acid reduced severity) (PMID: 39531736).
  - *Recapitulation:* models the essential-gene requirement and the hypomorphic allelic series; demonstrates treatability. *Limitation:* embryonic lethality means it models complete loss / severe reduction rather than the slowly progressive axial myopathy of patients; adult muscle-specific phenotype not captured.
- **In vitro model — recombinant human HMGCS1 protein:** biochemical characterization of dimerization, thermal stability, and enzymatic activity for four variants (PMID: 39531736).
- **Mouse (*Mus musculus*; Taxon 10090) — *Hmgcs1* (MGI:107592; Gene 208715):** IMPC reports the **homozygous knockout is preweaning-lethal with complete penetrance** (Viability Outcome), confirming essentiality and matching zebrafish lethality and the human gnomAD constraint. **Heterozygous** mice show **abnormal auditory brainstem response (hearing)** and **increased circulating ALT (liver)** — intriguingly echoing the hearing loss and hepatic involvement of the downstream GGPS1 mevalonate-pathway disease. No muscle-specific/conditional CMYO28 mouse model is yet reported; such a model would be the logical next tool to capture the slowly progressive axial myopathy that the lethal global null cannot.
- **Comparator pathway models:** **HMGCR** (PMID: 37167966, 36745799) and **GGPS1** (Y259C knock-in mouse; PMID 32403198).
- **Resources:** ZFIN (zebrafish *hmgcs1*), MGI/IMPC (mouse *Hmgcs1*, MGI:107592), Alliance of Genome Resources.

---

## Supported vs Refuted Hypotheses

**Supported:**
- H1 — Biallelic HMGCS1 variants cause a recessive rigid-spine congenital myopathy (CMYO28). **Supported** (5 patients/4 families; functional validation).
- H2 — Disease variants are **hypomorphic** (partial LoF), not dominant-negative. **Supported** (dimerization retained; reduced stability/activity; reduced zebrafish rescue).
- H3 — The defect lies in the **mevalonate/isoprenoid pathway**, shared with HMGCR/GGPS1 myopathies. **Supported** (pathway position; phenotypic convergence).
- H4 — **Mevalonic acid** can mitigate the phenotype. **Supported in animal model** (zebrafish); unproven in humans.
- H5 — HMGCS1 is **developmentally essential**, so only partial-LoF (hypomorphic) alleles are viable and disease-causing; complete biallelic LoF is lethal. **Supported** by convergent cross-species essentiality: zebrafish null death by ~day 3, mouse *Hmgcs1* homozygous preweaning lethality (MGI:107592, IMPC), and extreme human constraint (gnomAD pLI=0.99999, LOEUF=0.30, lof_z=5.08).
- H6 — The clinical signature is **axial/rigid-spine–predominant with high-penetrance fatty muscle replacement and restrictive respiratory decline**. **Supported** by Monarch/HPO frequencies: spinal rigidity, scoliosis, elevated CK, fatty muscle replacement, reduced FVC, and rimmed vacuoles each at 100% of reported cases; facial weakness, ptosis, and reduced LVEF absent.

**Refuted / not supported:**
- Dominant-negative or protein-aggregation mechanism — **refuted** (dimerization preserved; recessive inheritance).
- Autoimmune mechanism (as in anti-HMGCR myopathy) — **not applicable** to HMGCS1 genetic disease.

## Limitations and Future Directions

- Evidence rests essentially on **one cohort (n=5)** and model systems; prevalence, penetrance, natural history, sex ratio, and QoL are **not yet quantified**. HPO frequencies are derived from this small case series, so point estimates (e.g., "100%") are precision-limited.
- No human metabolomic/proteomic/muscle-imaging dataset specific to HMGCS1 patients; **no clinical trial** of mevalonic acid.
- **Future:** patient registry and natural-history study; muscle-specific conditional mouse model; metabolite biomarker (mevalonate/isoprenoid panel); formal statin-contraindication guidance; trial of mevalonic acid or downstream isoprenoid supplementation (CoQ10, GGOH).

## Key Evidence Sources
- **PMID 39531736** — Dofash et al., *Brain* 2025;148(5):1707–1722 (defining study; patients, variants, functional, zebrafish, treatment).
- **PMID 37167966** — Morales-Rosado et al., biallelic HMGCR → recessive LGMD (pathway comparator).
- **PMID 36745799** — Yogev et al., HMGCR LoF limb-girdle muscular disease / statin-myopathy mechanism.
- **PMID 32403198** — Foley et al., *Ann Neurol* 2020; GGPS1 → muscular dystrophy/hearing loss/ovarian insufficiency; defines isoprenoid/prenylation branch, Y259C knock-in mouse, delayed membrane repair (pathway comparator).
- **PMID 35869884** — Kaiyrzhanov et al., GGPS1 cohort (hearing loss variable, 46%).
- **PMID 38129970** — Altassan et al., GGPS1 phenotype/genotype expansion (hepatic involvement).
- **UniProt Q01581 / PDB 2P8U** — HMGCS1 protein structure and function annotation.
- **PMID 37807786** — Bouman et al., SELENON-RM natural history/QoL (clinical analog).
- **PMID 35868898** — Bouman et al., cardiac involvement in SELENON-RM (secondary PH risk, analog).


## Artifacts

- [OpenScientist final report](Congenital_Myopathy_28_With_Rigid_Spine-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Congenital_Myopathy_28_With_Rigid_Spine-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 6 |
| Quoted claims found in source | 6 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 8 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 40 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 6 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 2 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0010142` (obsolete farnesyl diphosphate biosynthetic process, mevalonate pathway) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0010142` (1 mention) - the report calls it "farnesyl diphosphate biosynthetic process"; GO calls it **obsolete farnesyl diphosphate biosynthetic process, mevalonate pathway**
- `CL:0000188` (2 mentions) - the report calls it "Cell level:** skeletal myofibers"; CL calls it **cell of skeletal muscle**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.

37 of 40 terms resolved to a current term; the rest could not be looked up either way.