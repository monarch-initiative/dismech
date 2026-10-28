---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-28T01:27:32.127430'
end_time: '2026-10-28T01:32:48.942040'
duration_seconds: 316.81
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: MAK-related Retinopathy
  mondo_id: MONDO:0700229
  category: Mendelian
  causal_genes: MAK
  omim_id: not recorded
  synonyms: retinitis pigmentosa 62; RP62; MAK retinitis pigmentosa
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
  web_search_requests: 3
  num_turns: 24
  total_cost_usd: 2.463612799999999
  session_id: 0bfb328d-96db-5dca-803a-342a247b0264
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 11
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MAK-related Retinopathy
- **MONDO ID:** MONDO:0700229 (if available)
- **Causal gene(s):** MAK
- **OMIM:** not recorded
- **Synonyms:** retinitis pigmentosa 62; RP62; MAK retinitis pigmentosa
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **MAK-related Retinopathy** covering all of the
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

Let me write a small script instead.

Progress: core clinical and genetic papers are pulled with verified quotes. Now I'm getting the mechanism, animal-model and gene-therapy papers.

Status: research is done (verified abstracts for about 20 PMIDs, plus the MONDO and GenCC records). Writing the report now.

# MAK-related Retinopathy (MONDO:0700229): research report

**Causal gene: *MAK*** (male germ cell-associated kinase; HGNC:6816; chromosome 6p24). MAK-related retinopathy is a non-syndromic, autosomal recessive rod-cone degeneration, which is to say retinitis pigmentosa (RP). It is caused by biallelic loss-of-function variants in *MAK*. The most common variant by far is a founder 353-bp Alu insertion in exon 9, which is enriched in people of Ashkenazi Jewish ancestry.

**How the evidence was gathered.**
- I retrieved the abstract text for every quoted PMID from NCBI E-utilities during this session. Each quote is short and verbatim, but quotes still need confirming against `references_cache/` with `just fetch-reference`.
- I checked the MONDO and GenCC/ClinGen records directly.
- The ontology CURIEs in the term tables come from memory. They are leads only, and each must be looked up before it is bound.

---

## 1. Disease information

**Overview.** MONDO defines MONDO:0700229 as "Any retinopathy caused by variants in the MAK gene." It is a spectrum term, created in January 2024 on the ClinGen Ocular Clinical Domain Working Group's request (mondo issue #6562), and it currently has one child:

- **MONDO:0013611 "retinitis pigmentosa 62"** is defined as "Any retinitis pigmentosa in which the cause of the disease is a mutation in the MAK gene." Its synonyms are RP62, retinitis pigmentosa type 62, and MAK retinitis pigmentosa. Its cross-references are OMIM:614181, UMLS:C3280042, MedGen:481672, DOID:0110380 and GARD:0015767.
- The MONDO record notes that the parent may later be merged with its single child if no other clinical subtype appears.

**Identifiers**

| System | ID |
|---|---|
| MONDO (spectrum) | MONDO:0700229 (GARD:0026379) |
| MONDO (RP62) | MONDO:0013611 |
| OMIM (phenotype) | 614181 (RP62) |
| OMIM (gene) | 154235. *This is from memory; verify it.* |
| HGNC | HGNC:6816 (`hgnc:6816` in dismech) |
| Orphanet | No MAK-specific entry. The covering class is ORPHA:791, retinitis pigmentosa. |
| ICD-10 / ICD-11 | H35.52 (hereditary retinal dystrophy) / 9B70 (RP), both generic |
| MeSH | D012174 Retinitis Pigmentosa (generic) |

**Gene-disease validity.** ClinGen's Retina GCEP rated the pair **Definitive, autosomal recessive**. It evaluated the pair on 2023-03-02 and submitted it to GenCC on 2026-02-19.
- Its summary says: "In summary, MAK is definitively associated with autosomal recessive MAK-related retinopathy."
- It also says: "MAK-related retinopathy appears to cause non-syndromic retinal disease."
- The mechanism ClinGen records is loss of function.

