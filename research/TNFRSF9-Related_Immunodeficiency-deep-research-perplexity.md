---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-11-24T16:12:21.205694'
end_time: '2026-11-24T16:17:44.300231'
duration_seconds: 323.09
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: TNFRSF9-Related Immunodeficiency
  mondo_id: MONDO:0859526
  category: Mendelian
  causal_genes: not recorded
  omim_id: OMIM:620282
  synonyms: IMD109; CD137 deficiency; 4-1BB deficiency; TNFRSF9 deficiency
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 19
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 4
  validator_version: 0.8.0
term_validation:
  total_terms: 14
  verified: 13
  not_found: 1
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.071
  labels_checked: 12
  labels_matching: 7
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: HP:0005261
    reported_labels:
    - Autoimmune lymphoproliferative syndrome
    ontology_label: Joint hemorrhage
  - term_id: HP:0004459
    reported_labels:
    - Recurrent otitis media
    ontology_label: Exostosis of the external auditory canal
  labels_variant: 3
  unresolved_terms:
  - HP:0002899
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** TNFRSF9-Related Immunodeficiency
- **MONDO ID:** MONDO:0859526 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** OMIM:620282
- **Synonyms:** IMD109; CD137 deficiency; 4-1BB deficiency; TNFRSF9 deficiency
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **TNFRSF9-Related Immunodeficiency** covering all of the
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

# TNFRSF9-Related Immunodeficiency (IMD109 / CD137 Deficiency): A Comprehensive Research Synthesis

TNFRSF9-related immunodeficiency is a rare autosomal recessive primary immune disorder caused by biallelic loss-of-function variants in the **TNFRSF9** gene, which encodes the costimulatory receptor CD137 (also known as 4‑1BB), a member of the tumor necrosis factor receptor superfamily that is crucial for T‑cell expansion, survival, and effector function.[3][4][12][15][16] This condition, formally designated Immunodeficiency 109 with lymphoproliferation (IMD109; OMIM 620282; MONDO:0859526), is characterized by recurrent sinopulmonary infections in childhood, hypogammaglobulinemia, persistent Epstein–Barr virus (EBV) viremia, and a striking predisposition to EBV-associated lymphoproliferative disease and lymphoma, despite numerically normal T, B, and NK cell counts.[16][18][19] Human cases and functional studies have shown that CD137 deficiency severely impairs CD8+ T‑cell expansion, cytotoxicity, and mitochondrial function, leading to failure of immune surveillance of EBV-infected cells and downstream lymphomagenesis, while also perturbing B‑cell differentiation and antibody production.[12][14][15][10][11] Because fewer than a dozen affected individuals have been reported worldwide, largely from consanguineous families, current knowledge is derived from carefully documented case series, mechanistic experimental work in patient cells, and complementary insights from 4‑1BB/4‑1BBL-deficient mouse models that elucidate the broader role of this pathway in antiviral cytotoxic responses.[17][12][15] The following report synthesizes available evidence on disease characteristics, pathophysiology, clinical expression, diagnostics, treatment, and models, and maps these features to ontology terms suitable for a structured disease-knowledge base.

## 1. Disease Information

### 1.1 Definition and Clinical Overview

TNFRSF9-related immunodeficiency, also known as Immunodeficiency 109 with lymphoproliferation (IMD109), is a Mendelian primary immune disorder that arises from autosomal recessive mutations in TNFRSF9 at chromosome 1p36.23, encoding the activation-inducible TNF receptor family member CD137/4‑1BB.[3][16][18] MedGen defines the condition as an autosomal recessive primary immune disorder with childhood onset of recurrent sinopulmonary infections, susceptibility to EBV infection, EBV viremia, and EBV-associated lymphoproliferative disease or B‑cell lymphoma, together with defective CD8+ T‑cell function despite normal lymphocyte counts.[18][19] OMIM similarly summarizes IMD109 as a primary immunodeficiency characterized by immunodeficiency and EBV-induced lymphoproliferation caused by 4‑1BB deficiency, based on the original descriptions by Alosaimi et al. (2019) and Somekh et al. (2019).[16][14][12] Orphanet lists the disorder under “Epstein–Barr virus-induced lymphoproliferative disease due to CD137 deficiency” and “EBV-induced lymphoproliferative disease due to Cell differentiation 137 protein deficiency,” emphasizing its unique association with EBV susceptibility and lymphoid proliferations.[13]

Clinically, affected individuals typically present in early childhood with recurrent bacterial respiratory infections, including sinusitis, otitis media, bronchitis, and pneumonia, often progressing to bronchiectasis and chronic lung disease, alongside hypogammaglobulinemia indicative of impaired humoral immunity.[10][14][18] Later in childhood or adolescence, many patients develop persistent high-level EBV viremia and EBV-driven lymphoproliferative disease, which may manifest as EBV-positive B‑cell lymphoma, autoimmune lymphoproliferative syndrome–like phenotypes, or chronic active EBV infection with hemophagocytic lymphohistiocytosis-like features.[12][14][10][18] Immunologic evaluation typically reveals normal counts of T, B, and NK cells, but marked functional defects in CD8+ T cells including reduced proliferative capacity, diminished interferon‑γ and perforin expression, impaired cytotoxicity against EBV-infected targets, and defective mitochondrial biogenesis and function upon activation.[12][14][15] These features place IMD109 firmly within the spectrum of **inborn errors of immunity** targeting T‑cell costimulatory pathways, with a distinctive link to EBV-related lymphomagenesis.

From a data provenance perspective, the description of TNFRSF9-related immunodeficiency is based primarily on aggregated disease-level resources synthesizing individual case reports and case series rather than large-scale epidemiological datasets or electronic health record mining. OMIM, MedGen, and Orphanet aggregate clinical and genetic information from a small number of peer-reviewed publications describing families with confirmed TNFRSF9 mutations.[16][18][13][14][12] The most substantial human evidence comes from two landmark 2019 studies: Alosaimi et al., who reported two consanguineous Saudi families with homozygous TNFRSF9 G109S mutations and EBV-induced lymphoproliferation,[14][16] and Somekh et al., who described four unrelated patients with distinct homozygous TNFRSF9 variants presenting with immunodeficiency, autoimmunity, and malignancy, including EBV-related lymphoma.[9][12] Subsequent case reports and literature reviews have added further patients and refined the phenotype, but the total remains fewer than ten individuals, underscoring the rarity of the disease and the central role of expert-curated resources.[10][11]

### 1.2 Key Identifiers and Synonyms

Multiple overlapping identifiers and synonyms are used in the literature and databases for TNFRSF9-related immunodeficiency. OMIM assigns the phenotype the entry number **620282**, under the name “Immunodeficiency 109 with lymphoproliferation (IMD109)” and links it causally to TNFRSF9 (OMIM 602250) located at 1p36.23.[16] MedGen uses the concept ID **C5830346** for “Immunodeficiency 109 with lymphoproliferation (IMD109)” and explicitly associates the condition with TNFRSF9 at 1p36.23, as well as the MONDO term MONDO:0859526 for cross-resource ontology integration.[18][19] The disease is categorized in Orphanet under “EBV-induced lymphoproliferative disease due to CD137 deficiency” and similar label variants emphasizing EBV-induced lymphoproliferation and CD137/Cell differentiation 137 protein deficiency.[13]

At the gene level, NCBI Gene lists TNFRSF9 as “TNF receptor superfamily member 9” with Gene ID 3604 for Homo sapiens, located on chromosome 1 with genomic coordinates in GRCh38 assembly, and notes that this receptor contributes to clonal expansion, survival, and development of T cells.[3][6] The NCBI Genetic Testing Registry (GTR) entry for TNFRSF9 highlights the alternative gene names and disease associations, listing TNFRSF9 (also known as ILA, 4‑1BB, CD137, CDw137, IMD109) and referencing available genetic tests.[4] The Affinage/Immune Deficiency Resource further summarizes TNFRSF9 as an activation-inducible TNF receptor superfamily costimulatory receptor that amplifies T‑cell effector responses upon engagement of its ligand 4‑1BBL, with established human disease causality when biallelic loss-of-function mutations abolish CD137 expression and impair EBV-specific CD8+ T‑cell responses.[15]

Common synonyms used in clinical and research publications include “CD137 deficiency,” “4‑1BB deficiency,” “TNFRSF9 deficiency,” and “Immunodeficiency and EBV-induced lymphoproliferation caused by 4‑1BB deficiency,” reflecting the historical discovery of the disease via functional CD137 analysis and the naming of the seminal JACI article.[14][10][16] In ontological contexts, “TNFRSF9-related immunodeficiency” and “Immunodeficiency 109 with lymphoproliferation (IMD109)” are preferred, as they explicitly link the phenotype to the causal gene and maintain consistency with the Mondo Disease Ontology MONDO:0859526.[18][19] For knowledge-base integration, it is critical to disambiguate this condition from other numbered immunodeficiencies, such as “Immunodeficiency 108,” “Immunodeficiency 110,” etc., which refer to distinct genes and mechanisms, by always pairing the disease label with TNFRSF9 as the causal locus and OMIM 620282 as the phenotype identifier.[16]

### 1.3 Alignment with Controlled Vocabularies and Ontologies

The clinical features of TNFRSF9-related immunodeficiency align with several Human Phenotype Ontology (HPO) terms. Recurrent upper and lower respiratory tract infections correspond to HPO terms such as *Recurrent respiratory infections* (HP:0002205) and *Bronchiectasis* (HP:0002110) in cases where structural lung damage develops.[10][14][18] Hypogammaglobulinemia is captured by the HPO term *Hypogammaglobulinemia* (HP:0004313), while persistent EBV viremia and susceptibility to EBV-induced lymphoproliferative disease can be mapped to *Recurrent viral infections* (HP:0004429) and *Abnormal susceptibility to EBV infection*, the latter currently represented indirectly via OMIM and MedGen descriptions but increasingly recognized in the HPO framework.[18][19][13] Lymphoproliferative manifestations, including EBV-positive B‑cell lymphoma and autoimmune lymphoproliferative syndrome-like features, correspond to *Lymphadenopathy* (HP:0002716), *B‑cell lymphoma* (HP:0002899), and *Autoimmune lymphoproliferative syndrome* (HP:0005261), while hemophagocytic lymphohistiocytosis-like episodes in some patients reflect HPO terms related to *Hemophagocytic lymphohistiocytosis*.[10][12][19]

At the disease-ontology level, MONDO:0859526 corresponds to “Immunodeficiency 109 with lymphoproliferation,” enabling cross-mapping to OMIM, Orphanet, MedGen, and other resources.[18][19] From the perspective of MeSH and ICD classification, the condition intersecting categories include “Primary Immunodeficiency Diseases,” “Lymphoproliferative Disorders,” and “Epstein-Barr Virus Infections,” but there is not yet a specific ICD-10 or ICD-11 code dedicated solely to TNFRSF9-related immunodeficiency; rather, coding is typically based on clinical manifestations such as “Common variable immunodeficiency,” “Non-Hodgkin lymphoma,” “Hodgkin lymphoma,” or “Hemophagocytic lymphohistiocytosis,” supplemented by specialized immunodeficiency codes in some national systems. This reflects the nascent stage of formal nosology for ultra-rare inborn errors of immunity.

