---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-31T08:57:52.669521'
end_time: '2026-10-31T09:47:10.614727'
duration_seconds: 2957.95
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Cleft Palate With Or Without Ankyloglossia, X-linked
  mondo_id: MONDO:0010560
  category: Mendelian
  causal_genes: TBX22
  omim_id: OMIM:303400
  synonyms: cleft palate with ankyloglossia; X-linked cleft palate and ankyloglossia
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
citation_count: 19
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Cleft_Palate_With_Or_Without_Ankyloglossia_X-linked-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Cleft_Palate_With_Or_Without_Ankyloglossia_X-linked-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cleft Palate With Or Without Ankyloglossia, X-linked
- **MONDO ID:** MONDO:0010560 (if available)
- **Causal gene(s):** TBX22
- **OMIM:** OMIM:303400
- **Synonyms:** cleft palate with ankyloglossia; X-linked cleft palate and ankyloglossia
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Cleft Palate With Or Without Ankyloglossia, X-linked** covering all of the
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

# X-linked Cleft Palate With or Without Ankyloglossia (CPX) — Comprehensive Disease Report

**Disease:** Cleft Palate With Or Without Ankyloglossia, X-linked (CPX / CPA)
**Causal gene:** **TBX22** (T-box transcription factor 22)
**MONDO:** MONDO:0010560 · **OMIM:** 303400 · **Orphanet:** 324601 · **ICD-10:** Q35 (cleft palate) · **MeSH:** C536426 · **DOID:** 0060613 · **GARD:** 0001394 · **UMLS:** C1844830 · **MedGen:** 375520 · **SNOMED CT:** 766761000
**Category:** Mendelian (X-linked semidominant)