**Data provenance.** All of the information comes from aggregated published case series and cohorts (about 11 to 24 patients each). None comes from EHR data. There is no GeneReviews chapter specific to MAK. The general "Nonsyndromic Retinitis Pigmentosa Overview" (Fahim et al., PMID:20301590, NBK1417) covers it.

## 2. Etiology

- **Cause.** Biallelic germline loss-of-function variants in *MAK*.
- **Major allele.** The exon 9 Alu insertion. All 21 homozygous probands in the discovery series were Jewish (PMID:21825139).
  - It is reported as c.1297_1298ins353 and as p.K429insAlu (PMID:26894652). Confirm the HGVS name in ClinVar.
- **Other alleles.**
  - A nonsense variant in a consanguineous Turkish family, plus missense variants in five more probands (PMID:21835304).
  - Two novel null variants in a non-Jewish patient: c.1195_1196delAC p.(Thr399fs), and a splice-acceptor variant upstream of exon 4 (PMID:29781741).
  - The missense c.46G>A p.(Gly16Arg), found compound heterozygous with the Alu allele (PMID:26558903).
- **Risk factors.** The main risk factor is Ashkenazi Jewish ancestry, through a founder effect (see §9). Consanguinity matters for the non-founder alleles. No environmental risk factors are known.
- **Protective factors and gene-environment interactions.** None reported.
- **Modifier genes.** None established. Light exposure has not been studied for this disease.

## 3. Phenotypes

These are the features with the strongest evidence. Every HPO ID in the table is from memory and needs verification.

| Phenotype | Suggested HPO (verify) | Onset / course / frequency | Evidence |
|---|---|---|---|
| Night blindness (first symptom) | Nyctalopia HP:0000662 | Present in all patients. Onset ranges from childhood to age 43 (mean 23). | "All patients experienced typical RP symptoms of night blindness followed by visual field constriction." and "Symptoms initiated between childhood and the age of 43 (mean: 23 years)." (PMID:25385675) |
| Visual field constriction, with early superior-temporal loss | Constriction of peripheral visual field HP:0001133 | Progressive | "Kinetic fields showed early loss in the superior-temporal quadrant." (PMID:22110072) |
| Rod-cone dysfunction on ERG | Rod-cone dystrophy HP:0000510 | All patients | "all patients had rod>cone dysfunction" (PMID:22110072) |
| Central acuity largely preserved; disease relatively mild | — (a course modifier, not a separate phenotype) | Slow course | "Visual acuities could be normal into the eighth decade of life." (PMID:22110072); "MAK-associated RP appears to be relatively mild" (PMID:25385675); median BCVA 20/25 (PMID:40578471) |
| Cystoid macular edema / intraretinal cystoid spaces | Cystoid macular edema HP:0040049 | About 33% | "33% of patients developed cystoid macular edema." (PMID:40578471); "Optical coherence tomography showed cystoid changes in each fovea." (PMID:26894652) |
| Thinning of the outer retina on SD-OCT, with progressive ellipsoid zone (EZ) loss | Abnormal retinal morphology on OCT (find a specific HP term) | The EZ narrows by about 210 µm per year | "SD-OCT demonstrated thinning of the overall retina, outer nuclear layer" (PMID:25385675) |
| Midperipheral pigmentary retinopathy | Bone spicule pigmentation HP:0007737; Attenuation of retinal blood vessels HP:0007843 | Typical of RP | Classic RP signs (PMID:22110072) |
| Parafoveal capillary rarefaction and increased cone spacing in advanced disease | — | Late | "central foveal structure is maintained until late stages of disease" (PMID:29103961) |

**Not present.** "MAK-associated RP is not associated with syndromic features" (PMID:25385675). There is no hearing, renal, or other ciliopathy involvement.

**Quality of life.** No instrument-based data (e.g., NEI-VFQ-25) were found for this disease. The main impacts come from night blindness and loss of peripheral field, which affect mobility and driving. Reading vision is usually preserved until late.

## 4. Genetic and molecular information

- **Gene.** *MAK* encodes a CMGC-family Ser/Thr kinase related to ICK and MOK (the RCK kinases).
  - The retina expresses its own isoform, which includes exons 9 and 12.
  - The developmental switch to that isoform fails in patient iPSCs: "the developmental switch to the MAK transcript bearing exons 9 and 12 did not occur" (PMID:21825139).