Overall, disease information for TNFRSF9-related immunodeficiency is derived from aggregated disease-level resources that curate individual patient data from peer-reviewed case reports and mechanistic studies. OMIM, MedGen, Orphanet, NCBI Gene, GTR, and specialized immunodeficiency databases provide harmonized textual summaries that are suitable for knowledge-base population, but the extremely small number of known patients and lack of population-based registries mean that quantitative epidemiologic parameters remain limited and must be interpreted cautiously.[16][18][13][15]

## 2. Etiology

### 2.1 Genetic Causal Factors

The primary causal factor in TNFRSF9-related immunodeficiency is biallelic loss-of-function mutation in the **TNFRSF9** gene, which encodes the costimulatory receptor CD137/4‑1BB.[3][4][12][16] TNFRSF9 is located at chromosomal region 1p36.23 and is a protein-coding gene belonging to the tumor necrosis factor receptor superfamily.[3][16] The encoded receptor is expressed on activated T cells, B cells, and NK cells, where it functions as an activation-inducible costimulatory receptor that amplifies T‑cell effector responses upon engagement by its ligand, 4‑1BBL (TNFSF9), expressed on activated antigen-presenting cells.[3][15][17] The essential role of CD137 in antiviral T‑cell responses and immune homeostasis is underscored by both human genetic deficiency and animal models, as summarized in Affinage’s curated entry: “Biallelic loss-of-function mutations in TNFRSF9 abolish protein expression and cause defective CD8+ T cell expansion, cytotoxicity, and mitochondrial function, manifesting as failure to control EBV-infected T cells (chronic active EBV infection).”[15]

The first reported pathogenic TNFRSF9 variants causing IMD109 were homozygous missense mutations affecting conserved residues in the extracellular domain of CD137. Alosaimi et al. (2019) identified a homozygous G109S missense mutation (NM_001561:c.325G>A: p.Gly109Ser) in two unrelated children from consanguineous Saudi families with immunodeficiency and EBV-induced lymphoproliferation.[14][16][10] This mutation abolished surface expression of 4‑1BB and prevented binding to its ligand, leading to profound functional deficits. As summarized in the JACI article: “The two patients shared a homozygous G109S missense mutation in 4‑1BB that abolished protein expression and ligand binding.”[14] Somekh et al. (2019, Blood) expanded the genetic spectrum by identifying four distinct homozygous TNFRSF9 mutations—missense and frameshift variants—in four unrelated patients presenting with immunodeficiency, autoimmunity, and malignancy.[9][12] Their functional studies showed markedly reduced or absent CD137 expression on activated T, B, and NK cells, confirming a loss-of-function phenotype.[12]

Subsequent reports document additional pathogenic variants, such as a novel TNFRSF9 variant described in a recent case report and literature review of severe lymphoproliferative disease secondary to CD137 deficiency.[10] Another publication focusing on a “novel TNFRSF9 variant” associated with immune dysregulation and EBV-driven lymphomagenesis reiterates that IMD109 is a rare autosomal recessive disorder with only nine reported patients to date and ties these variants to the same functional pathway of impaired CD137-mediated costimulation.[11] In all described families, the inheritance is autosomal recessive with homozygous mutations in affected individuals, and heterozygous relatives are asymptomatic carriers, consistent with a classic recessive model.[14][12][16][10][11]

The functional consequences of these mutations are uniformly consistent with **loss of function**. Flow cytometry and immunoblotting in patient T cells show absent or severely reduced CD137 surface and total protein expression after activation, and in vitro assays demonstrate defective CD8+ T‑cell expansion, diminished interferon‑γ and perforin production, impaired cytotoxicity against EBV-transformed B cells, and compromised mitochondrial biogenesis and membrane potential in activated T cells.[12][14][15] These defects can be rescued by genetic reconstitution of CD137, confirming that the disease phenotype is directly attributable to TNFRSF9 dysfunction.[12] Therefore, TNFRSF9-related immunodeficiency is mechanistically best described as a **biallelic germline loss-of-function disorder of a T‑cell costimulatory receptor**, leading to a specific failure of EBV-specific immune surveillance.

### 2.2 Genetic Risk and Modifier Factors

Given the ultra-rare nature of TNFRSF9-related immunodeficiency, formal quantitative genetic risk factors beyond the causative biallelic variants have not yet been characterized in population-based studies. However, several lines of evidence suggest possible modifier influences and overlapping genetic contributions in some patients. Somekh et al. reported at least one individual with combined PIK3CD and TNFRSF9 deficiencies causing chronic active EBV infection of T cells, suggesting that defects in the PI3Kδ pathway and CD137 costimulation can interact to exacerbate disease severity.[15] In this context, the Affinage resource notes that “Genetic interaction with PIK3CD [is] not fully separated in all cases,” indicating that in some patients, coexisting gene defects may modulate the clinical phenotype of CD137 deficiency.[15]

Furthermore, more general genetic variability in other immune checkpoints, antiviral pathways, or EBV-entry receptors might influence susceptibility, severity, or particular manifestations of IMD109, but such hypotheses have yet to be systematically tested. No specific susceptibility loci, independent of TNFRSF9, have been reported to increase risk of clinically overt disease in heterozygous carriers or the general population. Nor are there known protective TNFRSF9 variants that attenuate disease; rather, common polymorphisms in TNFRSF9 have mostly been studied in the context of cancer immunotherapy and T‑cell activation, not primary immunodeficiency.

### 2.3 Environmental and Infectious Risk Factors

The most salient environmental and infectious factor in TNFRSF9-related immunodeficiency is **Epstein–Barr virus (EBV) infection**, which acts as a critical trigger for lymphoproliferation and malignancy in genetically susceptible individuals.[9][12][14][18][19] EBV is a ubiquitous herpesvirus infecting the majority of humans worldwide, typically establishing lifelong latency with only minor clinical consequences in immunocompetent hosts. In IMD109, however, defective CD137-mediated T‑cell costimulation leads to failure of effective CD8+ T‑cell responses against EBV-infected cells, allowing persistent high-level viremia and uncontrolled proliferation of EBV-infected B cells or T/NK cells.[12][14][15] MedGen emphasizes that “Affected individuals are susceptible to infection with EBV and develop EBV viremia and EBV-associated lymphoproliferative disease or B-cell lymphoma,” indicating that EBV exposure is a necessary environmental cofactor for the full disease phenotype.[18][19]

In addition to EBV, recurrent bacterial sinopulmonary infections are prominent features of IMD109, suggesting that exposure to common respiratory pathogens (e.g., Streptococcus pneumoniae, Haemophilus influenzae) contributes to morbidity, though these infections are more a consequence of immunodeficiency than a cause of the underlying disorder.[10][14][18] Lifestyle or occupational exposures have not been systematically evaluated in this rare condition, but standard considerations such as smoking, air pollution, and crowding are likely to influence infection risk and severity in affected individuals, as they do in other immunodeficiencies.

Consanguinity is an important contextual risk factor at the family level. All early reported families with TNFRSF9 pathogenic variants were consanguineous, reflecting the increased probability of homozygosity for rare recessive alleles in such populations.[14][16][10] While consanguinity is not a direct cause of the disease, it is a well-recognized demographic risk factor for autosomal recessive disorders and is particularly relevant for genetic counseling and carrier screening in communities where consanguineous marriage is common.

### 2.4 Protective Factors and Gene–Environment Interactions

Because TNFRSF9-related immunodeficiency is defined by a clear monogenic etiology, genuine protective factors that prevent disease in homozygous mutation carriers are not currently documented. Heterozygous carriers appear asymptomatic, suggesting that one functional TNFRSF9 allele suffices to maintain adequate CD137-mediated costimulation, but this is simply the normal heterozygous state rather than a protective modifier.[14][16] Among affected individuals, however, variability in clinical course—ranging from severe EBV-driven lymphoma to more indolent chronic EBV viremia—indicates that other genetic or environmental factors modulate disease expression.

Potential protective environmental factors include aggressive infection prevention and early treatment, such as vaccination against common respiratory pathogens and avoidance of excessive viral exposures, although EBV infection is nearly universal and currently lacks a licensed vaccine. Immunoglobulin replacement therapy and prophylactic antimicrobials can reduce the burden of infections and may indirectly protect against EBV-driven lymphomagenesis by decreasing inflammatory stimuli that promote lymphocyte expansion.[10][14][18] Hematopoietic stem cell transplantation (HSCT) has been used in some patients and appears curative, representing a therapeutic intervention that effectively eliminates the underlying immunodeficiency and thereby protects against future EBV-driven lymphoproliferation.[10][14]

The gene–environment interaction at the heart of IMD109 can be conceptualized as follows: biallelic loss-of-function mutations in TNFRSF9 result in defective CD137 expression and signaling on activated T cells, which in turn leads to impaired CD8+ T‑cell expansion, cytotoxicity, and mitochondrial function. Upon exposure to EBV, these defective T cells fail to control viral infection and elimination of EBV-infected cells, allowing persistent viremia and expansion of infected lymphocytes that eventually culminate in lymphoproliferative disease and lymphoma.[12][14][15][18] This causal chain underscores the synergy between a monogenic defect and a ubiquitous viral pathogen, analogous to other EBV-associated inborn errors of immunity such as deficiencies of perforin, MAGT1, or CD27. It also highlights how environmental factors—timing and intensity of EBV exposure, co-infections, and immunomodulatory therapies—interact with TNFRSF9 genotype to shape disease trajectory.

From an ontology standpoint, this interplay can be annotated with GO biological process terms such as *T cell costimulation*, *positive regulation of T cell proliferation*, and *response to virus*, along with CHEBI entities representing EBV-related viral components and host cytokines involved in the response. While formal gene–environment databases have not yet cataloged IMD109, emerging frameworks for inborn errors of immunity increasingly emphasize the integration of genomic, immunologic, and environmental data to fully capture disease etiology.

## 3. Phenotypes

### 3.1 Core Immunologic and Infectious Phenotypes

The core phenotype of TNFRSF9-related immunodeficiency involves a combination of recurrent infections, particularly of the sinopulmonary tract, and profound but selective susceptibility to Epstein–Barr virus infection and associated lymphoproliferation, against a backdrop of numerically normal lymphocyte counts but impaired T‑cell function.[12][14][18][19] MedGen and OMIM both emphasize that IMD109 is characterized by onset of recurrent sinopulmonary infections in childhood, with affected individuals experiencing repeated episodes of otitis media, sinusitis, bronchitis, and pneumonia leading to chronic lung complications such as bronchiectasis.[18][19][16] In the case series by Alosaimi et al., both patients had recurrent sinopulmonary infections beginning around age three, with one developing bronchiectasis and ultimately severe EBV-associated lymphoproliferative disease.[14][10] The recent case report and literature review by Osman similarly describes “recurrent sinopulmonary infections, persistent EBV viremia, and EBV-driven lymphoproliferation,” aligning well with the canonical phenotype.[10]

These recurrent infections can be captured by HPO terms such as *Recurrent respiratory infections* (HP:0002205), *Recurrent sinusitis* (HP:0000246), *Recurrent otitis media* (HP:0004459), and *Bronchiectasis* (HP:0002110). Hypogammaglobulinemia, often noted in laboratory evaluations, corresponds to *Hypogammaglobulinemia* (HP:0004313) and is associated with recurrent bacterial infections, though B‑cell numbers are typically normal.[10][14][18] Immunologic workups in reported patients show normal absolute counts of CD4+ and CD8+ T cells, B cells, and NK cells, but functional assays reveal defective proliferation and cytotoxic responses, particularly in CD8+ T cells after stimulation, mapping to HPO terms such as *Abnormal T-cell activation* and *Impaired cytotoxic T-cell function*.[12][14][18]

