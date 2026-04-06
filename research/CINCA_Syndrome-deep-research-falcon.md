---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-09T11:45:22.412402'
end_time: '2026-02-09T11:48:52.520150'
duration_seconds: 210.11
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: CINCA Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 18
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** CINCA Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **CINCA Syndrome**.
Focus on the molecular and cellular mechanisms underlying disease progression.

### Required Information

#### 1. Core Pathophysiology
- What are the primary pathophysiological mechanisms?
- What molecular pathways are dysregulated?
- What cellular processes are affected?

#### 2. Key Molecular Players
- **Genes/Proteins**: Which genes are causally involved or implicated?
- **Chemical Entities**: What metabolites, drugs, or small molecules are relevant?
- **Cell Types**: Which cell types are primarily affected?
- **Anatomical Locations**: Which tissues/organs are involved?

#### 3. Biological Processes (for GO annotation)
- What biological processes (GO terms) are disrupted?
- Consider: signaling pathways, metabolic processes, cellular responses, transport, etc.

#### 4. Cellular Components
- Where in the cell do key processes occur?
- Consider: organelles, membrane compartments, extracellular space, etc.

#### 5. Disease Progression
- What is the sequence of events from initial trigger to clinical manifestation?
- Are there distinct stages or phases?

#### 6. Phenotypic Manifestations
- What are the key clinical phenotypes?
- How do they relate to the underlying mechanisms?

### Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Prioritize recent reviews and landmark papers
- Include direct quotes where possible to support key statements

### Output Format

Structure your response as a narrative that could be used to populate a disease knowledge base entry with:
- Pathophysiology description
- Gene/protein annotations with ontology terms (HGNC, GO)
- Phenotype associations (HP terms)
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Evidence items with PMIDs


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

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** CINCA Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **CINCA Syndrome**.
Focus on the molecular and cellular mechanisms underlying disease progression.

### Required Information

#### 1. Core Pathophysiology
- What are the primary pathophysiological mechanisms?
- What molecular pathways are dysregulated?
- What cellular processes are affected?

#### 2. Key Molecular Players
- **Genes/Proteins**: Which genes are causally involved or implicated?
- **Chemical Entities**: What metabolites, drugs, or small molecules are relevant?
- **Cell Types**: Which cell types are primarily affected?
- **Anatomical Locations**: Which tissues/organs are involved?

#### 3. Biological Processes (for GO annotation)
- What biological processes (GO terms) are disrupted?
- Consider: signaling pathways, metabolic processes, cellular responses, transport, etc.

#### 4. Cellular Components
- Where in the cell do key processes occur?
- Consider: organelles, membrane compartments, extracellular space, etc.

#### 5. Disease Progression
- What is the sequence of events from initial trigger to clinical manifestation?
- Are there distinct stages or phases?

#### 6. Phenotypic Manifestations
- What are the key clinical phenotypes?
- How do they relate to the underlying mechanisms?

### Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Prioritize recent reviews and landmark papers
- Include direct quotes where possible to support key statements

### Output Format

Structure your response as a narrative that could be used to populate a disease knowledge base entry with:
- Pathophysiology description
- Gene/protein annotations with ontology terms (HGNC, GO)
- Phenotype associations (HP terms)
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Evidence items with PMIDs


Plan
- Define disease entity and nomenclature; identify authoritative recent sources.
- Synthesize core molecular and cellular pathophysiology (NLRP3 inflammasome → ASC specks → caspase-1 → IL-1β/IL-18; pyroptosis; regulatory nodes such as NEK7, ubiquitin, autophagy) and map dysregulated pathways. (booshehri2019capsandnlrp3 pages 6-8, putnam2024thediscoveryof pages 8-9)
- Detail key molecular players, cell types, tissues, and their roles in CINCA/NOMID, including somatic mosaicism. (booshehri2019capsandnlrp3 pages 3-4, bonet2024clinicalfeaturesoutcomes pages 13-16, bonet2024clinicalfeaturesoutcomes pages 11-13)
- Summarize disease progression and phenotype correlations; extract recent statistics from 2023–2024 cohorts where available. (shu2023thegeneticand pages 1-2, bonet2024clinicalfeaturesoutcomes pages 11-13)
- Compile current therapeutic mechanisms and real-world outcomes for IL-1 blockade; note emerging NLRP3 inhibitors. (booshehri2019capsandnlrp3 pages 6-8, bonet2024clinicalfeaturesoutcomes pages 13-16, shu2023thegeneticand pages 1-2)
- Provide structured ontology-style annotations (HGNC, GO, CL, UBERON; CHEBI where applicable) with evidence notes.