- **Variant classes.** Mobile-element (Alu) insertion, nonsense, frameshift, splice-site, and kinase-domain missense variants.
  - In the kinase-domain missense variants, "an in vitro kinase assay indicates that these mutations result in a loss of kinase activity." (PMID:21835304)
- **Functional consequence.** Loss of function. The Alu allele "results in a loss of normal MAK transcript" (PMID:34518651).
- **Origin.** Germline. There is no somatic or mosaic involvement.
- **Population frequency.** The Ashkenazi carrier frequency is about 1 in 55 (1,207 controls; PMID:22110072).
- **Detection caveat.** The Alu insertion "is missed by standard NGS-based variant callers". A targeted in-silico read search detected it with "100% sensitivity and specificity" and solved two previously unsolved pedigrees (PMID:26558903).
- **Not reported.** Modifier genes, epigenetic changes, and chromosomal abnormalities.
- **ClinVar.** The classification of individual variants should be pulled from ClinVar. It was not retrieved here.

## 5. Environmental information

None known. There are no infectious agents and no established lifestyle factors.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Biallelic *MAK* loss-of-function variants** (the Alu insertion, null variants, or kinase-dead missense variants) **lead to** loss of the retinal MAK transcript or of kinase activity.
   - Demonstrated in patient iPSCs (PMID:21825139) and in in-vitro kinase assays (PMID:21835304).
2. **Loss of MAK kinase activity at the photoreceptor ciliary tip and axoneme leads to** failure to phosphorylate its substrates and to regulate intraflagellar transport (IFT).
   - In mouse, "Mak was localized both in the connecting cilia and outer-segment axonemes of photoreceptor cells."
   - MAK phosphorylates the N-terminal region of RP1 (PMID:21148103).
   - "the ciliopathy kinase Mak is a ciliary tip-localized IFT regulator" (PMID:39293864).
   - The upstream activator is CCRK: "Ccrk kinase is an upstream activator of Mak and Ick in retinal photoreceptor cells." (PMID:39293864)
   - In *C. elegans*, the ortholog DYF-5 phosphorylates the tubulin-binding module of IFT-74, promoting tubulin unloading (PMID:35969738). This is invertebrate evidence, inferred to apply in humans.
3. **Disrupted IFT and microtubule regulation lead to** abnormal axoneme length and structure. Here the species differ:
   - **Mouse:** "photoreceptors exhibit elongated cilia and progressive degeneration", with "accumulation of intraflagellar transport 88 (IFT88) and IFT57" (PMID:21148103).
   - **Zebrafish:** "mak mutants failed to generate axonemes", unlike the mouse (PMID:38813692).
   - **Human:** "At the stages studied, there was no evidence of photoreceptor ciliary elongation." (PMID:22110072) Whether human cilia lengthen is therefore unresolved. This is a candidate `HUMAN_MODEL_MISMATCH` discussion.
4. **Ciliary transport failure leads to** mislocalization of outer-segment cargo.
   - "abnormal rhodopsin accumulation in the Mak-null photoreceptor cell bodies at postnatal day 14" (PMID:21148103).
   - In zebrafish, both rods and cones "completely lacked outer segments" (PMID:38813692).
5. **Outer-segment dysfunction and protein mislocalization lead to** photoreceptor apoptosis, starting with rods ("underwent apoptosis", PMID:38813692), followed by secondary cone loss.
6. **Rod loss leads to** nyctalopia and peripheral field constriction. Later cone loss leads to EZ narrowing and outer nuclear layer (ONL) thinning. CME is a parallel downstream feature whose mechanism is not established.

**Branch: partial redundancy with ICK.** "Simultaneous disruption of Mak and Ick resulted in loss of photoreceptor ciliary axonemes" (PMID:39293864). In mouse, ICK partly compensates for loss of MAK. This compensation is a plausible reason the human disease is mild, but that is my inference.

### Suggested terms (all from memory; verify every one)

- **GO biological process:**
  - photoreceptor cell maintenance (GO:0045494)
  - intraciliary transport (GO:0042073)
  - regulation of cilium assembly (GO:1902017)
  - protein phosphorylation (GO:0006468)
  - apoptotic process (GO:0006915)