EBV-related phenotypes are central to TNFRSF9-related immunodeficiency. Persistent high-level EBV viremia, recurrent EBV infections, and EBV-induced lymphoproliferative disease can be reasonably associated with HPO terms *Recurrent viral infections* (HP:0004429), *Severe viral infection* (HP:0005428), and *Epstein–Barr virus infection*, though the latter is currently captured via disease ontologies rather than a standalone HPO term.[18][19][13] Clinical manifestations include fever, lymphadenopathy, hepatosplenomegaly, cytopenias, and in some cases hemophagocytic lymphohistiocytosis, reflecting multi-organ involvement downstream of immune dysregulation.[10][12][14] These features substantially impact quality of life by causing chronic fatigue, reduced exercise tolerance, frequent hospitalizations, and prolonged treatment courses, often during key developmental years.

### 3.2 Lymphoproliferative and Malignant Phenotypes

A hallmark of TNFRSF9-related immunodeficiency is the predisposition to EBV-associated lymphoproliferative disease and lymphoma, often at an early age.[9][12][14][10][18] Somekh et al. investigated four patients from unrelated families presenting with immunodeficiency, autoimmunity, and malignancy, and reported that “Patients 1 and 3 developed EBV-related B-cell lymphoma, patient 2 had an autoimmune lymphoproliferative syndrome–like phenotype, and patient 4 was diagnosed as having common variable immune deficiency.”[9][12] Alosaimi et al. described EBV-positive B-cell lymphoproliferative disease with hemophagocytic lymphohistiocytosis in one patient, and EBV-induced lymphoproliferation in another.[14][16][10] Osman’s case report documents severe EBV-associated lymphoproliferative disease, reinforcing that lymphoid malignancy is a frequent and severe outcome.[10]

These clinical manifestations align with HPO terms such as *Lymphadenopathy* (HP:0002716), *Splenomegaly* (HP:0001744), *Hepatomegaly* (HP:0002240), *B-cell lymphoma* (HP:0002899), and *Autoimmune lymphoproliferative syndrome* (HP:0005261). In some cases, classic Hodgkin lymphoma has been reported, reflecting a germinal center B‑cell malignancy characterized by Reed–Sternberg cells, which MedGen notes as a possible associated neoplastic process in the broader context of EBV-associated lymphomas.[19] The temporal relationship between EBV viremia and lymphomagenesis suggests that uncontrolled EBV infection acts as a chronic antigenic stimulus driving expansion of susceptible B‑cell clones, which, in the absence of effective CD8+ T‑cell surveillance, accumulate genetic and epigenetic changes culminating in malignant transformation.[12][14][15]

The severity of lymphoproliferative disease varies. Some patients have localized lymphadenopathy and reversible lymphoid expansions responsive to therapies such as rituximab (anti-CD20) and antiviral measures.[10][14] Others develop aggressive lymphomas requiring intensive chemotherapy and HSCT, with risks of treatment-related morbidity and mortality.[10][14][12] Quality of life is markedly compromised by these malignancies, with prolonged hospitalizations, systemic symptoms such as weight loss and night sweats, and psychological distress. From a disease-ontology perspective, the association between IMD109 and specific lymphoma subtypes can be annotated using NCIT terms such as “B-cell Non-Hodgkin Lymphoma” and “Hodgkin Lymphoma,” allowing linkage to cancer databases and prognostic models.

### 3.3 Autoimmune, Immunoregulatory, and Systemic Phenotypes

Beyond infection and malignancy, TNFRSF9-related immunodeficiency encompasses autoimmune and immunoregulatory abnormalities. Somekh et al. describe a patient with an autoimmune lymphoproliferative syndrome–like phenotype, including autoimmune cytopenias and expanded double-negative T cells, reminiscent of FAS pathway deficiency but mechanistically distinct.[9][12] This suggests that CD137 signaling contributes to immune homeostasis, including regulatory T‑cell function and peripheral tolerance, such that its absence predisposes to autoimmunity. Alosaimi et al. also reported autoimmune features in the context of EBV-induced lymphoproliferation.[14][16][10] These observations correspond to broader HPO terms such as *Autoimmunity* (HP:0002960), *Autoimmune cytopenia*, and *Immune dysregulation*.

In addition, some patients have laboratory evidence of hypogammaglobulinemia and impaired vaccine responses, leading to a clinical diagnosis of common variable immunodeficiency (CVID)-like disease.[9][12][10] Thus, IMD109 can present primarily as a humoral immunodeficiency, with EBV susceptibility emerging later, or as a combined immunodeficiency with both cellular and humoral components. Fatigue, failure to thrive, and growth delay may occur due to chronic infection and inflammation, impacting daily functioning and psychosocial well-being.

From a quality-of-life perspective, recurrent infections, chronic EBV viremia, and lymphoproliferative disease contribute to substantial limitations in physical functioning, social participation, and emotional health. Instruments such as the SF‑36 and EQ‑5D, if applied, would likely show marked impairment across domains of physical functioning, vitality, and general health perception. Formal quality-of-life studies have not yet been published for this ultra-rare condition, but extrapolation from similar immunodeficiencies suggests a significant burden, especially in the absence of definitive treatments such as HSCT.

### 3.4 Phenotype Onset, Severity, Progression, and Frequency

IMD109 is typically a pediatric-onset disease. MedGen specifies “onset of recurrent sinopulmonary infections in childhood,” and clinical reports indicate symptom onset in early childhood (around ages 2–5), with EBV-related complications emerging in later childhood or adolescence.[18][19][14][10][12] Severity ranges from moderate recurrent infections with manageable EBV viremia to severe, life-threatening lymphoproliferative disease and malignancy. In Alosaimi’s cohort, one patient developed bronchiectasis, pneumococcal septicemia, and EBV-induced lymphoproliferation with hemophagocytic lymphohistiocytosis, illustrating the severe end of the spectrum.[10][14] Somekh’s patients included both lymphoma cases and CVID-like phenotypes, suggesting heterogeneity in disease expression.[9][12]

Symptom progression is generally chronic and progressive rather than self-limited. Recurrent infections tend to accumulate structural damage, particularly in the lungs, while EBV viremia, once established, often persists or recurs despite conventional antiviral therapy.[10][14][12] Lymphoproliferative manifestations may appear episodically but can evolve into chronic or malignant disease. Without definitive intervention, the disease course is likely lifelong and associated with substantial morbidity. Because only nine patients have been reported to date,[11] precise frequency estimates for individual phenotypes are limited, but recurrent infections and EBV susceptibility appear universal, while lymphoma and autoimmune features occur in a substantial subset.

Overall, the phenotype profile of TNFRSF9-related immunodeficiency integrates recurrent bacterial infections, EBV-induced lymphoproliferative disease and lymphoma, autoimmune manifestations, and humoral immunodeficiency, all downstream of a core defect in CD137-mediated T‑cell costimulation. These features can be systematically mapped to HPO terms and linked to ontology-based representations of immune dysregulation and inborn errors of immunity, providing a structured foundation for knowledge-base integration.

## 4. Genetic and Molecular Information

### 4.1 The Causal Gene TNFRSF9: Structure, Function, and Expression

TNFRSF9 (TNF receptor superfamily member 9) is a protein-coding gene located on chromosome 1 in humans, corresponding to 1p36.23 in cytogenetic notation.[3][16][6] NCBI Gene describes TNFRSF9 as encoding a member of the TNF receptor superfamily whose protein contributes to the clonal expansion, survival, and development of T cells.[3] The receptor is known by several alternative names, including CD137, 4‑1BB, and ILA, reflecting its discovery as an activation-induced T‑cell surface antigen and costimulatory molecule.[4][15] Structurally, CD137 is a type I membrane glycoprotein with an extracellular domain containing multiple cysteine-rich repeats characteristic of TNF receptor family members, a transmembrane region, and a cytoplasmic tail that interacts with TNF receptor-associated factors (TRAFs) to mediate downstream signaling.[15]

TNFRSF9 expression is largely restricted to activated immune cells. In T cells, CD137 is upregulated upon T‑cell receptor (TCR) engagement and provides a secondary, costimulatory signal that enhances proliferation, survival, cytokine production (e.g., interferon‑γ), and cytotoxicity, particularly in CD8+ T cells.[15][12][17] The ligand for CD137, 4‑1BBL (TNFSF9), is expressed on activated antigen-presenting cells such as dendritic cells, macrophages, and B cells, where it binds CD137 on activated T cells to deliver costimulatory signals.[17] Studies of 4‑1BBL-deficient mice and mice lacking both 4‑1BBL and CD28 reveal that 4‑1BBL plays an important role in skin allograft rejection and cytotoxic T‑cell responses to influenza virus, particularly when CD28 signals are absent or suboptimal, underscoring the redundancy and specialization of costimulatory pathways.[17]

Beyond T cells, CD137 is expressed on activated B cells and NK cells, suggesting broader roles in immune regulation and effector functions.[12] Engagement of CD137 has biphasic effects, enhancing effector responses in some contexts while promoting survival and memory formation in others. In cancer immunotherapy, agonistic antibodies targeting CD137 have been used to boost antitumor T‑cell responses, demonstrating the receptor’s central role in immune activation and highlighting the potential consequences of its deficiency.[12][15] At the molecular level, CD137 signaling activates NF‑κB, MAPK, and PI3K–AKT pathways, promotes mitochondrial biogenesis and function in T cells, and upregulates anti-apoptotic molecules, collectively supporting robust effector activity and long-term persistence.[12][15]

In experimental models, TNFRSF9 has orthologs in other species, including mice (Tnfrsf9, Gene ID 21942) and rats (Tnfrsf9, Gene ID 500590).[1][2][7] These orthologs share similar structure and function, and their manipulation in knockout models provides important insights into CD137 biology and its role in antiviral responses and allograft rejection.[17][1][2] Such comparative data reinforce the evolutionary conservation of TNFRSF9’s function and its likely essential role in immune defense against pathogens like EBV.

### 4.2 Pathogenic Variants: Types, Classification, and Functional Consequences

All known pathogenic TNFRSF9 variants causing IMD109 are homozygous germline mutations with loss-of-function effects that abolish or severely reduce CD137 expression and signaling.[14][12][10][11][16] The initial variant described by Alosaimi et al., c.325G>A (p.Gly109Ser), is a missense mutation in the extracellular domain that disrupts folding or ligand binding, leading to absent 4‑1BB surface expression and inability to bind 4‑1BBL.[14][16][10] In vitro studies showed complete loss of protein expression and ligand binding, confirming a null-like functional impact.[14] OMIM catalogs this variant as a pathogenic missense mutation associated with Immunodeficiency 109 with EBV-induced lymphoproliferation.[16]

