---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-11T12:44:09.998686'
end_time: '2026-11-11T12:59:56.904469'
duration_seconds: 946.91
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: ZIC1-Related Craniosynostosis
  mondo_id: MONDO:0014705
  category: Mendelian
  causal_genes: ZIC1
  omim_id: OMIM:616602
  synonyms: craniosynostosis type 6; ZIC1 craniosynostosis; craniosynostosis caused
    by mutation in ZIC1
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
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderAuthError
  status_code: 403
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 22
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ZIC1-Related_Craniosynostosis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ZIC1-Related_Craniosynostosis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ZIC1-Related Craniosynostosis
- **MONDO ID:** MONDO:0014705 (if available)
- **Causal gene(s):** ZIC1
- **OMIM:** OMIM:616602
- **Synonyms:** craniosynostosis type 6; ZIC1 craniosynostosis; craniosynostosis caused by mutation in ZIC1
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **ZIC1-Related Craniosynostosis** covering all of the
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

# ZIC1-Related Craniosynostosis (Craniosynostosis Type 6, CRS6): A Comprehensive Disease Report

**Disease:** ZIC1-Related Craniosynostosis
**Causal gene:** **ZIC1** (Zinc finger of the cerebellum 1 / Zic family member 1)
**MONDO:** MONDO:0014705 · **OMIM:** 616602 · **Synonyms:** craniosynostosis type 6; ZIC1 craniosynostosis

---

## Summary

ZIC1-Related Craniosynostosis (craniosynostosis type 6, CRS6; OMIM 616602; MONDO:0014705) is a rare autosomal-dominant Mendelian disorder caused by heterozygous **gain-of-function variants in the final (third) exon of the *ZIC1* gene** (chromosome 3q24; HGNC:12872), which encodes a C2H2 zinc-finger transcription factor central to neural development and neural-crest specification. The defining clinical picture is **severe craniosynostosis, specifically involving the coronal sutures (usually bicoronal), together with variable learning disability**, often accompanied by facial dysmorphism and structural brain abnormalities. The disease was first delineated by Twigg and colleagues in 2015 in five families, and the phenotypic spectrum was substantially expanded by Watts and colleagues in 2026 across 22 families / 30 individuals.

The molecular logic of ZIC1 disorders is strikingly dependent on **where in the gene the variant falls**. Truncating (and one missense) variants clustered in the terminal exon 3 **escape nonsense-mediated decay (NMD)**, producing a stable, abnormally active protein that acts through a **gain-of-function / dominant mechanism** — this causes craniosynostosis. In contrast, missense substitutions in exons 1–2 that disrupt the zinc-finger DNA-binding domain cause **loss of ZIC1 function**, producing a **neurodevelopmental disorder without craniosynostosis**; and heterozygous loss of ZIC1 together with its neighbour ZIC4 causes **Dandy-Walker malformation** (cerebellar vermis hypoplasia). ZIC1 therefore sits at the centre of an allelic series in which gain and loss of function produce opposite ends of a developmental spectrum.

Mechanistically, ZIC1 is a **core neural-plate-border / neural-crest specifier** (acting with PAX3) and patterns the **coronal suture via the supraorbital regulatory center**, the boundary between neural-crest-derived frontal bone and mesoderm-derived parietal bone. Gain-of-function ZIC1 drives **osteogenic differentiation (RUNX2, osteocalcin) and Hedgehog signaling (Patched1)** at the expense of other lineages, providing a plausible route to premature bone formation at the suture. ZIC1 integrates **Sonic hedgehog, retinoic acid, and TGFβ/BMP** signaling and regulates engrailed (EN1/EN2) target genes. Management is **surgical** (cranial vault remodeling, fronto-orbital advancement, spring-assisted or distraction techniques) with developmental, ophthalmologic and neurosurgical surveillance; there is no gene-targeted therapy.

---

## Key Findings

### Finding 1 — CRS6 is caused by heterozygous gain-of-function variants in the final exon of ZIC1

