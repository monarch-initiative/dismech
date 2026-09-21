---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-19T09:19:54.136670'
end_time: '2026-08-19T09:33:44.753786'
duration_seconds: 830.62
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hypomyelinating Leukodystrophy 10
  mondo_id: ''
  category: Mendelian
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
citation_count: 12
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 10
  validator_version: 0.2.1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Hypomyelinating_Leukodystrophy_10-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hypomyelinating_Leukodystrophy_10-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypomyelinating Leukodystrophy 10
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hypomyelinating Leukodystrophy 10** covering all of the
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

# Hypomyelinating Leukodystrophy 10 (HLD10 / PYCR2 Deficiency): Comprehensive Disease Characterization

**Disease:** Hypomyelinating Leukodystrophy 10 (HLD10)
**Gene:** *PYCR2* (Pyrroline-5-Carboxylate Reductase 2)
**Category:** Mendelian, autosomal recessive
**Key identifiers:** OMIM #616420 · MONDO:0014635 · locus 1q42.12

---

## Summary

Hypomyelinating leukodystrophy 10 (HLD10) is a rare autosomal recessive neurometabolic leukodystrophy caused by biallelic loss-of-function and missense variants in **PYCR2**, the gene encoding the mitochondrial enzyme pyrroline-5-carboxylate reductase 2, which catalyzes the final step of L-proline biosynthesis. The disorder was first defined molecularly in 2015 by Nakayama et al., who mapped it to chromosome 1q42.12 and demonstrated that biallelic *PYCR2* mutations cause postnatal microcephaly with hypomyelination ([PMID: 25865492](https://pubmed.ncbi.nlm.nih.gov/25865492/)). Affected children characteristically present with postnatally acquired (progressive) microcephaly, moderate-to-profound global developmental delay, failure to thrive, craniofacial dysmorphism, hyperkinetic movements, axial hypotonia with variable appendicular spasticity, and seizures. Brain MRI shows hypomyelination/delayed myelination, thin corpus callosum, and generalized white-matter volume loss. Severely affected patients do not survive beyond the first decade of life.

Mechanistically, the disease is now understood as a mitochondrial and amino-acid metabolic disorder with a specific neurotoxic endpoint. Loss of PYCR2 destabilizes the enzyme, depletes PYCR1 in neural lineages, decreases mitochondrial membrane potential, and increases susceptibility to apoptosis under oxidative stress. The pivotal mechanistic insight, provided by Escande-Beillard et al. (2020), is that loss of PYCR2 upregulates **SHMT2**, driving excessive cerebral glycine that produces axonal beading and neurodegeneration; knockdown of SHMT2 partially rescues these deficits, nominating the glycine metabolic pathway as a therapeutic target ([PMID: 32330411](https://pubmed.ncbi.nlm.nih.gov/32330411/)). Notably, routine peripheral/serum metabolic profiles are normal, so the pathology is a compartmentalized cerebral metabolic derangement rather than a systemically measurable one.

The phenotypic spectrum is broader than originally appreciated. While the canonical presentation is a severe, often lethal infantile leukodystrophy, a milder allele (p.Val128Ala) has been reported to cause hereditary spastic paraplegia (HSP) in late childhood without overt hypomyelinating leukodystrophy. Population genetics are shaped by consanguinity and founder effects, exemplified by the Thai c.400G>A (p.Val134Met) founder allele on a shared 2.3 Mb haplotype estimated at ~1450 years old. There is no disease-specific or curative therapy; management is supportive, and SHMT2/glycine-lowering represents the leading mechanism-based experimental direction.

---

## Key Findings

### Finding 1 — HLD10 is an autosomal recessive disorder caused by biallelic *PYCR2* variants

HLD10 (OMIM #616420) maps to chromosome **1q42.12** and is caused by biallelic (homozygous or compound heterozygous) loss-of-function and missense variants in *PYCR2*, encoding pyrroline-5-carboxylate reductase 2, a **mitochondrial enzyme catalyzing the final step of proline biosynthesis**. Zaki et al. identified 11 consanguineous families, establishing autosomal recessive inheritance. The disorder's molecular architecture is consistent across cohorts: the majority of reported cases are homozygous with consanguineous family histories, with only rare compound-heterozygous exceptions.

> *"This is an autosomal recessive disorder mapped to chromosome 1q42.12 due to mutations in the PYCR2 gene, encoding an enzyme involved in proline synthesis in mitochondria."* — [PMID: 27130255](https://pubmed.ncbi.nlm.nih.gov/27130255/)

> *"PYCR2 pathogenic variants lead to an autosomal recessive hypomyelinating leukodystrophy 10 (HLD10), characterized by global developmental delay, microcephaly, facial dysmorphism, movement disorder, and hypomyelination."* — [PMID: 34037307](https://pubmed.ncbi.nlm.nih.gov/34037307/)

### Finding 2 — Core clinical phenotype: postnatal microcephaly, developmental delay, hypomyelination, poor survival

The characteristic presentation includes postnatally acquired (**progressive**) microcephaly, moderate-to-profound global developmental delay, failure to thrive, craniofacial dysmorphism, hyperkinetic movements, axial hypotonia with variable appendicular spasticity, and seizures. Brain MRI shows hypomyelination/delayed myelination, thin corpus callosum, global brain/white-matter atrophy, and T2 white-matter hyperintensities. Severely affected patients do not survive beyond the first decade. A crucial diagnostic clue is that **routine serum metabolic profiles are unremarkable/normal**, distinguishing HLD10 from classical inborn errors of metabolism with peripheral biochemical signatures.

> *"The characteristic clinical presentation of patients with PYCR2 mutations included failure to thrive, microcephaly, craniofacial dysmorphism, progressive psychomotor disability, hyperkinetic movements, and axial hypotonia with variable appendicular spasticity. Patients did not survive beyond the first decade of life."* — [PMID: 27130255](https://pubmed.ncbi.nlm.nih.gov/27130255/)

> *"All patients presented with postnatally acquired microcephaly, moderate to profound global developmental delay, and failure to thrive. Brain MRI in these patients showed thin corpus callosum, delayed myelination, and generalized white-matter volume loss."* — [PMID: 27860360](https://pubmed.ncbi.nlm.nih.gov/27860360/)

### Finding 3 — Mechanism: PYCR2 loss raises cerebral glycine via SHMT2 upregulation, driving neurodegeneration

Escande-Beillard et al. (2020) solved the PYCR2 apo-enzyme crystal structure, showed that a p.Gly249Val mutation at the dimer interface lowers enzymatic activity, and demonstrated that *Pycr2*-knockout mice phenocopy the human disorder and deplete PYCR1 in neural lineages. In situ neurotransmitter quantification in mutant mouse and patient brains revealed encephalopathy driven by **excessive cerebral glycine caused by SHMT2 upregulation**; SHMT2 knockdown partially reversed axonal beading and rescued neurite length in *Pycr2*-KO neurons. Zaki et al. independently showed that both missense and nonsense mutations impair PYCR2 protein multimerization, the biophysical basis of loss of function.

> *"loss of PYCR2 upregulates SHMT2, which is responsible for glycine synthesis. This hyperglycemia could be partially reversed by SHMT2 knockdown, which rescued the axonal beading and neurite lengths of cultured Pycr2 knockout neurons."* — [PMID: 32330411](https://pubmed.ncbi.nlm.nih.gov/32330411/)

> *"knocking out Pycr2 in mice phenocopies the human disorder and depletes PYCR1 levels in neural lineages"* — [PMID: 32330411](https://pubmed.ncbi.nlm.nih.gov/32330411/)

> *"Both nonsense and missense mutations were identified, which impaired protein multimerization."* — [PMID: 27130255](https://pubmed.ncbi.nlm.nih.gov/27130255/)

### Finding 4 — Gene identification (2015): variants destabilize the protein and sensitize cells to oxidative-stress apoptosis

Nakayama et al. (2015, *Am J Hum Genet*) identified biallelic *PYCR2* mutations as the cause of postnatal microcephaly with hypomyelination through linkage mapping plus whole-exome sequencing in two consanguineous families (homozygous **c.355C>T p.Arg119Cys** and **c.751C>T p.Arg251Cys**). Patient lymphoblastoid cells showed strongly reduced PYCR2; transfected variant proteins retained normal mitochondrial localization but were present at lower amounts, indicating **reduced protein stability** as the loss-of-function mechanism. A CRISPR-Cas9 PYCR2-knockout HEK293FT line showed decreased mitochondrial membrane potential and increased susceptibility to apoptosis under oxidative stress, linking PYCR2 loss to mitochondrial dysfunction.

> *"A PYCR2-deficient HEK293FT cell line generated by genome editing with the clustered regularly interspaced short palindromic repeat (CRISPR)-Cas9 system showed that PYCR2 loss of function led to decreased mitochondrial membrane potential and increased susceptibility to apoptosis under oxidative stress."* — [PMID: 25865492](https://pubmed.ncbi.nlm.nih.gov/25865492/)

> *"both variant proteins retained normal mitochondrial localization but had lower amounts than the wild-type protein, suggesting that the variant proteins were less stable"* — [PMID: 25865492](https://pubmed.ncbi.nlm.nih.gov/25865492/)

### Finding 5 — Zebrafish *pycr1b* knockdown recapitulates microcephaly, rescued by wild-type human *PYCR2* mRNA

Nakayama et al. (2015) performed morpholino-based knockdown of the zebrafish *PYCR2* ortholog *pycr1b*, which recapitulated the human microcephaly phenotype. The phenotype was rescued by **wild-type** human *PYCR2* mRNA but **not** by mutant (p.Arg119Cys / p.Arg251Cys) mRNAs, confirming both the pathogenicity of the specific variants and the functional conservation of the gene across vertebrates.

> *"Morpholino-based knockdown of a zebrafish PYCR2 ortholog, pycr1b, recapitulated the human microcephaly phenotype, which was rescued by wild-type human PYCR2 mRNA, but not by mutant mRNAs"* — [PMID: 25865492](https://pubmed.ncbi.nlm.nih.gov/25865492/)

### Finding 6 — Phenotypic spectrum extends to a milder late-childhood hereditary spastic paraplegia

Sager et al. (2023) reported a novel homozygous missense *PYCR2* variant (**NM_013328 c.383T>C, p.Val128Ala**) in 5 male patients from 2 related families presenting as **hereditary spastic paraplegia (HSP) in late childhood WITHOUT hypomyelinating leukodystrophy**. Developmental milestones were normal without dysmorphic features; ~80% had mild intention tremor from ~6 years and ~80% had progressive lower-limb spasticity/gait difficulty from age 8–12 years; ages ranged 6–26 years. This is the first report of *PYCR2* variants causing HSP and considerably widens the recognized clinical spectrum, with implications for genetic diagnosis of milder cases.

> *"manifest Hereditary Spastic Paraplegia (HSP) is the only symptom without hypomyelinating leukodystrophy. This is the first study that report the PYCR2 gene variants as a cause of HSP in late childhood."* — [PMID: 37141741](https://pubmed.ncbi.nlm.nih.gov/37141741/)

> *"A novel homozygous missense (NM_013328: c.383T > C, p.V128A) variant in the PYCR2 gene is detected in 5 patient from 2 related families."* — [PMID: 37141741](https://pubmed.ncbi.nlm.nih.gov/37141741/)

### Finding 7 — Founder effects and consanguinity-driven population genetics (Thai c.400G>A founder allele)

Manaspon et al. (2021) reviewed all 35 previously reported *PYCR2* patients: the majority were homozygous with consanguineous family history (except two compound-heterozygous cases); all had microcephaly and developmental delay; hypotonia and peripheral spasticity were common; hypomyelination/delayed myelination was the typical radiographic feature. In two unrelated Thai families, the **c.400G>A (p.Val134Met)** variant was found on a shared 2.3 Mb haplotype (estimated allele age ~1450 years), indicating a common ancestor/founder effect; it accounted for 3 of 4 mutant alleles in Thai patients.

> *"Haplotype analysis revealed that the two families' members shared a 2.3 Mb region covering the c.400G>A variant, indicating a common ancestry. The variant was estimated to age 1450 years ago."* — [PMID: 34037307](https://pubmed.ncbi.nlm.nih.gov/34037307/)

> *"majorities of cases were homozygous with a consanguineous family history, except patient 1 and another reported case who were compound heterozygous. All patients had microcephaly and developmental delay. Hypotonia and peripheral spasticity were common."* — [PMID: 34037307](https://pubmed.ncbi.nlm.nih.gov/34037307/)

### Finding 8 — No disease-specific therapy; SHMT2/glycine-lowering is the leading mechanism-based target

No curative or disease-modifying therapy is approved for HLD10; care is supportive (anticonvulsants; spasticity, nutritional, and rehabilitation management). Because routine serum metabolic profiles are normal, peripheral proline supplementation is not clearly rational. The strongest mechanism-based lead is **lowering cerebral glycine**: Escande-Beillard et al. showed SHMT2 knockdown partially reversed axonal beading and rescued neurite lengths in *Pycr2*-knockout neurons, identifying the glycine metabolic pathway as a possible intervention point. No HLD10-specific clinical trials are currently registered.

> *"Our findings identify the glycine metabolic pathway as a possible intervention point to alleviate the neurological symptoms of PYCR2-mutant patients."* — [PMID: 32330411](https://pubmed.ncbi.nlm.nih.gov/32330411/)

---

## Section-by-Section Report

### 1. Disease Information

HLD10 is a rare autosomal recessive hypomyelinating leukodystrophy — a genetic white-matter disorder characterized by MRI evidence of absent or near-absent myelin development combined with postnatal (progressive) microcephaly, severe neurodevelopmental impairment, and failure to thrive. It is one of a numbered series of hypomyelinating leukodystrophies (HLD1–HLD~24+), each defined by a distinct causal gene; HLD10 is the *PYCR2*-associated entity.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| OMIM | #616420 |
| MONDO | MONDO:0014635 |
| Gene (HGNC) | *PYCR2* |
| Locus | 1q42.12 |
| MeSH | Hereditary Central Nervous System Demyelinating Diseases (closest); Leukodystrophy |
| Orphanet | Within genetic hypomyelinating leukodystrophy group |

**Synonyms / alternative names:** Hypomyelinating leukodystrophy 10 with microcephaly; PYCR2-related microcephaly with hypomyelination; postnatal microcephaly with hypomyelination and failure to thrive; PYCR2 deficiency.

**Source of information:** Aggregated disease-level resources (OMIM, published case series/cohorts) and individual patient case reports; no large EHR-derived registry exists given the disorder's rarity.

### 2. Etiology

**Primary cause:** Biallelic (homozygous or compound heterozygous) pathogenic variants in *PYCR2* (genetic, Mendelian). The etiology is monogenic; there is no evidence of infectious, environmental, or acquired causation.

**Genetic risk factors:** The only established genetic risk factor is inheriting two pathogenic *PYCR2* alleles. **Consanguinity** is the dominant epidemiologic driver — most reported families are consanguineous, and homozygosity for founder or private variants predominates (Findings 1, 7).

**Environmental risk factors:** None identified. HLD10 is fully genetically determined. No toxin, exposure, dietary, or lifestyle factor has been implicated.

**Protective factors:** None specifically identified. In principle, heterozygous carriers are unaffected (recessive), and outbreeding in consanguineous populations reduces incidence.

**Gene–environment interactions:** No documented GxE interaction. Because peripheral metabolism is normal and the disorder is highly penetrant when biallelic, environmental modulation appears minimal; phenotypic variability is primarily allele-driven (e.g., the milder p.Val128Ala HSP allele — Finding 6).

### 3. Phenotypes

| Phenotype | Type | Onset | Severity/Progression | Frequency | Suggested HPO |
|---|---|---|---|---|---|
| Progressive (postnatal) microcephaly | Physical/sign | Postnatal (acquired) | Severe, progressive | Nearly universal | HP:0005484 (Postnatal microcephaly) |
| Global developmental delay | Sign | Infantile | Moderate–profound | Universal | HP:0001263 |
| Failure to thrive | Sign | Infantile | Severe | Very common | HP:0001508 |
| Hypomyelination / delayed myelination (MRI) | Imaging/lab | Infantile | Progressive | Universal | HP:0006808 (Hypomyelination) |
| Thin corpus callosum | Imaging | Congenital/infantile | Static/progressive | Common | HP:0033725 |
| Cerebral/white-matter atrophy | Imaging | Infantile | Progressive | Common | HP:0002283 / HP:0012762 |
| Axial hypotonia | Sign | Infantile | Variable | Common | HP:0008936 |
| Appendicular / lower-limb spasticity | Sign | Infantile–childhood | Variable | Common | HP:0001257 / HP:0002061 |
| Hyperkinetic movements | Sign | Infantile | Variable | Common | HP:0002487 |
| Seizures | Sign | Infantile | Variable | Frequent | HP:0001250 |
| Craniofacial dysmorphism | Physical | Congenital | Variable | Common | HP:0001999 |
| Intention tremor (mild allele) | Sign | ~6 yr | Mild | ~80% of HSP-phenotype patients | HP:0002080 |
| Hereditary spastic paraplegia (mild allele) | Sign | Late childhood (8–12 yr) | Progressive, milder | Mild-allele families | HP:0001258 |

**Quality of life impact:** In the severe (classic) form, profound global disability, non-ambulatory/non-verbal status, feeding difficulty, and death within the first decade impose maximal burden on affected children and caregivers. In the milder HSP form, quality of life is affected principally by progressive gait impairment with preserved cognition (Finding 6). Formal QoL instrument data (EQ-5D, SF-36) are not available for this ultra-rare disease.

### 4. Genetic / Molecular Information

**Causal gene:** *PYCR2* (HGNC), 1q42.12; encodes pyrroline-5-carboxylate reductase 2, a mitochondrial enzyme catalyzing the final (NAD(P)H-dependent) step of L-proline biosynthesis (reduction of Δ¹-pyrroline-5-carboxylate to proline).

**Pathogenic variants (representative):**

| Variant (cDNA) | Protein | Type | Phenotype | Population/Note | Source |
|---|---|---|---|---|---|
| c.355C>T | p.Arg119Cys | Missense (destabilizing) | Classic HLD10 | Consanguineous; original 2015 report | [PMID: 25865492](https://pubmed.ncbi.nlm.nih.gov/25865492/) |
| c.751C>T | p.Arg251Cys | Missense (destabilizing) | Classic HLD10 | Consanguineous; original 2015 report | [PMID: 25865492](https://pubmed.ncbi.nlm.nih.gov/25865492/) |
| c.400G>A | p.Val134Met | Missense | Classic HLD10 | Thai founder allele (~1450 yr) | [PMID: 34037307](https://pubmed.ncbi.nlm.nih.gov/34037307/) |
| (Gly249Val) | p.Gly249Val | Missense at dimer interface (↓activity) | HLD10 | Functional/structural study | [PMID: 32330411](https://pubmed.ncbi.nlm.nih.gov/32330411/) |
| c.383T>C | p.Val128Ala | Missense (mild) | HSP without leukodystrophy | 2 related families, 5 males | [PMID: 37141741](https://pubmed.ncbi.nlm.nih.gov/37141741/) |

**Variant classification:** Reported disease alleles are classified pathogenic/likely pathogenic under ACMG/AMP, supported by functional evidence (reduced protein stability, impaired multimerization, decreased enzymatic activity, zebrafish rescue failure).

**Variant types:** Both **missense** (reduced stability / impaired multimerization / reduced activity) and **nonsense** variants have been reported; all converge on loss of function (Findings 3, 4).

**Allele frequency:** Pathogenic alleles are rare in population databases (gnomAD), consistent with a recessive, largely founder/consanguinity-driven disorder.

**Origin:** **Germline** (constitutional, biallelic). No somatic contribution.

**Functional consequence:** **Loss of function** — missense variants act principally by destabilizing the protein and impairing multimerization; nonsense variants truncate the protein. Downstream, PYCR1 is depleted in neural lineages (Finding 3).

**Modifier genes:** None formally established. *SHMT2* is a mechanistic effector (its upregulation drives glycine toxicity) rather than a classic modifier; *PYCR1* depletion is a downstream consequence. Phenotype severity tracks primarily with the specific *PYCR2* allele.

**Epigenetic information:** No disease-specific DNA-methylation or histone-modification signature has been reported for HLD10 (not available).

**Chromosomal abnormalities:** None; HLD10 is a single-gene disorder without recurrent structural/copy-number changes (not applicable).

### 5. Environmental Information

No environmental, lifestyle, or infectious factors contribute to HLD10. It is a purely genetic Mendelian disorder. Consanguinity (a social/demographic rather than environmental exposure) increases the probability of homozygosity for pathogenic alleles but is not an environmental cause of the molecular defect. Infectious agents are not applicable.

### 6. Mechanism / Pathophysiology

**Molecular pathway:** Proline biosynthesis and one-carbon/serine–glycine metabolism. PYCR2 catalyzes the terminal reduction of pyrroline-5-carboxylate (P5C) to L-proline in mitochondria. Loss of PYCR2 activity perturbs this node and, critically, triggers compensatory **upregulation of SHMT2** (serine hydroxymethyltransferase 2), which synthesizes glycine — producing pathological cerebral glycine excess (Finding 3).

**Causal chain (upstream → downstream):**

```
Biallelic PYCR2 LoF variants (missense destabilizing / nonsense)
        │
        ▼
Reduced PYCR2 protein amount + impaired multimerization  → loss of enzyme activity
        │
        ├─► Depletion of PYCR1 in neural lineages
        │
        ├─► ↓ Mitochondrial membrane potential → ↑ apoptosis under oxidative stress
        │
        └─► ↑ SHMT2 expression → ↑ cerebral glycine
                     │
                     ▼
            Axonal beading, reduced neurite length, neurodegeneration
                     │
                     ▼
     Hypomyelination + progressive microcephaly + white-matter atrophy
                     │
                     ▼
   Global developmental delay, movement disorder, seizures, failure to thrive
```

**Cellular processes:** Apoptosis (increased under oxidative stress), mitochondrial dysfunction (decreased membrane potential), and neuronal/axonal degeneration (axonal beading, neurite shortening). The hypomyelination appears to be at least partly secondary to a primary neuronal/axonal defect (a "leuko-axonopathy"-type mechanism), consistent with the neurotransmitter/glycine-driven neurodegeneration.

**Protein dysfunction:** Missense variants retain correct mitochondrial localization but are present at lower amounts (reduced stability) and impair multimerization; the p.Gly249Val substitution at the dimer interface lowers catalytic activity — the apo-enzyme crystal structure was solved to demonstrate this (Findings 3, 4).

**Metabolic changes:** Elevated cerebral glycine (via SHMT2); perturbed proline biosynthesis. Importantly, **peripheral/serum metabolic profiles are normal**, indicating a CNS-compartmentalized metabolic derangement (Finding 2).

**Immune involvement / tissue-damage mechanisms:** No autoimmune or inflammatory driver; oxidative stress-sensitized apoptosis and glycine excitotoxic-type neurodegeneration are the operative injury mechanisms.

**Suggested ontology terms:**
- GO biological process: proline biosynthetic process (GO:0006561); glycine biosynthetic process (GO:0006545); myelination (GO:0042552); apoptotic process (GO:0006915); neuron projection development (GO:0031175).
- GO cellular component: mitochondrion (GO:0005739); mitochondrial matrix (GO:0005759).
- CL cell types: oligodendrocyte (CL:0000128); neuron (CL:0000540); central nervous system neuron.
- CHEBI: L-proline (CHEBI:17203); glycine (CHEBI:15428); L-1-pyrroline-5-carboxylate (CHEBI:17388).

### 7. Anatomical Structures Affected

- **Primary organ / body system:** Central nervous system / brain (nervous system). UBERON: brain (UBERON:0000955); white matter (UBERON:0002316); corpus callosum (UBERON:0002336); cerebral hemisphere.
- **Tissue level:** Cerebral white matter (myelin) with generalized volume loss; thin corpus callosum; cerebral atrophy.
- **Cell level:** Oligodendrocytes (myelinating cells; CL:0000128) and neurons/axons (CL:0000540) are affected; PYCR1 depletion occurs in neural lineages.
- **Subcellular level:** Mitochondria (GO:0005739) — reduced membrane potential and increased oxidative-stress apoptosis.
- **Localization / lateralization:** Diffuse and **bilateral / symmetric** white-matter involvement, typical of hypomyelinating leukodystrophies.

### 8. Temporal Development

- **Onset:** Congenital-to-infantile in the classic form; microcephaly is postnatally acquired and **progressive** (head circumference normal at birth then decelerating). The milder HSP allele has late-childhood onset (spasticity 8–12 yr; tremor from ~6 yr).
- **Onset pattern:** Insidious/chronic and progressive.
- **Progression:** Progressive neurodegeneration with failure to thrive; severe cases are fatal within the first decade. The mild HSP phenotype progresses more slowly, with survival into adulthood (ages reported up to 26 years).
- **Course:** Chronic, progressive, lifelong; no remission.
- **Critical periods:** Early postnatal myelination window is the period of maximal vulnerability and the theoretical window for any myelination-directed or glycine-lowering intervention.

### 9. Inheritance and Population

- **Inheritance:** Autosomal recessive.
- **Penetrance:** High/complete for the biallelic classic phenotype; **variable expressivity** exists across alleles (severe leukodystrophy vs. milder HSP).
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Founder effects:** Documented — the Thai **c.400G>A (p.Val134Met)** founder allele on a shared 2.3 Mb haplotype, estimated age ~1450 years, accounting for 3 of 4 mutant alleles in Thai patients (Finding 7).
- **Consanguinity:** Central to the epidemiology; most families are consanguineous and patients homozygous.
- **Carrier frequency / prevalence / incidence:** Not precisely established; the disorder is ultra-rare with ~35+ patients reported in the literature as of the 2021 review. Prevalence in outbred populations is very low; locally elevated where founder alleles and consanguinity coincide.
- **Population demographics:** Reported across consanguineous populations (Middle Eastern, South/Southeast Asian including Thai and Indian patients). No strong sex bias in the classic form; the reported HSP-allele families comprised affected males (small sample). Age distribution skews pediatric owing to early mortality in the severe form.

### 10. Diagnostics

- **Recommended approach:** Molecular genetic diagnosis is definitive. Because **routine serum/urine metabolic tests are normal**, biochemical screening does not establish the diagnosis and can mislead.
- **Genetic testing:** Whole-exome sequencing (WES) is the highest-yield test and was the discovery method; whole-genome sequencing (WGS) or leukodystrophy/hypomyelination gene panels including *PYCR2* are appropriate. Single-gene testing is reasonable in populations with known founder alleles (e.g., Thai c.400G>A). Chromosomal microarray/karyotype/FISH are not indicated (single-gene disorder).
- **Imaging:** Brain MRI is the key phenotyping modality — hypomyelination/delayed myelination (delayed T2 hypointensity, often T1 hyperintensity), thin corpus callosum, cerebral and white-matter atrophy. Serial MRI helps distinguish primary hypomyelination from progressive atrophy.
- **Biomarkers:** No validated peripheral biomarker; cerebral glycine elevation is a mechanistic finding (MR spectroscopy could theoretically detect elevated glycine, but this is not an established clinical biomarker).
- **Differential diagnosis:** Other hypomyelinating leukodystrophies and microcephaly syndromes — e.g., PMD/PLP1 (HLD1), HIKESHI-related HLD (with febrile-illness crises, Ashkenazi founder), SLC25A12/AGC1-related leuko-axonopathy, and KIF1C-related spastic-ataxia/HLD. *PYCR2* disease is distinguished by progressive postnatal microcephaly, failure to thrive, normal peripheral metabolics, and biallelic *PYCR2* variants. The milder allele overlaps clinically with hereditary spastic paraplegias.
- **Screening:** Cascade/carrier testing in affected consanguineous families; targeted founder-allele carrier screening is feasible where relevant (e.g., Thai c.400G>A).

### 11. Outcome / Prognosis

- **Survival/mortality:** Severe (classic) HLD10 is **fatal within the first decade of life**. The milder HSP-phenotype patients survive into adulthood.
- **Morbidity/function:** Profound, lifelong disability in the classic form (non-ambulatory, non-verbal, feeding-dependent, seizures). The mild form causes progressive gait impairment with relatively preserved cognition.
- **Complications:** Failure to thrive, feeding difficulty, seizures, aspiration/respiratory complications, and consequences of severe neurodisability.
- **Prognostic factors:** Genotype is the principal determinant — null/severely destabilizing biallelic variants predict the severe lethal phenotype, whereas partial-function alleles (e.g., p.Val128Ala) predict the milder HSP course.
- **Recovery potential:** None; the disorder is progressive and neurodegenerative.

### 12. Treatment

- **Disease-specific therapy:** None approved. Management is **supportive/symptomatic** — anticonvulsants for seizures, spasticity management (physiotherapy, antispasticity agents), nutritional support for failure to thrive, and multidisciplinary rehabilitation (physical, occupational, speech therapy).
- **Mechanism-based experimental direction:** **Glycine-lowering / SHMT2 inhibition** is the leading strategy, supported by the demonstration that SHMT2 knockdown partially rescues axonal beading and neurite length in *Pycr2*-KO neurons (Finding 8). Dietary/pharmacologic glycine reduction and SHMT2-targeted approaches are conceptually motivated but unproven clinically.
- **Rational cautions:** Because peripheral proline metabolism is normal, systemic proline supplementation lacks clear rationale.
- **Clinical trials:** No HLD10-specific registered trials.
- **Suggested NCIT terms:** Supportive Care; Anticonvulsant Agent; Physical Therapy; Nutritional Support (used generically; no disease-specific intervention exists).

### 13. Prevention

- **Primary prevention:** **Genetic counseling** for consanguineous couples and affected families; carrier testing and reproductive options (preimplantation genetic testing, prenatal diagnosis) are the principal preventive measures given the recessive, high-penetrance nature.
- **Screening:** Cascade carrier testing within families; founder-allele carrier screening where population-relevant (e.g., Thai c.400G>A).
- **Behavioral/public-health:** Awareness of consanguinity-associated recessive disease risk; no vaccine or environmental intervention is applicable.
- **Counseling:** 25% recurrence risk for carrier–carrier couples; genetic counseling is central.

### 14. Other Species / Natural Disease

- **Orthologs / model species:** Mouse *Pycr2*; zebrafish ortholog *pycr1b*. No naturally occurring animal disease has been documented (OMIA); model organisms are engineered/experimental.
- **Comparative biology:** The gene and its function are evolutionarily conserved — zebrafish *pycr1b* knockdown reproduces microcephaly rescued by human *PYCR2* mRNA (Finding 5), and *Pycr2*-KO mice phenocopy the human disorder (Finding 3), demonstrating conserved requirement for PYCR2 in neurodevelopment.
- **Zoonotic/transmission:** Not applicable (genetic disorder).

### 15. Model Organisms

| Model | Type | Key features | Recapitulation | Reference |
|---|---|---|---|---|
| *Pycr2* knockout mouse | Mammalian, genetic KO | Phenocopies human disorder; depletes PYCR1 in neural lineages; elevated cerebral glycine via SHMT2; SHMT2 knockdown rescues axonal beading/neurite length | High — reproduces neurodegeneration and the core mechanism | [PMID: 32330411](https://pubmed.ncbi.nlm.nih.gov/32330411/) |
| Zebrafish *pycr1b* morphant | Vertebrate, morpholino knockdown | Recapitulates microcephaly; rescued by WT human *PYCR2* mRNA but not mutant mRNAs | Good for microcephaly; validates variant pathogenicity | [PMID: 25865492](https://pubmed.ncbi.nlm.nih.gov/25865492/) |
| PYCR2-KO HEK293FT (CRISPR-Cas9) | Cellular, in vitro | ↓ Mitochondrial membrane potential; ↑ apoptosis under oxidative stress | Models mitochondrial/apoptotic mechanism | [PMID: 25865492](https://pubmed.ncbi.nlm.nih.gov/25865492/) |
| Patient lymphoblastoid cells; transfected variant proteins | In vitro | Reduced PYCR2; variants normally localized but less stable | Models loss-of-function via reduced stability | [PMID: 25865492](https://pubmed.ncbi.nlm.nih.gov/25865492/) |
| Recombinant PYCR2 (crystal structure) | Structural/biochemical | Apo-enzyme structure; p.Gly249Val at dimer interface lowers activity | Structural basis of pathogenicity | [PMID: 32330411](https://pubmed.ncbi.nlm.nih.gov/32330411/) |

**Model applications:** Dissecting the SHMT2/glycine mechanism, testing glycine-lowering interventions, validating variant pathogenicity, and studying mitochondrial dysfunction. **Limitations:** Morpholino knockdown is transient and can carry off-target effects; the milder human HSP phenotype has not been separately modeled; therapeutic rescue to date is partial and in vitro/animal only.

---

## Mechanistic Model / Interpretation

The evidence converges on a coherent model in which **PYCR2 is a mitochondrial enzyme whose loss produces a compartmentalized cerebral metabolic and mitochondrial crisis**. Two mechanistic arms operate downstream of the same biallelic loss-of-function lesion:

1. **A mitochondrial/apoptotic arm** (established 2015): destabilized or truncated PYCR2 → reduced enzyme → decreased mitochondrial membrane potential → heightened apoptosis under oxidative stress, with PYCR1 co-depletion in neural lineages.
2. **A glycine-excess arm** (established 2020): PYCR2 loss → SHMT2 upregulation → excess cerebral glycine → axonal beading, neurite shortening, and neurodegeneration.

The second arm is the more actionable one because it is **reversible in models** — SHMT2 knockdown partially rescues neuronal morphology. Both arms terminate in the same clinical endpoint: progressive postnatal microcephaly, hypomyelination/white-matter atrophy, and severe neurodevelopmental disability. The observation that peripheral metabolics are normal despite cerebral glycine elevation underscores that this is a brain-restricted metabolic disease, which also explains why classical biochemical newborn screening does not detect it and why genetic testing is essential.

Allelic severity maps onto phenotype: severe destabilizing/null biallelic genotypes produce the lethal infantile leukodystrophy, while partial-function alleles (p.Val128Ala) produce a milder, later-onset hereditary spastic paraplegia without overt leukodystrophy — a genotype–phenotype gradient rather than two separate diseases.

---

## Evidence Base

| PMID | Study | Contribution | Evidence type |
|---|---|---|---|
| [25865492](https://pubmed.ncbi.nlm.nih.gov/25865492/) | Nakayama et al. 2015, *Am J Hum Genet* | Gene identification; reduced protein stability; CRISPR-KO mitochondrial/apoptosis phenotype; zebrafish *pycr1b* rescue | Human genetics + in vitro + model organism |
| [27130255](https://pubmed.ncbi.nlm.nih.gov/27130255/) | Zaki et al. — *PYCR2 mutations cause a lethal syndrome* | 11 consanguineous families; AR locus 1q42.12; impaired multimerization; core phenotype and lethal prognosis | Human clinical/genetics |
| [27860360](https://pubmed.ncbi.nlm.nih.gov/27860360/) | Homozygous *PYCR2* variants, progressive microcephaly & hypomyelination | Confirms postnatal microcephaly, MRI features, normal metabolics | Human clinical |
| [32330411](https://pubmed.ncbi.nlm.nih.gov/32330411/) | Escande-Beillard et al. 2020 — *Loss of PYCR2 causes neurodegeneration via SHMT2* | Crystal structure; *Pycr2*-KO mouse; SHMT2/glycine mechanism and rescue; therapeutic target | Structural + model organism + mechanistic |
| [34037307](https://pubmed.ncbi.nlm.nih.gov/34037307/) | Manaspon et al. 2021 — Thai cohort | Review of 35 patients; consanguinity dominance; Thai c.400G>A founder allele (~1450 yr) | Human genetics/population |
| [37141741](https://pubmed.ncbi.nlm.nih.gov/37141741/) | Sager et al. 2023 — *PYCR2 causes HSP in late childhood* | First HSP phenotype; p.Val128Ala; spectrum expansion | Human clinical/genetics |
| [34055512](https://pubmed.ncbi.nlm.nih.gov/34055512/) | Indian child case report | Compound-heterozygous HLD10; normal metabolics; MRI hypomyelination | Human clinical (case) |
| [33771508](https://pubmed.ncbi.nlm.nih.gov/33771508/) | Disease variants of human Δ¹-pyrroline-5-carboxylate reductase | Biochemistry of PYCR enzymology | In vitro/biochemical |

Supporting/contextual literature on the hypomyelinating leukodystrophy landscape and differentials includes reviews of hypomyelinating disorders and MRI approaches ([PMID: 26477299](https://pubmed.ncbi.nlm.nih.gov/26477299/), [PMID: 27235001](https://pubmed.ncbi.nlm.nih.gov/27235001/)), the expanded genetic white-matter disorder gene catalog ([PMID: 32704519](https://pubmed.ncbi.nlm.nih.gov/32704519/)), and comparators such as HIKESHI-related HLD ([PMID: 34111619](https://pubmed.ncbi.nlm.nih.gov/34111619/)), SLC25A12/AGC1 leuko-axonopathy ([PMID: 31403263](https://pubmed.ncbi.nlm.nih.gov/31403263/)), and KIF1C-related classification ambiguity ([PMID: 40794111](https://pubmed.ncbi.nlm.nih.gov/40794111/)).

---

## Limitations and Knowledge Gaps

- **Small evidence base:** Only ~35+ patients reported; prevalence, incidence, carrier frequency, and sex ratio are not precisely quantified.
- **Genotype–phenotype correlations** are still coarse; the full determinants of the severe-vs-mild spectrum are not systematically mapped.
- **Biomarkers:** No validated peripheral or imaging biomarker (e.g., MRS glycine) is clinically established for diagnosis or monitoring.
- **Therapeutics:** Glycine-lowering/SHMT2 inhibition rescue is partial and demonstrated only in vitro/animal; no human therapeutic data or registered trials exist.
- **Two mechanistic arms** (mitochondrial-apoptotic vs glycine-excess) are not fully integrated — their relative contributions to hypomyelination versus neuronal loss remain to be resolved.
- **Epigenetics, immune involvement, and structural genomics** are not characterized (not applicable/unknown).
- **Model gaps:** The milder HSP phenotype lacks a dedicated model; morpholino data carry inherent caveats.

---

## Proposed Follow-up Experiments / Actions

1. **Test glycine-lowering interventions in vivo:** Evaluate dietary glycine restriction and/or SHMT2 pharmacologic inhibition in *Pycr2*-KO mice for effects on myelination, brain growth, and survival — the most direct translation of the mechanistic finding.
2. **Genotype–phenotype registry:** Aggregate all reported and new *PYCR2* patients with standardized allele annotation, MRI phenotyping, and outcomes to define severity predictors and refine the severe-vs-HSP spectrum.
3. **MR spectroscopy for cerebral glycine:** Prospectively test whether MRS-detectable brain glycine elevation can serve as a diagnostic/monitoring biomarker.
4. **iPSC-derived oligodendrocyte/neuron models** from patients (severe and mild alleles) to dissect whether hypomyelination is primary (oligodendrocyte-autonomous) or secondary to axonal/neuronal glycine toxicity.
5. **Structure-guided variant functional classification:** Use the apo-enzyme structure to model additional missense VUS (stability, dimer-interface, activity) and improve ACMG classification.
6. **Population carrier screening** for founder alleles (e.g., Thai c.400G>A) in high-consanguinity communities, paired with genetic counseling programs.
7. **Integrate the two mechanistic arms:** Experiments manipulating oxidative-stress/mitochondrial function and glycine levels independently to determine their relative causal weight for the hypomyelination endpoint.

---

*Report compiled from an autonomous multi-iteration literature investigation (8 confirmed findings, 17 papers reviewed). Evidence types span human clinical/genetics, model organism (mouse, zebrafish), in vitro/cellular, and structural/biochemical studies.*


## Artifacts

- [OpenScientist final report](Hypomyelinating_Leukodystrophy_10-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Hypomyelinating_Leukodystrophy_10-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.