Somekh et al. reported four distinct homozygous TNFRSF9 variants in four unrelated patients, including missense and frameshift mutations.[9][12] All mutations resulted in markedly reduced or abrogated expression of CD137 on activated T, B, and NK cells, consistent with severe loss of function.[12] The Blood article notes: “We identified 4 distinct homozygous mutations in TNFRSF9 encoding the tumor necrosis factor receptor superfamily member CD137/4-1BB, leading to reduced, or loss of, protein expression. Lymphocytic responses crucial for immune surveillance, including activation, proliferation, and differentiation, were impaired. Genetic reconstitution of CD137 reversed these defects.”[9][12] This provides strong functional evidence, including rescue experiments, supporting the pathogenic classification of these variants.

The literature review by Osman and the subsequent report on a novel TNFRSF9 variant add further examples of pathogenic mutations, emphasizing that all reported variants are classified as pathogenic or likely pathogenic under ACMG/AMP guidelines, based on segregation with disease in consanguineous families, absence or extremely low frequency in population databases, predicted deleterious effect on protein structure or function, and direct functional evidence in patient cells.[10][11] No variants have been reported as gain-of-function or dominant-negative; the disease mechanism appears uniformly loss-of-function and recessive. ClinVar and similar variant databases, though not directly listed in the search results, likely categorize these variants accordingly.

Allele frequencies in population databases such as gnomAD have not been specifically described for IMD109-causing variants in the available sources, but given the rarity of the disease and apparent geographic clustering, it is reasonable to infer that these pathogenic alleles are extremely rare (minor allele frequency far below 0.01%) and may represent private or family-specific mutations.[11][16] In consanguineous families, homozygosity arises from shared ancestry rather than high population frequency. Somatic TNFRSF9 mutations have not been implicated in IMD109, although somatic alterations in CD137-related pathways may influence cancer immunotherapy responses.

Functionally, the consequences of TNFRSF9 mutations can be summarized as **abolition of CD137 protein expression**, **loss of ligand binding**, **defective T‑cell costimulation**, **impaired CD8+ T‑cell expansion**, **reduced IFN‑γ and perforin expression**, **diminished cytotoxicity against EBV-infected targets**, and **markedly reduced mitochondrial biogenesis, membrane potential, and function in activated T cells**.[12][14][15] These cellular and molecular defects translate directly into the clinical phenotype of immunodeficiency and EBV-induced lymphoproliferation. In knowledge-base terms, these effects can be annotated with GO processes such as *T cell activation*, *positive regulation of T cell proliferation*, *cytotoxic T-cell mediated immunity*, and *mitochondrial organization*, as well as NCIT terms for “Immune Checkpoint” and “Costimulatory Receptor.”

### 4.3 Modifier Genes and Epigenetic Information

As noted above, combined deficiency of PIK3CD and TNFRSF9 has been reported in at least one patient with chronic active EBV infection of T cells, suggesting that PIK3CD (encoding the p110δ catalytic subunit of PI3Kδ) may act as a modifier gene in the context of CD137 deficiency.[15] In this case, the interplay between PI3Kδ signaling and CD137 costimulation complicates attribution of specific phenotypic features to each gene, and Affinage remarks that “Genetic interaction with PIK3CD not fully separated in all cases,” highlighting an open question for future research.[15] Beyond PIK3CD, no additional modifier genes have been conclusively identified, though other components of the CD137 signaling pathway—TRAFs, NF‑κB subunits, mitochondrial regulators—are plausible candidates.

Epigenetic information specifically relating to TNFRSF9-related immunodeficiency is not yet available. However, EBV infection itself induces significant epigenetic changes in host B cells and other lymphocytes, including DNA methylation and histone modifications affecting genes involved in proliferation, apoptosis, and immune recognition. In the context of IMD109, such EBV-driven epigenetic alterations may synergize with CD137 deficiency to promote lymphomagenesis, but this remains speculative. Large-scale epigenomic projects such as ENCODE and Roadmap Epigenomics have characterized TNFRSF9 regulatory elements in normal immune cells, but disease-specific epigenomic signatures for CD137 deficiency have not been reported in the literature captured by current search results.

### 4.4 Chromosomal Abnormalities and Structural Genomics

TNFRSF9 is located at 1p36.23, a region that has been implicated in various structural abnormalities and tumor suppressor gene deletions in other diseases, but no recurrent chromosomal rearrangements involving TNFRSF9 have been described in IMD109.[16][18][3] The disease is caused by intragenic point mutations or small indels rather than large-scale deletions, translocations, or inversions. Chromosomal microarray or karyotyping are not expected to reveal TNFRSF9 abnormalities in affected individuals, and diagnosis relies on sequence-level analysis (e.g., whole-exome sequencing).

The NCBI Genome Data Viewer provides genomic context for TNFRSF9, including its location and neighboring genes on chromosome 1, but structural features such as copy number variants or balanced translocations are not part of the disease mechanism in IMD109.[6] This distinguishes TNFRSF9-related immunodeficiency from syndromes involving 1p36 deletions, which have distinct phenotypes and gene content.

In summary, the genetic and molecular landscape of TNFRSF9-related immunodeficiency is well-defined at the level of causative variants and functional consequences, but relatively unexplored regarding modifier genes, epigenetic changes, and structural genomics. Future multi-omics studies integrating transcriptomics, proteomics, and epigenomics in patient cells may reveal additional mechanistic layers and potential therapeutic targets.

## 5. Environmental Information

### 5.1 Environmental and Lifestyle Factors

As a monogenic primary immunodeficiency, TNFRSF9-related immunodeficiency owes its fundamental cause to germline genetic variation rather than environmental exposures. However, environmental factors influence disease expression, severity, and complications. Recurrent bacterial sinopulmonary infections, often with encapsulated organisms such as Streptococcus pneumoniae, are major contributors to morbidity, leading to bronchiectasis and chronic lung disease.[10][14][18] Lifestyle factors such as exposure to tobacco smoke, air pollution, and occupational respiratory irritants may exacerbate these infections, although such associations have not been systematically studied in the small patient cohorts.

Nutritional status and general health behaviors likely modulate infection resilience. Adequate nutrition, good hygiene, and avoidance of crowded, high-exposure environments may reduce infection frequency, while malnutrition and poor living conditions may worsen outcomes. In the context of EBV, the timing and intensity of exposure—often through close contact with saliva—are important environmental variables, but since EBV infection is nearly universal, these factors primarily influence age at primary infection rather than overall risk.

### 5.2 Infectious Agents: EBV and Beyond

Epstein–Barr virus is the central infectious agent in TNFRSF9-related immunodeficiency, functioning both as a trigger of symptomatic disease and a driver of lymphomagenesis. Somekh et al. explicitly state: “CD137 deficiency is a novel inborn error of immunity with immune dysregulation and EBV-associated lymphomagenesis.”[12] In their cohort, EBV viremia, EBV-related B‑cell lymphoma, and EBV-driven immune dysregulation were common. Alosaimi et al. likewise describe EBV viremia and EBV-induced lymphoproliferation in patients with 4‑1BB deficiency.[14][16][10] MedGen and Orphanet emphasize EBV-induced lymphoproliferative disease as a defining feature of IMD109.[18][19][13]

In addition to EBV, other pathogens may contribute to disease complications. Recurrent bacterial infections are prominent, and viral infections such as influenza may pose increased risks due to impaired T‑cell responses. However, there is no evidence that TNFRSF9-related immunodeficiency confers susceptibility to a broad range of pathogens comparable to severe combined immunodeficiency; rather, EBV stands out as the key pathogen whose control is particularly dependent on CD137-mediated CD8+ T‑cell responses.[12][15][17]

From an ontology perspective, EBV can be annotated as an NCBI Taxonomy entity (Human gammaherpesvirus 4) and associated with CHEBI representations of viral components where relevant. The interaction between EBV and host immune pathways, particularly CD137, can be captured by GO terms related to response to virus, regulation of lymphocyte proliferation, and immune effector processes.

### 5.3 Gene–Environment Interactions in Immunopathogenesis

The interaction between TNFRSF9 genotype and EBV exposure exemplifies a classic gene–environment interaction. In individuals with normal CD137 function, EBV infection is typically controlled by robust CD8+ T‑cell responses, leading to asymptomatic latency or mild infectious mononucleosis. In TNFRSF9-deficient individuals, defective CD137 signaling impairs CD8+ T‑cell expansion, cytotoxicity, and memory formation, resulting in failure to contain EBV-infected cells and persistent viremia.[12][14][15] This failure of immune surveillance allows EBV-infected B cells (or T/NK cells) to expand, accumulate mutations, and progress to lymphoproliferative disease and lymphoma.[12][14][10]

These interactions can be modeled as a causal chain in which environmental exposure (EBV infection) acts on a genetically predisposed host (TNFRSF9 deficiency) to produce disease manifestations (lymphoproliferation and lymphoma). Such models are increasingly used in immunology and precision medicine to conceptualize the interplay of monogenic defects and ubiquitous pathogens. Ontologically, this scenario can be represented by linking MONDO:0859526 to EBV-related disease concepts and GO processes mediating antiviral immunity, providing a structured framework for knowledge-base integration.

## 6. Mechanism / Pathophysiology

### 6.1 Ordered Causal Chain from Mutation to Clinical Manifestation

Step 1. Biallelic germline loss-of-function mutations in TNFRSF9 lead to absent or severely reduced expression of the CD137/4‑1BB receptor on activated T cells, B cells, and NK cells.[12][14][16]

Step 2. Loss of functional CD137 results in defective costimulatory signaling via the CD137–4‑1BBL pathway, leading to impaired activation, clonal expansion, survival, and effector differentiation of CD8+ T cells following antigenic stimulation; this is demonstrated by reduced proliferation, IFN‑γ and perforin expression, cytotoxicity, and mitochondrial biogenesis in patient T cells.[12][14][15]

Step 3. Impaired CD8+ T‑cell responses lead to failure of immune surveillance against Epstein–Barr virus-infected B cells and other lymphocytes, resulting in persistent EBV viremia and accumulation of EBV-infected lymphoid cells; this is strongly supported by human clinical data and in vitro functional assays.[12][14][18]

Step 4. Persistent EBV infection and uncontrolled expansion of infected lymphocytes result in chronic immune activation, lymphadenopathy, hepatosplenomegaly, and EBV-induced lymphoproliferative disease, with some clones acquiring additional genetic and epigenetic changes that culminate in B‑cell lymphoma or Hodgkin lymphoma; this step is inferred from clinical correlations and known EBV oncogenesis mechanisms.[12][14][10][19]

Step 5. Defective CD137 signaling also perturbs B‑cell activation and differentiation, contributing to hypogammaglobulinemia and CVID-like humoral immunodeficiency, which in turn predisposes to recurrent bacterial sinopulmonary infections and chronic lung damage such as bronchiectasis.[9][12][10][18]

Step 6. Broader immune dysregulation arising from CD137 deficiency, including impaired regulatory mechanisms and abnormal lymphocyte homeostasis, leads to autoimmune phenomena such as autoimmune cytopenias and autoimmune lymphoproliferative syndrome–like features; this step is supported by clinical observations but mechanistically inferred.[9][12]

Step 7. The combination of recurrent infections, chronic EBV viremia, lymphoproliferative disease, malignancy, and autoimmunity produces the full clinical phenotype of TNFRSF9-related immunodeficiency, encompassing substantial morbidity, potential mortality, and reduced quality of life, which may be ameliorated or reversed by HSCT that restores normal immune function.[10][14][12]