Disease overview and nomenclature
CINCA syndrome (Chronic Infantile Neurologic, Cutaneous, and Articular), also called Neonatal-Onset Multisystem Inflammatory Disease (NOMID), represents the most severe end of the cryopyrin-associated periodic syndromes (CAPS) caused by autosomal-dominant, gain-of-function variants in NLRP3 (also known as CIAS1). CAPS spans familial cold autoinflammatory syndrome (FCAS), Muckle–Wells syndrome (MWS), and CINCA/NOMID, with shared molecular pathogenesis centered on the NLRP3 inflammasome and excessive IL‑1 signaling. Recent authoritative reviews and cohort studies reaffirm these definitions and the CAPS continuum. URL examples: Immunological Reviews (Dec 2024): https://doi.org/10.1111/imr.13292; Journal of Clinical Immunology (2019): https://doi.org/10.1007/s10875-019-00638-z; Frontiers in Immunology (Sep 2023): https://doi.org/10.3389/fimmu.2023.1267933. (putnam2024thediscoveryof pages 8-9, booshehri2019capsandnlrp3 pages 3-4, shu2023thegeneticand pages 1-2)

Pathophysiology description (molecular and cellular)
- Core mechanism: NLRP3 gain-of-function lowers the activation threshold and enables constitutive assembly of the NLRP3 inflammasome. Upon priming and diverse triggers, mutant NLRP3 nucleates ASC (PYCARD) into a cytosolic “speck,” recruiting and activating caspase‑1, which cleaves pro‑IL‑1β and pro‑IL‑18 and executes gasdermin‑D–dependent pyroptosis. CAPS models and human cell studies demonstrate enhanced ASC speck formation, caspase‑1 activation, and IL‑1β release; disease phenotypes are myeloid‑cell driven and depend on ASC and caspase‑1, with contributions from IL‑18 and pyroptosis. (booshehri2019capsandnlrp3 pages 6-8)
- Regulatory nodes: ASC speck formation is modulated by ubiquitination (linear and K63-linked) and by NEK7-dependent transport to the microtubule organizing center (MTOC), which interfaces with autophagic degradation; alternative splicing of NLRP3 (e.g., Δexon5) disrupts NEK7 binding, impeding ASC specking and IL‑1β release. These layers explain how GOF variants tilt the balance toward persistent inflammasome activation in severe CAPS (CINCA/NOMID). URL: Immunological Reviews 2024 (Dec 2024), https://doi.org/10.1111/imr.13292. (putnam2024thediscoveryof pages 8-9)
- Dysregulated pathways: IL‑1–mediated signaling is dominant, but murine and in vitro data indicate partial roles for IL‑18 and downstream inflammatory mediators; oxidative stress and aberrant phosphorylation states can further potentiate cryopyrin activation. (booshehri2019capsandnlrp3 pages 6-8)

Cells, tissues, and anatomical involvement
- Principal cell types: myeloid lineage cells (monocytes/macrophages, neutrophils) are the main source of inflammasome activity in CAPS; mosaic-variant distribution studies show a substantial fraction of patients with myeloid-restricted VAF, underscoring their central role. (bonet2024clinicalfeaturesoutcomes pages 13-16)
- Tissue targets: skin (neutrophilic urticarial dermatosis), bone and cartilage (overgrowth and dysplasia, calcified physeal lesions), central nervous system/meninges (chronic sterile meningitis with elevated CSF pressure and leukocytosis), inner ear/cochlea (progressive sensorineural hearing loss), and eyes (uveitis, papilledema, optic atrophy). These manifestations map to local innate immune activation by mutant NLRP3-expressing myeloid cells and resident cells (e.g., chondrocytes, microglia). (booshehri2019capsandnlrp3 pages 3-4, arık2025autoinflammatorydiseasemolecular pages 3-4)