- **GO molecular function:** protein serine/threonine kinase activity (GO:0004674)
- **GO cellular component:**
  - photoreceptor connecting cilium (GO:0032391)
  - ciliary tip (GO:0097542)
  - axoneme (GO:0005930)
  - photoreceptor outer segment (GO:0001750)
- **CL:** retinal rod cell (CL:0000604) and retinal cone cell (CL:0000573)

**Molecular profiling.** No disease-specific omics datasets were found. A regional human retina RNA-seq study exists (Whitmore, PMID:25446321), but it is not disease-specific.

## 7. Anatomical structures affected

- **Organ and tissue.** The retina only (UBERON:0000966, verify), and specifically the photoreceptor layer and outer nuclear layer. Involvement is bilateral and symmetric.
- **Regions.** Damage starts in the midperiphery and the superior-temporal field, and the fovea is spared until late (PMID:22110072, PMID:29103961).
- **Subcellular.** The connecting cilium, the outer-segment axoneme and the ciliary tip.
- **Other organs.** None. MAK is also expressed in testis, but no male infertility phenotype has been reported in patients.

## 8. Temporal development

- **Onset.** Insidious, from childhood to the fifth decade (mean about 23 years; PMID:25385675). In one non-founder patient, onset was in the fourth decade (PMID:29781741).
- **Progression.** Slow and lifelong.
  - The EZ horizontal width declines by "209.78 µm/year (95% CI: 181.37-238.18, P < .001)".
  - Foveal ONL thickness declines by 1.24 µm/year.
  - In the same cohort, 83% retained attenuated photopic ERGs and 55% retained rod responses (PMID:40578471, 18 patients aged 20 to 83).
- **Outcome measure.** Because central vision stays stable, the authors propose EZ width as the trial outcome measure.
- **Comparison with DHDDS-RP.** MAK patients had better acuity and fields at older ages than DHDDS patients, whose "cone responses became nondetectable at a much younger age than MAK patients." (PMID:29276052)
- **Remission.** None.

## 9. Inheritance and population

- **Inheritance.** Autosomal recessive (HP:0000007), with full penetrance in biallelic individuals. Expressivity is variable, mainly in age at onset.
- **Founder effect.** "Haplotype analyses revealed that inheritance of the MAK mutation was attributable to a founder effect." (PMID:25255364)

**Frequency among RP patients**

| Population | Finding | Source |
|---|---|---|
| Unrelated RP patients overall | 1.2% (21 of 1,799 probands) | PMID:21825139 |
| North American recessive or isolated RP | 2.1% overall; 25.7% of cases with Jewish ancestry | PMID:25255364 |
| Ashkenazi Jewish families in Israel | The leading cause: 39% of genetically solved families (230 families studied) | PMID:29276052 |

- Stone et al. called MAK-RP the most common heritable retinal disease among Ashkenazi Jews (PMID:22110072).
- **Population prevalence.** No published figure. A rough estimate from the carrier frequency is about (1/55)² / 4 ≈ 1 in 12,000 Ashkenazi births. That is my calculation, not a sourced figure, so do not record it as one.
- **Sex ratio.** About equal, as expected for autosomal recessive inheritance (7 of 18 were female in PMID:40578471).

## 10. Diagnostics

- **Clinical tests.**
  - Full-field ERG, showing rod>cone dysfunction.
  - Kinetic or static perimetry.
  - SD-OCT, for EZ width, ONL thickness and CME.
  - Fundus autofluorescence (FAF), including ultra-widefield. In 11 MAK patients, macular FAF patterns differed from those in DHDDS patients (PMID:35501492).
  - Adaptive optics, which in early disease shows normal cone spacing (PMID:29103961).
- **Genetic testing.**
  - Use a retinal dystrophy gene panel, exome or genome sequencing, **but ask specifically for Alu/mobile-element insertion detection**. Standard callers miss the founder allele (PMID:26558903).
  - Alternatively, run a targeted Alu PCR assay first in Ashkenazi patients.
  - CMA, karyotype, FISH, mitochondrial and repeat-expansion testing do not apply.