### 6.2 Molecular Pathways: CD137–4‑1BBL Costimulation and Downstream Signaling

At the molecular level, TNFRSF9 encodes CD137, an activation-inducible TNF receptor superfamily member that functions as a costimulatory receptor on T cells.[3][15] Upon TCR engagement and antigen recognition, CD137 is upregulated on the surface of CD4+ and CD8+ T cells. Its ligand, 4‑1BBL (TNFSF9), is expressed on activated antigen-presenting cells, including dendritic cells, macrophages, and B cells.[17] The engagement of CD137 by 4‑1BBL provides a second signal that synergizes with TCR signaling to enhance T‑cell activation, proliferation, survival, and effector functions, particularly in cytotoxic CD8+ T cells.[15][17]

CD137 signaling recruits TNF receptor-associated factors (TRAFs) to its cytoplasmic tail, activating downstream pathways such as NF‑κB, MAPK (including ERK and p38), and PI3K–AKT.[15] These pathways induce transcription of genes involved in cytokine production (e.g., IFN‑γ, TNF‑α), cytotoxic effector molecules (e.g., perforin, granzymes), survival and anti-apoptotic proteins (e.g., Bcl‑xL), and metabolic regulators that support mitochondrial biogenesis and oxidative phosphorylation.[12][15] The net effect is robust expansion and functional maturation of CD8+ T cells capable of eliminating infected or malignant cells.

In TNFRSF9-related immunodeficiency, the absence or severe reduction of CD137 abrogates these signaling cascades. Somekh et al. show that patient CD8+ T cells have markedly reduced proliferation, diminished IFN‑γ and perforin expression, impaired cytotoxicity against EBV-transformed B cells, and significantly reduced mitochondrial biogenesis, membrane potential, and function upon activation.[12][15] Genetic reconstitution of CD137 in patient cells restores these functions, confirming that the observed defects are due to loss of CD137 signaling.[12] Thus, key GO biological process terms impacted include *T cell activation*, *positive regulation of T cell proliferation*, *cytotoxic T-cell mediated immunity*, *regulation of cytokine production*, and *mitochondrial organization*.

The CD137–4‑1BBL pathway also interacts with other costimulatory systems, such as CD28 and OX40. Studies in mice lacking 4‑1BBL and CD28 indicate that 4‑1BBL can compensate for CD28 deficiency in certain cytotoxic responses, particularly to influenza virus, and that different immune responses vary in their dependence on costimulation.[17] In IMD109, the loss of CD137 removes a critical costimulatory axis, leaving T cells reliant on other pathways that may be insufficient to control EBV, a virus that particularly challenges cytotoxic T‑cell function.

### 6.3 Cellular Processes: CD8+ T‑cell Dysfunction, B‑cell Defects, and Immune Dysregulation

At the cellular level, the principal defect in TNFRSF9-related immunodeficiency is CD8+ T‑cell dysfunction. Patient CD8+ T cells demonstrate impaired expansion upon activation, reduced expression of key effector molecules such as IFN‑γ and perforin, diminished cytotoxicity against EBV-infected cells, and defective mitochondrial function.[12][14][15] These abnormalities involve multiple cellular processes, including cell cycle progression, apoptosis regulation, mitochondrial biogenesis, and effector differentiation. GO terms such as *cell proliferation*, *apoptotic process*, *mitochondrion organization*, and *T-cell mediated cytotoxicity* are directly relevant.

CD137 deficiency also impacts B‑cell biology. Some patients exhibit hypogammaglobulinemia and impaired antibody responses to vaccines, suggesting defective B‑cell activation, class-switch recombination, or long-lived plasma cell formation.[9][12][10] CD137 is expressed on activated B cells, and its signaling may influence B‑cell survival and differentiation, although the precise mechanisms are less well characterized than in T cells. Nevertheless, the clinical phenotype of CVID-like humoral immunodeficiency indicates that B‑cell processes such as germinal center reactions, somatic hypermutation, and plasma cell differentiation are disturbed in IMD109.

Immune dysregulation extends beyond effector cells. Somekh et al. describe autoimmune lymphoproliferative syndrome–like features, implying abnormalities in lymphocyte homeostasis, regulatory T‑cell function, or peripheral tolerance.[9][12] CD137 signaling may contribute to the survival and function of regulatory T cells or other immunoregulatory populations, and its loss could tilt the balance toward autoimmunity. NK cells, which also express CD137, may be affected, potentially contributing to impaired control of viral infections and malignant cells. Collectively, these cellular defects define an immunological landscape marked by reduced antiviral cytotoxicity, impaired humoral immunity, and aberrant immune regulation.

### 6.4 Protein Dysfunction: Loss of CD137 Expression and Function

The protein-level dysfunction in TNFRSF9-related immunodeficiency is straightforward: pathogenic mutations abolish or severely reduce CD137 expression and function.[14][12][10][11] Missense mutations in the extracellular domain, such as G109S, disrupt protein folding or ligand-binding sites, preventing proper surface expression.[14][16][10] Frameshift or nonsense mutations elsewhere in the gene can lead to truncated proteins subject to nonsense-mediated decay or incapable of signaling. In all cases, flow cytometry demonstrates absent or markedly reduced CD137 expression on activated T cells, B cells, and NK cells.[12][14][10][11]

Without functional CD137, the receptor cannot bind 4‑1BBL, and downstream signaling events are not initiated. This represents a classic loss-of-function scenario affecting a cell-surface receptor, akin to other TNF receptor family deficiencies (e.g., CD27 deficiency). There is no evidence of dominant-negative effects, as heterozygous carriers with one functional allele are asymptomatic. Thus, the disease mechanism at the protein level is best described as **biallelic loss-of-function of CD137**, leading to **loss of a critical costimulatory signal in T cells**.

### 6.5 Metabolic Changes: Mitochondrial Dysfunction in Activated T Cells

One particularly novel aspect of CD137 deficiency highlighted by Somekh et al. and summarized in Affinage is the role of CD137 signaling in mitochondrial biogenesis and function in activated T cells.[12][15] In CD137-deficient patient cells, activated CD8+ T cells show significantly reduced mitochondrial biogenesis, membrane potential, and respiratory function, which correlates with impaired effector responses. These findings indicate that CD137 costimulation not only amplifies classic signaling pathways but also supports the metabolic reprogramming necessary for sustained T‑cell proliferation and cytotoxic activity.

Metabolic changes in CD137-deficient T cells thus include reduced oxidative phosphorylation capacity, diminished mitochondrial mass, and impaired mitochondrial membrane potential, leading to energy deficits that compromise effector functions. GO terms such as *mitochondrial biogenesis*, *oxidative phosphorylation*, and *regulation of membrane potential* capture these processes. Metabolomics studies have not yet been performed in IMD109, but one would predict alterations in ATP production, reactive oxygen species, and metabolic intermediates related to mitochondrial pathways.

### 6.6 Immune System Involvement and Tissue Damage Mechanisms

The immune system involvement in TNFRSF9-related immunodeficiency is multifaceted. CD8+ T‑cell defects lead to failure of antiviral immunity, particularly against EBV, causing chronic infection and systemic immune activation.[12][14][18] B‑cell abnormalities result in hypogammaglobulinemia and recurrent bacterial infections.[9][10][18] NK cell dysfunction may further impair innate antiviral responses. Autoimmune phenomena reflect dysregulated immune regulation and peripheral tolerance.[9][12]

Tissue damage mechanisms downstream of these immune defects include direct viral cytopathic effects, collateral tissue injury from chronic inflammation, and structural damage from recurrent infections. In the lungs, repeated bacterial pneumonias lead to bronchiectasis, with destruction of airway architecture and impaired mucus clearance, contributing to chronic respiratory symptoms.[10][14] In the liver and spleen, EBV-driven lymphoid infiltrates cause hepatosplenomegaly and disruption of normal organ function.[10][12][19] In lymph nodes and other lymphoid tissues, lymphoproliferative disease and lymphoma lead to architectural distortion, mass effects, and systemic symptoms such as fever, weight loss, and night sweats.

Oxidative stress, necrosis, apoptosis, and fibrosis likely contribute to tissue damage, though specific mechanistic studies have not yet been reported for IMD109. These processes can be annotated with GO terms such as *inflammatory response*, *fibrosis*, *cell death*, and *response to oxidative stress*. The interplay between immune deficiency and tissue damage underscores the importance of early diagnosis and intervention to preserve organ function.

### 6.7 Molecular Profiling and Advanced Technologies

While the number of IMD109 patients is small, the mechanistic studies performed in available cohorts exemplify the use of advanced technologies. Somekh et al. used whole-exome sequencing to identify TNFRSF9 mutations, flow cytometry to analyze CD137 expression and lymphocyte subsets, in vitro cytotoxicity assays to measure EBV-specific T‑cell function, mitochondrial function assays to assess biogenesis and membrane potential, and genetic reconstitution experiments to restore CD137 expression and test causality.[12][15] These approaches integrate genomics, immunophenotyping, functional assays, and metabolic profiling, constituting a multi-omics perspective even if not formally labeled as such.

Other reports used whole-exome sequencing and immunologic workups to identify and characterize TNFRSF9-deficient patients, demonstrating the utility of high-throughput sequencing for diagnosing ultra-rare inborn errors of immunity.[14][10][11][16] Transcriptomic, proteomic, and epigenomic analyses specific to IMD109 have not yet been published, but the methodologies employed in related conditions suggest that future studies could reveal additional layers of dysregulation.

Single-cell analysis, spatial transcriptomics, and functional genomics screens (e.g., CRISPR) have not been specifically applied to TNFRSF9 deficiency in humans, but CRISPR-based screens in model systems have implicated CD137 pathways in T‑cell activation and exhaustion, with relevance to cancer immunotherapy. Such data, while not disease-specific, provide broader context for understanding CD137 biology and potential therapeutic interventions.

Collectively, the mechanistic evidence for TNFRSF9-related immunodeficiency comes primarily from human clinical and cellular studies, complemented by mouse models of 4‑1BB and 4‑1BBL deficiency, and relies on cutting-edge genomic and immunologic technologies that underscore the disease’s status as a paradigmatic inborn error of immunity affecting a costimulatory receptor.

## 7. Anatomical Structures Affected

### 7.1 Organ-Level Involvement

The primary organs affected in TNFRSF9-related immunodeficiency are those of the immune and lymphoid systems, particularly lymph nodes, spleen, and bone marrow, where EBV-infected lymphocytes accumulate and lymphoproliferative disease arises.[10][12][19] Hepatomegaly and splenomegaly are common, reflecting infiltration by lymphoid cells and EBV-driven proliferation.[10][12][18] Lymphadenopathy involves multiple nodal stations, including cervical, mediastinal, abdominal, and peripheral nodes, and can lead to compressive symptoms and cosmetic concerns.[10][12]

The respiratory system is also significantly affected, especially the lungs and airways. Recurrent sinopulmonary infections lead to bronchiectasis and chronic lung disease, involving the bronchi, bronchioles, and parenchyma.[10][14][18] Uberon terms such as *lung*, *bronchus*, and *upper respiratory tract* are relevant for anatomical mapping. The liver, as a site of EBV latency and lymphoid infiltration, exhibits hepatomegaly and abnormal function in some patients.[10][12][19] Bone marrow may show reactive changes or infiltration by lymphoma cells, impacting hematopoiesis and contributing to cytopenias.