Somatic mosaicism and its implications
- Frequency and patterns: Many clinically definite CAPS—especially severe phenotypes—previously testing negative for germline variants are explained by post‑zygotic (somatic) NLRP3 variants with low variant allele fractions (VAFs). In the largest mosaic CAPS cohort to date, mosaic patients harbored heterogeneous NLRP3 missense variants (exon 4 hot spots); mean VAF was ~11.3% (range 1.3–34.8%). Mosaicism was detected across leukocyte compartments with two predominant patterns: 64.3% had both myeloid and lymphoid involvement, while 35.7% were myeloid‑restricted; VAFs were longitudinally stable in ~54%, increased in ~23%, and decreased in ~23% over >12 months. (bonet2024clinicalfeaturesoutcomes pages 11-13, bonet2024clinicalfeaturesoutcomes pages 13-16)
- Functional parity: Post‑zygotic variants generally conferred inflammasome activation comparable to germline GOF alleles; ASC‑speck assays showed robust activation that was suppressible by the NLRP3 inhibitor MCC950 in most variants (partial resistance noted for p.D303H). Clinically, mosaic and germline patients responded similarly to IL‑1 blockade. (bonet2024clinicalfeaturesoutcomes pages 13-16)

Disease progression and phenotype correlations
- Sequence: CINCA/NOMID typically begins at birth or in the neonatal period with persistent urticarial rash and fever, followed by chronic aseptic meningitis/raised intracranial pressure, progressive sensorineural hearing loss, ocular inflammation with risk of optic atrophy, and abnormal bone/cartilage growth leading to arthropathy. Without timely IL‑1 blockade, cumulative tissue damage accrues in CNS, ear, and eye. (arık2025autoinflammatorydiseasemolecular pages 3-4, booshehri2019capsandnlrp3 pages 3-4)
- Quantitative features from recent cohorts: A 2023 multi-patient pediatric CAPS cohort reported high neurologic burden consistent with severe phenotypes, including meningitis (75%) and ventriculomegaly (83.3%) in a subset with detailed neuroimaging/CSF data; canakinumab-treated children (n=10) experienced improvements across musculoskeletal, neurologic, auditory, and visual domains over 10–20 months. URL: Frontiers in Immunology (Sep 2023): https://doi.org/10.3389/fimmu.2023.1267933. (shu2023thegeneticand pages 1-2)
- Systemic inflammatory profile: In mosaic CAPS, common clinical features included urticarial rash (100%), arthralgia (87%), fever (75%), arthritis (68%), and headache (56%), with anemia, neutrophilia, leukocytosis, and thrombocytosis; CRP/ESR were markedly elevated, and long diagnostic delays were observed (mean disease duration ~27 years in the studied adult-biased cohort). URL: medRxiv (Dec 2024): https://doi.org/10.1101/2024.12.15.24318703. (bonet2024clinicalfeaturesoutcomes pages 11-13)

Therapeutic mechanisms, applications, and outcomes
- IL‑1 blockade as disease‑modifying therapy: Anakinra (recombinant IL‑1 receptor antagonist), rilonacept (soluble decoy for IL‑1), and canakinumab (anti‑IL‑1β monoclonal antibody) interrupt the IL‑1 axis downstream of NLRP3 activation. Clinical and experimental data show rapid suppression of systemic inflammation, prevention of new organ damage, and improvement or stabilization of hearing and ocular outcomes, though some established damage may be irreversible; dosing adjustments are sometimes necessary for sustained control. (booshehri2019capsandnlrp3 pages 6-8)
- Recent outcomes: In the 2023 pediatric cohort, canakinumab produced multi-domain improvement where non–IL‑1 regimens largely failed, underscoring IL‑1 dependence of disease activity in severe CAPS. URL: Frontiers in Immunology (Sep 2023): https://doi.org/10.3389/fimmu.2023.1267933. (shu2023thegeneticand pages 1-2)
- Emerging targeted approaches: In vitro, MCC950 abrogated ASC specks in most mosaic-variant cells, supporting the prospect of direct NLRP3 inhibition as a complementary or alternative strategy in CAPS, with variant-specific sensitivity. URL: medRxiv (Dec 2024): https://doi.org/10.1101/2024.12.15.24318703. (bonet2024clinicalfeaturesoutcomes pages 13-16)

