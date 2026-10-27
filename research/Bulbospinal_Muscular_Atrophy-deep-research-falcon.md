---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-19T21:03:45.689456'
end_time: '2026-08-19T21:12:58.584876'
duration_seconds: 552.9
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Bulbospinal Muscular Atrophy
  mondo_id: MONDO:0016113
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 32
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 8
  on_topic: 5
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Bulbospinal_Muscular_Atrophy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---


## Curation Note — NEC (Named Entity Confusion) verdict: DO NOT CURATE FROM THIS REPORT

Added by the curator during dismech issue #8940, after running
`just preflight-dr research/Bulbospinal_Muscular_Atrophy-deep-research-falcon.md MONDO:0016113`.

The automated preflight returned **SKIP** (MONDO records no `RO:0004003` causal gene for
MONDO:0016113, because it is a grouping term), so the manual NEC checks in CLAUDE.md §2b
were applied. All three flagged a mismatch:

- **Gene check.** The report's gene mentions are dominated by `AR` (46 mentions vs 1 for the
  next disease gene). `AR` is the causal gene of Kennedy disease (MONDO:0010735), a single
  X-linked disease — not of the MONDO:0016113 grouping.
- **OMIM check.** The report asserts OMIM `313200` (spinal and bulbar muscular atrophy,
  X-linked 1 = Kennedy disease). MONDO:0016113 has **no** OMIM xref; its xrefs are
  GARD:0020365, MEDGEN:95977, NANDO:1200001, Orphanet:206701, SCTID:230253001,
  UMLS:C0393547, icd11.foundation:1604214898.
- **Synonym check.** MONDO:0016113 carries "SBMA" and "spinal-bulbar muscular atrophy" as
  EXACT synonyms even though it is tagged `disease_grouping` / `ordo_group_of_disorders`.
  Those strings are the everyday clinical names of Kennedy disease, so the provider resolved
  the query to the wrong MONDO entity.

**Verdict: the report describes Kennedy disease, not the bulbospinal muscular atrophy
grouping.** Per CLAUDE.md §2b it was discarded in full — no PMID, snippet, ontology term, or
claim from it was used in `kb/groupings/Bulbospinal_Muscular_Atrophies.yaml`, which was built
instead from MONDO/Orphanet structure and from already-cached, already-verified literature on
the member entries. It is committed only as run provenance and as a worked example of the
synonym collision recorded in that grouping's `mondo_0016113_sbma_synonym_collision`
discussion. Kennedy disease itself is already curated at `kb/disorders/Kennedy_Disease.yaml`.

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Bulbospinal Muscular Atrophy
- **MONDO ID:** MONDO:0016113 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Bulbospinal Muscular Atrophy** covering all of the
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

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Bulbospinal Muscular Atrophy
- **MONDO ID:** MONDO:0016113 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Bulbospinal Muscular Atrophy** covering all of the
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


# Bulbospinal Muscular Atrophy (Spinal and Bulbar Muscular Atrophy/Kennedy Disease): Research Report

**Scope and evidence date.** “Bulbospinal muscular atrophy” here denotes **spinal and bulbar muscular atrophy (SBMA), or Kennedy disease**, not SMN1-associated 5q spinal muscular atrophy. Evidence below is disease-level aggregate literature, population genomics, clinical-trial registries, and experimental models—not individual-patient EHR data. Sources were reviewed through the retrieved 2024 literature; trial-registry records may contain later status updates. PMID was not exposed in the retrieved records, so DOI and ClinicalTrials.gov identifiers are supplied rather than guessing PMIDs.

The following table provides a compact curation layer; the narrative then addresses all requested domains.