- **No biochemical biomarkers** exist.
- **Differential diagnosis.**
  - DHDDS-RP (also Ashkenazi): cones fail earlier.
  - FAM161A-RP.
  - Other forms of recessive RP.
  - Syndromic ciliopathies (Usher, Bardet-Biedl), which can be excluded by the absence of extraocular features.
- **Screening.** Ashkenazi carrier-screening panels can include the MAK Alu allele. There is no newborn screening.

## 11. Outcome and prognosis

- Lifespan is normal, and the disease causes no deaths.
- The disease is relatively favorable for RP: "patients with MAK-RP maintain functional central vision and have a favorable prognosis" (PMID:40578471).
- The main complication is CME, in about a third of patients.
- Prognostic factors: genotype (MAK versus DHDDS), and probably null versus missense variants, although that has not been established.
- No quality-of-life instrument data exist.

## 12. Treatment

- **No approved disease-specific therapy.** No MAK trials appear on ClinicalTrials.gov (search run 2026-10-28).
- **Supportive care.**
  - Low-vision rehabilitation (NCIT:C15315 Rehabilitation; verify).
  - CME management, e.g., carbonic anhydrase inhibitors. These are used empirically in RP, with no MAK-specific data.
  - Genetic counseling (NCIT:C15240).
- **Preclinical gene augmentation (Iowa).**
  - A clinical-grade vector restored "the cells ability to regulate primary cilia length" in patient iPSC-derived cells.
  - In zebrafish, "the visual defect in mak knockdown zebrafish was mitigated".
  - Subretinal delivery showed "no evidence of local or systemic toxicity at 1-month or 3-months" (PMID:34518651).
  - Suggested NCIT term: Gene Therapy, NCIT:C15238. Suggested modality: `GENE_THERAPY`.
- **CRISPR correction.** Homology-directed repair excising the Alu insertion "demonstrated restoration of the retinal transcript and protein in patient cells" (PMID:28619647). This supports autologous cell or gene-editing approaches.
- **Kinase-pathway approach (mouse).** "Gene delivery of Ick and pharmacological inhibition of FGF receptors" suppressed ciliopathy phenotypes, which suggests "activation of Ick as a potential therapeutic approach for retinitis pigmentosa caused by MAK mutations" (PMID:39293864; see also the review PMID:40636449).

## 13. Prevention

- **Primary prevention.** Ashkenazi carrier screening, cascade testing of relatives, and preimplantation or prenatal testing for couples who both carry the allele.
- **Secondary prevention.** Early genotyping that includes Alu detection.
- **Tertiary prevention.** Monitoring for CME with OCT, and low-vision support.
- **Not applicable.** Vaccination and public-health measures.

## 14. Other species and natural disease

- No naturally occurring animal disease is recorded. I did not formally search OMIA.
- **Conserved orthologs:**
  - mouse *Mak*
  - zebrafish *mak*
  - *C. elegans* DYF-5 (with the CCRK ortholog DYF-18, which acts in the same pathway on kinesin-2 handover; PMID:29655266)
  - *Chlamydomonas* CrMAK, whose "Loss of CrMAK or its kinase activity leads to aciliated cells" (PMID:41231942)
- The ortholog NCBI Gene and MGI/ZFIN IDs were not retrieved and must be looked up.

## 15. Model organisms