Secondary organ involvement includes the nervous system (in cases of CNS lymphoma or inflammatory complications), gastrointestinal tract (due to lymphoma or infections), and cardiovascular system (affected indirectly by systemic inflammation and anemia). However, the core anatomical focus remains the lymphoid and respiratory systems.

### 7.2 Tissue and Cell-Level Involvement

At the tissue level, IMD109 affects lymphoid tissue, including secondary lymphoid organs such as lymph nodes and spleen, and mucosa-associated lymphoid tissue in the respiratory tract.[10][12][19] The affected cell populations include CD8+ T cells, CD4+ T cells, B cells, and NK cells, all of which express CD137 upon activation and participate in immune responses to EBV and other pathogens.[12][14][15] Cell Ontology terms such as *CD8-positive, alpha-beta T cell*, *B cell*, and *natural killer cell* are directly relevant.

Within lymphoid tissues, germinal center B cells, memory B cells, and plasma cells are involved, given the humoral immunodeficiency and lymphoma risk. Germinal center reactions may be abnormal, leading to faulty selection and survival of B‑cell clones. In the respiratory tract, epithelial cells and underlying lymphoid structures are subject to frequent infection and inflammation, causing tissue damage and remodeling.

Subcellularly, mitochondria in activated T cells are key compartments affected in CD137 deficiency, as described in functional assays showing impaired mitochondrial biogenesis and function.[12][15] GO cellular component terms such as *mitochondrion*, *mitochondrial inner membrane*, and *immunological synapse* can be used to annotate these features. The immunological synapse, where CD137 and other receptors cluster to mediate T‑cell activation, is disrupted by loss of CD137, affecting signal integration and cell–cell communication.

### 7.3 Localization and Lateralization

Localization of disease manifestations in IMD109 is typically systemic and bilateral. Lymphadenopathy involves multiple nodal groups, often symmetrically. Hepatosplenomegaly is midline or bilateral. Bronchiectasis and lung involvement can be patchy but often affect both lungs over time, with localized areas of damage in specific lobes depending on infection patterns.[10][14] There is no consistent lateralization (right vs left) in lymphoproliferative disease, though particular tumors may arise in specific anatomical sites (e.g., unilateral cervical lymphadenopathy, mediastinal mass).

Uberon terms such as *systemic circulation*, *immune system*, *lymphoid tissue*, and *respiratory system* are appropriate for anchoring anatomical data in a knowledge base. Imaging studies (CT, MRI, PET) reveal the distribution of lymphoid masses and organ enlargement but do not suggest unique anatomical predilections beyond those seen in other EBV-associated lymphoproliferative disorders.

## 8. Temporal Development

### 8.1 Age of Onset and Onset Pattern

TNFRSF9-related immunodeficiency typically manifests in childhood. MedGen explicitly notes that “Immunodeficiency-109 with EBV-induced lymphoproliferation (IMD109) is an autosomal recessive primary immune disorder characterized by onset of recurrent sinopulmonary infections in childhood.”[18][19] Alosaimi’s patients presented at around three years of age with recurrent sinopulmonary infections and hypogammaglobulinemia.[10][14] EBV viremia and lymphoproliferative disease emerged later, often in late childhood or early adolescence.[10][14][12] Somekh’s cohort similarly includes pediatric patients with EBV-related lymphoma and immunodeficiency.[9][12]

The onset pattern is chronic and insidious rather than acute. Recurrent infections accumulate over time, and EBV exposure leads to gradual development of persistent viremia and lymphoproliferation. There may be acute episodes, such as hemophagocytic lymphohistiocytosis or lymphoma, but these occur against a backdrop of chronic immune dysfunction. Adult-onset cases have not been reported, though milder phenotypes might theoretically remain undiagnosed until later in life.

### 8.2 Disease Progression, Course, and Critical Periods

Disease progression in IMD109 can be conceptualized in stages: early recurrent infections and hypogammaglobulinemia in childhood; onset of EBV viremia and lymphoproliferative disease in later childhood or adolescence; progression to lymphoma in some patients; and chronic complications such as bronchiectasis and organ damage.[10][14][12][18] The rate of progression varies, with some individuals rapidly developing severe EBV-driven lymphoproliferation and others having more indolent courses.

The disease course often exhibits a relapsing–remitting pattern in terms of lymphoproliferative manifestations, with episodes of EBV-driven lymphoid expansion responding to therapies such as rituximab and antivirals, but persistent underlying susceptibility leading to recurrences.[10][14][12] Recurrent infections may also flare and subside, but chronic structural damage accumulates. Without definitive therapy such as HSCT, the disorder is generally lifelong and progressive.

Critical periods likely include early childhood, when recurrent infections and hypogammaglobulinemia first appear, and the period surrounding primary EBV infection, when failure of immune control sets the stage for chronic viremia and lymphoproliferation. These windows represent opportunities for intervention: early immunoglobulin replacement and infection prevention may reduce complications, and prompt recognition and treatment of EBV viremia and lymphoproliferative disease may improve outcomes. However, data on the natural history of IMD109 are limited, and formal staging systems have not been proposed.

## 9. Inheritance and Population

### 9.1 Inheritance Pattern, Penetrance, and Expressivity

TNFRSF9-related immunodeficiency follows an **autosomal recessive** inheritance pattern. OMIM and MedGen both classify IMD109 as autosomal recessive and link it to homozygous TNFRSF9 mutations at 1p36.23.[16][18][19] All reported patients are homozygous for pathogenic variants, and their parents are heterozygous carriers. Consanguinity is common, with multiple families described as consanguineous, consistent with recessive inheritance.[14][16][10][12][11]

Penetrance appears to be complete for individuals with biallelic loss-of-function TNFRSF9 mutations, in the sense that all identified homozygous carriers have clinically significant immunodeficiency and EBV susceptibility.[14][12][10][11] However, expressivity is variable. Some patients present predominantly with recurrent infections and CVID-like humoral immunodeficiency, while others develop severe EBV-driven lymphoproliferation, lymphoma, autoimmunity, or hemophagocytic lymphohistiocytosis.[9][10][12] This variability reflects differences in environmental exposures, coexisting genetic factors, and stochastic events in lymphomagenesis. Genetic anticipation, germline mosaicism, and dominant effects have not been reported in IMD109, given the recessive loss-of-function mechanism.

### 9.2 Epidemiology, Prevalence, and Incidence

Due to its extreme rarity, precise epidemiologic estimates for TNFRSF9-related immunodeficiency are not available. Orphanet lists “EBV-induced lymphoproliferative disease due to CD137 deficiency” among rare diseases but does not provide specific prevalence or incidence figures.[13] The literature indicates that only nine patients have been reported worldwide to date, as noted in the introduction of a recent paper: “First described by Alosaimi, et al. in 2019, IMD109 is extremely rare, with only 9 reported patients to date.”[11] Given this small number and the lack of systematic screening, the true prevalence may be slightly higher, but the condition clearly falls within the ultra-rare category (prevalence likely <1/1,000,000).

Epidemiologic data from national registries, CDC, WHO, or Global Burden of Disease do not specifically capture IMD109, and patients may be coded under broader categories such as CVID, lymphoma, or EBV-associated disorders. Mortality and survival data are similarly limited and based on case outcomes rather than population-based statistics.

### 9.3 Population Demographics, Geographic Distribution, and Consanguinity

Available reports suggest that TNFRSF9-related immunodeficiency occurs predominantly in populations with high rates of consanguinity, such as Saudi Arabia and other regions where consanguineous marriage is common.[14][16][10] Alosaimi’s two patients were from Saudi consanguineous families, and other reported patients originate from diverse backgrounds but share consanguineous parentage.[10][11][12] This demographic pattern reflects the autosomal recessive inheritance and rarity of pathogenic TNFRSF9 variants.

Geographic distribution is currently based on individual case locations, including Saudi Arabia and other countries represented in Somekh’s cohort, but no region-specific prevalence data exist. Sex ratio appears approximately equal in the limited number of cases, with both male and female patients described, and there is no evidence of sex-linked influences on disease expression.[14][12][10][11]

Carrier frequency in the general population is unknown but presumed to be very low. In consanguineous families with known pathogenic variants, carrier frequency can be high among relatives, underscoring the importance of family-based genetic counseling and testing. Large datasets such as gnomAD may eventually provide estimates for specific TNFRSF9 variants, but such analyses have not been explicitly reported in the current literature.

## 10. Diagnostics

### 10.1 Clinical Evaluation, Laboratory Tests, and Biomarkers

The diagnostic workup for TNFRSF9-related immunodeficiency begins with clinical suspicion based on recurrent infections, hypogammaglobulinemia, EBV viremia, and lymphoproliferative disease in a child from a consanguineous family.[10][14][12][18] Standard laboratory tests include complete blood counts, inflammatory markers, liver function tests, and quantitative immunoglobulins. Hypogammaglobulinemia is often present, with low IgG and sometimes IgA or IgM.[10][14] EBV load can be measured by PCR in blood, revealing persistent high-level viremia.[10][12][18]

Immunologic tests are critical. Flow cytometry is used to assess lymphocyte subsets (CD4+ and CD8+ T cells, B cells, NK cells), which are typically numerically normal.[12][18][19] Functional assays, such as T‑cell proliferation in response to mitogens or antigens, cytotoxicity assays against EBV-transformed B cells, and cytokine production assays, reveal impaired CD8+ T‑cell function.[12][14][15] Specific biomarkers include reduced IFN‑γ and perforin expression in activated CD8+ T cells and reduced mitochondrial biogenesis and membrane potential in these cells, as measured by flow cytometric or microscopic techniques.[12][15]

CD137 expression itself can be assessed by flow cytometry. In TNFRSF9-deficient patients, CD137 expression on activated T cells, B cells, and NK cells is markedly reduced or absent, providing a direct diagnostic clue.[12][14][10][11] This test can differentiate IMD109 from other EBV-associated immunodeficiencies where CD137 is intact. Histopathology of lymph nodes or other tissues involved in lymphoproliferative disease may show EBV-positive B‑cell proliferations, lymphoma, or hemophagocytic lymphohistiocytosis, depending on the clinical scenario.[10][12][14][19] Immunohistochemistry for CD20, CD3, EBV-encoded RNA (EBER), and other markers can characterize the lymphoid infiltrates and guide treatment.

Imaging studies, such as CT, MRI, and PET, are used to evaluate lymphadenopathy, organomegaly, and lymphoma extent. These do not specifically indicate IMD109 but are essential for staging and management. Functional tests such as pulmonary function testing may reveal obstructive or restrictive patterns in patients with bronchiectasis and chronic lung disease.[10][14]

### 10.2 Genetic Testing Strategies

Definitive diagnosis of TNFRSF9-related immunodeficiency relies on genetic testing. Whole-exome sequencing (WES) has been the primary method used to identify pathogenic TNFRSF9 variants in reported patients.[14][12][10][11] In Alosaimi’s study, WES in two unrelated children with immunodeficiency and EBV-induced lymphoproliferation revealed the homozygous G109S missense mutation in TNFRSF9.[14][16][10] Somekh et al. also used WES to identify homozygous TNFRSF9 mutations in four patients with immune dysregulation and lymphoma.[9][12] These approaches demonstrate the utility of WES for diagnosing ultra-rare inborn errors of immunity, especially in consanguineous families.