| Domain | Curated value | Evidence type | Ontology/identifier suggestion |
|---|---|---|---|
| Disease name | Spinal and bulbar muscular atrophy (SBMA), also called Kennedy disease; older synonym: bulbospinal muscular atrophy (pradat2020thefrenchnational pages 1-2, zanovello2023unexpectedfrequencyof pages 1-2) | Human clinical review; population-genomics primary study | MONDO:0016113; MeSH D055534 |
| Core disease identifiers | MONDO:0016113; OMIM 313200; ORPHA 481; MeSH D055534 “Bulbo-Spinal Atrophy, X-Linked” (NCT06169046 chunk 1) | Curated disease/resource mapping in conversation; ClinicalTrials MeSH browse | MONDO:0016113; OMIM:313200; Orphanet:481; MeSH:D055534 |
| Etiologic gene | AR (androgen receptor), exon 1 CAG-repeat expansion on the X chromosome (pradat2020thefrenchnational pages 1-2, zanovello2023unexpectedfrequencyof pages 1-2) | Human clinical review; population-genomics primary study | HGNC:644; NCBI Gene:367 |
| Pathogenic repeat threshold | Pathogenic alleles generally defined as \>=38 CAG repeats; conversation sources also note disease beyond 37 repeats and typical disease range about 39–72 repeats (zanovello2023unexpectedfrequencyof pages 1-2, hashizume2020diseasemechanismbiomarker pages 8-12, cantara2024antisenseoligonucleotides(asos) pages 14-16, NCT06862596 chunk 1, NCT06169046 chunk 1) | Population-genomics primary study; review; trial eligibility criteria | Repeat expansion testing; AR CAG repeat |
| Inheritance | X-linked recessive / X-linked adult-onset disorder; full phenotype primarily in males, with female carriers often asymptomatic or mildly affected (pradat2020thefrenchnational pages 1-2, querin2017kennedydisease(xlinked pages 1-5) | Human clinical reviews | HP:0001419; NCIT:C85867 |
| Typical onset/course | Adult onset, commonly 30–50 years, slowly progressive; mean onset around early 40s reported in recent genomic study background (querin2017kennedydisease(xlinked pages 1-5, cantara2024antisenseoligonucleotides(asos) pages 14-16, zanovello2023unexpectedfrequencyof pages 1-2) | Human clinical review; population-genomics primary study | HP:0003581; HP:0003677 |
| Major motor phenotype | Progressive proximal limb weakness and atrophy; ~70% first notice lower-limb weakness, and one review reports proximal weakness in 97% with lower-limb involvement in 86.7% (hashizume2020diseasemechanismbiomarker pages 1-5, querin2017kennedydisease(xlinked pages 1-5) | Human clinical reviews | HP:0003323; HP:0003202 |
| Bulbar phenotype | Dysarthria and dysphagia are common and often later manifestations; dysphagia reported in ~80% in review literature (pradat2020thefrenchnational pages 1-2, querin2017kennedydisease(xlinked pages 1-5, querin2017kennedydisease(xlinked pages 5-9) | Human clinical reviews/guideline | HP:0001260; HP:0002015 |
| Tremor/sensory phenotype | Postural hand tremor can predate weakness by >10 years; sensory abnormalities reported in many patients (72–100% in review summary) (hashizume2020diseasemechanismbiomarker pages 1-5, querin2017kennedydisease(xlinked pages 5-9) | Human clinical reviews | HP:0001337; HP:0003401 |
| Endocrine/reproductive phenotype | Partial androgen insensitivity with gynecomastia, testicular atrophy, erectile dysfunction, reduced fertility (hashizume2020diseasemechanismbiomarker pages 1-5, querin2017kennedydisease(xlinked pages 5-9, badders2018selectivemodulationof pages 1-3) | Human clinical reviews; mechanistic primary study intro | HP:0000132; HP:0000047 |
| Metabolic phenotype | Glucose intolerance, hyperlipidemia/dyslipidemia, insulin resistance, fatty liver/metabolic syndrome are recognized extra-neurological features (pradat2020thefrenchnational pages 1-2, querin2017kennedydisease(xlinked pages 5-9, zanovello2023unexpectedfrequencyof pages 1-2) | Human consensus guideline; population-genomics background | HP:0003074; HP:0003124 |
| Respiratory/cause of death | Overt respiratory failure is uncommon, but aspiration pneumonia and respiratory infections are major complications; respiratory infectious diseases account for >50% of deaths in one review summary (hashizume2020diseasemechanismbiomarker pages 1-5, querin2017kennedydisease(xlinked pages 12-15) | Human clinical reviews | HP:0002093; HP:0006536 |
| Cardiac involvement | Cardiac repolarization abnormalities/Brugada-type ECG are recognized in some cohorts; trial protocols exclude affected patients (pradat2020thefrenchnational pages 1-2, querin2017kennedydisease(xlinked pages 5-9, NCT06862596 chunk 1, NCT05517603 chunk 1) | Human consensus guideline; trial eligibility | HP:0011715 |
| Principal organs/tissues | Lower motor neuron system and skeletal muscle are primary sites; dorsal root ganglia/sensory system and extra-neurological tissues are also involved (hashizume2020diseasemechanismbiomarker pages 1-5, querin2017kennedydisease(xlinked pages 5-9, cortes2014motorneurondegeneration pages 1-2) | Human review; mouse mechanistic study | UBERON:0001017 spinal cord; UBERON:0001134 skeletal muscle |
| Principal cell types | Lower motor neurons and skeletal myofibers are central; evidence also implicates sensory neurons/dorsal root ganglion cells (hashizume2020diseasemechanismbiomarker pages 1-5, querin2017kennedydisease(xlinked pages 5-9, iida2019srcinhibitionattenuates pages 1-2) | Human review; mouse/human tissue primary study | CL:0000100 motor neuron; CL:0000187 muscle cell |
| Core upstream mechanism | Ligand-dependent toxic gain of function of polyglutamine-expanded AR, especially androgen-dependent nuclear accumulation of mutant AR (hashizume2020diseasemechanismbiomarker pages 1-5, hashizume2020diseasemechanismbiomarker pages 8-12, badders2018selectivemodulationof pages 1-3) | Human review; mechanistic primary study | GO:0005634 nucleus; GO:0006915 apoptotic process |
| Key downstream mechanisms | Transcriptional dysregulation, altered proteostasis/autophagy, mitochondrial dysfunction, metabolic shift, and Src pathway activation; phosphorylated Src is increased before onset in mouse spinal cord and muscle (pradat2020thefrenchnational pages 1-2, hashizume2020diseasemechanismbiomarker pages 15-19, iida2019srcinhibitionattenuates pages 1-2) | Human consensus review; mouse phosphoproteomic primary study | GO:0016567 protein ubiquitination; GO:0000422 autophagy; GO:0005739 mitochondrion; GO:0030971 receptor tyrosine kinase signaling |
| Muscle-driven disease component | Skeletal muscle is not only affected but can drive neuromuscular degeneration; muscle-specific excision of mutant AR rescued neuromuscular phenotypes in BAC fxAR121 mice (cortes2014motorneurondegeneration pages 1-2, hashizume2020diseasemechanismbiomarker pages 8-12) | Mouse primary study; review | GO:0006936 muscle contraction |
| Epidemiology: classical prevalence | Traditional prevalence estimates are about 1–2 per 100,000 or ~1:30,000 males, depending on study and population (hashizume2020diseasemechanismbiomarker pages 1-5, zanovello2023unexpectedfrequencyof pages 1-2) | Human reviews; population-genomics background | Orphanet epidemiology field |
| Epidemiology: 2023 expansion frequency | 2023 whole-genome analysis estimated pathogenic AR expansion frequency at 1:3182 X chromosomes (95% CI 1:2309–1:4386) (zanovello2023unexpectedfrequencyof pages 1-2) | Human population-genomics primary study | AR CAG expansion frequency |
| Epidemiology: 2023 modeled prevalence | Using the new mutation frequency, modeled disease prevalence was 1:6887 males, suggesting underdiagnosis and/or reduced penetrance (zanovello2023unexpectedfrequencyof pages 1-2) | Human population-genomics primary study | SBMA prevalence estimate |
| Population structure/founder effects | Founder effects have been noted in Japanese, Finnish, and Italian populations in review literature (hashizume2020diseasemechanismbiomarker pages 8-12) | Review synthesis | Population note |
| Diagnostic confirmation | Diagnosis is confirmed by genetic testing for AR CAG-repeat expansion; suspicion arises from adult male with slowly progressive LMN syndrome plus bulbar/endocrine features (pradat2020thefrenchnational pages 1-2, querin2017kennedydisease(xlinked pages 5-9) | Human consensus guideline; review | Repeat expansion assay |
| Electrophysiology/labs | EMG typically shows diffuse motor neuron involvement with sensory abnormalities; CK/CPK is often elevated, sometimes markedly (pradat2020thefrenchnational pages 1-2, querin2017kennedydisease(xlinked pages 5-9) | Human consensus guideline; review | LOINC/EMG concept; CHEBI:17347 creatine kinase |
| Imaging/functional diagnostics | Muscle MRI/fat fraction measures, quantitative muscle testing, 2-minute and 6-minute walk tests, AMAT, SBMAFRS/m-SBMAFRS are used in studies and trials (hashizume2020diseasemechanismbiomarker pages 1-5, NCT00303446 chunk 1, NCT06411912 chunk 1, NCT06169046 chunk 1) | Human review; clinical trial records | SBMAFRS; AMAT; 6MWT |
| Biomarkers | Serum creatinine is a promising progression biomarker and may decline before weakness onset; CK and muscle/fat MRI are also used (hashizume2020diseasemechanismbiomarker pages 1-5, hashizume2020diseasemechanismbiomarker pages 8-12) | Human review | CHEBI:16737 creatinine |
| Differential diagnosis | ALS, SMA/non-5q SMA, myopathies, and neuropathies are key differentials (querin2017kennedydisease(xlinked pages 5-9) | Human clinical review | Differential diagnosis note |
| Standard management | No approved disease-modifying therapy established; care is multidisciplinary and symptomatic, emphasizing physiotherapy, speech therapy, nutritional support, aspiration/respiratory care, pain management, and endocrine/metabolic monitoring (pradat2020thefrenchnational pages 1-2, querin2017kennedydisease(xlinked pages 12-15) | Human consensus guideline; review | NCIT supportive care; speech therapy; physiotherapy |
| Hormonal therapy evidence | Anti-androgen approaches have biologic rationale and some signal, but no established therapy; dutasteride trial and leuprorelin studies did not establish a standard of care (hashizume2020diseasemechanismbiomarker pages 1-5, querin2017kennedydisease(xlinked pages 12-15, NCT00303446 chunk 1) | Review; clinical trial registry | NCIT dutasteride; leuprorelin |
| Exercise/rehabilitation | Exercise is used supportively; high-intensity/functional exercise has been explored in interventional studies (querin2017kennedydisease(xlinked pages 12-15) | Human review | NCIT rehabilitation |
| Recent/active trial: NIDO-361 | Phase 2 PIONEER KD, randomized placebo-controlled, 54 participants, oral NIDO-361 for 12 months; endpoints include lean muscle volume, m-SBMAFRS, 2MWT/6MWT, actigraphy (NCT06411912 chunk 1) | ClinicalTrials.gov record | NCT06411912 |
| Recent/active trial: AJ201 | Phase 1/2a randomized placebo-controlled study, 25 participants, oral AJ201 600 mg/day for 12 weeks; endpoints include safety and change in mutant AR protein in skeletal muscle (NCT05517603 chunk 1) | ClinicalTrials.gov record | NCT05517603 |
| Recent/active trial: clenbuterol | Phase 2 placebo-controlled BetaSBMA trial, recruiting, estimated n=90, 48-week clenbuterol; primary endpoint 6MWT, with QoL and serum creatinine secondary measures (NCT06169046 chunk 1) | ClinicalTrials.gov record | NCT06169046 |
| Recent/active trial: mexiletine | Phase 2/3 Med-SBMA trial, recruiting, estimated n=68; mexiletine 300 mg/day for 12 weeks, outcomes include ALSFRS-R, SBMAFRS, tongue pressure, FVC, PEF (NCT06862596 chunk 1) | ClinicalTrials.gov record | NCT06862596 |
| Historical trial: dutasteride | Completed phase 2 NIH placebo-controlled trial; aimed to test 0.5 mg/day for 24 months with QMT primary outcome and QoL/functional secondary outcomes (NCT00303446 chunk 1) | ClinicalTrials.gov record | NCT00303446 |
| Historical trial: BVS857 | Completed phase 2 placebo-controlled study, 37 participants; evaluated safety and thigh muscle volume by MRI (NCT02024932 chunk 1) | ClinicalTrials.gov record | NCT02024932 |
| Model systems | Drosophila, transgenic/knock-in mice, and cellular systems including ASO-responsive models have been used; fly and mouse studies supported AF2 modulation, peripheral AR silencing, and Src inhibition (badders2018selectivemodulationof pages 1-3, cortes2014motorneurondegeneration pages 1-2, iida2019srcinhibitionattenuates pages 1-2) | Animal and in vitro primary studies | MGI mouse models; Drosophila model |
| Prevention/genetic counseling | No primary prevention for disease occurrence once expansion is inherited; useful measures are genetic counseling, cascade testing, and reproductive counseling around X-linked transmission (inferred from established genetic diagnosis and counseling relevance in reviews) (pradat2020thefrenchnational pages 1-2, querin2017kennedydisease(xlinked pages 19-22) | Human consensus guideline; review | Genetic counseling; X-linked risk counseling |


*Table: This table condenses the key disease-knowledge-base fields for spinal and bulbar muscular atrophy/Kennedy disease, including identifiers, genetics, phenotypes, mechanism, epidemiology, diagnostics, management, and recent trials. It is designed for rapid curation while keeping claims conservative and tied to cited conversation evidence.*

## 1. Disease information

SBMA is a rare, chronic, adult-onset, X-linked neuromuscular disease caused by an expanded CAG repeat in exon 1 of **AR**, encoding an abnormally long polyglutamine tract in the androgen receptor. It combines slowly progressive lower-motor-neuron and primary skeletal-muscle disease with partial androgen insensitivity and metabolic manifestations. Bulbar dysfunction usually appears later than limb weakness. It is distinct from childhood 5q-SMA and typically progresses much more slowly than amyotrophic lateral sclerosis (ALS). (pradat2020thefrenchnational pages 1-2, zanovello2023unexpectedfrequencyof pages 1-2)

**Identifiers and synonyms**

- Preferred names: spinal and bulbar muscular atrophy; SBMA; Kennedy disease.
- Alternatives: bulbospinal muscular atrophy; X-linked bulbospinal neuronopathy; X-linked spinal and bulbar muscular atrophy; Kennedy syndrome.
- **MONDO:** MONDO:0016113.
- **OMIM:** 313200.
- **Orphanet:** ORPHA:481.
- **MeSH:** D055534, *Bulbo-Spinal Atrophy, X-Linked*; the trial-registry hierarchy also places it under motor-neuron, neuromuscular, hereditary neurodegenerative, and X-linked genetic diseases. (NCT06169046 chunk 1)
- **ICD:** SBMA lacks a consistently disease-specific ICD-10-CM code and is generally represented under broader spinal muscular atrophy/motor-neuron disease categories; coding should be jurisdiction-specific. ICD-11 likewise should be verified against the deployment used by the knowledge base rather than inferred from an older ICD-10 mapping.

The French national protocol describes it as “a rare, adult-onset, X-linked recessive neuromuscular disease caused by CAG expansions in exon 1 of the androgen receptor gene.” [Published April 2020; DOI URL: https://doi.org/10.1186/s13023-020-01366-z.] (pradat2020thefrenchnational pages 1-2)

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal factor

The necessary inherited lesion is a **germline CAG-repeat expansion in AR at Xq12**. Most current clinical and population-genomic sources define a pathogenic allele as **≥38 CAG repeats**, although conventional reviews often describe unaffected and disease ranges as approximately 9/11–36 and 39–72, respectively. Borderline alleles require careful laboratory interpretation and phenotype correlation. (hashizume2020diseasemechanismbiomarker pages 8-12, cantara2024antisenseoligonucleotides(asos) pages 14-16, zanovello2023unexpectedfrequencyof pages 1-2)

The expansion produces two linked effects: partial impairment of normal AR activity, explaining androgen-insensitivity features, and a dominant toxic gain of function of ligand-bound polyglutamine-expanded AR in vulnerable tissues. Longer repeats correlate strongly with earlier onset and often greater severity, but explain only part of phenotypic variability and do not reliably determine an individual progression rate. (hashizume2020diseasemechanismbiomarker pages 8-12, querin2017kennedydisease(xlinked pages 1-5, badders2018selectivemodulationof pages 1-3)

### Risk factors

- **Genetic:** a pathogenic AR expansion; longer repeat length; an affected maternal lineage; and population founder effects reported in Finnish, Japanese, and Italian groups. No second locus has reached the status of a routinely actionable clinical modifier. (hashizume2020diseasemechanismbiomarker pages 8-12)
- **Sex and hormones:** high post-pubertal androgen exposure is the major biological context determining penetrance. Full disease is overwhelmingly male; heterozygous females are usually asymptomatic or mildly affected because of lower androgen exposure and X-inactivation mosaicism. (pradat2020thefrenchnational pages 1-2, badders2018selectivemodulationof pages 1-3)
- **Age:** penetrance is age-dependent; onset is commonly in the fourth or fifth decade, although reported ranges extend from about 18 to 64 years. (querin2017kennedydisease(xlinked pages 1-5, cantara2024antisenseoligonucleotides(asos) pages 14-16)
- **Environmental/lifestyle:** no toxin, infection, smoking exposure, occupation, diet, or alcohol exposure has been established as a cause. Reduced activity, obesity, dyslipidemia, and insulin resistance can aggravate disability or cardiometabolic burden but are not proven initiators.

### Protective factors and gene–environment interaction

No validated naturally protective human AR allele or environmental exposure prevents SBMA. Lower androgen signaling is protective in female carriers and in castrated or hormonally manipulated animal models, but pharmacological androgen deprivation has anabolic, sexual, skeletal, and metabolic costs and is **not established preventive therapy**. The clearest gene–environment-like interaction is therefore **expanded AR × androgen ligand**: testosterone or dihydrotestosterone binding promotes AR activation, nuclear entry, altered co-regulator engagement, and toxicity. (hashizume2020diseasemechanismbiomarker pages 8-12, iida2019srcinhibitionattenuates pages 1-2, badders2018selectivemodulationof pages 1-3)

## 3. Phenotypes

| Phenotype and type | Typical characteristics and frequency | Suggested HPO terms |
|---|---|---|
| Proximal limb weakness/atrophy—sign and manifestation | Insidious, progressive, usually lower limbs first; approximately 70% first notice lower-limb weakness. One review reports proximal weakness in 97% and lower-limb involvement in 86.7%. Major effects are falls, stair-climbing difficulty, loss of work capacity, and eventually loss of ambulation. (hashizume2020diseasemechanismbiomarker pages 1-5, querin2017kennedydisease(xlinked pages 1-5) | HP:0003323 proximal muscle weakness; HP:0003690 limb muscle weakness; HP:0003202 muscle atrophy |
| Fasciculations and cramps—sign/symptom | Common in limb, facial, and perioral muscles; cramps or tremor may be prodromal and fluctuate. | HP:0002380 fasciculations; HP:0003394 muscle cramps |
| Postural hand tremor—sign | Can precede weakness by more than ten years and is an important prodromal clue. (hashizume2020diseasemechanismbiomarker pages 1-5) | HP:0001337 tremor; HP:0002173 postural tremor |
| Dysarthria—sign | Usually later and progressive; impairs communication and social participation. (pradat2020thefrenchnational pages 1-2) | HP:0001260 dysarthria |
| Dysphagia—symptom/sign | Reported in about 80%; progressive bulbar weakness increases choking, malnutrition, and aspiration-pneumonia risk. (querin2017kennedydisease(xlinked pages 1-5, querin2017kennedydisease(xlinked pages 5-9) | HP:0002015 dysphagia; HP:0002020 gastroesophageal reflux if present |
| Sensory neuropathy—sign/laboratory | Reduced reflexes and sensory nerve action potentials; sensory abnormalities were reported in 72–100% in reviewed cohorts, often subclinical. Neuropathic pain was reported in 58%. (querin2017kennedydisease(xlinked pages 5-9) | HP:0000763 sensory neuropathy; HP:0003401 hypoesthesia; HP:0009830 peripheral neuropathic pain |
| Respiratory impairment—functional abnormality | Peak expiratory flow and cough effectiveness may decline; frank ventilatory failure is less common than in ALS, but aspiration and respiratory infections are major mortality drivers. (hashizume2020diseasemechanismbiomarker pages 1-5, hashizume2020diseasemechanismbiomarker pages 15-19) | HP:0002093 respiratory insufficiency; HP:0002783 recurrent lower respiratory infection; HP:0006536 aspiration pneumonia |
| Gynecomastia—physical/endocrine | Suggestive but not universal; reflects partial androgen insensitivity. (pradat2020thefrenchnational pages 1-2) | HP:0000771 gynecomastia |
| Testicular atrophy, erectile dysfunction, reduced fertility—endocrine/reproductive | Variable and often under-recognized; substantially affects sexual health and family planning. (hashizume2020diseasemechanismbiomarker pages 1-5, badders2018selectivemodulationof pages 1-3) | HP:0000047 hypospadias is **not** typical; use HP:0008734 testicular atrophy, HP:0000802 erectile dysfunction, HP:0003251 male infertility as applicable |
| Metabolic/endocrine abnormalities—laboratory/systemic | Glucose intolerance/insulin resistance, dyslipidemia, abdominal obesity, and fatty liver occur more often than expected. (pradat2020thefrenchnational pages 1-2, zanovello2023unexpectedfrequencyof pages 1-2) | HP:0001952 glucose intolerance; HP:0003074 hyperglycemia; HP:0003124 hypercholesterolemia; HP:0001397 hepatic steatosis |
| CK elevation—laboratory | CK is commonly elevated and can reach up to 38-fold the upper limit in reviewed cases, reflecting prominent muscle pathology and sometimes causing misdiagnosis as myositis or muscular dystrophy. (querin2017kennedydisease(xlinked pages 5-9) | HP:0003236 elevated circulating creatine kinase |
| Cardiac electrical abnormality—sign/test | Brugada-pattern/repolarization abnormalities were reported in >10% in one Japanese cohort, including two sudden deaths among 144 patients, but this frequency was not reproduced consistently in Caucasian cohorts. (querin2017kennedydisease(xlinked pages 5-9) | HP:0011715 abnormal cardiac electrophysiology; HP:0030156 Brugada pattern |

**Quality of life.** Progressive weakness, fatigue, falls, loss of ambulation, speech/swallowing limitations, fertility concerns, and dependence in eating and other activities substantially reduce quality of life. Some patients ultimately require wheelchairs and assistance with daily tasks. Clinical studies use SF-36, ALSAQ-40, INQoL, SBMAFRS, AMAT, 2MWT, and 6MWT; however, robust phenotype-specific utility weights such as EQ-5D norms remain sparse. (querin2017kennedydisease(xlinked pages 15-19, NCT00303446 chunk 1, NCT06169046 chunk 1, badders2018selectivemodulationof pages 1-3)

## 4. Genetic and molecular information

- **Causal gene:** **AR**, androgen receptor; HGNC:644; NCBI Gene:367; OMIM gene 313700. The pathogenic repeat lies in exon 1 and expands the N-terminal polyglutamine tract.
- **Variant class:** germline, X-linked short tandem repeat expansion; HGVS representations should state the assay-derived repeat number rather than treating the disorder as a conventional SNV. It is a toxic gain-of-function allele with partial AR loss of normal function.
- **Classification:** expansions in the established disease range are pathogenic; borderline 36–38-repeat calls show laboratory and literature variability and require expert interpretation. Ordinary WES may not size the expansion reliably.
- **Population frequency:** a 2023 WGS study of 74,277 unrelated individuals found an expansion frequency of **1:3,182 X chromosomes** (95% CI 1:2,309–1:4,386; denominator 117,734 X chromosomes). Its WGS pipeline showed 100% sensitivity, 99% specificity, and 97.4% positive predictive value against fragment-PCR sizing. [Received July 28, 2022; published online February 17, 2023; https://doi.org/10.1093/brain/awad050.] (zanovello2023unexpectedfrequencyof pages 1-2)
- **Modifier genes:** putative modifiers include proteostasis/chaperone, co-regulator, transcriptional, and metabolic pathways, but no modifier is recommended for routine predictive testing.
- **Epigenetics:** altered chromatin/co-regulator engagement and transcription are integral downstream effects of mutant AR, but no validated diagnostic DNA-methylation signature or epigenetic therapy exists.
- **Chromosomal abnormalities:** no recurrent deletion, translocation, inversion, aneuploidy, or copy-number alteration defines classic SBMA; CMA, karyotyping, and FISH are therefore not first-line tests.
- **Somatic instability/mosaicism:** repeat sizing can vary modestly by tissue and assay, but classic disease is inherited through a germline X-chromosomal expansion; somatic cancer-style testing is not relevant.

## 5. Environmental information

No infectious agent, toxin, radiation exposure, pollution, or occupational exposure is established as causal or triggering. SBMA is not communicable. Lifestyle factors principally modify complications: appropriate activity may preserve conditioning, whereas inactivity, obesity, poor nutrition, and cardiometabolic disease can worsen function. Excessively fatiguing exercise should be avoided and programs individualized. Alcohol, smoking, and specific diets have no proven disease-modifying effect. The biologically decisive non-genetic exposure is endogenous androgen after puberty. (querin2017kennedydisease(xlinked pages 12-15, badders2018selectivemodulationof pages 1-3)

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic trigger:** expanded AR CAG repeat → elongated AR polyglutamine tract.
2. **Ligand activation:** testosterone/DHT binding causes conformational activation and nuclear translocation.
3. **Protein toxicity:** mutant AR misfolding, soluble oligomers/inclusions, abnormal AF-2 co-regulator binding, and impaired proteostasis alter transcription, trafficking, ubiquitin–proteasome and autophagy functions.
4. **Cellular stress:** mitochondrial dysfunction, oxidative stress, disturbed creatine handling, and aberrant Src–p130Cas/STAT3 signaling develop.
5. **Tissue pathology:** both lower motor neurons and skeletal myofibers are primary targets; denervation and cell-autonomous myofiber toxicity reinforce one another at the motor unit.
6. **Clinical output:** progressive weakness/atrophy, fasciculations, bulbar dysfunction, impaired cough, sensory abnormalities, and systemic androgen/metabolic manifestations. (hashizume2020diseasemechanismbiomarker pages 1-5, hashizume2020diseasemechanismbiomarker pages 8-12, cortes2014motorneurondegeneration pages 1-2, iida2019srcinhibitionattenuates pages 1-2)

### Human and model evidence

Human pathology and imaging show lower-motor-neuron loss plus mixed neurogenic and myopathic muscle changes. Skeletal muscle loses fast type-II fibers, relatively increases type-I fibers, and shifts from glycolytic toward oxidative metabolism. Serum creatinine begins declining before clinically evident weakness, supporting a preclinical muscle phase. (hashizume2020diseasemechanismbiomarker pages 1-5, hashizume2020diseasemechanismbiomarker pages 8-12)

The strongest experimental evidence that muscle is causal comes from BAC fxAR121 mice: muscle-specific excision of mutant AR completely rescued neuromuscular phenotypes despite persistent CNS expression, while peripheral AR-targeting ASO rescued weakness and premature death. This establishes skeletal muscle as a therapeutic target but does not prove that neuronal targeting is unnecessary in humans. (cortes2014motorneurondegeneration pages 1-2)

A phosphoprotein screen in AR-97Q mice found phosphorylated Src increased in spinal cord and muscle before symptoms; p130Cas was identified downstream, and Src inhibition improved behavioral and histopathological phenotypes. Increased p-Src was also observed in human autopsy spinal cord and muscle, providing cross-species support, although therapeutic efficacy remains preclinical. [Published September 2019; https://doi.org/10.1038/s41467-019-12282-7.] (iida2019srcinhibitionattenuates pages 1-2)

AF-2-domain screening in Drosophila identified tolfenamic acid and MEPB; MEPB then dose-dependently improved body weight, rotarod performance, grip strength, neuronal loss, neurogenic atrophy, and testicular atrophy in a mouse model. This validates selective AR co-regulator modulation as an androgen-sparing strategy, not as an approved treatment. [Published May 2018; https://doi.org/10.1038/nm.4500.] (badders2018selectivemodulationof pages 1-3)

### Molecular profiling and ontology suggestions

- **Transcriptomics:** transcriptional dysregulation is established, including impaired muscular creatine-transporter **SLC6A8** expression, but no transcriptomic panel is clinically validated. (iida2019srcinhibitionattenuates pages 1-2)
- **Proteomics/phosphoproteomics:** pre-onset Src/STAT3-pathway activation in mouse spinal cord and muscle; human tissue validation for p-Src. (iida2019srcinhibitionattenuates pages 1-2)
- **Metabolomics/lipidomics:** glycolytic-to-oxidative switching, insulin resistance, dyslipidemia, fatty liver, and mitochondrial deficits are reported; no diagnostic metabolomic signature exists. (hashizume2020diseasemechanismbiomarker pages 1-5, zanovello2023unexpectedfrequencyof pages 1-2)
- **Single-cell/spatial/multi-omics:** no mature, replicated human single-cell or spatial atlas is ready for diagnostic implementation. These are important evidence gaps.
- **Functional screens:** Drosophila compound screens, conditional mouse genetics, ASO experiments, and phosphoprotein assays have nominated AF-2, AR RNA, muscle AR, and Src as targets. (cortes2014motorneurondegeneration pages 1-2, iida2019srcinhibitionattenuates pages 1-2, badders2018selectivemodulationof pages 1-3)

Suggested terms: **GO:0005634** nucleus; **GO:0005739** mitochondrion; **GO:0005776** autophagosome; GO terms for androgen-receptor signaling, protein folding, macroautophagy, mitochondrial organization, oxidative stress response, skeletal-muscle atrophy, and motor-neuron apoptotic process. Cell terms include **CL:0000100 motor neuron**, **CL:0000187 muscle cell/myocyte**, skeletal myofiber, and dorsal-root-ganglion sensory neuron.

## 7. Anatomical structures affected

- **Primary nervous structures:** spinal-cord anterior horn and brainstem motor nuclei; motor axons and motor units. Suggested anatomy: UBERON spinal cord, ventral horn, brainstem, peripheral nerve, neuromuscular junction.
- **Primary muscular structures:** proximal lower-limb muscle early, followed by upper limbs, facial, masticatory, tongue, pharyngeal, laryngeal, and respiratory muscles. **UBERON:0001134 skeletal muscle tissue**.
- **Sensory system:** dorsal-root ganglia and sensory axons explain reduced sensory action potentials and sensory symptoms. (querin2017kennedydisease(xlinked pages 5-9)
- **Secondary/systemic sites:** testes, breast tissue, liver, adipose tissue, pancreas/metabolic system, and possibly cardiac conduction tissue.
- **Subcellular:** nucleus and cytoplasm for mutant AR; mitochondria, proteasome/autophagy–lysosome machinery, and sarcomeric/myofiber compartments.
- **Laterality:** generally bilateral and relatively symmetric, although functional asymmetry can occur; focal unilateral disease is atypical.

## 8. Temporal development

SBMA is chronic and insidious. Tremor, cramps, CK elevation, or declining creatinine can precede weakness by years; hand tremor may precede weakness by more than a decade. Typical weakness onset is 30–50 years, with a mean of approximately 43 years in the 2023 genomic-study background. Lower-limb weakness usually precedes upper-limb and bulbar impairment. (hashizume2020diseasemechanismbiomarker pages 1-5, querin2017kennedydisease(xlinked pages 1-5, zanovello2023unexpectedfrequencyof pages 1-2)

Progression is lifelong and approximately linear only at a cohort level; a 2024 ASO review cites about **2% annual muscle-strength decline**. Individual trajectories vary. One review reported mean life expectancy of 71.3 years and mean disease duration of 27.3 years, but these older cohort estimates should not be interpreted as universal survival predictions. There is no relapsing-remitting course or spontaneous remission. (querin2017kennedydisease(xlinked pages 1-5, cantara2024antisenseoligonucleotides(asos) pages 14-16)

Clinically useful stages are: prodromal biochemical/tremor phase; early ambulatory limb weakness; intermediate multisystem and bulbar involvement; advanced loss of ambulation with aspiration/cough risk. Early molecular intervention is theoretically preferable before irreversible motor-unit loss, but no validated human treatment window has been defined.

## 9. Inheritance and population epidemiology

SBMA is X-linked. A heterozygous mother has a 50% probability of transmitting the expanded allele in each pregnancy; sons inheriting it are at high age-dependent risk of disease, while daughters become carriers and usually have no or minor neuromuscular manifestations. An affected male transmits the expansion to all daughters and no sons. Penetrance in expansion-positive males is substantial but appears age- and repeat-dependent rather than absolutely complete, especially near the threshold. Expressivity is variable. Anticipation may occur through intergenerational repeat change, but it is less predictable than in some repeat disorders; counseling should not promise a specific onset from repeat length. Consanguinity is not relevant to X-linked transmission, and germline mosaicism is not a major recognized mechanism.

Classical prevalence estimates are **1–2 per 100,000** or about 1:30,000 males; older incidence estimates include approximately 1:400,000/year. Geographic clusters include Finland’s Vasa region, where 13 cases among 85,000 males yielded 1:6,538, historically attributed to a founder effect. (hashizume2020diseasemechanismbiomarker pages 1-5, querin2017kennedydisease(xlinked pages 1-5, zanovello2023unexpectedfrequencyof pages 1-2)

The pivotal 2023 WGS analysis found pathogenic expansions roughly tenfold more frequently than classical diagnosed prevalence and modeled male disease prevalence at **1:6,887**, more than fourfold above the commonly reported estimate. The authors explicitly concluded that the discrepancy may reflect “underdiagnosis…reduced penetrance, and/or pleomorphic clinical manifestations.” This is a modeled prevalence—not a population-screened clinical case count. (zanovello2023unexpectedfrequencyof pages 1-2)

Men comprise nearly all fully affected patients; female carriers can have cramps, tremor, or mild weakness. Founder effects and diagnostic access produce geographic variation. A current carrier frequency cannot be reduced to one global figure beyond the 2023 estimate of approximately 1:3,182 X chromosomes in the aggregated genomic cohorts.

## 10. Diagnostics

### Recommended pathway

1. Suspect SBMA in an adult man with slowly progressive lower-motor-neuron weakness, often lower-limb predominant, plus tremor/cramps, bulbar dysfunction, gynecomastia, infertility, sensory abnormalities, high CK, or a compatible maternal family history.
2. Perform neurologic, bulbar, respiratory, endocrine/metabolic, reproductive, and cardiac assessment.
3. Confirm with **targeted AR CAG-repeat sizing**, generally fragment-length PCR with an expansion-appropriate validated assay.
4. Use EMG/NCS, CK, creatinine, liver enzymes, glucose/HbA1c, lipid profile, ECG, pulmonary function, and swallow assessment to characterize burden and exclude mimics. The French consensus recommends initial evaluation in a specialist motor-neuron/neuromuscular center. (pradat2020thefrenchnational pages 1-2)

### Tests and biomarkers

- **EMG:** diffuse chronic denervation/reinnervation; fasciculations may occur. Sensory NCS can show reduced SNAPs despite modest symptoms. (pradat2020thefrenchnational pages 1-2, querin2017kennedydisease(xlinked pages 5-9)
- **Blood:** elevated CK and transaminases of muscle origin; falling creatinine correlates with muscle loss and may precede weakness. Glucose, lipids, and liver indices identify systemic disease. (hashizume2020diseasemechanismbiomarker pages 1-5)
- **Functional:** SBMAFRS, AMAT, quantitative muscle testing, grip strength, timed up-and-go, 2MWT/6MWT, tongue pressure, FVC and peak expiratory flow.
- **Imaging:** muscle MRI, fat fraction/infiltration, and lean muscle volume are promising progression and pharmacodynamic biomarkers; they are not diagnostic substitutes for genetic testing. (hashizume2020diseasemechanismbiomarker pages 1-5, NCT06411912 chunk 1)
- **Swallowing:** clinical examination and instrumental videofluoroscopic or endoscopic assessment when choking, weight loss, or recurrent infection occurs.
- **Biopsy:** usually unnecessary after molecular confirmation; if performed, muscle can show mixed neurogenic group atrophy and myopathic changes. Nerve or spinal-cord biopsy has no clinical role.

### Genetic modalities

Targeted repeat-expansion testing is first line. WGS can detect the expansion using validated repeat callers plus orthogonal confirmation—the 2023 ExpansionHunter pipeline performed well—but routine short-read WES, ordinary multigene panels without repeat analysis, CMA, karyotyping, FISH, and mitochondrial-DNA testing can miss or do not address the causal lesion. RNA-seq, proteomics, metabolomics, epigenomics, and liquid biopsy remain research tools. (zanovello2023unexpectedfrequencyof pages 1-2)

### Differential diagnosis and screening

Key mimics are ALS, progressive muscular atrophy, other non-5q hereditary motor neuropathies/SMA, limb-girdle muscular dystrophy, inflammatory myopathy, inclusion-body myositis, myotonic dystrophy, Pompe disease, and Charcot–Marie–Tooth disease. Sensory abnormalities, endocrine signs, very slow progression, maternal X-linked history, and AR testing favor SBMA over ALS. (querin2017kennedydisease(xlinked pages 5-9)

Population or newborn screening is not standard because SBMA is adult-onset, rare, and lacks an approved presymptomatic disease-modifying therapy. **Cascade testing** of at-risk adult relatives is appropriate after genetic counseling. Prenatal and preimplantation genetic testing are technically possible once the familial expansion is documented.

## 11. Outcome and prognosis

SBMA usually progresses more slowly and has longer survival than ALS. There are no broadly validated 5- or 10-year survival tables. Older aggregate data reported mean life expectancy around 71.3 years and mean duration 27.3 years, but ascertainment, geography, repeat size, and supportive care limit generalizability. (querin2017kennedydisease(xlinked pages 1-5)

Major morbidity includes falls, fractures, loss of ambulation, fatigue, chronic pain/cramps, communication and swallowing disability, malnutrition, aspiration, sexual/reproductive dysfunction, diabetes/dyslipidemia/fatty liver, and caregiver dependence. Respiratory infectious disease accounts for more than half of deaths in one review, with aspiration pneumonia a prominent mechanism; invasive ventilatory failure is comparatively uncommon. (hashizume2020diseasemechanismbiomarker pages 1-5, querin2017kennedydisease(xlinked pages 12-15)

Earlier onset is associated with longer CAG length. Functional baseline, bulbar involvement, mobility, cough/swallow safety, body composition, and cardiometabolic disease are clinically meaningful prognostic features. Creatinine, muscle MRI fat fraction/volume, 6MWT, and SBMAFRS are promising longitudinal markers, but none independently predicts an individual outcome with sufficient accuracy for deterministic counseling. (hashizume2020diseasemechanismbiomarker pages 1-5, querin2017kennedydisease(xlinked pages 15-19)

## 12. Treatment and current applications

### Current real-world standard

There is **no approved, proven disease-modifying treatment**. Multidisciplinary supportive care is standard: individualized physiotherapy and moderate exercise; occupational therapy, mobility aids, fall prevention and orthoses; speech/communication therapy; swallow and dietetic assessment; texture modification and gastrostomy when necessary; cough augmentation, breath stacking, secretion clearance, vaccination, and prompt treatment of respiratory infection; pain/cramp treatment; and management of diabetes, dyslipidemia, fatty liver, erectile dysfunction, and fertility concerns. Non-invasive ventilation is needed less often than in ALS but should be used when physiologically indicated. Testosterone replacement is not supported and may theoretically worsen ligand-dependent toxicity. (pradat2020thefrenchnational pages 1-2)

Suggested NCIT intervention concepts include physical therapy, occupational therapy, speech therapy, nutritional support, gastrostomy, noninvasive ventilation, cough-assist therapy, genetic counseling, and supportive care. Drug concepts should be annotated as investigational unless approved for another indication.

### Historical pharmacological programs

- **Leuprorelin/GnRH agonism:** reduced mutant AR accumulation and showed possible swallowing signals in small studies, but efficacy was insufficient to establish routine therapy and anti-androgen adverse effects include sexual dysfunction and loss of anabolic muscle support. (hashizume2020diseasemechanismbiomarker pages 1-5, iida2019srcinhibitionattenuates pages 1-2)
- **Dutasteride:** NIH phase 2, randomized quadruple-masked trial, actual n=57, 0.5 mg/day for 24 months; primary endpoint was quantitative muscle-strength change with functional, SF-36, neurophysiological, hormone, and CK outcomes. It did not establish an effective standard treatment. ClinicalTrials.gov: https://clinicaltrials.gov/study/NCT00303446. (NCT00303446 chunk 1)
- **BVS857, an IGF-1 mimetic:** completed phase 2, n=37, assessing safety and MRI thigh-muscle volume; immunogenicity and limited preliminary efficacy prevented clinical adoption. ClinicalTrials.gov: https://clinicaltrials.gov/study/NCT02024932. (NCT02024932 chunk 1)
- **Clenbuterol:** a small earlier cohort suggested motor improvement but CK elevation and cardiovascular concerns remained; it is not standard care. (querin2017kennedydisease(xlinked pages 12-15)

### Recent development pipeline

- **AJ201/JM17:** completed phase 1/2a randomized study (2023–April 2024), n=25, 600 mg/day for 12 weeks. It evaluated safety, PK, and change in mutant AR protein in skeletal-muscle biopsies; no efficacy conclusion should be drawn from a registry record without peer-reviewed results. https://clinicaltrials.gov/study/NCT05517603. (NCT05517603 chunk 1)
- **NIDO-361, PIONEER KD:** phase 2 randomized placebo-controlled study begun March 2024, actual n=54, oral 100 mg then 200 mg daily for 12 months. Primary measures include thigh/whole-body lean-muscle volume and safety; secondary measures include m-SBMAFRS, walking, actigraphy, and grip. The registry later lists completion, but peer-reviewed clinical efficacy was not present in the retrieved 2023–2024 evidence. https://clinicaltrials.gov/study/NCT06411912. (NCT06411912 chunk 1)
- **BetaSBMA clenbuterol:** phase 2, estimated n=90, 0.04 mg/day for 48 weeks; primary endpoint 6MWT, with SBMAFRS, AMAT, FVC, creatinine, ALSAQ-40, and INQoL. https://clinicaltrials.gov/study/NCT06169046. (NCT06169046 chunk 1)
- **Mexiletine Med-SBMA:** phase 2/3 study initiated in 2025, estimated n=68, 300 mg/day for 12 weeks; measures ALSFRS-R/SBMAFRS, strength, tongue pressure, walking, FVC and PEF. It excludes Brugada-pattern ECG and significant conduction disease. https://clinicaltrials.gov/study/NCT06862596. This is a post-2024 registry development, included for current context. (NCT06862596 chunk 1)

### Advanced therapeutics

AR-lowering ASOs and siRNAs improve disease in mice, including near-complete AR-protein reduction and phenotypic rescue; key translational problems are safe chronic suppression, preserving normal AR function, and delivery to both muscle and CNS. A 2024 review states that ASOs can “decrease levels of toxic proteins” and identifies SBMA as an active target, but no SBMA ASO is approved. [April 2024; https://doi.org/10.3390/ijms25094809.] (cantara2024antisenseoligonucleotides(asos) pages 14-16)

Gene replacement is inappropriate for a toxic gain-of-function allele; editing or allele-selective silencing is conceptually attractive but preclinical. Stem-cell therapy, immunotherapy, and surgery do not address the causal disease. There is no validated SBMA pharmacogenomic dosing guideline or combination algorithm.

## 13. Prevention

Primary lifestyle prevention is not possible because the initiating lesion is inherited. Prevention is therefore reproductive and complication-oriented:

- **Primary/genetic:** pedigree assessment, genetic counseling, informed carrier/cascade testing, and discussion of preimplantation or prenatal testing. Testing minors for an adult-onset condition without childhood intervention generally requires careful ethical justification.
- **Secondary:** recognize tremor, cramps, high CK, gynecomastia, sensory NCS abnormalities, or family history early; confirm molecularly and establish baseline swallow, respiratory, cardiac, metabolic, and functional assessments.
- **Tertiary:** fall prevention, tailored exercise, healthy weight and metabolic control, aspiration precautions, cough augmentation, nutrition support, respiratory-infection vaccination according to national schedules, and prompt treatment of pneumonia. Vaccines prevent infections, not SBMA itself. (pradat2020thefrenchnational pages 1-2, querin2017kennedydisease(xlinked pages 12-15)

No prophylactic anti-androgen, ASO, vitamin, diet, or supplement has established benefit in asymptomatic carriers.

## 14. Other species and natural disease

**AR orthologs** are highly conserved across mammals and are present in mouse (*Mus musculus*, NCBI Taxon 10090), rat (*Rattus norvegicus*, 10116), dog (*Canis lupus familiaris*, 9615), zebrafish (*Danio rerio*, 7955), fruit fly (*Drosophila melanogaster*, 7227; nuclear-receptor modeling rather than a direct human-equivalent AR physiology), and nematodes. No well-established naturally occurring companion-animal or wildlife disease caused by the homologous pathogenic polyglutamine expansion was identified in the retrieved evidence. Thus, veterinary breed/VBO associations and natural cross-species prevalence are not established.

There is no infectious transmission, zoonotic potential, or cross-species contagion. Comparative value comes from conserved steroid-receptor activation, proteostasis, transcription, and muscle–motor-neuron interactions rather than natural disease.

## 15. Model organisms and experimental systems

- **Transgenic and knock-in mice:** AR-97Q and other expanded-AR lines reproduce androgen-dependent weakness, atrophy, motor-neuron and muscle pathology, nuclear AR accumulation, endocrine abnormalities, and shortened survival. They enabled Src-inhibitor, hormonal, chaperone, IGF-1, and ASO studies. BAC fxAR121 conditional mice demonstrated muscle-driven disease. Limitations include very long repeats, supraphysiologic expression, rapid course, strain/sex effects, and incomplete replication of decades-long human disease. (cortes2014motorneurondegeneration pages 1-2, iida2019srcinhibitionattenuates pages 1-2)
- **Drosophila:** expanded human AR causes androgen-dependent lethality, locomotor and neuromuscular-junction defects; its speed and genetic tractability enabled AF-2 compound screening. Limitations are divergent endocrine physiology and simplified neuromuscular anatomy. (badders2018selectivemodulationof pages 1-3)
- **Cellular systems:** transfected neuronal and muscle lines, primary myotubes, and patient-derived cells support studies of AR localization, aggregation, transcription, autophagy, mitochondria, Src/p130Cas, and oligonucleotide knockdown. They lack intact motor-unit and endocrine physiology.
- **Patient iPSC-derived motor neurons/myocytes and co-cultures:** promising for isogenic CRISPR controls and human-specific drug screening, but maturation, aging, and systemic androgen exposure remain limitations.
- **Organoids/spatial systems:** not yet validated as standard SBMA models.

Model resources should be sought in MGI, IMSR/MMRRC, FlyBase, Cellosaurus, GEO/SRA, and relevant patient-biobank repositories. The most informative translational strategy is triangulation across muscle, motor-neuron, and whole-animal systems rather than reliance on a single model.

## Expert synthesis and evidence gaps

The contemporary view is that SBMA is **not simply a motor-neuron disease**: it is an androgen-dependent, multisystem polyglutamine disorder in which skeletal muscle is an initiating and therapeutically important compartment. This view is supported by human mixed neurogenic/myopathic pathology, preclinical muscle-specific rescue, and muscle-focused biomarkers and trials. (hashizume2020diseasemechanismbiomarker pages 1-5, cortes2014motorneurondegeneration pages 1-2)

The most consequential recent epidemiologic development is the 2023 observation that pathogenic AR expansions may be much more common than diagnosed SBMA. It argues for greater diagnostic vigilance in adult men labeled with ALS, limb-girdle dystrophy, inflammatory myopathy, unexplained high CK, infertility, or metabolic disease, while also raising unresolved questions about reduced penetrance and pleiotropy. (zanovello2023unexpectedfrequencyof pages 1-2)

Major gaps are the absence of an approved disease-modifying therapy; limited prospective, ethnically diverse natural-history cohorts; uncertain penetrance of borderline repeats; lack of validated surrogate endpoints; sparse female-carrier and quality-of-life data; and limited human single-cell, spatial, and longitudinal multi-omic datasets. Registry and preclinical signals should not be conflated with clinical benefit.

References

1. (pradat2020thefrenchnational pages 1-2): P. Pradat, E. Bernard, P. Corcia, P. Couratier, C. Jublanc, G. Querin, C. Morélot Panzini, F. Salachas, C. Vial, K. Wahbi, P. Bede, C. Desnuelle, Nadine Andoni Giorgia Gianni Thierry Cédric Cyril Jean Cl Le Forestier Echaniz-Laguna Querin Sorarù Perez Ra, N. le Forestier, A. Echaniz-Laguna, G. Querin, G. Soraru', T. Perez, Cédric Ramos, C. Goizet, J. Desport, M. Pugeat, B. Pichon, S. Maniez, J. Robillard, C. Coupé, Laurence Laurier Betram, Sandra Roy Bellina, N. Lévêque, J. Penot, and Valérie Goutines Caramel. The french national protocol for kennedy’s disease (sbma): consensus diagnostic and management recommendations. Orphanet Journal of Rare Diseases, Apr 2020. URL: https://doi.org/10.1186/s13023-020-01366-z, doi:10.1186/s13023-020-01366-z. This article has 75 citations and is from a peer-reviewed journal.

2. (zanovello2023unexpectedfrequencyof pages 1-2): Matteo Zanovello, Kristina Ibáñez, Anna-Leigh Brown, Prasanth Sivakumar, Alessandro Bombaci, Liana Santos, Joke J F A van Vugt, Giuseppe Narzisi, Ramita Karra, Sonja W Scholz, Jinhui Ding, J Raphael Gibbs, Adriano Chiò, Clifton Dalgard, Ben Weisburd, John C Ambrose, Prabhu Arumugam, Roel Bevers, Marta Bleda, Freya Boardman-Pretty, Christopher R Boustred, Helen Brittain, Mark J Caulfield, Georgia C Chan, Greg Elgar, Tom Fowler, Adam Giess, Angela Hamblin, Shirley Henderson, Tim J P Hubbard, Rob Jackson, Louise J Jones, Dalia Kasperaviciute, Melis Kayikci, Athanasios Kousathanas, Lea Lahnstein, Sarah E A Leigh, Ivonne U S Leong, Javier F Lopez, Fiona Maleady-Crowe, Meriel McEntagart, Federico Minneci, Loukas Moutsianas, Michael Mueller, Nirupa Murugaesu, Anna C Need, Peter O’Donovan, Chris A Odhams, Christine Patch, Mariana Buongermino Pereira, Daniel Perez-Gil, John Pullinger, Tahrima Rahim, Augusto Rendon, Tim Rogers, Kevin Savage, Kushmita Sawant, Richard H Scott, Afshan Siddiq, Alexander Sieghart, Samuel C Smith, Alona Sosinsky, Alexander Stuckey, Mélanie Tanguy, Ana Lisa Taylor Tavares, Ellen R A Thomas, Simon R Thompson, Arianna Tucci, Matthew J Welland, Eleanor Williams, Katarzyna Witkowska, Suzanne M Wood, Wouter Van Rheenen, Sara L Pulit, Annelot M Dekker, Ahmad Al Khleifat, William J Brands, Alfredo Iacoangeli, Kevin P Kenna, Ersen Kavak, Maarten Kooyman, Russell L McLaughlin, Bas Middelkoop, Matthieu Moisse, Raymond D Schellevis, Aleksey Shatunov, William Sproviero, Gijs H P Tazelaar, Rick A A Van der Spek, Perry T C Van Doormaal, Kristel R Van Eijk, Joke Van Vugt, A Nazli Basak, Ian P Blair, Jonathan D Glass, Orla Hardiman, Winston Hide, John E Landers, Jesus S Mora, Karen E Morrison, Stephen Newhouse, Wim Robberecht, Christopher E Shaw, Pamela J Shaw, Philip Van Damme, Michael A Van Es, Naomi R Wray, Ammar Al-Chalabi, Leonard H Van den Berg, Jan H Veldink, Michael G Hanna, Linda Greensmith, Hemali Phatnani, Jan H Veldink, Bryan J Traynor, James Polke, Henry Houlden, Pietro Fratta, and Arianna Tucci. Unexpected frequency of the pathogenic ar cag repeat expansion in the general population. Brain, 146:2723-2729, Feb 2023. URL: https://doi.org/10.1093/brain/awad050, doi:10.1093/brain/awad050. This article has 37 citations and is from a highest quality peer-reviewed journal.

3. (NCT06169046 chunk 1): Gianni Soraru. A Placebo-controlled Study of Clenbuterol in Spinal and Bulbar Muscular Atrophy. Gianni Soraru. 2024. ClinicalTrials.gov Identifier: NCT06169046

4. (hashizume2020diseasemechanismbiomarker pages 8-12): Atsushi Hashizume, Kenneth H Fischbeck, Maria Pennuto, Pietro Fratta, and Masahisa Katsuno. Disease mechanism, biomarker and therapeutics for spinal and bulbar muscular atrophy (sbma). Journal of Neurology, Neurosurgery &amp; Psychiatry, 91:1085-1091, Sep 2020. URL: https://doi.org/10.1136/jnnp-2020-322949, doi:10.1136/jnnp-2020-322949. This article has 73 citations.

5. (cantara2024antisenseoligonucleotides(asos) pages 14-16): Silvia Cantara, Giorgia Simoncelli, and Claudia Ricci. Antisense oligonucleotides (asos) in motor neuron diseases: a road to cure in light and shade. International Journal of Molecular Sciences, Apr 2024. URL: https://doi.org/10.3390/ijms25094809, doi:10.3390/ijms25094809. This article has 47 citations.

6. (NCT06862596 chunk 1): Masahisa Katsuno. Clinical Trial of Mexiletine Hydrochloride for Spinal and Bulbar Muscular Atrophy. Masahisa Katsuno. 2025. ClinicalTrials.gov Identifier: NCT06862596

7. (querin2017kennedydisease(xlinked pages 1-5): G. Querin, Gianni Sorarù, and P. Pradat. Kennedy disease (x-linked recessive bulbospinal neuronopathy): a comprehensive review from pathophysiology to therapy. Revue neurologique, 173 5:326-337, May 2017. URL: https://doi.org/10.1016/j.neurol.2017.03.019, doi:10.1016/j.neurol.2017.03.019. This article has 52 citations and is from a peer-reviewed journal.

8. (hashizume2020diseasemechanismbiomarker pages 1-5): Atsushi Hashizume, Kenneth H Fischbeck, Maria Pennuto, Pietro Fratta, and Masahisa Katsuno. Disease mechanism, biomarker and therapeutics for spinal and bulbar muscular atrophy (sbma). Journal of Neurology, Neurosurgery &amp; Psychiatry, 91:1085-1091, Sep 2020. URL: https://doi.org/10.1136/jnnp-2020-322949, doi:10.1136/jnnp-2020-322949. This article has 73 citations.

9. (querin2017kennedydisease(xlinked pages 5-9): G. Querin, Gianni Sorarù, and P. Pradat. Kennedy disease (x-linked recessive bulbospinal neuronopathy): a comprehensive review from pathophysiology to therapy. Revue neurologique, 173 5:326-337, May 2017. URL: https://doi.org/10.1016/j.neurol.2017.03.019, doi:10.1016/j.neurol.2017.03.019. This article has 52 citations and is from a peer-reviewed journal.

10. (badders2018selectivemodulationof pages 1-3): Nisha M Badders, Ane Korff, Helen C Miranda, Pradeep K Vuppala, Rebecca B Smith, Brett J Winborn, Emmanuelle R Quemin, Bryce L Sopher, Jennifer Dearman, James Messing, Nam Chul Kim, Jennifer Moore, Brian D Freibaum, Anderson P Kanagaraj, Baochang Fan, Heather Tillman, Ping-Chung Chen, Yingzhe Wang, Burgess B. Freeman III, Yimei Li, Hong Joo Kim, Albert R La Spada, and J Paul Taylor. Selective modulation of the androgen receptor activation function-2 domain rescues degeneration in spinal bulbar muscular atrophy. Nature medicine, 24:427-437, Mar 2018. URL: https://doi.org/10.1038/nm.4500, doi:10.1038/nm.4500. This article has 57 citations and is from a highest quality peer-reviewed journal.

11. (querin2017kennedydisease(xlinked pages 12-15): G. Querin, Gianni Sorarù, and P. Pradat. Kennedy disease (x-linked recessive bulbospinal neuronopathy): a comprehensive review from pathophysiology to therapy. Revue neurologique, 173 5:326-337, May 2017. URL: https://doi.org/10.1016/j.neurol.2017.03.019, doi:10.1016/j.neurol.2017.03.019. This article has 52 citations and is from a peer-reviewed journal.

12. (NCT05517603 chunk 1):  A Study to Evaluate Safety, Tolerability, Pharmacokinetics, and Pharmacodynamics Of AJ201 In Patients. AnnJi Pharmaceutical Co., Ltd.. 2023. ClinicalTrials.gov Identifier: NCT05517603

13. (cortes2014motorneurondegeneration pages 1-2): Constanza J Cortes and Albert R La Spada. Motor neuron degeneration in spinal and bulbar muscular atrophy is a skeletal muscle-driven process: relevance to therapy development and implications for related motor neuron diseases. Rare Diseases, 2:e962402, Jan 2014. URL: https://doi.org/10.4161/2167549x.2014.962402, doi:10.4161/2167549x.2014.962402. This article has 9 citations.

14. (iida2019srcinhibitionattenuates pages 1-2): M. Iida, K. Sahashi, Naohide Kondo, H. Nakatsuji, G. Tohnai, Y. Tsutsumi, S. Noda, Ayuka Murakami, Kazunari Onodera, Y. Okada, M. Nakatochi, Yuka Tsukagoshi Okabe, S. Shimizu, M. Mizuno, H. Adachi, H. Okano, G. Sobue, and M. Katsuno. Src inhibition attenuates polyglutamine-mediated neuromuscular degeneration in spinal and bulbar muscular atrophy. Nature Communications, Sep 2019. URL: https://doi.org/10.1038/s41467-019-12282-7, doi:10.1038/s41467-019-12282-7. This article has 24 citations and is from a highest quality peer-reviewed journal.

15. (hashizume2020diseasemechanismbiomarker pages 15-19): Atsushi Hashizume, Kenneth H Fischbeck, Maria Pennuto, Pietro Fratta, and Masahisa Katsuno. Disease mechanism, biomarker and therapeutics for spinal and bulbar muscular atrophy (sbma). Journal of Neurology, Neurosurgery &amp; Psychiatry, 91:1085-1091, Sep 2020. URL: https://doi.org/10.1136/jnnp-2020-322949, doi:10.1136/jnnp-2020-322949. This article has 73 citations.

16. (NCT00303446 chunk 1):  Dutasteride to Treat Spinal and Bulbar Muscular Atrophy (SBMA). National Institute of Neurological Disorders and Stroke (NINDS). 2006. ClinicalTrials.gov Identifier: NCT00303446

17. (NCT06411912 chunk 1):  A Study of NIDO-361 in Patients With SBMA. Nido Biosciences, Inc.. 2024. ClinicalTrials.gov Identifier: NCT06411912

18. (NCT02024932 chunk 1):  Safety, Tolerability, and Efficacy of BVS857 in Patients With Spinal and Bulbar Muscular Atrophy. Novartis Pharmaceuticals. 2014. ClinicalTrials.gov Identifier: NCT02024932

19. (querin2017kennedydisease(xlinked pages 19-22): G. Querin, Gianni Sorarù, and P. Pradat. Kennedy disease (x-linked recessive bulbospinal neuronopathy): a comprehensive review from pathophysiology to therapy. Revue neurologique, 173 5:326-337, May 2017. URL: https://doi.org/10.1016/j.neurol.2017.03.019, doi:10.1016/j.neurol.2017.03.019. This article has 52 citations and is from a peer-reviewed journal.

20. (querin2017kennedydisease(xlinked pages 15-19): G. Querin, Gianni Sorarù, and P. Pradat. Kennedy disease (x-linked recessive bulbospinal neuronopathy): a comprehensive review from pathophysiology to therapy. Revue neurologique, 173 5:326-337, May 2017. URL: https://doi.org/10.1016/j.neurol.2017.03.019, doi:10.1016/j.neurol.2017.03.019. This article has 52 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Bulbospinal_Muscular_Atrophy-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 8 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.