Key concepts and definitions (current understanding)
- CINCA/NOMID is the severe, neonatal-onset CAPS phenotype due to NLRP3 GOF variants; somatic mosaicism is common in clinically definitive cases lacking germline findings and can be myeloid-restricted; pathogenesis is driven by dysregulated NLRP3 inflammasome activity with IL‑1β/IL‑18 overproduction and pyroptosis; IL‑1 blockade is first-line, disease-modifying therapy. (booshehri2019capsandnlrp3 pages 3-4, booshehri2019capsandnlrp3 pages 6-8, bonet2024clinicalfeaturesoutcomes pages 13-16)

Recent developments (2023–2024 priority)
- Pediatric cohort (China, 2023): 30 CAPS patients, 19 NLRP3 substitutions (8 novel), functional activation confirmed ex vivo; canakinumab improved neurologic, auditory, and visual outcomes over 10–20 months; severe case with somatic mosaicism documented. URL: https://doi.org/10.3389/fimmu.2023.1267933 (Sep 2023). (shu2023thegeneticand pages 1-2)
- Mosaic CAPS dynamics (2024): Largest mosaic cohort showed diverse post‑zygotic variants, mean VAF ~11%, two lineage-distribution patterns, and consistent response to IL‑1 blockade; MCC950 inhibited ASC specking for most variants. URL: https://doi.org/10.1101/2024.12.15.24318703 (Dec 2024). (bonet2024clinicalfeaturesoutcomes pages 11-13, bonet2024clinicalfeaturesoutcomes pages 13-16)
- Mechanistic refinements (2024): NEK7–MTOC trafficking, ASC ubiquitination, and alternative splicing act as control points of speck formation and IL‑1β maturation, helping explain disease variability and potential therapeutic leverage points beyond cytokine blockade. URL: https://doi.org/10.1111/imr.13292 (Dec 2024). (putnam2024thediscoveryof pages 8-9)

Statistics and data points (selected)
- Mosaic CAPS VAF: mean ~11.3% (range 1.3–34.8%); lineage distribution: 64.3% myeloid+lymphoid vs 35.7% myeloid-only; VAF course: stable ~53.8%, increase ~23.1%, decrease ~23.1% (follow-up >12 months). (bonet2024clinicalfeaturesoutcomes pages 11-13, bonet2024clinicalfeaturesoutcomes pages 13-16)
- Symptom frequencies in mosaic CAPS cohort: urticarial rash 100%, arthralgia 87%, fever 75%, arthritis 68%, headache 56%; systemic inflammation with cytopenias/cytoses and elevated CRP/ESR. (bonet2024clinicalfeaturesoutcomes pages 11-13)
- Pediatric CAPS (2023) with severe neuro involvement: meningitis 75% and ventriculomegaly 83.3% in reported subset; IL‑1β blockade (canakinumab) improved multi-organ domains over 10–20 months. (shu2023thegeneticand pages 1-2)

Structured annotations for knowledge base integration
- Genes/Proteins (HGNC):
  - NLRP3 (HGNC:16400): cytosolic pattern-recognition receptor forming the NLRP3 inflammasome; GOF in CINCA/NOMID. (booshehri2019capsandnlrp3 pages 6-8, putnam2024thediscoveryof pages 8-9)
  - PYCARD/ASC (HGNC:17617): adaptor forming ASC specks; essential for inflammasome assembly. (booshehri2019capsandnlrp3 pages 6-8, putnam2024thediscoveryof pages 8-9)
  - CASP1 (HGNC:1509): effector protease cleaving pro‑IL‑1β/IL‑18; executes pyroptosis with gasdermin D. (booshehri2019capsandnlrp3 pages 6-8)
  - IL1B (HGNC:5992), IL18 (HGNC:5988): inflammasome cytokines elevated in CAPS. (booshehri2019capsandnlrp3 pages 6-8)
  - NEK7 (HGNC:17644): scaffold regulating NLRP3 activation via MTOC trafficking. (putnam2024thediscoveryof pages 8-9)
- Biological processes (GO terms):
  - Inflammasome complex assembly (GO:0061702); IL‑1–mediated signaling pathway (GO:0070498); positive regulation of interleukin‑1β production (GO:0032731); pyroptosis (GO:0070269); caspase‑1 activation (GO:0000422; “activation of cysteine-type endopeptidase activity involved in pyroptosis”). (booshehri2019capsandnlrp3 pages 6-8, putnam2024thediscoveryof pages 8-9)