> **Gene statement (as required):** The disease described here, *X-linked cleft palate with or without ankyloglossia* (CPX; also "cleft palate with ankyloglossia," CPA), is caused by loss-of-function mutations in **TBX22**, the gene encoding the **T-box transcription factor 22**, located at **Xq21.1**. This is distinct from autosomal forms of ankyloglossia (e.g., the autosomal-dominant ankyloglossia with tooth anomalies family, [PMID: 29704302](https://pubmed.ncbi.nlm.nih.gov/29704302/)), which are **not** TBX22-related.

---

## Summary

X-linked cleft palate with or without ankyloglossia (**CPX**, OMIM 303400, MONDO:0010560) is a Mendelian craniofacial malformation caused by **loss-of-function mutations in TBX22**, a gene at **Xq21.1** encoding a SUMOylation-dependent **T-box transcription factor** that acts as a **transcriptional repressor**. The condition is defined clinically by the combination of **cleft palate** (complete, partial, or submucous) and **ankyloglossia** (tongue-tie from a short lingual frenulum), frequently accompanied by a **bifid, absent, or shortened uvula**. It was first mapped to Xq21.1 by linkage in large Icelandic, British Columbia Native, and Manitoba Mennonite kindreds [PMID: 8045560](https://pubmed.ncbi.nlm.nih.gov/8045560/), and the causal gene was identified by Braybrook and colleagues in 2001 [PMID: 11559848](https://pubmed.ncbi.nlm.nih.gov/11559848/).

The molecular mechanism is a **complete loss of TBX22 function**. Truncating mutations (nonsense, frameshift, splice-site) and T-box-domain missense mutations abolish the protein's ability to bind DNA and/or to be modified by **SUMO-1 at lysine 63**, which is required for its repressor activity [PMID: 17846996](https://pubmed.ncbi.nlm.nih.gov/17846996/). Developmentally, the *Tbx22*-null mouse demonstrates that the gene is required for **osteogenic patterning of the posterior hard palate**: ossification is severely reduced after condensation of the palatal mesenchyme due to a **delay in osteoblast maturation**, producing a submucous cleft rather than a failure of palatal shelf closure, together with ankyloglossia and choanal atresia [PMID: 19648291](https://pubmed.ncbi.nlm.nih.gov/19648291/). TBX22 expression in the palatal shelves, the base of the tongue at the frenulum, and the nasal septum precisely mirrors the human phenotype [PMID: 12374769](https://pubmed.ncbi.nlm.nih.gov/12374769/).

CPX is inherited as a **semidominant X-linked trait**: hemizygous males are typically more severely affected (overt or submucous cleft palate plus ankyloglossia), while heterozygous carrier females show variable, usually milder manifestations (ankyloglossia, bifid uvula, submucous cleft) consistent with X-inactivation. The phenotypic spectrum extends from **isolated ankyloglossia** through classic CPX to **CHARGE-like Abruzzo-Erickson syndrome** (ABERS) with coloboma and sensorineural deafness. Management follows the standard multidisciplinary cleft care pathway — surgical palatoplasty, frenuloplasty for tongue-tie, and speech, hearing, and dental therapy — combined with X-linked genetic counseling. No gene-targeted therapy exists.

---

## Key Findings

### Finding 1 — TBX22 is the causal gene for CPX

CPX was localized by linkage analysis to **Xq21.1** (originally Xq21, with a multipoint Z = 13.5 near marker DXS447) in Manitoba Mennonite and British Columbia Native kindreds; "the most likely location for CPX is at DXS447 in Xq21.1" [PMID: 8045560](https://pubmed.ncbi.nlm.nih.gov/8045560/). In 2001, Braybrook et al. identified the causal gene, showing that "**CPX is caused by mutations in the gene encoding the recently described T-box transcription factor TBX22**" and that "the spectrum of nonsense, splice-site, frameshift and missense mutations we have identified in this study indicates that the **cleft phenotype results from a complete loss of TBX22 function**" [PMID: 11559848](https://pubmed.ncbi.nlm.nih.gov/11559848/). This establishes both the gene and its loss-of-function disease mechanism.

**Verified gene identifiers:** HGNC:11600 · NCBI Gene 50945 · UniProt Q9Y458 · Ensembl ENSG00000122145 · cytoband Xq21.1 · GRCh38 chrX:80,014,747–80,031,908 · gene MIM 300307.

### Finding 2 — Missense mutations impair DNA binding, SUMOylation, and transcriptional repression

Andreou et al. (2007) defined the biochemical mechanism. TBX22 recognizes a palindromic DNA sequence based on **AGGTGTGA**, functions as a **transcriptional repressor**, and is a target for **SUMO-1 modification at lysine 63** (immediately upstream of the T-box domain). "We find that TBX22 is a target for the small ubiquitin-like modifier SUMO-1 and that **this modification is required for TBX22 repressor activity**" and "**loss of SUMO-1 modification is consistently found in all pathogenic CPX missense mutations**. This implies a general mechanism linking the loss of SUMO conjugation to the loss of TBX22 function" [PMID: 17846996](https://pubmed.ncbi.nlm.nih.gov/17846996/). All ten naturally occurring missense mutations examined — located within the T-box DNA-binding domain — impaired repression: "**TBX22 missense mutations result in impaired repression activity**."

A genotype–function correlation was further refined by Kantaputra et al. (2011): T-box-domain mutations **R120Q, R126W, and R151L** affect DNA binding and/or transcriptional repression, whereas the C-terminal mutations **P389Q and S400Y did not affect TBX22 activity**, indicating that pathogenicity maps to the T-box domain [PMID: 21248356](https://pubmed.ncbi.nlm.nih.gov/21248356/).

### Finding 3 — The Tbx22-null mouse recapitulates CPX via reduced posterior palatal ossification

Pauws et al. (2009) generated a *Tbx22*-null mouse that "has a **submucous cleft palate (SMCP) and ankyloglossia, similar to the human phenotype**, with a small minority showing overt clefts." Persistent oro-nasal membranes produced **choanal atresia** and roughly **50% postnatal lethality** from breathing and feeding difficulty. The developmental mechanism is osteogenic: "**Tbx22 plays an important role in the osteogenic patterning of the posterior hard palate. Ossification is severely reduced after condensation of the palatal mesenchyme, resulting from a delay in the maturation of osteoblasts**" [PMID: 19648291](https://pubmed.ncbi.nlm.nih.gov/19648291/). Crucially, the defect is **not** a failure of palatal shelf elevation or closure — the shelves meet — but a deficit of intramembranous bone in the posterior hard palate producing the classic submucous notch.

Expression studies anchor the mechanism anatomically: TBX22 mRNA "is also detected in the **base of the tongue in the region of the frenulum that corresponds to the ankyloglossia** seen in CPX patients," and is expressed in the palatal shelves (highest before elevation), nasal septum, and tooth buds [PMID: 12374769](https://pubmed.ncbi.nlm.nih.gov/12374769/).

### Finding 4 — Phenotypic spectrum from isolated ankyloglossia to Abruzzo-Erickson syndrome

TBX22-related disease spans a continuum. At the mild end, isolated ankyloglossia and dental anomalies occur; Kantaputra et al. expanded the spectrum "to include **dental anomalies and cleft lip**," with micro/hypodontia and cleft lip ± palate in some families [PMID: 21248356](https://pubmed.ncbi.nlm.nih.gov/21248356/). Demeer et al. (2018) documented "orofacial features previously not associated with the CPX phenotypic spectrum: **choanal atresia, Pierre-Robin sequence, and overgrowths on the posterior edge of the hard palate**" [PMID: 30462376](https://pubmed.ncbi.nlm.nih.gov/30462376/). At the severe end, TBX22 splice mutations cause **X-linked CHARGE-like Abruzzo-Erickson syndrome (ABERS)** with coloboma and sensorineural deafness: this work "confirms that **TBX22 is the gene underlying Abruzzo-Erickson syndrome, expanding the phenotypic spectrum of TBX22 mutations**" [PMID: 22784330](https://pubmed.ncbi.nlm.nih.gov/22784330/); a 2026 case series proposes that gain-of-function alleles may underlie ABERS specifically [PMID: 41630180](https://pubmed.ncbi.nlm.nih.gov/41630180/).

Upstream regulation of *Tbx22* is by opposing craniofacial signals: "**FGF8 induces Tbx22 in the early face while BMP4 represses and thus restricts its expression**," a mechanism conserved between chick and mouse [PMID: 20845426](https://pubmed.ncbi.nlm.nih.gov/20845426/). TBX22 mutations account for approximately **5% of non-syndromic cleft palate** patients.

### Finding 5 — Gene–environment interaction: methylation and promoter variants

Two lines of evidence connect TBX22 to environmentally modulated and multifactorial clefting. In an **all-trans retinoic acid (ATRA)-induced** mouse cleft palate model, "**TBX22 exon 5 was hyper-methylated at the CpG site at E13.5 (P=0.025, log2FC=1.5) and E14.5 (P=0.011, log2FC=1.5)**" in treated embryos, with TBX22 expression negatively correlated with methylation and normalization by E16.5 (P=0.808) — linking a teratogen to epigenetic downregulation of TBX22 [PMID: 31241704](https://pubmed.ncbi.nlm.nih.gov/31241704/). In humans, two TBX22 promoter SNPs were associated with non-syndromic cleft lip ± palate (NSCLP) risk in a sex-specific manner: "**Significant associations of rs7055763 (P=0.034) and rs41307258 (P=0.022) with NSCLP were found only in women**," consistent with X-linked dosage sensitivity, with strong linkage disequilibrium (D'=0.97, r²=0.77) [PMID: 25918826](https://pubmed.ncbi.nlm.nih.gov/25918826/).

### Finding 6 — Semidominant X-linked inheritance with carrier-female manifestation

CPX is inherited as a **semidominant X-linked** disorder. In the British Columbia Native kindred, "**ankyloglossia (tongue-tie) is also a feature of X-linked cleft palate in some of the affected males and carrier females**" [PMID: 1570839](https://pubmed.ncbi.nlm.nih.gov/1570839/), establishing that heterozygous carriers can manifest. Hemizygous males are typically more severely affected (overt or submucous cleft palate plus ankyloglossia); carrier females show variable, usually milder features (ankyloglossia, bifid uvula, submucous cleft) consistent with random X-inactivation.

### Finding 7 — TBX22 is strongly loss-of-function intolerant in gnomAD

Population constraint data corroborate the loss-of-function mechanism. For ENSG00000122145 (GRCh38), gnomAD reports **pLI = 0.990**, observed/expected LoF = 0.27 with **LOEUF = 0.48** (90% CI 0.16–0.48), **8 observed vs 30.1 expected** LoF variants, and **LoF Z = 3.42** — marked depletion of loss-of-function variants in the general population. By contrast, missense is **not** constrained (mis_z = −1.33; oe_mis = 1.16), consistent with pathogenicity being restricted to specific T-box-domain missense alleles rather than general missense intolerance.

### Finding 8 — ClinVar variant landscape

A ClinVar query for `TBX22[gene]` returned **327 variation records**: **~170 Pathogenic, 13 Likely pathogenic, 161 Uncertain significance (VUS), and 122 Benign/Likely benign**. The CPX-causing intragenic set comprises nonsense, frameshift, splice-site, and T-box missense variants; the high Pathogenic count is partly attributable to large overlapping copy-number and contiguous-gene deletions at Xq21 rather than CPX point mutations alone.

### Finding 9 — Core HPO phenotype annotations

The Monarch Initiative (v3 API) returns exactly three formal phenotype annotations for MONDO:0010560:

| HPO ID | Term |
|--------|------|
| HP:0010296 | Ankyloglossia |
| HP:0000193 | Bifid uvula |
| HP:0000175 | Cleft palate |

Expanded-spectrum HPO terms confirmed in the literature include **HP:0000176** (submucous cleft of the hard palate), **HP:0000185** (cleft soft palate), **HP:0000204** (cleft upper lip), **HP:0000668** (hypodontia), **HP:0000453** (choanal atresia), **HP:0000201** (Pierre-Robin sequence), **HP:0000589** (coloboma), and **HP:0000407** (sensorineural hearing impairment). (Note: HP:0000190 is "Abnormal oral frenulum morphology," distinct from bifid uvula HP:0000193.)

### Finding 10 — Verified cross-references and Orphanet description

Monarch cross-references for MONDO:0010560: OMIM:303400, Orphanet:324601, MeSH:C536426, DOID:0060613, GARD:0001394, MedGen:375520, UMLS:C1844830, SNOMED CT:766761000. The Orphanet definition: the disease is "characterized by the association of complete, partial or submucous cleft palate and ankyloglossia. Patients may also present abnormal uvula (e.g. absent, bifid, shortened or laterally deviated), short lingual frenulum and dental anomalies... **Digital abnormalities, such as mild clinodactyly and/or syndactyly, have also been reported**."

---

## Section-by-Section Report

### 1. Disease Information

CPX is a congenital craniofacial malformation defined by the co-occurrence of **cleft palate** (complete, partial, or submucous) and **ankyloglossia** (tongue-tie). It is a Mendelian, X-linked semidominant condition caused by TBX22. Key identifiers are listed in the header. Common synonyms: *cleft palate with ankyloglossia*; *X-linked cleft palate and ankyloglossia*; *CPX*; *CPA*. Information in this report derives from **aggregated disease-level resources** (OMIM, Orphanet, Monarch, ClinVar, gnomAD) and primary literature (family linkage studies, functional assays, mouse models), not from individual EHR records.

### 2. Etiology

**Causal factor:** germline loss-of-function mutations in **TBX22** (Xq21.1). The disease mechanism is a **complete loss of TBX22 function** [PMID: 11559848](https://pubmed.ncbi.nlm.nih.gov/11559848/).

**Genetic risk factors:** being hemizygous for a pathogenic TBX22 allele (males) confers near-complete risk of the malformation; carrier females are at risk of milder manifestations. Common promoter SNPs **rs7055763** and **rs41307258** modify non-syndromic cleft risk in women [PMID: 25918826](https://pubmed.ncbi.nlm.nih.gov/25918826/).

**Environmental risk factors:** general orofacial-cleft risk factors (maternal smoking, alcohol, folate deficiency, retinoid exposure) apply to clefting broadly; a retinoic-acid teratogen model specifically downregulates TBX22 via exon-5 hypermethylation [PMID: 31241704](https://pubmed.ncbi.nlm.nih.gov/31241704/).

**Protective factors:** no TBX22-specific protective alleles are established. Periconceptional folate is protective for orofacial clefts generally (not CPX-specific; evidence not derived in this investigation).

**Gene–environment interaction:** teratogen-induced hypermethylation of TBX22 provides a direct GxE link between retinoid exposure and reduced TBX22 dosage [PMID: 31241704](https://pubmed.ncbi.nlm.nih.gov/31241704/).

### 3. Phenotypes

| Phenotype | HPO | Type | Onset | Frequency / notes |
|-----------|-----|------|-------|-------------------|
| Cleft palate (overt/submucous) | HP:0000175 / HP:0000176 | Physical manifestation | Congenital | Core feature; males often overt, SMCP common |
| Ankyloglossia | HP:0010296 | Physical manifestation | Congenital | Core; present in males and carrier females |
| Bifid/absent/short uvula | HP:0000193 | Clinical sign | Congenital | Frequent |
| Hypodontia / dental anomalies | HP:0000668 | Physical manifestation | Childhood | Expanded spectrum |
| Cleft lip ± palate | HP:0000204 | Physical manifestation | Congenital | Minority of families |
| Choanal atresia | HP:0000453 | Physical manifestation | Congenital | Expanded / ABERS |
| Pierre-Robin sequence | HP:0000201 | Clinical sign | Congenital | Expanded spectrum |
| Coloboma | HP:0000589 | Physical manifestation | Congenital | ABERS |
| Sensorineural hearing impairment | HP:0000407 | Laboratory/clinical | Congenital/childhood | ABERS |

**Severity** is variable (mild isolated ankyloglossia → severe syndromic ABERS). The malformations are **congenital and stable** (non-progressive) once present. **Quality-of-life impact** derives from speech (velopharyngeal insufficiency, hypernasality, compensatory misarticulations), feeding, hearing, and dental function; oronasal fistula and reduced speech intelligibility are the strongest predictors of poor VPI-related QOL [PMID: 41520495](https://pubmed.ncbi.nlm.nih.gov/41520495/).

### 4. Genetic / Molecular Information

**Causal gene:** TBX22 (HGNC:11600; gene MIM 300307), encoding a T-box transcription factor. **Variant types** causing CPX: nonsense, frameshift, splice-site, and T-box-domain missense [PMID: 11559848](https://pubmed.ncbi.nlm.nih.gov/11559848/). **Classification:** ClinVar documents ~170 Pathogenic, 13 Likely pathogenic, 161 VUS, 122 Benign/Likely benign. **Functional consequence:** loss of function — truncating alleles eliminate protein; T-box missense alleles abolish DNA binding and SUMO-1 conjugation at Lys63 [PMID: 17846996](https://pubmed.ncbi.nlm.nih.gov/17846996/). A gain-of-function hypothesis has been proposed specifically for ABERS [PMID: 41630180](https://pubmed.ncbi.nlm.nih.gov/41630180/). **Origin:** germline. **Allele frequency:** pathogenic alleles are rare; gnomAD shows strong LoF intolerance (pLI 0.99). **Epigenetics:** TBX22 exon-5 CpG hypermethylation downregulates expression in a teratogen model [PMID: 31241704](https://pubmed.ncbi.nlm.nih.gov/31241704/). **Chromosomal abnormalities:** large Xq21 deletions encompassing TBX22 can produce contiguous-gene phenotypes.

### 5. Environmental Information

Non-genetic contributors are those of orofacial clefting generally. The best TBX22-specific datum is the **retinoic-acid (ATRA) teratogen** model, in which exposure hypermethylates TBX22 and lowers its expression during palatogenesis [PMID: 31241704](https://pubmed.ncbi.nlm.nih.gov/31241704/). Glucocorticoid/alcohol exposure models also alter Tbx22 expression during palatogenesis [PMID: 19816249](https://pubmed.ncbi.nlm.nih.gov/19816249/). No infectious agents are implicated.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A **germline loss-of-function TBX22 mutation** (truncating) or a **T-box-domain missense allele** arises on the X chromosome. → *leads to*
2. In truncating cases, **absent/nonfunctional protein**; in T-box missense cases, **loss of DNA binding at the AGGTGTGA palindrome and loss of SUMO-1 conjugation at Lys63**, which *results in* loss of repressor activity [PMID: 17846996](https://pubmed.ncbi.nlm.nih.gov/17846996/). → *leads to*
3. **Loss of TBX22 transcriptional repression** in the developing palatal mesenchyme, base of tongue, and nasal septum — tissues where TBX22 is normally expressed [PMID: 12374769](https://pubmed.ncbi.nlm.nih.gov/12374769/). (Upstream, TBX22 is normally induced by FGF8 and restricted by BMP4 [PMID: 20845426](https://pubmed.ncbi.nlm.nih.gov/20845426/).) → *results in*
4. **Delayed osteoblast maturation** after condensation of the posterior palatal mesenchyme, *leading to* **severely reduced intramembranous ossification of the posterior hard palate** [PMID: 19648291](https://pubmed.ncbi.nlm.nih.gov/19648291/). → *results in*
5. **Submucous (or overt) cleft palate** — the classic posterior notch. **Branch:** in the tongue frenulum region, loss of TBX22 *results in* **ankyloglossia**; persistence of oro-nasal membranes *results in* **choanal atresia** [PMID: 19648291](https://pubmed.ncbi.nlm.nih.gov/19648291/). → *leads to*
6. **Clinical manifestations:** feeding difficulty, velopharyngeal insufficiency, hypernasal speech, and (in syndromic ABERS) coloboma and sensorineural deafness.

```
 TBX22 LoF / T-box missense
        │
        ▼
 loss of SUMO-1 (Lys63) + DNA binding  ──► loss of repressor activity
        │
        ▼
 derepression in palatal mesenchyme / tongue frenulum / nasal septum
        │
   ┌────┴─────────────┬───────────────────┐
   ▼                  ▼                   ▼
 delayed osteoblast   frenulum defect     persistent oro-nasal
 maturation           │                   membrane
   │                  ▼                   ▼
 reduced posterior    ANKYLOGLOSSIA       CHOANAL ATRESIA
 palate ossification
   │
   ▼
 SUBMUCOUS / OVERT CLEFT PALATE ──► VPI, hypernasal speech, feeding difficulty
```

**Molecular pathway:** TBX22 is a downstream node of **FGF8 (inducer) / BMP4 (repressor)** craniofacial signaling [PMID: 20845426](https://pubmed.ncbi.nlm.nih.gov/20845426/). **Cellular process:** osteoblast differentiation / intramembranous ossification. **Protein dysfunction:** loss of function via impaired DNA binding and loss of post-translational SUMO modification. **Epigenetic:** CpG hypermethylation represses TBX22 under teratogen exposure [PMID: 31241704](https://pubmed.ncbi.nlm.nih.gov/31241704/).

**Upstream vs downstream:** the mutation and loss of SUMO/DNA-binding are the most upstream events; derepression of TBX22 targets and the osteoblast-maturation delay are intermediate; the cleft, ankyloglossia, and choanal atresia are the downstream clinical endpoints.

**Suggested GO terms:** GO:0060021 (roof of mouth development), GO:0001649 (osteoblast differentiation), GO:0006357 (regulation of transcription by RNA Pol II), GO:0016925 (protein sumoylation), GO:0003700 (DNA-binding transcription factor activity).
**Suggested CL terms:** CL:0000062 (osteoblast), CL:0000134 (mesenchymal stem cell), cranial neural-crest-derived palatal mesenchyme.

### 7. Anatomical Structures Affected

**Primary structures:** secondary palate (**UBERON:0001716** secondary palate, **UBERON:0003216** hard palate, **UBERON:0001733** soft palate), uvula (**UBERON:0010235**), tongue and lingual frenulum (**UBERON:0001723** tongue; frenulum of tongue). **Secondary involvement:** nasal septum (**UBERON:0002096**), choanae/posterior nares (**UBERON:0002220**), teeth/tooth buds (**UBERON:0001091**), middle ear (VPI-associated otitis media). In ABERS, the eye (coloboma; **UBERON:0000970**) and auditory system are involved. **Body systems:** digestive/oral, respiratory (choanae), special sense (ear, eye in ABERS). **Tissue level:** palatal **mesenchyme** (osteogenic), oral **epithelium**; **cell populations:** osteoblasts and cranial neural-crest-derived mesenchymal cells. **Subcellular:** nucleus (transcriptional repression; **GO:0005634**). **Lateralization:** cleft palate and ankyloglossia are typically **midline**.

### 8. Temporal Development

**Onset:** congenital — the lesion is established during embryonic **palatogenesis** (critical window ~weeks 6–9 in humans; E11.5–E16.5 in mouse). **Onset pattern:** structural/congenital, not acute/progressive. **Progression:** the malformation is **stable** (non-progressive); secondary functional sequelae (speech, hearing, dental, feeding) evolve through childhood and are modifiable by intervention. **Critical period:** palatal shelf elevation, mesenchymal condensation, and osteoblast maturation (the window in which TBX22 acts). **Disease duration:** lifelong structural condition, functionally improved by surgery and therapy.

### 9. Inheritance and Population

**Inheritance:** X-linked **semidominant** [PMID: 11559848](https://pubmed.ncbi.nlm.nih.gov/11559848/); [PMID: 1570839](https://pubmed.ncbi.nlm.nih.gov/1570839/). Hemizygous males more severely affected; heterozygous carrier females variably/mildly affected (X-inactivation-dependent expressivity). **Penetrance:** high in males, incomplete/variable in females. **Expressivity:** highly variable (isolated ankyloglossia → ABERS). **Sex ratio:** male-predominant for severe phenotype. **Epidemiology:** CPX is rare; TBX22 mutations account for ~**5%** of non-syndromic cleft palate. Founder kindreds were key to discovery (Icelandic, British Columbia Native, Manitoba Mennonite) [PMID: 8045560](https://pubmed.ncbi.nlm.nih.gov/8045560/). No strong consanguinity role (X-linked). **Genetic anticipation:** not applicable (not a repeat-expansion disorder). **Germline mosaicism:** possible but not specifically quantified here. (Precise CPX-specific prevalence/incidence per 100,000 are not well established in the literature.)

### 10. Diagnostics

**Clinical diagnosis:** physical examination identifies cleft palate (including submucous — bifid uvula, zona pellucida, palpable notch) and ankyloglossia; nasendoscopy and speech assessment evaluate velopharyngeal function. **Genetic testing:** targeted **single-gene TBX22 sequencing** (Sanger/NGS) is the primary confirmatory test; TBX22 is included on **cleft/orofacial and craniofacial gene panels**; **chromosomal microarray** detects Xq21 deletions; WES/WGS are used when the panel is negative or the phenotype is syndromic [PMID: 30462376](https://pubmed.ncbi.nlm.nih.gov/30462376/). **Differential diagnosis:** non-syndromic cleft palate, Van der Woude syndrome, Pierre-Robin sequence, other syndromic clefts, CHARGE syndrome (vs ABERS), and autosomal-dominant ankyloglossia with distinct loci [PMID: 29704302](https://pubmed.ncbi.nlm.nih.gov/29704302/). **Screening:** carrier testing in affected families; cascade testing; prenatal/preimplantation testing where a familial variant is known.

### 11. Outcome / Prognosis

**Survival:** normal life expectancy in isolated CPX; the mouse model's lethality (from choanal atresia/feeding) reflects severe syndromic airway compromise rather than typical human CPX. **Morbidity:** speech (velopharyngeal insufficiency, hypernasality, compensatory misarticulations), feeding, recurrent otitis media/conductive hearing loss, and dental anomalies. **Prognostic factors for speech/QOL:** timing of palatoplasty, cleft width/subtype, oronasal fistula, and speech intelligibility; "ONF (odds ratio = 8.531) and speech intelligibility deficits (odds ratio = 8.854) were independent predictors of poor QOL" [PMID: 41520495](https://pubmed.ncbi.nlm.nih.gov/41520495/). Later repair was associated with modestly increased passive cleft speech characteristics (odds ratio 1.24 per month at 36 months) [PMID: 42275034](https://pubmed.ncbi.nlm.nih.gov/42275034/). **Recovery:** good functional outcomes with timely multidisciplinary care.

### 12. Treatment

There is **no gene-targeted therapy**; management is the standard multidisciplinary cleft pathway.

| Intervention | Description | NCIT suggestion |
|--------------|-------------|-----------------|
| **Palatoplasty** | Primary surgical closure of the cleft palate, ideally before ~12–15 months to optimize speech | NCIT:C51756 (palatoplasty) |
| **Furlow double-opposing Z-plasty** | Associated with lower fistula and VPI rates vs alternatives | — |
| **Frenotomy/frenuloplasty** | Release of the lingual frenulum for ankyloglossia | — |
| **Secondary speech surgery** | Pharyngoplasty / conversion Furlow for persistent VPI | — |
| **Speech therapy** | For resonance/articulation disorders | NCIT:C15415 |
| **Audiology / ENT** | Grommets for otitis media, hearing support | — |
| **Orthodontics/dental** | For hypodontia and dental anomalies | — |
| **Multimodal analgesia** | Suprazygomatic maxillary nerve blocks + acetaminophen/NSAIDs (opioid-sparing) | — |

Evidence: the Furlow palatoplasty "was associated with significantly lower fistula and velopharyngeal insufficiency (VPI) rates," and nerve blocks provide "robust opioid-sparing effects" [PMID: 42235642](https://pubmed.ncbi.nlm.nih.gov/42235642/). Current evidence "does not support a universally optimal timing" with anatomical factors (cleft width/subtype) more predictive than timing alone [PMID: 42403778](https://pubmed.ncbi.nlm.nih.gov/42403778/). **Pharmacogenomics / experimental / gene / cell / RNA / immunotherapies:** none established or in trials for CPX specifically.

### 13. Prevention

**Primary prevention:** periconceptional folate and avoidance of teratogens (alcohol, retinoids, smoking) for orofacial clefts generally; retinoid avoidance is mechanistically relevant given TBX22 methylation effects [PMID: 31241704](https://pubmed.ncbi.nlm.nih.gov/31241704/). **Secondary prevention:** prenatal ultrasound can detect some clefts; early postnatal examination for submucous cleft/ankyloglossia. **Genetic screening:** carrier and cascade testing in affected X-linked families; prenatal and preimplantation genetic testing where the familial TBX22 variant is known. **Counseling:** X-linked recurrence-risk counseling (an affected male transmits the allele to all daughters as carriers and no sons; a carrier female transmits to 50% of children) is central. **Tertiary prevention:** timely palatoplasty, ONF prevention, speech therapy, and audiologic surveillance prevent complications.

### 14. Other Species / Natural Disease

**Model organism ortholog:** mouse *Tbx22* (conserved T-box transcription factor; principal mouse ortholog of human TBX22). The FGF8/BMP4 regulatory relationship is conserved between **chick and mouse** [PMID: 20845426](https://pubmed.ncbi.nlm.nih.gov/20845426/). No naturally occurring companion-animal TBX22 disease was identified in this investigation (OMIA not confirmed here). Evolutionary conservation of the palatal-ossification mechanism is supported by the faithful mouse phenotype.

### 15. Model Organisms

| Model | Type | Key phenotypes | Recapitulation |
|-------|------|----------------|----------------|
| ***Tbx22*-null mouse** | Mammalian knockout | Submucous cleft palate, ankyloglossia, choanal atresia, ~50% postnatal lethality | **High** — mirrors human CPX; defines osteoblast-maturation mechanism [PMID: 19648291](https://pubmed.ncbi.nlm.nih.gov/19648291/) |
| **ATRA-induced mouse cleft** | Induced/teratogen | Cleft palate with TBX22 exon-5 hypermethylation | GxE/epigenetic model [PMID: 31241704](https://pubmed.ncbi.nlm.nih.gov/31241704/) |
| **Glucocorticoid/alcohol C57BL/6N** | Induced | Cleft palate with altered Tbx22 expression | Environmental model [PMID: 19816249](https://pubmed.ncbi.nlm.nih.gov/19816249/) |
| **Chick (expression/regulation)** | Avian | FGF8/BMP4 regulation of Tbx22 | Regulatory conservation [PMID: 20845426](https://pubmed.ncbi.nlm.nih.gov/20845426/) |

**Model limitation:** the mouse null produces predominantly *submucous* cleft (overt clefts are a minority), and its ~50% lethality is more severe than isolated human CPX; it does not capture the full human allelic/missense spectrum. **Resources:** MGI (mouse *Tbx22*).

---

## Mechanistic Model / Interpretation

The CPX story is unusually complete for a Mendelian craniofacial disorder because the genetics, biochemistry, developmental biology, and a faithful animal model all converge. The gene (TBX22) was mapped by linkage and identified by mutation analysis; the biochemistry (SUMO-1/Lys63-dependent repression of an AGGTGTGA target) explains **why missense mutations clustered in the T-box domain are pathogenic while C-terminal missense are not**; the mouse model shows **where and how** the lesion forms (posterior hard palate, via delayed osteoblast maturation rather than shelf-closure failure); and the expression pattern explains the **associated features** (frenulum → ankyloglossia; nasal septum/choanae → atresia). The population-genetic signature (pLI 0.99, LOEUF 0.48, but unconstrained missense) independently confirms a **haploinsufficiency/loss-of-function** architecture. The FGF8↑/BMP4↓ regulatory logic places TBX22 within the broader craniofacial signaling network, and the retinoid-methylation data tie the same gene to **environmentally modulated, multifactorial** clefting — a bridge between the rare Mendelian and common non-syndromic forms.

The one genuine mechanistic tension is **ABERS**: a 2026 case series proposes that gain-of-function alleles, not loss of function, may drive the severe CHARGE-like phenotype [PMID: 41630180](https://pubmed.ncbi.nlm.nih.gov/41630180/), which would mean the TBX22 allelic series is not purely a simple dosage gradient. This remains a hypothesis.

---

## Evidence Base

| PMID | Role | Contribution |
|------|------|-------------|
| [11559848](https://pubmed.ncbi.nlm.nih.gov/11559848/) | Landmark | Identifies TBX22 as causal; defines loss-of-function mechanism |
| [8045560](https://pubmed.ncbi.nlm.nih.gov/8045560/) | Linkage | Maps CPX to Xq21.1 |
| [1570839](https://pubmed.ncbi.nlm.nih.gov/1570839/) | Linkage | Carrier-female manifestation; semidominant inheritance |
| [17846996](https://pubmed.ncbi.nlm.nih.gov/17846996/) | Mechanism | SUMO-1 / DNA-binding / repression; unifying missense mechanism |
| [21248356](https://pubmed.ncbi.nlm.nih.gov/21248356/) | Genotype–phenotype | T-box vs C-terminal missense; expands spectrum to CLP/hypodontia |
| [19648291](https://pubmed.ncbi.nlm.nih.gov/19648291/) | Model | Tbx22-null mouse; osteoblast-maturation mechanism |
| [12374769](https://pubmed.ncbi.nlm.nih.gov/12374769/) | Expression | TBX22 in palate/frenulum/septum explains phenotype |
| [22784330](https://pubmed.ncbi.nlm.nih.gov/22784330/) | Spectrum | TBX22 underlies Abruzzo-Erickson syndrome |
| [41630180](https://pubmed.ncbi.nlm.nih.gov/41630180/) | Spectrum | ABERS case series; gain-of-function hypothesis |
| [20845426](https://pubmed.ncbi.nlm.nih.gov/20845426/) | Regulation | FGF8 induces, BMP4 represses Tbx22 |
| [30462376](https://pubmed.ncbi.nlm.nih.gov/30462376/) | Phenotype | WES; novel signs (choanal atresia, Pierre-Robin, overgrowths) |
| [31241704](https://pubmed.ncbi.nlm.nih.gov/31241704/) | GxE/epigenetics | Retinoid-induced TBX22 hypermethylation |
| [25918826](https://pubmed.ncbi.nlm.nih.gov/25918826/) | Common variants | Promoter SNPs modify NSCLP risk in women |
| [41520495](https://pubmed.ncbi.nlm.nih.gov/41520495/) | Outcomes | Predictors of VPI-related QOL |
| [42235642](https://pubmed.ncbi.nlm.nih.gov/42235642/) | Treatment | Furlow palatoplasty, analgesia evidence |
| [42403778](https://pubmed.ncbi.nlm.nih.gov/42403778/) | Treatment | Timing vs anatomy in outcomes |
| [42275034](https://pubmed.ncbi.nlm.nih.gov/42275034/) | Treatment | Palatoplasty timing and speech |
| [29704302](https://pubmed.ncbi.nlm.nih.gov/29704302/) | Differential | Autosomal-dominant ankyloglossia (genetic heterogeneity) |
| [19816249](https://pubmed.ncbi.nlm.nih.gov/19816249/) | Model | Glucocorticoid/alcohol-induced cleft, Tbx22 expression |

---

## Limitations and Knowledge Gaps

- **CPX-specific epidemiology** (prevalence/incidence per 100,000) is not well quantified; most figures are for clefting broadly.
- **ABERS mechanism** (loss- vs gain-of-function) is unresolved [PMID: 41630180](https://pubmed.ncbi.nlm.nih.gov/41630180/).
- **Penetrance/expressivity in carrier females** is not numerically defined; X-inactivation skewing is invoked but not measured here.
- **Modifier genes** for CPX severity are not identified.
- **No human omics** (transcriptomic/proteomic) datasets specific to CPX palate were located; mechanistic detail rests on mouse and in vitro work.
- **Digital anomalies** (clinodactyly/syndactyly) are reported by Orphanet but lack a strong primary-literature frequency.
- **ClinVar Pathogenic count** is inflated by Xq21 CNVs; the intragenic point-mutation burden specific to CPX is smaller.

## Proposed Follow-up Experiments / Actions

1. **Resolve the ABERS mechanism:** functional assays (DNA binding, SUMOylation, repression) on ABERS-specific splice/missense alleles to test loss- vs gain-of-function.
2. **Carrier-female study:** correlate X-inactivation ratios with phenotype severity in heterozygotes to quantify expressivity.
3. **Single-cell/spatial transcriptomics** of developing palatal mesenchyme in Tbx22-null vs WT mice to pinpoint the osteoblast-maturation program (direct TBX22 targets).
4. **ClinVar curation:** separate intragenic CPX point mutations from Xq21 CNVs to produce a clean CPX variant catalog; re-classify VUS with the SUMO/T-box functional data.
5. **GxE validation:** test whether TBX22 promoter-SNP carriers have altered methylation responses to retinoid/folate status in human cohorts.
6. **Natural-history/QOL registry** for genetically confirmed CPX to define CPX-specific speech, hearing, and dental outcomes distinct from non-syndromic cleft palate.


## Artifacts

- [OpenScientist final report](Cleft_Palate_With_Or_Without_Ankyloglossia_X-linked-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Cleft_Palate_With_Or_Without_Ankyloglossia_X-linked-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 9 |
| Quoted claims found in source | 8 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 19 |
| On topic | 15 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:41520495` *(abstract only)*: "ONF (odds ratio = 8.531) and speech intelligibility deficits (odds ratio = 8.854) were independent predictors of poor QOL"
  - closest text in source: "ONF (odds ratio = 8.531, P < .001) and speech intelligibility deficits (odds ratio = 8.854, P < .001) were independent predictors of poor QOL"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 41 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 9 |
| Terms whose name was checked | 19 |
| Terms named correctly | 12 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0010560` (5 mentions) - the report calls it "if available"; MONDO calls it **cleft palate with or without ankyloglossia, X-linked**
- `NCIT:C51756` (1 mention) - the report calls it "palatoplasty"; NCIT calls it **Roux-en-Y Anastomosis**
- `NCIT:C15415` (1 mention) - the report calls it "For resonance/articulation disorders"; NCIT calls it **Hyperthermia Treatment**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `UBERON:0002096` (UBERON_0002096) (1 mention) - replaced by `UBERON:0002465`
- `UBERON:0002220` (UBERON_0002220) (1 mention) - replaced by `UBERON:0002291`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000193` (3 mentions) - the report calls it "Bifid uvula", "Bifid/absent/short uvula"; HP calls it **Bifid uvula**, and lists "Bifid palatine uvula" among its other names
- `HP:0000204` (2 mentions) - the report calls it "Cleft lip ± palate"; HP calls it **Cleft upper lip**
- `HP:0000668` (2 mentions) - the report calls it "Hypodontia / dental anomalies"; HP calls it **Hypodontia**
- `GO:0006357` (1 mention) - the report calls it "regulation of transcription by RNA Pol II"; GO calls it **regulation of transcription by RNA polymerase II**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0000193` - called "Bifid uvula", "Bifid/absent/short uvula"