The NCBI Genetic Testing Registry lists TNFRSF9 as a gene with available genetic tests, including targeted sequencing panels for primary immunodeficiencies and single-gene tests.[4] In clinical practice, the recommended genetic testing approach for suspected IMD109 involves initial WES or a comprehensive primary immunodeficiency gene panel, which includes TNFRSF9 and other EBV-related genes (e.g., PIK3CD, CD27, MAGT1), followed by confirmatory Sanger sequencing of identified variants. Single-gene testing for TNFRSF9 may be appropriate in families with known pathogenic variants or in cases with strongly suggestive clinical and functional features.

Whole-genome sequencing (WGS) could theoretically identify TNFRSF9 variants and structural anomalies, but since IMD109 is caused by intragenic point mutations or small indels, WES or targeted sequencing are sufficient. Chromosomal microarray (CMA), karyotyping, and FISH are not expected to detect TNFRSF9 abnormalities, as there are no recurrent large-scale structural variants associated with IMD109.[16][18][3] Mitochondrial DNA testing and repeat expansion analyses are not relevant to this disease.

Omics-based diagnostics beyond genomics, such as transcriptomics or proteomics, have not yet been applied clinically to IMD109, but research studies have used flow cytometry-based proteomic analysis (for CD137 expression and effector molecules) and functional assays to characterize disease mechanisms.[12][14][15] In a knowledge-base context, genetic testing can be annotated with NCIT terms such as “Germline Genetic Testing,” “Whole-Exome Sequencing,” and “Targeted Gene Panel Testing.”

### 10.3 Clinical Criteria, Differential Diagnosis, and Screening

Currently, there are no formal standardized diagnostic criteria or guidelines specifically for TNFRSF9-related immunodeficiency, given its rarity. However, the combination of recurrent sinopulmonary infections, hypogammaglobulinemia, EBV viremia, EBV-associated lymphoproliferative disease or lymphoma, normal lymphocyte counts, and defective CD8+ T‑cell function in a child from a consanguineous family should prompt consideration of IMD109.[18][19][14][12][10]

Differential diagnosis includes other inborn errors of immunity associated with EBV susceptibility and lymphoproliferation, such as perforin deficiency (PRF1), CD27 deficiency, MAGT1 deficiency, CTPS1 deficiency, and PIK3CD gain-of-function, as well as more common conditions like CVID, autoimmune lymphoproliferative syndrome (FAS pathway defects), and post-transplant lymphoproliferative disorder.[15][12][10] Distinguishing features include the specific pattern of CD8+ T‑cell dysfunction, absence of CD137 expression, and genetic findings. For example, CD27 deficiency involves impaired costimulation via CD27–CD70, while PRF1 deficiency affects granule-mediated cytotoxicity; both can present with EBV-driven disease but have distinct functional and genetic tests.

Screening for IMD109 in asymptomatic individuals is not currently practiced, given the rarity of the disease. However, cascade screening of relatives in affected families using genetic testing and CD137 expression assays is recommended to identify carriers and at-risk individuals, especially in consanguineous populations. Newborn screening programs do not include IMD109, and inclusion would not be practical at present due to cost and low prevalence.

## 11. Outcome / Prognosis

### 11.1 Survival, Mortality, and Disease-Specific Outcomes

Because only a small number of IMD109 patients have been reported, systematic survival and mortality statistics are not available. However, clinical reports indicate that the disease carries substantial risk of morbidity and mortality, particularly due to EBV-associated lymphomagenesis and severe lymphoproliferative disease.[9][12][14][10] Some patients have died from complications of lymphoma, hemophagocytic lymphohistiocytosis, or severe infections, while others have survived following intensive therapy, including HSCT.[10][14][12]

Osman’s case report describes a patient who developed severe EBV-associated lymphoproliferative disease and underwent HSCT, with the literature review noting that HSCT appears to be the only curative option for CD137 deficiency.[10] Alosaimi’s patients received various treatments, including intravenous immunoglobulin (IVIG), rituximab, and HSCT, with variable outcomes.[10][14] Somekh’s cohort includes patients who developed EBV-related lymphoma and autoimmunity, with complex clinical courses.[9][12] Disease-specific mortality is primarily due to EBV-driven lymphoma and severe EBV-related immune dysregulation.

### 11.2 Morbidity, Disability, and Quality of Life

Morbidity in TNFRSF9-related immunodeficiency is substantial and multifaceted. Recurrent sinopulmonary infections cause chronic respiratory symptoms, hospitalizations, and structural lung damage such as bronchiectasis, leading to long-term disability and reduced physical functioning.[10][14][18] EBV viremia and lymphoproliferative disease result in systemic symptoms (fever, fatigue, weight loss), organomegaly, and in some cases aggressive lymphoma, requiring chemotherapy and HSCT.[10][12][14] Autoimmune manifestations add complexity and treatment burden, potentially causing cytopenias, bleeding, and increased infection risk.[9][12]

Quality of life is likely markedly impaired, although formal studies using instruments such as SF‑36 or EQ‑5D have not been reported. Patients experience chronic fatigue, limitations in physical activity, social isolation due to infection risk, and psychological stress related to serious illness and uncertain prognosis. Parents and families face emotional and financial burdens. In the absence of curative therapy, these impacts may persist or worsen over time.

### 11.3 Prognostic Factors and Biomarkers

Prognostic factors in IMD109 are not well-defined due to small patient numbers, but several features likely influence outcomes. Age at onset and severity of EBV viremia, the presence and aggressiveness of lymphoma, degree of hypogammaglobulinemia, and response to therapies such as rituximab and HSCT are important determinants of prognosis.[10][14][12] Patients who receive timely HSCT may have improved survival and quality of life compared to those managed with supportive care alone.[10][14]

Potential prognostic biomarkers include EBV viral load in blood, CD8+ T‑cell functional metrics (proliferation, cytotoxicity, mitochondrial function), and CD137 expression levels upon activation. Persistent high EBV viremia and severely impaired CD8+ T‑cell responses may predict higher risk of lymphoma and severe lymphoproliferative disease.[12][15] However, formal prognostic models have not been developed, and each case requires individualized assessment.

## 12. Treatment

### 12.1 Supportive and Immunomodulatory Therapies

Current treatment strategies for TNFRSF9-related immunodeficiency focus on supportive care, infection control, and management of lymphoproliferative disease, as well as curative options such as HSCT. Supportive treatments include intravenous immunoglobulin (IVIG) replacement to correct hypogammaglobulinemia and reduce recurrent bacterial infections.[10][14] Antibiotic prophylaxis may be used to prevent sinopulmonary infections, and aggressive treatment of acute infections is essential to prevent complications.

For EBV-related lymphoproliferative disease, rituximab, a monoclonal antibody targeting CD20 on B cells, is commonly employed to deplete EBV-infected B cells and control lymphoid proliferations.[10][14] Osman’s literature review notes that patients with EBV viremia and EBV-driven lymphoproliferation received IVIG and anti-CD20 monoclonal antibody rituximab, sometimes followed by HSCT.[10] Antiviral agents such as ganciclovir or acyclovir may be used, though their efficacy against latent EBV-infected cells is limited.

Immunosuppressive therapies may be required for autoimmune manifestations and hemophagocytic lymphohistiocytosis, including corticosteroids, cyclosporine, or etoposide-based regimens, but these must be balanced against infection risks in an already immunodeficient patient. NCIT terms such as “Immunoglobulin Replacement Therapy,” “Rituximab Therapy,” and “Antiviral Therapy” can be used to annotate these interventions.

### 12.2 Hematopoietic Stem Cell Transplantation and Advanced Therapies

Hematopoietic stem cell transplantation (HSCT) represents the only known **curative** treatment for TNFRSF9-related immunodeficiency, as it replaces the defective immune system with donor cells possessing functional TNFRSF9 and CD137.[10][14][12] In reported cases, HSCT has been performed in patients with severe EBV-associated lymphoproliferative disease or lymphoma, leading to resolution of immunodeficiency and improved long-term outcomes.[10][14] Osman’s case report and literature review emphasize the role of HSCT in managing severe CD137 deficiency and preventing recurrent EBV viremia and lymphoproliferation.[10]

HSCT can be annotated with NCIT terms such as “Allogeneic Hematopoietic Stem Cell Transplantation” and represents an advanced cell therapy. It carries risks of graft-versus-host disease, infections, and transplant-related mortality, but offers the possibility of cure. Optimal timing, conditioning regimens, and donor selection require careful consideration in the context of individual patient characteristics and disease severity.

Gene therapy and gene editing approaches targeting TNFRSF9 have not yet been developed for clinical use in IMD109, though in principle, viral vector-mediated gene transfer or CRISPR-based correction of TNFRSF9 in hematopoietic stem cells could restore CD137 function. However, the rarity of the disease and the complexity of such interventions make them unlikely in the near term. RNA-based therapies and targeted immunotherapies such as CD137 agonists are being explored in cancer, but their use in CD137-deficient immunodeficiency would be limited by the absence of the target receptor.

### 12.3 Treatment Outcomes, Side Effects, and Personalized Approaches

Treatment outcomes in IMD109 vary. Supportive therapies such as IVIG and antibiotic prophylaxis can reduce infection burden but do not address EBV susceptibility or lymphoproliferative risk. Rituximab and chemotherapy can control lymphoma but carry significant toxicity. HSCT offers cure but is associated with substantial risks and requires specialized centers.[10][14][12] Side effects of treatments include infusion reactions, immunosuppression, organ toxicity, and long-term complications such as secondary malignancies.

Personalized medicine approaches involve tailoring treatment based on TNFRSF9 genotype, CD8+ T‑cell functional status, EBV load, and comorbidities. For example, patients with less severe infection burden and no lymphoma may be managed with conservative supportive care and close monitoring, while those with aggressive EBV-driven lymphoproliferation may require early HSCT. Pharmacogenomic considerations are limited, as TNFRSF9 mutations do not directly affect drug metabolism, but variants in other genes (e.g., PIK3CD) may influence responses to specific therapies.

In knowledge-base annotations, NCIT terms for specific therapies, along with descriptive metadata on indications, mechanisms, and outcomes, can facilitate structured representation of treatment strategies in IMD109.

## 13. Prevention

### 13.1 Primary, Secondary, and Tertiary Preventive Strategies

Primary prevention of TNFRSF9-related immunodeficiency is not feasible at the individual level, given its genetic nature, but preventive strategies can focus on **genetic counseling**, carrier screening, and informed reproductive decisions in consanguineous families with known pathogenic TNFRSF9 variants.[14][16][10][11] Counseling can discuss risks of autosomal recessive inheritance, options for prenatal diagnosis or preimplantation genetic testing, and implications for future offspring. NSGC and ACMG guidelines support such approaches for severe inborn errors of immunity.

Secondary prevention involves early detection and management of disease manifestations. For recurrent infections, prompt diagnosis of immunodeficiency and initiation of IVIG and prophylactic antibiotics can prevent chronic lung damage. For EBV-related lymphoproliferation, regular monitoring of EBV viral load, lymphocyte counts, and clinical symptoms can facilitate early intervention with rituximab or antiviral therapy, potentially preventing progression to lymphoma.[10][14][12]