- Cellular components:
  - NLRP3 inflammasome complex; ASC speck (inflammasome focus) in cytosol; microtubule organizing center (MTOC); autophagosome. (putnam2024thediscoveryof pages 8-9, booshehri2019capsandnlrp3 pages 6-8)
- Cell types (CL):
  - Monocyte (CL:0000576), macrophage (CL:0000775), neutrophil (CL:0000094) as principal effectors; chondrocyte (CL:0000136), osteoblast (CL:0000062) in bone/cartilage lesions; microglial cell (CL:0002319) and meningeal macrophages in CNS disease; keratinocyte (CL:0000312) in skin; cochlear hair cell (CL:0002370) as damage target. (booshehri2019capsandnlrp3 pages 3-4, bonet2024clinicalfeaturesoutcomes pages 13-16, booshehri2019capsandnlrp3 pages 6-8)
- Anatomical locations (UBERON):
  - Skin (UBERON:0002097), meninges (UBERON:0002316), brain (UBERON:0000955), cochlea (UBERON:0001844), eye (UBERON:0000970), growth plate/epiphysis (UBERON:0003860). (booshehri2019capsandnlrp3 pages 3-4, arık2025autoinflammatorydiseasemolecular pages 3-4)
- Chemical entities (illustrative):
  - Anakinra (IL‑1 receptor antagonist), canakinumab (anti‑IL‑1β mAb), rilonacept (IL‑1 trap), MCC950 (small‑molecule NLRP3 inhibitor under investigation); all act on the IL‑1/NLRP3 axis with demonstrated or emerging efficacy in CAPS/CINCA contexts. (booshehri2019capsandnlrp3 pages 6-8, bonet2024clinicalfeaturesoutcomes pages 13-16, shu2023thegeneticand pages 1-2)

Phenotype associations (HPO examples)
- Urticarial rash (HP:0001025); recurrent fever (HP:0001954); chronic aseptic meningitis (HP:0002925); increased CSF pressure (HP:0010886); ventriculomegaly (HP:0002119); sensorineural hearing impairment (HP:0000407); uveitis (HP:0000554); papilledema (HP:0001085); optic atrophy (HP:0000648); abnormal bone growth/epiphyseal overgrowth and arthropathy (HP:0000939, HP:0002814). (booshehri2019capsandnlrp3 pages 3-4, shu2023thegeneticand pages 1-2, arık2025autoinflammatorydiseasemolecular pages 3-4)

Expert opinions and authoritative analysis
- Foundational and translational insights from Hoffman and colleagues emphasize that CAPS pathogenesis is inflammasome‑centric, myeloid‑driven, and profoundly IL‑1 dependent, explaining the transformative impact of IL‑1 blockade across the CAPS spectrum, including CINCA/NOMID. URL: Journal of Clinical Immunology (Apr 2019): https://doi.org/10.1007/s10875-019-00638-z; Immunological Reviews (Dec 2024): https://doi.org/10.1111/imr.13292. (booshehri2019capsandnlrp3 pages 3-4, putnam2024thediscoveryof pages 8-9)

Current applications and real‑world implementations
- Routine practice includes early genetic testing (with attention to mosaicism), serial audiology and ophthalmology, neuroimaging/CSF assessment when indicated, and prompt initiation of IL‑1 blockade to prevent irreversible CNS/ear/eye damage; these recommendations are echoed in recent reviews. (arık2025autoinflammatorydiseasemolecular pages 3-4)
- Clinical experience in 2023–2024 cohorts shows IL‑1β blockade (canakinumab) achieving broad symptom control and organ protection in children and sustained benefits in mosaic adults; direct NLRP3 inhibition (e.g., MCC950 ex vivo) may offer future precision approaches, potentially guided by variant sensitivity. (shu2023thegeneticand pages 1-2, bonet2024clinicalfeaturesoutcomes pages 13-16)