The foundational study by **Twigg et al. (2015)** identified heterozygous mutations in the **final (third) exon of *ZIC1*** across five families — four nonsense changes and one missense change — producing a "distinct phenotype in which severe craniosynostosis, specifically involving the coronal sutures, and variable learning disability are the most characteristic features" [PMID: 26340333](https://pubmed.ncbi.nlm.nih.gov/26340333/). Critically, the **position** of the nonsense mutations within the terminal exon predicts that mutant transcripts **escape nonsense-mediated decay (NMD)** — a prediction the authors confirmed in a cell line derived from an affected individual: *"The location of the nonsense mutations predicts escape of mutant ZIC1 transcripts from nonsense-mediated decay, which was confirmed in a cell line from an affected individual."* Because the mutant message is not degraded, a truncated/altered but **stable protein** is produced, and functional assays in *Xenopus* showed the variants **enhance or alter engrailed-2 target gene expression** — behaviour consistent with a **gain-of-function / dominant** mechanism rather than simple haploinsufficiency. This establishes the gene (ZIC1), the variant location (terminal exon 3), the mechanism (NMD escape → stable active protein), and the core phenotype (coronal craniosynostosis + learning disability).

- **HGNC:** 12872 (ZIC1) · **NCBI Gene:** 7545 · **OMIM gene:** 600470 · **Variant classes:** nonsense (stop-gain), missense, frameshift (all truncating/terminal-exon)
- **Functional consequence:** gain of function / dominant (not loss of function)

### Finding 2 & 6 — Genotype–phenotype correlation: exon-3 truncations → craniosynostosis; exon 1–2 missense → NDD alone

The largest cohort to date, **Watts et al. (2026)**, reported *"18 different heterozygous ZIC1 variants from 22 families, comprising 30 individuals"* [PMID: 42028696](https://pubmed.ncbi.nlm.nih.gov/42028696/), and resolved a clean genotype–phenotype dichotomy:

| Variant location | Variant type | Mechanism | Phenotype |
|---|---|---|---|
| **Final exon 3** | Truncating (nonsense/frameshift), rare missense | **Gain of function** (escapes NMD) | Craniosynostosis + facial dysmorphism + structural brain abnormalities + developmental delay (12 families) |
| **Exons 1–2 (zinc-finger domain)** | Missense | **Loss of function** | Neurodevelopmental disorder **without** craniosynostosis (10 families) |

In the authors' words: *"Variants associated with craniosynostosis were clustered in the final exon (3) and were predominantly truncating variants predicted to escape nonsense-mediated decay, whereas 10 families had a neurodevelopmental disorder alone without craniosynostosis."* This finding is central to clinical interpretation: the same gene produces two distinct disorders depending on variant position and mechanistic direction. It also means that **ACMG classification and phenotype prediction must consider variant location**, not merely predicted protein truncation.

### Finding 3 — Mechanism: ZIC1 patterns the coronal suture via the supraorbital regulatory center and controls osteogenic lineage

Twigg et al. localized ZIC1 function anatomically: *"Analysis of mouse embryos revealed a localized domain of Zic1 expression at embryonic days 11.5-12.5 in a region overlapping the supraorbital regulatory center, which patterns the coronal suture"* [PMID: 26340333](https://pubmed.ncbi.nlm.nih.gov/26340333/). The supraorbital regulatory center is the osteogenic/suture-patterning hub from which the frontal and parietal bones and the intervening coronal suture arise. Independently, **Thottappillil et al. (2025)** showed that ZIC1 overexpression in human skeletal progenitor cells *"led to an increase in osteoblast antigen expression (RUNX2, OCN), activation of Hedgehog signaling (Patched1), and an increase in brown adipogenesis markers"* [PMID: 40151950](https://pubmed.ncbi.nlm.nih.gov/40151950/) — i.e., excess ZIC1 **drives osteogenic differentiation and Hedgehog signaling**, a direct mechanistic route to premature suture ossification. The coronal suture is a developmental boundary between **neural-crest-derived frontal bone and paraxial-mesoderm-derived parietal bone**, whose integrity depends on Shh-responsive supraorbital cells [PMID: 26589924](https://pubmed.ncbi.nlm.nih.gov/26589924/).

### Finding 7 — ZIC1 is a core neural-plate-border / neural-crest specifier (with PAX3)

ZIC1 operates upstream in craniofacial development as a **neural-crest specifier**. Bellchambers et al. state that *"The zinc finger of the cerebellum 1 (ZIC1) transcription factor is considered a core component of the vertebrate gene regulatory network that specifies neural crest fate at the neural plate border"* [PMID: 34638777](https://pubmed.ncbi.nlm.nih.gov/34638777/). In *Xenopus*, zic1 and pax3 are the core neural-plate-border factors initiating the neural-crest gene regulatory network, and their relative levels differentially regulate downstream NC genes (snai2, sox8): *"These differences correlate with dynamic expression of the neural plate border factors pax3 and zic1"* [PMID: 41718037](https://pubmed.ncbi.nlm.nih.gov/41718037/). Because the **frontal bone derives from cranial neural crest** and the **parietal bone from paraxial mesoderm**, ZIC1's role in NC specification mechanistically links it to the craniofacial skeleton and the coronal suture [PMID: 32916911](https://pubmed.ncbi.nlm.nih.gov/32916911/).

### Finding 8 — ZIC1 integrates Shh, retinoic acid, and TGFβ/BMP signaling

A review by **Aruga & Millen (2018)** describes Zic-mediated developmental control operating through regulation of neuronal progenitor proliferation/differentiation and patterning of the cerebellar primordium, with *"embryonic interactions with sonic hedgehog signaling, retinoic acid signaling, and TGFβ signaling ... described during mouse cerebellar development"* [PMID: 29442326](https://pubmed.ncbi.nlm.nih.gov/29442326/). The same review independently confirms that *"ZIC1 gain of function mutations contribute to coronal craniosynostosis, a rare skull malformation."* These three pathways (Shh, RA, TGFβ/BMP) are the principal signaling systems ZIC1 interfaces with and are relevant to both the osteogenic/suture branch and the cerebellar branch of ZIC1 biology.

### Finding 4 — Allelic opposite: ZIC1/ZIC4 loss of function causes Dandy-Walker malformation

Loss-of-function biology sits at the other end of the ZIC1 spectrum. **Grinberg et al. (2004)** established that heterozygous deletion of the linked genes ZIC1 and ZIC4 underlies Dandy-Walker malformation (DWM), and that *"Mice with a heterozygous deletion of these two linked genes have a phenotype that closely resembles DWM, providing a mouse model for this malformation"* [PMID: 15338008](https://pubmed.ncbi.nlm.nih.gov/15338008/). **Blank et al. (2011)** showed the cerebellar hypoplasia results from reduced postnatal granule-cell progenitor proliferation via Shh-dependent function: *"Expression of the Shh-downstream genes Ptch1, Gli1 and Mycn was downregulated in Zic1/4 mutants"* [PMID: 21307096](https://pubmed.ncbi.nlm.nih.gov/21307096/). This LoF mechanism (reduced Hedgehog output) is the mechanistic mirror image of the GoF craniosynostosis mechanism (increased Hedgehog/osteogenic output), tying both ends of the spectrum to the same Shh pathway.

### Finding 5 — Variable expressivity, postnatal suture fusion, and parental gonadal mosaicism

**Vandervore et al. (2018)** described two siblings with a novel heterozygous frameshift at the end of ZIC1 exon 3 presenting with neonatal microcephaly, agenesis of the corpus callosum, brachycephaly, reduced posterior fossa volume, cerebellar/pons hypoplasia, scoliosis, tethered cord and partial rhombencephalosynapsis. The variant was absent in both parents: *"The mutation was not detected in DNA of both parents, which suggests parental gonadal mosaicism"* [PMID: 30391508](https://pubmed.ncbi.nlm.nih.gov/30391508/) — a finding with direct recurrence-risk implications. Importantly, *"Craniosynostosis was not present at birth, which explains why ZIC1 mutations were not initially considered,"* demonstrating **postnatal onset of suture fusion** and variable expressivity. A separate report (**Murakami et al. 2024**) found that a de novo 3q inversion with a breakpoint **7 kb downstream of ZIC1** produced a bicoronal craniosynostosis / rhombencephalosynapsis phenotype via transcriptional dysregulation of ZIC1 — showing that regulatory (position-effect) disruption can phenocopy coding gain-of-function [PMID: 37950019](https://pubmed.ncbi.nlm.nih.gov/37950019/).

---

## Section-by-Section Report

### 1. Disease Information

ZIC1-Related Craniosynostosis (CRS6) is a rare autosomal-dominant Mendelian skull malformation syndrome in which **premature fusion of the coronal sutures** (craniosynostosis) co-occurs with **variable learning disability / developmental delay**, frequently with facial dysmorphism and structural brain abnormalities. The **causal gene is ZIC1**, encoding the zinc-finger-of-the-cerebellum-1 transcription factor.

- **Key identifiers:** OMIM 616602 (phenotype); MONDO:0014705; HGNC:12872 / NCBI Gene 7545 / OMIM gene 600470 (ZIC1). ICD-10 Q75.0 (craniosynostosis); ICD-11 LD24.0. MeSH: "Craniosynostoses" (D003398). Orphanet lists coronal/complex craniosynostosis entities; a ZIC1-specific Orphanet code was not confirmed in this investigation.
- **Synonyms:** craniosynostosis type 6; ZIC1 craniosynostosis; craniosynostosis caused by mutation in ZIC1.
- **Information source:** Disease-level knowledge is derived from **aggregated case series and cohort studies** (Twigg 2015, 5 families; Watts 2026, 22 families/30 individuals; Vandervore 2018, 1 family), not EHR/population registries, reflecting the disorder's rarity.

### 2. Etiology

- **Primary cause — genetic:** heterozygous **gain-of-function variants in the final (third) exon of ZIC1** that escape NMD, yielding a stable, abnormally active protein [PMID: 26340333](https://pubmed.ncbi.nlm.nih.gov/26340333/). No environmental or infectious cause is implicated.
- **Genetic risk factors:** the causal variant itself (exon-3 truncating/missense). No modifier genes or susceptibility loci are established for CRS6; penetrance for craniosynostosis among exon-3 variant carriers appears high but expressivity is variable.
- **Environmental / protective / gene-environment factors:** **None established.** CRS6 is a monogenic disorder; there is no evidence of environmental risk factors, protective alleles, lifestyle factors, or gene–environment interactions. (Not applicable for this Mendelian disorder.)

### 3. Phenotypes

| Phenotype | Type | HPO suggestion | Onset / severity / frequency |
|---|---|---|---|
| Coronal craniosynostosis (usually bicoronal) | Physical/structural | HP:0004440 (coronal craniosynostosis); HP:0001363 (craniosynostosis) | Congenital or **postnatal** onset; severe; near-defining in the CS subgroup |
| Learning disability / developmental delay | Behavioral/cognitive | HP:0001328 (specific learning disability); HP:0001263 (global developmental delay) | Childhood; variable severity; common |
| Facial dysmorphism | Clinical sign | HP:0001999 (abnormal facial shape) | Congenital; variable; frequent in CS subgroup |
| Structural brain abnormalities (callosal agenesis, cerebellar/pons hypoplasia, rhombencephalosynapsis) | Imaging/structural | HP:0001274 (agenesis of corpus callosum); HP:0001321 (cerebellar hypoplasia) | Congenital; variable |
| Microcephaly | Physical | HP:0000252 | Neonatal (reported) |
| Scoliosis; tethered cord | Skeletal/neural | HP:0002650 (scoliosis); HP:0002144 (tethered cord) | Childhood; reported in sib pair |
| Reduced posterior fossa volume | Imaging | HP:0002707 | Congenital |

Evidence: coronal synostosis + learning disability as the characteristic dyad [PMID: 26340333](https://pubmed.ncbi.nlm.nih.gov/26340333/); facial dysmorphism + structural brain abnormalities + developmental delay in the craniosynostosis subgroup [PMID: 42028696](https://pubmed.ncbi.nlm.nih.gov/42028696/); microcephaly, callosal agenesis, cerebellar/pons hypoplasia, scoliosis, tethered cord, rhombencephalosynapsis [PMID: 30391508](https://pubmed.ncbi.nlm.nih.gov/30391508/).

**Quality-of-life impact:** craniosynostosis carries risk of raised intracranial pressure and ophthalmologic sequelae requiring surgery and surveillance; learning disability affects education/independence. Disorder-specific QoL instruments for CRS6 were not identified. Non-syndromic single-suture data show unicoronal synostosis is associated with ophthalmologic complications (~23.6%) and that surgical timing affects ICP/hydrocephalus risk [PMID: 42153715](https://pubmed.ncbi.nlm.nih.gov/42153715/) — relevant context, though not CRS6-specific.

### 4. Genetic / Molecular Information

- **Causal gene:** **ZIC1** (HGNC:12872; NCBI Gene 7545; chromosome 3q24; OMIM gene 600470).
- **Pathogenic variants (craniosynostosis):** nonsense, frameshift and rare missense changes **clustered in terminal exon 3**, predicted to **escape NMD** → stable protein → **gain of function** [PMID: 26340333](https://pubmed.ncbi.nlm.nih.gov/26340333/); [PMID: 42028696](https://pubmed.ncbi.nlm.nih.gov/42028696/). A frameshift at the end of exon 3 was documented with gonadal mosaicism [PMID: 30391508](https://pubmed.ncbi.nlm.nih.gov/30391508/).
- **Pathogenic variants (NDD without craniosynostosis):** **missense in exons 1–2** disrupting the zinc-finger domain → **loss of function** [PMID: 42028696](https://pubmed.ncbi.nlm.nih.gov/42028696/).
- **Classification:** per ACMG/AMP, exon-3 truncating variants escaping NMD are classified as pathogenic/likely pathogenic in the appropriate phenotypic context; **specific HGVS nomenclature was intentionally deferred to ClinVar/HGMD** during the investigation to avoid transcription error.
- **Allele frequency:** these are rare/private disease variants, not present at appreciable frequency in gnomAD (consistent with a severe dominant disorder); ZIC1 is highly constrained.
- **Origin:** germline (de novo or inherited); **gonadal/germline mosaicism documented** [PMID: 30391508](https://pubmed.ncbi.nlm.nih.gov/30391508/). No somatic disease role.
- **Chromosomal abnormalities:** a de novo **3q inversion with breakpoint 7 kb downstream of ZIC1** caused a ZIC1-dysregulation phenotype (bicoronal craniosynostosis + rhombencephalosynapsis), implicating position/TAD effects [PMID: 37950019](https://pubmed.ncbi.nlm.nih.gov/37950019/). Heterozygous **ZIC1;ZIC4 deletions** cause the allelic Dandy-Walker malformation [PMID: 15338008](https://pubmed.ncbi.nlm.nih.gov/15338008/).
- **Modifier / epigenetic:** no established modifier genes; variable expressivity suggests unidentified modifiers or stochastic/developmental factors. No disease-specific epigenetic signature reported.

### 5. Environmental Information

**Not applicable.** CRS6 is a monogenic gain-of-function disorder with no identified environmental, lifestyle, toxic, or infectious contributing factors.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (gain-of-function / craniosynostosis branch):**

1. A heterozygous truncating (or rare missense) variant arises in the **final exon 3 of ZIC1** (germline; sometimes de novo or via gonadal mosaicism). *(demonstrated)*
2. Because the premature stop/frameshift lies in the terminal exon, the mutant transcript **escapes nonsense-mediated decay**, so a **stable, truncated/altered ZIC1 protein is produced**. *(demonstrated — confirmed in patient cell line)* [PMID: 26340333]
3. The stable mutant protein acts in a **gain-of-function / dominant** manner, **altering/enhancing ZIC1 target-gene regulation** (e.g., engrailed-2/EN targets in Xenopus assay). *(demonstrated in vitro)*
4. In the developing skull, excess/aberrant ZIC1 activity in the **supraorbital regulatory center** (where Zic1 is expressed at mouse E11.5–12.5) **dysregulates patterning of the coronal suture**. *(inferred from expression domain + functional data)* [PMID: 26340333]
5. Elevated ZIC1 activity **drives osteogenic differentiation (RUNX2, osteocalcin) and activates Hedgehog signaling (Patched1)** in skeletal progenitors, **at the expense of alternative lineages**. *(demonstrated in human progenitor overexpression; mechanistic bridge to suture)* [PMID: 40151950]
6. This **tips the osteogenic/non-osteogenic boundary at the neural-crest/mesoderm interface** toward premature bone formation, **leading to premature fusion of the coronal suture (craniosynostosis)**. *(inferred, consistent with coronal-boundary biology)* [PMID: 26589924; PMID: 32916911]
7. Premature coronal fusion **results in abnormal skull shape and can lead to raised intracranial pressure, ophthalmologic sequelae, and contributes (with ZIC1's brain-patterning roles) to learning disability / structural brain abnormalities**. *(clinical observation)* [PMID: 26340333; PMID: 42028696]

**Branch (loss-of-function):** Missense in exons 1–2 → disrupted zinc-finger DNA binding → **loss of ZIC1 function** → **neurodevelopmental disorder without craniosynostosis** [PMID: 42028696]; and ZIC1/ZIC4 deletion → **reduced Shh-dependent granule-cell proliferation (↓Ptch1, Gli1, Mycn)** → cerebellar hypoplasia / **Dandy-Walker malformation** [PMID: 21307096; PMID: 15338008].

```
                 ZIC1 locus (3q24)
                        |
      +-----------------+------------------+
  EXON 3 truncating               EXON 1-2 missense /
  (escapes NMD)                   ZIC1;ZIC4 deletion
      | GAIN of function              | LOSS of function
      v                               v
 up osteogenesis (RUNX2/OCN)     down Shh output (Ptch1/Gli1/Mycn)
 up Hedgehog (Patched1)          down granule-cell proliferation
      v                               v
 premature CORONAL suture fusion  cerebellar hypoplasia
 + learning disability            -> Dandy-Walker / NDD (no CS)
```

**Pathways / processes / ontology suggestions:**
- Molecular pathways: **Sonic hedgehog**, **retinoic acid**, **TGFβ/BMP** signaling; engrailed (EN1/EN2) target regulation [PMID: 29442326; PMID: 26340333].
- Biological processes (GO): regulation of transcription by RNA polymerase II (GO:0006357); neural crest cell fate specification (GO:0014036); cranial suture morphogenesis; ossification (GO:0001503); osteoblast differentiation (GO:0001649); smoothened/Hedgehog signaling pathway (GO:0007224); regulation of neuron differentiation (GO:0045664).
- Cell types (CL): cranial neural crest cell (CL:0000333 neural crest cell); osteoblast (CL:0000062); skeletal/osteogenic progenitor; cerebellar granule cell (CL:0001031) for the LoF branch.
- Subcellular (GO CC): nucleus (GO:0005634) — ZIC1 is a nuclear transcription factor.
- Chemical entities (CHEBI): retinoic acid (CHEBI:50211); zinc (CHEBI:29105, zinc-finger cofactor).

### 7. Anatomical Structures Affected

- **Organ level:** skull/calvaria (primary); brain (secondary — cerebellum, corpus callosum, pons, posterior fossa); orbit/visual system; vertebral column.
- **Body systems:** skeletal and nervous systems predominantly.
- **Tissue/cell:** cranial **neural-crest-derived frontal bone** and **mesoderm-derived parietal bone**; the **coronal suture** at their boundary; osteogenic progenitors; cerebellar granule neurons (LoF branch).
- **UBERON suggestions:** cranial suture / coronal suture (UBERON:0000063); frontal bone (UBERON:0001678); parietal bone (UBERON:0001679); cerebellum (UBERON:0002037); corpus callosum (UBERON:0002336); posterior cranial fossa; skull (UBERON:0003129).
- **Lateralization:** craniosynostosis is typically **bilateral/bicoronal**; can be asymmetric.

### 8. Temporal Development

- **Onset:** congenital developmental disorder; **craniosynostosis may be present at birth or develop postnatally** — in at least one family it was NOT present at birth [PMID: 30391508](https://pubmed.ncbi.nlm.nih.gov/30391508/). Brain/structural anomalies are congenital.
- **Progression:** suture fusion is **progressive during infancy/early childhood**; skull deformity and risk of raised ICP evolve until surgically corrected. Developmental/learning features are generally **stable/chronic** (non-degenerative).
- **Critical period:** the therapeutic window for cranial vault surgery is infancy/early childhood; surgical timing influences ICP and hydrocephalus risk (general craniosynostosis data) [PMID: 42153715](https://pubmed.ncbi.nlm.nih.gov/42153715/).
- **Duration:** lifelong condition; no spontaneous remission of the genetic defect.

### 9. Inheritance and Population

- **Inheritance:** **autosomal dominant** (heterozygous variants; de novo or inherited).
- **Penetrance / expressivity:** high penetrance for craniosynostosis among exon-3 variant carriers but **variable expressivity** (range of brain/skeletal involvement, and postnatal vs congenital synostosis) [PMID: 30391508](https://pubmed.ncbi.nlm.nih.gov/30391508/).
- **Mosaicism:** **parental gonadal (germline) mosaicism documented**, relevant to recurrence-risk counseling [PMID: 30391508](https://pubmed.ncbi.nlm.nih.gov/30391508/).
- **Epidemiology:** **ultra-rare** — fewer than ~30 families reported worldwide at the time of the Watts 2026 cohort (22 families/30 individuals) [PMID: 42028696](https://pubmed.ncbi.nlm.nih.gov/42028696/). Precise prevalence/incidence are not established; ZIC1 accounts for a small minority of craniosynostosis cases. No founder effect, consanguinity role, sex bias, or ethnic predilection established.

### 10. Diagnostics

- **Clinical/imaging:** diagnosis of craniosynostosis by **skull CT (gold standard for suture fusion)**, 3D CT, and clinical exam; brain MRI for structural anomalies (callosal agenesis, cerebellar/pons hypoplasia, rhombencephalosynapsis, posterior fossa volume) [PMID: 30391508](https://pubmed.ncbi.nlm.nih.gov/30391508/). Ophthalmologic monitoring (including OCT of the optic nerve, feasible in children with craniosynostosis [PMID: 41735680](https://pubmed.ncbi.nlm.nih.gov/41735680/)) for papilledema/raised ICP.
- **Genetic testing (confirmatory):** **single-gene sequencing of ZIC1, craniosynostosis gene panels, whole-exome or whole-genome sequencing**. WGS / long-read sequencing adds value for **structural/regulatory variants** — a de novo 3q inversion downstream of ZIC1 was resolved only by **Nanopore long-read sequencing** [PMID: 37950019](https://pubmed.ncbi.nlm.nih.gov/37950019/). Interpretation must weigh **variant location (exon 3 vs 1–2)** and NMD-escape prediction.
- **Differential diagnosis:** other syndromic coronal craniosynostoses — **Saethre-Chotzen (TWIST1, TCF12)**, Muenke (FGFR3), Apert/Crouzon (FGFR2), and craniosynostosis with MSX2 gain of function; also Gomez-Lopez-Hernandez syndrome (clinical overlap with the ZIC1 rhombencephalosynapsis presentation) [PMID: 37950019](https://pubmed.ncbi.nlm.nih.gov/37950019/). TWIST1/TCF12/EFNA4/EphA4/Jagged1 act in the same coronal-suture boundary network [PMID: 34878091; PMID: 16540516; PMID: 19201948; PMID: 20727876].
- **Screening:** no population newborn screening; **cascade/familial testing** and genetic counseling for at-risk relatives are appropriate given dominant inheritance and documented mosaicism.

### 11. Outcome / Prognosis

- **Survival:** not a life-limiting genetic defect per se; **life expectancy is not clearly shortened** and the disorder is chronic rather than fatal. No disease-specific mortality data for CRS6.
- **Morbidity:** driven by **raised intracranial pressure, visual compromise, neurodevelopmental/learning disability, and need for (often multiple) cranial surgeries**. Comparative syndromic craniosynostosis experience (e.g., Apert syndrome 53-year follow-up) suggests many patients have near-normal lifespan without high cancer risk [PMID: 42082645](https://pubmed.ncbi.nlm.nih.gov/42082645/) — reassuring context, though not ZIC1-specific.
- **Prognostic factors:** severity of synostosis, presence/severity of brain malformation, degree of learning disability, and timeliness of surgical intervention. Surgical timing influences ICP/hydrocephalus outcomes in craniosynostosis generally [PMID: 42153715](https://pubmed.ncbi.nlm.nih.gov/42153715/).

### 12. Treatment

**No gene-targeted or pharmacologic disease-modifying therapy exists.** Management is **surgical and supportive**:

- **Surgical (primary):** cranial vault remodeling, **fronto-orbital advancement and remodeling**, **endoscope-assisted suturectomy with postoperative orthotic/helmet therapy**, **spring-assisted cranioplasty**, and **distraction osteogenesis**; vector/technique chosen by phenotype and age [PMID: 42686138](https://pubmed.ncbi.nlm.nih.gov/42686138/); [PMID: 42853819](https://pubmed.ncbi.nlm.nih.gov/42853819/). NCIT suggestions: Cranial Vault Remodeling; Fronto-Orbital Advancement; Craniectomy.
- **Supportive/rehabilitative:** developmental support, physical/occupational/speech therapy for developmental delay (benefit of early intensive rehabilitation illustrated in a related syndromic craniosynostosis case [PMID: 41893374](https://pubmed.ncbi.nlm.nih.gov/41893374/)); ophthalmologic and neurosurgical surveillance for ICP.
- **Experimental/targeted:** none established; the gain-of-function mechanism theoretically suggests allele-specific knockdown (ASO/siRNA) as a conceptual avenue, but **no clinical trials exist for ZIC1 craniosynostosis**.

### 13. Prevention

- **Primary prevention:** not possible for a monogenic de novo/inherited disorder. **Genetic counseling** is the main preventive tool, including discussion of **gonadal mosaicism and recurrence risk** [PMID: 30391508](https://pubmed.ncbi.nlm.nih.gov/30391508/).
- **Reproductive options:** prenatal testing / preimplantation genetic testing for families with a known pathogenic ZIC1 variant.
- **Secondary/tertiary prevention:** early imaging detection of synostosis and ICP; timely surgery; ophthalmologic and developmental surveillance to prevent complications.

### 14. Other Species / Natural Disease

- **Orthologues:** mouse *Zic1* (NCBI Gene 22771), with linked *Zic4*; *Xenopus zic1*; zebrafish zic1. Strongly conserved across vertebrates.
- **Model-organism disease:** mouse *Zic1/Zic4* loss recapitulates **Dandy-Walker malformation** (the LoF allelic disorder), and Zic1 loss causes cerebellar hypoplasia and vertebral defects [PMID: 15338008; PMID: 21307096]. No naturally occurring companion-animal "ZIC1 craniosynostosis" is documented (OMIA entry not identified). No zoonotic/transmission relevance (genetic disorder).
- **Comparative biology:** evolutionary conservation of ZIC1 as a neural-crest/neural-plate-border specifier underlies the cross-species utility of *Xenopus* and mouse models [PMID: 34638777; PMID: 41718037].

### 15. Model Organisms

| Model | Type | Findings / recapitulation | PMID |
|---|---|---|---|
| Mouse *Zic1/Zic4* heterozygous deletion | Mammalian, LoF | Closely resembles Dandy-Walker malformation (cerebellar size/foliation defects) | [15338008](https://pubmed.ncbi.nlm.nih.gov/15338008/); [21307096](https://pubmed.ncbi.nlm.nih.gov/21307096/) |
| Mouse embryo Zic1 expression mapping | Mammalian | Zic1 domain overlaps supraorbital regulatory center patterning the coronal suture (E11.5–12.5) | [26340333](https://pubmed.ncbi.nlm.nih.gov/26340333/) |
| *Xenopus* engrailed-2 / NC-GRN assays | Amphibian, in vivo functional | GoF variants alter/enhance engrailed-2 targets; zic1/pax3 regulate NC specification | [26340333](https://pubmed.ncbi.nlm.nih.gov/26340333/); [41718037](https://pubmed.ncbi.nlm.nih.gov/41718037/) |
| Human skeletal progenitor cells (in vitro) | Cellular | ZIC1 overexpression → ↑RUNX2/OCN, ↑Hedgehog (Patched1), brown adipogenesis | [40151950](https://pubmed.ncbi.nlm.nih.gov/40151950/) |

**Limitation of models:** no published mouse model reproduces the **gain-of-function exon-3 ZIC1 craniosynostosis** phenotype directly; current mammalian models capture the **loss-of-function (Dandy-Walker)** end, so a dedicated knock-in model of a terminal-exon truncation is a key gap.

---

## Mechanistic Model / Interpretation

ZIC1 disorders are best understood as a **dosage- and location-dependent allelic series around a single transcription factor** that controls both neural-crest specification and Hedgehog-linked osteogenesis. The unifying variable is the **direction and magnitude of ZIC1 activity**:

- **Too much / aberrant activity** (terminal-exon truncations escaping NMD) → excess osteogenic + Hedgehog drive in the supraorbital/coronal region → **premature coronal fusion (craniosynostosis)** plus brain-patterning disturbance → learning disability.
- **Too little activity** (zinc-finger missense; ZIC1/ZIC4 deletion) → reduced Shh-dependent granule-cell proliferation → **cerebellar hypoplasia / Dandy-Walker**, or NDD without craniosynostosis.

The **Hedgehog pathway is the shared mechanistic hub**: gain of function **raises** Hedgehog output (Patched1 up in osteogenic cells), while loss of function **lowers** it (Ptch1/Gli1/Mycn down in cerebellum). This mirror symmetry, plus ZIC1's position at the neural-crest/mesoderm boundary that defines the coronal suture, explains why coronal sutures are specifically vulnerable and why the same gene yields opposite malformations.

---

## Evidence Base

| PMID | Study | Role in this report |
|---|---|---|
| [26340333](https://pubmed.ncbi.nlm.nih.gov/26340333/) | Twigg et al. 2015 — *Gain-of-function ZIC1 mutations in coronal craniosynostosis* | Foundational: gene, exon-3 location, NMD escape, GoF mechanism, supraorbital expression |
| [42028696](https://pubmed.ncbi.nlm.nih.gov/42028696/) | Watts et al. 2026 — *Expanding the ZIC1 phenotypic spectrum* | Largest cohort; genotype–phenotype (CS vs NDD) correlation |
| [40151950](https://pubmed.ncbi.nlm.nih.gov/40151950/) | Thottappillil et al. 2025 — *ZIC1 overexpression & osteogenic/brown-adipogenic differentiation* | Mechanism: ZIC1 drives osteogenesis + Hedgehog |
| [30391508](https://pubmed.ncbi.nlm.nih.gov/30391508/) | Vandervore et al. 2018 — *ZIC1 sibling phenotype* | Gonadal mosaicism, postnatal synostosis, variable expressivity |
| [37950019](https://pubmed.ncbi.nlm.nih.gov/37950019/) | Murakami et al. 2024 — *3q inversion dysregulating ZIC1* | Regulatory/position-effect phenocopy; long-read sequencing utility |
| [21307096](https://pubmed.ncbi.nlm.nih.gov/21307096/) | Blank et al. 2011 — *Zic1/4 loss & Dandy-Walker* | LoF branch; Shh target downregulation |
| [15338008](https://pubmed.ncbi.nlm.nih.gov/15338008/) | Grinberg et al. 2004 — *ZIC1;ZIC4 deletion in DWM* | LoF allelic disorder; mouse model |
| [34638777](https://pubmed.ncbi.nlm.nih.gov/34638777/) | Bellchambers et al. 2021 — *SUMOylation & ZIC neural-crest specification* | ZIC1 as core neural-crest specifier |
| [41718037](https://pubmed.ncbi.nlm.nih.gov/41718037/) | Montequin & LaBonne 2026 — *NPB TF dynamics* | zic1/pax3 at neural plate border |
| [29442326](https://pubmed.ncbi.nlm.nih.gov/29442326/) | Aruga & Millen 2018 — *ZIC1 review* | Shh/RA/TGFβ integration; independent GoF-craniosynostosis confirmation |
| [26589924](https://pubmed.ncbi.nlm.nih.gov/26589924/) / [32916911](https://pubmed.ncbi.nlm.nih.gov/32916911/) | Ishii 2015 / Siismets & Hatch 2020 | Coronal-suture developmental biology; NC/mesoderm boundary |

---

## Limitations and Knowledge Gaps

1. **Ultra-rare disease, small N.** The core phenotype rests on ~27 families total across the key reports; frequency/penetrance estimates are imprecise.
2. **No GoF animal model.** Existing mammalian models capture the loss-of-function (Dandy-Walker) end; no knock-in reproduces exon-3 truncation craniosynostosis, so the GoF causal chain (steps 4–6) is partly **inferred**.
3. **Variant-level detail deferred.** Specific HGVS nomenclature and per-variant ACMG classifications were intentionally not transcribed here (to avoid error) and should be drawn from ClinVar/HGMD.
4. **Mechanistic bridge is correlative.** The link from "ZIC1 drives osteogenesis/Hedgehog in vitro" to "premature coronal fusion in vivo" is biologically plausible but not directly demonstrated in a craniosynostosis model.
5. **No epidemiology, QoL, or natural-history registries** specific to CRS6; prognosis is extrapolated from the broader craniosynostosis literature.
6. **No disease-specific epigenetic, metabolomic, or proteomic data.**

## Proposed Follow-up Experiments / Actions

1. **Generate a conditional knock-in mouse** carrying a terminal-exon ZIC1 truncation (NMD-escape) to test whether it reproduces coronal synostosis and to map osteogenic/Hedgehog dysregulation in vivo.
2. **Single-cell / spatial transcriptomics of the embryonic coronal suture** in GoF models to define the cell populations (CL terms) and Hedgehog-pathway state at the neural-crest/mesoderm boundary.
3. **Curate a definitive ZIC1 variant table** from ClinVar/HGMD stratified by exon and mechanism, with ACMG classifications, to operationalize the genotype–phenotype rule for diagnostic labs.
4. **Assess Hedgehog-pathway modulation** (e.g., smoothened antagonists) in GoF osteogenic-progenitor models as a proof-of-concept for mechanism-based intervention.
5. **Establish a CRS6 natural-history/QoL registry** capturing age at synostosis onset, ICP events, surgeries, and visual/neurodevelopmental outcomes.
6. **Prospectively apply long-read genome sequencing** in ZIC1-negative but clinically compatible cases to detect regulatory/structural variants (as in the 3q inversion case).

---

*Evidence source types: human clinical (Twigg 2015, Watts 2026, Vandervore 2018, Murakami 2024); model organism (Grinberg 2004, Blank 2011 mouse; Montequin 2026 Xenopus); in vitro (Thottappillil 2025 human progenitors); review/computational (Aruga & Millen 2018, Bellchambers 2021).*


## Artifacts

- [OpenScientist final report](ZIC1-Related_Craniosynostosis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ZIC1-Related_Craniosynostosis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 22 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.