| Model | Phenotype | How well it matches human disease | Source |
|---|---|---|---|
| *Mak*⁻/⁻ mouse | Elongated photoreceptor cilia, IFT88/IFT57 accumulation, rhodopsin mislocalization, progressive degeneration | Partial. The degeneration matches, but the cilia elongation has not been seen in humans. | PMID:21148103 |
| *Mak*/*Ick* double KO and *Ccrk* mice | Loss of axonemes; the Ccrk-Mak/Ick axis is essential for photoreceptor survival | Mechanistic model, not a recapitulation of the disease | PMID:39293864 |
| Zebrafish *mak* mutant | Rapid embryonic degeneration; rods and cones lack outer segments; no axoneme | More severe and earlier than human disease; the axoneme defect is opposite to the mouse | PMID:38813692 |
| Zebrafish *mak* knockdown | Visual defect rescued by the MAK vector | Used to test gene therapy | PMID:34518651 |
| Patient iPSC-derived photoreceptor precursors (Alu homozygous) | Failure of the retinal-isoform splicing switch; cilia-length defect rescued by gene transfer or CRISPR | High for molecular steps; lacks outer segments | PMID:21825139, 28619647, 34518651 |
| *C. elegans* *dyf-5*, *Chlamydomonas* *Crmak* | Long or branched cilia, or no cilia; tubulin-unloading and IFT mechanisms | Basic mechanism only | PMID:35969738, 30955935, 41231942 |

**For the knowledge-base entry.** The differing cilia phenotypes in mouse, zebrafish and humans should go into a `HUMAN_MODEL_MISMATCH` discussion. A model link is `FAILS_TO_RECAPITULATE` against the ciliary-elongation claim for humans (PMID:22110072).

---

### Citation corrections and cautions

- **PMID:29781741 is Gray et al. 2018** (*Ophthalmic Genetics*). A search snippet attributed it to Kimchi et al.; the Kimchi *Ophthalmology* paper is **PMID:29276052**.
- **The 2013 eLife iPSC paper** (Tucker, PMID:23991284) is about *USH2A*, not MAK. Do not cite it for this disease.
- **Two PMIDs on ClinGen's list have no MAK content in their abstracts:** 33542393 and 33921607. Any MAK data in them would be in the full text only.

### Sources

- PubMed/E-utilities: [esearch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=MAK) and the abstracts of PMIDs 21825139, 21835304, 21148103, 22110072, 25385675, 25255364, 29276052, 40578471, 29781741, 29103961, 26894652, 26558903, 35501492, 39293864, 38813692, 40636449, 35253837, 34518651, 28619647, 29655266, 35969738 and 41231942
- [MONDO:0700229 (OLS)](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0700229) and [MONDO:0013611 (OLS)](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0013611)
- [GenCC/ClinGen submission](https://thegencc.org/submissions/GENCC_000102-HGNC_6816-MONDO_0700229-HP_0000007-GENCC_100001)
- [ClinicalTrials.gov API query](https://clinicaltrials.gov/api/v2/studies?query.term=MAK+retinitis+pigmentosa)
- [Iowa Institute for Vision Research note on MAK](https://ivr.uiowa.edu/node/43), [Kimchi 2018 (HUJI CRIS)](https://cris.huji.ac.il/en/publications/nonsyndromic-retinitis-pigmentosa-in-the-ashkenazi-jewish-populat/), [Kong 2025 (Mount Sinai)](https://scholars.mssm.edu/en/publications/ellipsoid-zone-loss-as-an-outcome-measure-in-mak-associated-retin/), [PMC3341124](https://pmc.ncbi.nlm.nih.gov/articles/PMC3341124), [eLife 00824](https://elifesciences.org/articles/00824), [PubMed 23991284](https://pubmed.ncbi.nlm.nih.gov/23991284/)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 29 |
| Quoted claims found in source | 28 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 25 |
| On topic | 20 |
| Off topic | 2 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:40636449` *(abstract only)*: "activation of Ick as a potential therapeutic approach for retinitis pigmentosa caused by MAK mutations"
  - closest text in source: "Here, we review the current understanding of the roles of these kinases during the IFT process, as well as their regulatory mechanisms, physiological and pathophysiological significance, and potential to treat ciliopathies and age-related obesity."

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:20301590` (1 mention) - Nonsyndromic Retinitis Pigmentosa Overview.
  - shared terms: genetic
- `PMID:29655266` (1 mention) - The kinases male germ cell-associated kinase and cell cycle-related kinase regulate kinesin-2 motility in Caenorhabditis elegans neuronal cilia.
  - shared terms: kinase, genetic

Weighed against this report's own most characteristic terms: `mak`, `patient`, `disease`, `gene`, `alu`, `retinal`, `loss`, `variant`, `cone`, `ashkenazi`, `insertion`, `kinase`, `outer`, `phenotype`, `mechanism`, `retina`, `photoreceptor`, `mondo`, `cme`, `genetic`.