Evidence items with PMIDs/DOIs and dates (selection)
- Putnam CD, Broderick L, Hoffman HM. Immunological Reviews. Dec 2024. DOI: 10.1111/imr.13292. URL: https://doi.org/10.1111/imr.13292. (putnam2024thediscoveryof pages 8-9)
- Booshehri LM, Hoffman HM. J Clin Immunol. Apr 2019. DOI: 10.1007/s10875-019-00638-z. URL: https://doi.org/10.1007/s10875-019-00638-z. (booshehri2019capsandnlrp3 pages 3-4, booshehri2019capsandnlrp3 pages 6-8)
- Shu Z et al. Front Immunol. Sep 2023. DOI: 10.3389/fimmu.2023.1267933. URL: https://doi.org/10.3389/fimmu.2023.1267933. (shu2023thegeneticand pages 1-2)
- Bonet N et al. medRxiv (preprint). Dec 2024. DOI: 10.1101/2024.12.15.24318703. URL: https://doi.org/10.1101/2024.12.15.24318703. (bonet2024clinicalfeaturesoutcomes pages 13-16, bonet2024clinicalfeaturesoutcomes pages 11-13)

Limitations and gaps
- Precise population-level frequencies for specific CINCA/NOMID sequelae (e.g., hearing loss prevalence, optic atrophy rates) vary across registries and are incompletely captured in the 2023–2024 sources summarized here; longitudinal outcomes under standardized IL‑1 blockade, particularly neuro-otologic endpoints, would benefit from harmonized reporting. (shu2023thegeneticand pages 1-2, bonet2024clinicalfeaturesoutcomes pages 11-13)

Conclusion
CINCA/NOMID is a prototypic inflammasomopathy driven by NLRP3 gain‑of‑function, with constitutive inflammasome activation (ASC specks → caspase‑1 → IL‑1β/IL‑18) and pyroptotic cell death in myeloid cells underpinning widespread tissue inflammation across skin, bone/cartilage, CNS/meninges, eye, and cochlea. Somatic mosaicism is common in severe CAPS and may be myeloid‑restricted, yet confers similar inflammasome hyperactivity and therapeutic responsiveness. Early, sustained IL‑1 blockade is the standard of care, improving systemic and organ‑specific outcomes, while emerging NLRP3 inhibitors show promise ex vivo and may soon expand therapeutic options. (booshehri2019capsandnlrp3 pages 6-8, bonet2024clinicalfeaturesoutcomes pages 13-16, shu2023thegeneticand pages 1-2, putnam2024thediscoveryof pages 8-9, booshehri2019capsandnlrp3 pages 3-4, bonet2024clinicalfeaturesoutcomes pages 11-13)

References

1. (booshehri2019capsandnlrp3 pages 6-8): Laela M. Booshehri and Hal M. Hoffman. Caps and nlrp3. Journal of Clinical Immunology, 39:277-286, Apr 2019. URL: https://doi.org/10.1007/s10875-019-00638-z, doi:10.1007/s10875-019-00638-z. This article has 275 citations and is from a domain leading peer-reviewed journal.

2. (putnam2024thediscoveryof pages 8-9): Christopher D. Putnam, Lori Broderick, and Hal M. Hoffman. The discovery of nlrp3 and its function in cryopyrin-associated periodic syndromes and innate immunity. Immunological reviews, 322:259-282, Dec 2024. URL: https://doi.org/10.1111/imr.13292, doi:10.1111/imr.13292. This article has 29 citations and is from a domain leading peer-reviewed journal.

3. (booshehri2019capsandnlrp3 pages 3-4): Laela M. Booshehri and Hal M. Hoffman. Caps and nlrp3. Journal of Clinical Immunology, 39:277-286, Apr 2019. URL: https://doi.org/10.1007/s10875-019-00638-z, doi:10.1007/s10875-019-00638-z. This article has 275 citations and is from a domain leading peer-reviewed journal.