Tertiary prevention focuses on limiting complications and disability in those with established disease. This includes rehabilitation for bronchiectasis, lung function preservation, psychosocial support, and long-term follow-up after HSCT to monitor for graft-versus-host disease and secondary malignancies. Clinical guidelines for immunodeficiency management and lymphoma treatment provide frameworks for such care.

### 13.2 Immunization, Screening, and Counseling

Immunization strategies for IMD109 follow general recommendations for primary immunodeficiency, with emphasis on inactivated vaccines for respiratory pathogens (e.g., pneumococcal, influenza) and avoidance of live attenuated vaccines in severely immunodeficient patients. EBV vaccination is not currently available, but future vaccines could play a critical preventive role in TNFRSF9-related immunodeficiency by reducing primary EBV infection risk.

Screening programs for IMD109 are currently limited to family-based genetic testing and immunologic evaluation in relatives of known patients. Carrier screening in high-risk populations could be considered where consanguinity is common, but the rarity of TNFRSF9 variants makes population-wide screening impractical. Risk stratification based on family history, consanguinity, and clinical features can identify individuals for targeted testing.

Genetic counseling is central to prevention at the family level. Counselors can explain autosomal recessive inheritance, the meaning of carrier status, and options for prenatal and preimplantation testing. For affected individuals, counseling can address reproductive risks and implications for offspring. Ontologically, these preventive measures can be annotated with NCIT terms such as “Genetic Counseling,” “Carrier Screening,” and “Prenatal Genetic Testing.”

## 14. Other Species / Natural Disease

### 14.1 Orthologous Genes and Comparative Biology

TNFRSF9 has orthologs in multiple species, including mice (Tnfrsf9, Gene ID 21942) and rats (Tnfrsf9, Gene ID 500590).[1][2][5][7] These orthologous genes encode TNF receptor superfamily member 9, sharing structure and function with human CD137. NCBI Gene entries for mouse and rat Tnfrsf9 indicate that the receptor enables signaling receptor activity and is involved in regulation of cell population proliferation, paralleling human gene ontology annotations.[1][2][7]

Comparative biology studies in mice, particularly 4‑1BB- and 4‑1BBL-deficient models, reveal that CD137 pathways are conserved across species and play key roles in cytotoxic T‑cell responses to viral infections and allografts.[17] Analysis of 4‑1BBL-deficient mice and mice lacking both 4‑1BBL and CD28 shows that 4‑1BBL contributes to skin allograft rejection and cytotoxic T‑cell responses to influenza virus, with CD28-independent costimulation leading to high-level IL‑2 production by T cells.[17] These findings reinforce the role of CD137–4‑1BBL in augmenting suboptimal CTL responses in vivo and provide mechanistic insight relevant to human CD137 deficiency.

### 14.2 Natural Disease in Other Species and Zoonotic Considerations

To date, naturally occurring TNFRSF9-related immunodeficiency has not been reported in non-human animals, such as companion animals or livestock, in the available literature. Online Mendelian Inheritance in Animals (OMIA) and veterinary databases do not list CD137 deficiency as a recognized disease, underscoring the rarity and human-centric focus of current knowledge.

Zoonotic potential is not directly relevant to TNFRSF9-related immunodeficiency, as the disease arises from human germline mutations and affects host immunity rather than pathogen transmissibility. EBV itself is a human-specific virus and does not infect other species in the same manner. However, comparative studies in animal models offer valuable insights into immune mechanisms and potential interventions that may be translatable to human disease.

## 15. Model Organisms

### 15.1 Mouse Models of 4‑1BB and 4‑1BBL Deficiency

Mouse models have been instrumental in elucidating the function of CD137 and its ligand, 4‑1BBL, and thereby shedding light on the pathophysiology of TNFRSF9-related immunodeficiency. Analysis of 4‑1BBL-deficient mice and mice lacking both 4‑1BBL and CD28 reveals that 4‑1BBL is a member of the TNF family expressed on activated antigen-presenting cells, and that it binds 4‑1BB on activated CD4+ and CD8+ T cells to provide CD28-independent costimulatory signals.[17] These signals lead to high-level IL‑2 production by primary resting T cells and support cytotoxic responses to viral infections.[17]

The immunological characterization of 4‑1BBL-deficient mice shows that these animals mount neutralizing IgM and IgG responses to vesicular stomatitis virus similar to wild-type mice, indicating redundancy in humoral responses.[17] However, 4‑1BBL-deficient mice exhibit a weaker CTL response to influenza virus than wild-type mice, and 4‑1BBL−/−CD28−/− mice respond poorly to influenza virus and display delayed skin allograft rejection.[17] These findings substantiate the idea that different immune responses vary in their dependence on costimulation and suggest a role for 4‑1BBL in augmenting suboptimal CTL responses in vivo.[17] In this sense, mouse models recapitulate aspects of CD137 deficiency, particularly impaired cytotoxic T‑cell responses to viral infections, analogous to EBV-related defects in humans.

### 15.2 Phenotype Recapitulation and Model Limitations

Mouse models provide valuable insights into CD137 biology but do not fully recapitulate the human phenotype of TNFRSF9-related immunodeficiency. For example, EBV is a human-specific virus, and mice do not develop EBV-associated lymphoproliferative disease or lymphoma in the same way. Instead, influenza and other murine viruses serve as proxies for viral infections. The absence of EBV in mice limits direct modeling of EBV-specific defects, though extrapolation from influenza and other viral responses is informative.[17]

Furthermore, mouse immune systems differ from human systems in many aspects, including costimulatory pathway usage, regulatory networks, and tumor biology. While 4‑1BB and 4‑1BBL deficiency in mice demonstrate impaired CTL responses and altered allograft rejection, they do not produce the exact constellation of recurrent bacterial infections, hypogammaglobulinemia, EBV viremia, and lymphoma seen in IMD109. This highlights the limitations of animal models and the need for human studies.

Nevertheless, mouse models remain essential for dissecting molecular pathways, testing therapeutic strategies (e.g., CD137 agonists or antagonists), and understanding redundancy and compensation among costimulatory receptors. They also provide platforms for CRISPR-based gene editing and functional genomics screens that can identify interacting genes and pathways relevant to CD137 function.

### 15.3 Applications and Resources

Applications of model organisms in TNFRSF9-related immunodeficiency research include studying the effects of CD137 or 4‑1BBL disruption on T‑cell activation, proliferation, and cytokine production; evaluating combination defects with other costimulatory pathways; and testing interventions such as agonistic antibodies or gene therapy vectors. Resources such as the Mouse Genome Informatics (MGI) database, International Mouse Phenotyping Consortium (IMPC), and other model organism repositories catalog relevant mouse lines, though specific entries for TNFRSF9 deficiency may require targeted searches.

In knowledge-base annotations, model organism data can be linked to human disease via orthology relationships and comparative phenotype ontologies, allowing integration of mechanistic insights across species. This supports translational research and the development of therapeutic strategies informed by both human and animal data.

## Conclusion

TNFRSF9-related immunodeficiency (Immunodeficiency 109 with lymphoproliferation, IMD109) is a paradigmatic example of an **inborn error of immunity** caused by biallelic loss-of-function mutations in a costimulatory receptor gene, TNFRSF9, encoding CD137/4‑1BB.[3][12][16][18] The disease’s distinctive clinical signature—childhood-onset recurrent sinopulmonary infections, hypogammaglobulinemia, persistent EBV viremia, and a marked predisposition to EBV-associated lymphoproliferative disease and lymphoma—reflects the central role of CD137 in supporting CD8+ T‑cell expansion, cytotoxicity, and mitochondrial function in antiviral responses.[12][14][15][18] Functional studies in patient cells demonstrate absent or severely reduced CD137 expression, defective CD8+ T‑cell proliferation and effector molecule production, impaired cytotoxicity against EBV-infected targets, and compromised mitochondrial biogenesis and membrane potential, all of which are restored by genetic reconstitution of CD137.[12][15] These findings, combined with complementary evidence from 4‑1BB and 4‑1BBL-deficient mice, provide a coherent mechanistic framework linking TNFRSF9 mutations to clinical manifestations via a defined causal chain.

From a knowledge-base perspective, TNFRSF9-related immunodeficiency can be precisely annotated with disease identifiers (OMIM 620282, MONDO:0859526, MedGen C5830346), gene and protein annotations (TNFRSF9, CD137, 4‑1BB), ontology terms for phenotypes (HPO), biological processes (GO), cell types (CL), anatomical locations (UBERON), chemical entities (CHEBI), and interventions (NCIT). This structured representation enables integration with broader datasets on inborn errors of immunity, EBV-associated disorders, and costimulatory pathways, and facilitates comparative analyses across diseases and model organisms.

Clinically, IMD109 is an ultra-rare but severe condition requiring high suspicion in children with recurrent infections, hypogammaglobulinemia, EBV viremia, and lymphoproliferative disease, particularly in consanguineous families.[10][14][12][18] Diagnostic evaluation relies on immunologic workups, functional assays of CD8+ T‑cell function, assessment of CD137 expression, and whole-exome sequencing or targeted gene panels to identify TNFRSF9 mutations.[14][12][10][11][4] Treatment strategies combine supportive care (IVIG, antibiotics), management of EBV-related lymphoproliferation (rituximab, chemotherapy), and curative options such as HSCT, which has shown success in restoring immune function and preventing recurrence.[10][14][12] Genetic counseling, carrier screening, and family-based prevention measures are essential components of care in affected families.

Despite significant advances in understanding CD137 biology and its role in immune homeostasis, many questions remain. The full spectrum of TNFRSF9 variants, potential modifier genes, epigenetic changes, and multi-omics signatures has yet to be elucidated. The small number of reported patients limits epidemiologic and prognostic analyses, and no standardized clinical guidelines specific to IMD109 exist. Future research should aim to expand case collections, perform deeper molecular profiling, and explore novel therapeutic approaches, including targeted immunotherapies and gene-based interventions. As part of a broader effort to catalog and understand inborn errors of immunity, TNFRSF9-related immunodeficiency offers a unique window into the interplay of costimulatory pathways, antiviral immunity, and lymphomagenesis, with implications extending beyond this rare disease to common conditions such as EBV-associated cancers and responses to cancer immunotherapy.[12][15]

In conclusion, TNFRSF9-related immunodeficiency exemplifies how precise genetic and mechanistic characterization of rare diseases can illuminate fundamental principles of human immunology, inform clinical management, and enrich ontology-driven knowledge bases that support translational research and precision medicine.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 14 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 12 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0005261` (2 mentions) - the report calls it "Autoimmune lymphoproliferative syndrome"; HP calls it **Joint hemorrhage**
- `HP:0004459` (1 mention) - the report calls it "Recurrent otitis media"; HP calls it **Exostosis of the external auditory canal**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0002899` (2 mentions), reported as "B‑cell lymphoma", "B-cell lymphoma" - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0004313` (2 mentions) - the report calls it "Hypogammaglobulinemia"; HP calls it **Decreased circulating immunoglobulin concentration**, and lists "Hypogammaglobulinemia" among its other names
- `HP:0000246` (1 mention) - the report calls it "Recurrent sinusitis"; HP calls it **Sinusitis**
- `HP:0005428` (1 mention) - the report calls it "Severe viral infection"; HP calls it **Severe recurrent varicella**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0002899` - called "B‑cell lymphoma", "B-cell lymphoma"