4. (bonet2024clinicalfeaturesoutcomes pages 13-16): Nuria Bonet, Jose M. Mascaro, Laura Hurtado-Navarro, Diego Angosto-Bazarra, Jose Luis Callejas-Rubio, Daniel Clemente, Alejandro Souto, Olalla Lima, Natalia Palmou-Fontana, Eulalia Baselga, Santiago Jiménez-Treviño, Agustin Remesal, Marta Andreu-Barasoain, Luis Fernandez-Dominguez, Josep Riera-Monroig, Maria Aparicio, Juan Garcia-Herrero, David Pesqué, Maria Teresa Sanchez-Calvin, Jose Miguel Lezana-Rosales, Maria Correyero-Plaza, Julio Garcia-Villalba, Victor Bolaño, Sara Peiro, Mar Diaz, Alexandru Vlagea, Daniel Lorca, Virginia Fabregat, Maria Carmen Anton, Susana Plaza, Luis Ignacio Gonzalez-Granado, Concepción Postigo, Jose Maria Garcia-Ruiz de Morales, Enrique Gómez de la Fuente, Estibaliz Iglesias, Javier Gomez-Roman, Caritina Vázquez-Triñanes, Juan Carlos Lopez-Robledillo, Norberto Ortego-Centeno, Ana María Giménez-Arnau, Josep M. Campistol, Hafid Laayouni, Iñaki Ortiz de Landazuri, Jordi Yagüe, Eva Gonzalez-Roca, Anna Mensa-Vilaro, Oscar Fornas, Eduardo Ramos, Pablo Pelegrin, Ferran Casals, and Juan I. Arostegui. Clinical features, outcomes of treatments, inflammasome function and longitudinal clonal dynamics into nlrp3 mosaicism: evidence from the largest cryopyrin-associated periodic syndromes cohort to date. MedRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.12.15.24318703, doi:10.1101/2024.12.15.24318703. This article has 0 citations.

5. (bonet2024clinicalfeaturesoutcomes pages 11-13): Nuria Bonet, Jose M. Mascaro, Laura Hurtado-Navarro, Diego Angosto-Bazarra, Jose Luis Callejas-Rubio, Daniel Clemente, Alejandro Souto, Olalla Lima, Natalia Palmou-Fontana, Eulalia Baselga, Santiago Jiménez-Treviño, Agustin Remesal, Marta Andreu-Barasoain, Luis Fernandez-Dominguez, Josep Riera-Monroig, Maria Aparicio, Juan Garcia-Herrero, David Pesqué, Maria Teresa Sanchez-Calvin, Jose Miguel Lezana-Rosales, Maria Correyero-Plaza, Julio Garcia-Villalba, Victor Bolaño, Sara Peiro, Mar Diaz, Alexandru Vlagea, Daniel Lorca, Virginia Fabregat, Maria Carmen Anton, Susana Plaza, Luis Ignacio Gonzalez-Granado, Concepción Postigo, Jose Maria Garcia-Ruiz de Morales, Enrique Gómez de la Fuente, Estibaliz Iglesias, Javier Gomez-Roman, Caritina Vázquez-Triñanes, Juan Carlos Lopez-Robledillo, Norberto Ortego-Centeno, Ana María Giménez-Arnau, Josep M. Campistol, Hafid Laayouni, Iñaki Ortiz de Landazuri, Jordi Yagüe, Eva Gonzalez-Roca, Anna Mensa-Vilaro, Oscar Fornas, Eduardo Ramos, Pablo Pelegrin, Ferran Casals, and Juan I. Arostegui. Clinical features, outcomes of treatments, inflammasome function and longitudinal clonal dynamics into nlrp3 mosaicism: evidence from the largest cryopyrin-associated periodic syndromes cohort to date. MedRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.12.15.24318703, doi:10.1101/2024.12.15.24318703. This article has 0 citations.

6. (shu2023thegeneticand pages 1-2): Zhou Shu, Yue Zhang, Tongxin Han, Yan Li, Yurong Piao, Fei Sun, Jin Ma, Wenxiu Mo, Jiapeng Sun, Koon-Wing Chan, Wanling Yang, Yu-Lung Lau, and Huawei Mao. The genetic and clinical characteristics and effects of canakinumab on cryopyrin-associated periodic syndrome: a large pediatric cohort study from china. Frontiers in Immunology, Sep 2023. URL: https://doi.org/10.3389/fimmu.2023.1267933, doi:10.3389/fimmu.2023.1267933. This article has 8 citations and is from a peer-reviewed journal.

7. (arık2025autoinflammatorydiseasemolecular pages 3-4): SD Arık and B Menentoğlu. Autoinflammatory disease: molecular insights, clinical spectrum, and emerging therapies: autoinflammation: mechanisms and management. Unknown journal, 2025.