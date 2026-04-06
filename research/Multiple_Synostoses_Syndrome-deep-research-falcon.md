---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-10T07:44:39.327680'
end_time: '2026-02-10T07:49:13.977549'
duration_seconds: 274.65
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Multiple Synostoses Syndrome
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
- **Disease Name:** Multiple Synostoses Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Multiple Synostoses Syndrome**.
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
- **Disease Name:** Multiple Synostoses Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Multiple Synostoses Syndrome**.
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


Disease Pathophysiology Research Report: Multiple Synostoses Syndrome (SYNS1–4)

Target Disease
- Disease Name: Multiple Synostoses Syndrome (SYNS)
- MONDO ID: Not specified in source set
- Category: Mendelian, autosomal dominant

Scope and nomenclature
Multiple synostoses syndromes comprise a genetically heterogeneous group characterized by progressive or congenital joint fusions involving hands/feet (carpal–tarsal coalitions, symphalangism), large joints (e.g., elbow, knee), vertebrae, and sometimes conductive hearing loss due to stapes ankylosis. Four principal subtypes are recognized by causal genes: SYNS1 (NOG), SYNS2 (GDF5), SYNS3 (FGF9), SYNS4 (GDF6). Mechanistically, they converge on dysregulation of BMP and FGF signaling during joint morphogenesis and maintenance. (wu2009multiplesynostosessyndrome pages 7-8, tang2017apointmutation pages 9-10, wang2016anewsubtype pages 3-5, terhal2018furtherdelineationof pages 1-2)

1) Core Pathophysiology
- Primary mechanisms:
  - Excess BMP pathway activity due to ligand gain-of-function and/or resistance to the BMP antagonist noggin (SYNS1/NOG, SYNS2/GDF5, SYNS4/GDF6) leading to ectopic chondrogenesis and failure of joint interzone formation/maintenance. Wang et al.: “a mutation in GDF6 … decreases its sensitivity to noggin and enhances its potency as a BMP signal” (J Bone Miner Res, Apr 2016; https://doi.org/10.1002/jbmr.2761). (wang2016anewsubtype pages 5-7, wang2016anewsubtype pages 3-5)
  - Impaired FGF9 signaling and altered FGF–BMP balance (SYNS3/FGF9), which disrupt joint interzone cell fate by failing to restrain chondrogenic differentiation and to support Gdf5 expression at nascent joints, producing synostosis. Tang et al.: “A point mutation in Fgf9 impedes joint interzone formation” (Hum Mol Genet, Apr 2017; https://doi.org/10.1093/hmg/ddx029). (tang2017apointmutation pages 9-10, tang2017apointmutation pages 1-2)
- Dysregulated pathways:
  - Canonical BMP/SMAD signaling is increased by GDF6 Y444N and analogous GDF5 knuckle-epitope variants that are noggin-resistant; enhanced ALP activity, SMAD1/5/8 reporter activation, and increased chondrogenesis are documented. “Increased BMP signaling resulting from reduced sensitivity to NOG” (Wang 2016). (wang2016anewsubtype pages 5-7, wang2016anewsubtype pages 3-5)
  - FGF signaling via FGF9 is reduced with S99N: diminished ERK activation, reduced FGFR3 binding, and impaired Wnt/β-catenin support, shifting interzone mesenchyme toward chondrogenesis and ossification. Wu et al. report that the S99N mutant “shows impaired signaling … and markedly reduced binding to FGFR3,” contextualized within SYNS genetics. (Am J Hum Genet, Jul 2009; https://doi.org/10.1016/j.ajhg.2009.06.007). (wu2009multiplesynostosessyndrome pages 7-8)
- Affected cellular processes:
  - Joint interzone formation and maintenance fail, with excess chondrogenesis at would-be joint spaces (FGF9 S99N) and exaggerated BMP-driven chondro-ossification (GDF6 Y444N; likely similar in NOG/GDF5). (tang2017apointmutation pages 9-10, wang2016anewsubtype pages 3-5)
  - Postnatal progression includes ectopic ossification and vertebral calcification/fusion with age in Fgf9 mutant models, consistent with progressive synostosis. (tang2017apointmutation pages 9-10)

2) Key Molecular Players
- Genes/Proteins (HGNC):
  - NOG (HGNC:7858; protein: Noggin) – extracellular BMP antagonist; heterozygous variants cause SYNS1 and related NOG-spectrum disorders; mechanistic axis is loss of BMP inhibition → increased BMP activity. (Summary context within Wu 2009 and cross-referenced in Wang 2016). (wu2009multiplesynostosessyndrome pages 7-8, wang2016anewsubtype pages 8-8)
  - GDF5 (HGNC:4221; BMP14) – BMP-family ligand critical for joint patterning; SYNS2 variants include noggin-resistant mutations in the knuckle epitope causing enhanced signaling. “Mutation within the GDF5 knuckle epitope causes noggin-resistance.” (cited within Wang 2016 synopsis). (wang2016anewsubtype pages 8-8)
  - FGF9 (HGNC:3680) – paracrine FGF controlling interzone cell fate; S99N (human) impairs signaling, reduces FGFR3 binding, and diminishes ERK/Wnt outputs; SYNS3 is FGF9-associated. (wu2009multiplesynostosessyndrome pages 7-8, tang2017apointmutation pages 1-2)
  - GDF6 (HGNC:4228; BMP13) – BMP-family ligand; SYNS4 Y444N decreases sensitivity to NOG and “enhances its potency as a BMP signal,” producing gain-of-function. (wang2016anewsubtype pages 5-7, wang2016anewsubtype pages 3-5, terhal2018furtherdelineationof pages 1-2)
- Chemical Entities (CHEBI) and modulators:
  - BMP ligands (class); antagonism by Noggin; FGF9–FGFR interactions regulate MAPK/ERK. Specific small-molecule therapeutics were not detailed in the source set; mechanistic chemicals are signaling proteins rather than small-molecule metabolites. (wu2009multiplesynostosessyndrome pages 7-8, wang2016anewsubtype pages 5-7)
- Cell Types (CL):
  - Interzone mesenchymal cells (joint progenitors) and chondrocytes are primary targets; osteoblasts/osteoclasts contribute to ossification outcomes and vertebral fusion. FGF9 normally “inhibits mesenchymal differentiation into chondrocytes … maintaining an undifferentiated interzone” and S99N causes “excess chondrogenesis within the interzone.” (tang2017apointmutation pages 9-10, tang2017apointmutation pages 1-2)
- Anatomical Locations (UBERON):
  - Distal appendicular skeleton: hand/foot (carpal/tarsal coalitions, symphalangism), large joints (elbow, knee), axial skeleton (vertebrae), middle ear (stapes) – consistent across SYNS subtypes with locus-specific variability. (wang2016anewsubtype pages 3-5, tang2017apointmutation pages 9-10, terhal2018furtherdelineationof pages 1-2)

3) Biological Processes (GO-style annotations)
- BMP signaling pathway; positive regulation of chondrocyte differentiation; cartilage development; joint morphogenesis; regulation by BMP antagonist (Noggin). Empirically supported by functional assays: “enhanced BMP signaling” with GDF6 Y444N and noggin resistance (ALP, SMAD1/5/8 reporter, micromass chondrogenesis). (wang2016anewsubtype pages 5-7, wang2016anewsubtype pages 3-5)
- FGF receptor signaling pathway; negative regulation of chondrogenesis in joint interzone; promotion of Gdf5 expression at nascent joints; MAPK/ERK cascade; crosstalk with Wnt/β-catenin. Demonstrated by FGF9 S99N effects on ERK, FGFR3 binding, and interzone gene programs. (wu2009multiplesynostosessyndrome pages 7-8, tang2017apointmutation pages 9-10)
- Ossification and endochondral bone development; ectopic chondrogenesis leading to synostosis when regulatory balance is perturbed. (tang2017apointmutation pages 9-10, wang2016anewsubtype pages 3-5)

4) Cellular Components
- Extracellular region: Noggin–BMP ligand interactions (NOG with GDF5/GDF6) governing receptor availability. (wang2016anewsubtype pages 3-5, terhal2018furtherdelineationof pages 1-2)
- Plasma membrane: BMP type I/II receptors and FGFRs on chondrogenic/interzone cells mediating SMAD and MAPK cascades. (tang2017apointmutation pages 9-10, terhal2018furtherdelineationof pages 1-2)
- ECM microenvironment at nascent joints (interzone) where ligand diffusion and receptor engagement set spatial signaling domains. (tang2017apointmutation pages 9-10)

5) Disease Progression
- Initiation (prenatal):
  - SYNS3 (FGF9 S99N): failure to establish/maintain an undifferentiated interzone at selected joints, “imped[ing] joint interzone formation,” with reduced Gdf5 expression at elbow/knee, leading to patterning defects and early fusion. (Hum Mol Genet, Apr 2017; https://doi.org/10.1093/hmg/ddx029). (tang2017apointmutation pages 9-10, tang2017apointmutation pages 1-2)
  - SYNS4 (GDF6 Y444N): heightened BMP signaling due to noggin resistance drives ectopic chondrogenesis where joints should form; carpal/tarsal fusions prominent. (J Bone Miner Res, Apr 2016; https://doi.org/10.1002/jbmr.2761). (wang2016anewsubtype pages 5-7, wang2016anewsubtype pages 3-5)
- Progression (postnatal):
  - Progressive vertebral fusion and increased ossification with age in Fgf9 mutant models; clinical SYNS cohorts show progressive ankylosis beyond congenital coalitions. (tang2017apointmutation pages 9-10)
- Tissue spectrum:
  - Digits (symphalangism), carpals/tarsals, elbows/knees, vertebrae, and middle ear ossicles (stapes ankylosis in subsets), reflecting locus-specific expressivity. (wang2016anewsubtype pages 3-5, tang2017apointmutation pages 9-10, terhal2018furtherdelineationof pages 1-2)

6) Phenotypic Manifestations (HPO terms/examples)
- Symphalangism (HP:0004691) and carpal–tarsal coalition (HP:0005048) with variable large-joint synostoses (e.g., elbow/knee; HP:0003031/HP:0010584). (tang2017apointmutation pages 9-10, wang2016anewsubtype pages 3-5)
- Vertebral fusion (HP:0002948) with progressive involvement in some FGF9-associated cases. (tang2017apointmutation pages 9-10)
- Conductive hearing loss due to stapes ankylosis (HP:0000405) – common in NOG/GDF6 subtypes; historically “unreported” in SYNS3 but 2023 family with FGF9 variant extends the spectrum to include conductive loss and cleft palate: “We extend the phenotypic spectrum of SYNS3 by suggesting that cleft palate and conductive hearing loss are part of the syndrome.” (Genes, Mar 2023; https://doi.org/10.3390/genes14030724). (schmetz2023fgf9associatedmultiplesynostoses pages 11-12, terhal2018furtherdelineationof pages 1-2)

Key Evidence Items (primary data, quotes, and dates)
- GDF6 SYNS4 mechanism and phenotype:
  - “A new subtype of multiple synostoses syndrome is caused by a mutation in GDF6 that decreases its sensitivity to noggin and enhances its potency as a BMP signal” (Journal of Bone and Mineral Research, Apr 2016; DOI:10.1002/jbmr.2761; URL: https://doi.org/10.1002/jbmr.2761). Functional assays: increased ALP, SMAD1/5/8 reporter activity, and chondrogenesis; clinical: bilateral wrist/ankle deformities at birth and progressive conductive deafness after age 40. (wang2016anewsubtype pages 5-7, wang2016anewsubtype pages 3-5)
- FGF9 SYNS3 mechanism and interzone biology:
  - “A point mutation in Fgf9 impedes joint interzone formation leading to multiple synostoses syndrome” (Human Molecular Genetics, Apr 2017; DOI:10.1093/hmg/ddx029; URL: https://doi.org/10.1093/hmg/ddx029). S99N disrupts FGF signaling, fails to repress Sox6/Sox9 in interzone, reduces Gdf5 at elbow/knee, and causes site-specific synostosis; progressive axial changes with age. (tang2017apointmutation pages 9-10, tang2017apointmutation pages 1-2)
  - Original human genetics of SYNS3: “Multiple synostoses syndrome is due to a missense mutation in exon 2 of FGF9” (American Journal of Human Genetics, Jul 2009; DOI:10.1016/j.ajhg.2009.06.007; URL: https://doi.org/10.1016/j.ajhg.2009.06.007). Shows S99N impairs ERK signaling, reduces FGFR3 binding, and alters Wnt/β-catenin context; delineates clinical spectrum. (wu2009multiplesynostosessyndrome pages 7-8)
- GDF6-related SYNS4 delineation and hearing loss:
  - “Further delineation of the GDF6 related multiple synostoses syndrome” (Am J Med Genet A, Jan 2018; DOI:10.1002/ajmg.a.38503; URL: https://doi.org/10.1002/ajmg.a.38503). Confirms gain-of-function and noggin-resistance mechanisms with variable conductive hearing loss (otosclerosis/stapes fixation can occur in childhood). (terhal2018furtherdelineationof pages 1-2)
- SYNS3 phenotype expansion and statistics:
  - “FGF9-Associated Multiple Synostoses Syndrome Type 3 in a Multigenerational Family” (Genes, Mar 2023; DOI:10.3390/genes14030724; URL: https://doi.org/10.3390/genes14030724). Reports a novel p.Trp144Arg variant; “only five different missense variants in FGF9 … reported in 18 affected individuals” previously; extends spectrum to include conductive hearing loss and cleft palate, with marked intrafamilial variability. (schmetz2023fgf9associatedmultiplesynostoses pages 11-12)

Expert perspectives and integrative analysis
- Convergent model: Three subtypes (SYNS1/NOG; SYNS2/GDF5; SYNS4/GDF6) feature excessive BMP activity—by reduced noggin inhibition or ligand hypermorphs—driving ectopic chondrogenesis and joint failure; SYNS3/FGF9 features reduced local FGF signaling that fails to preserve an interzone progenitor state and to support Gdf5 expression, further tilting the BMP–FGF balance toward chondro-ossification. Wang et al. explicitly note: “3 of the 4 SYNS identified are the result of increased BMP signaling (SYNS1, SYNS2, and here SYNS4), whereas SYNS3 is caused by a loss-of-function mutation in FGF9.” (J Bone Miner Res, 2016; https://doi.org/10.1002/jbmr.2761). (wang2016anewsubtype pages 8-8)
- Tissue selectivity and progression reflect spatially restricted expression (e.g., Fgf9 at elbow/knee), ligand diffusion/receptor context, and mechanical environments that modulate ossification postnatally (e.g., progressive vertebral involvement in Fgf9 S99N models). (tang2017apointmutation pages 9-10)
- Hearing loss biology: Whereas conductive hearing loss is classically linked to NOG/GDF6 subtypes via stapes fixation/otosclerosis, recent SYNS3 evidence suggests FGF9 perturbation can also affect middle-ear development or maintenance, broadening counseling/management considerations. (schmetz2023fgf9associatedmultiplesynostoses pages 11-12, terhal2018furtherdelineationof pages 1-2)

Applications and real-world implementations
- Genetic diagnosis and counseling: Gene-specific expectations guide surveillance—e.g., carpal/tarsal and vertebral imaging for all subtypes; audiologic monitoring prioritized for NOG/GDF6 and now considered in FGF9 families per 2023 report. (schmetz2023fgf9associatedmultiplesynostoses pages 11-12, terhal2018furtherdelineationof pages 1-2)
- Surgical/rehabilitative care: Although not detailed extensively in the current evidence set, mechanistic and anatomical insights underpin orthopedic management of coalitions/synostoses and stapes surgery timing in conductive loss. The recognition that interzone failure and ectopic ossification are ongoing processes supports staged, individualized orthopedic interventions. (tang2017apointmutation pages 9-10, terhal2018furtherdelineationof pages 1-2)

Structured annotations (ontology cross-references; examples)
- Genes/Proteins (HGNC): NOG (HGNC:7858); GDF5 (HGNC:4221); FGF9 (HGNC:3680); GDF6 (HGNC:4228). (wu2009multiplesynostosessyndrome pages 7-8, wang2016anewsubtype pages 8-8, tang2017apointmutation pages 9-10, terhal2018furtherdelineationof pages 1-2)
- Biological Processes (GO): BMP signaling pathway; joint morphogenesis; chondrocyte differentiation; FGF receptor signaling pathway; MAPK cascade; regulation by BMP antagonist activity. (wang2016anewsubtype pages 3-5, tang2017apointmutation pages 9-10)
- Cellular Components (GO): extracellular region (ligand–antagonist interactions); plasma membrane (BMPRs, FGFRs); extracellular matrix at nascent joint interzone. (terhal2018furtherdelineationof pages 1-2, tang2017apointmutation pages 9-10)
- Cell Types (CL): interzone mesenchymal progenitors; chondrocytes; osteoblasts; osteoclasts. (tang2017apointmutation pages 9-10)
- Anatomical Locations (UBERON): hand (carpal bones), foot (tarsal bones), elbow, knee, vertebral column, middle ear (stapes). (wang2016anewsubtype pages 3-5, tang2017apointmutation pages 9-10, terhal2018furtherdelineationof pages 1-2)
- Phenotypes (HPO): symphalangism (HP:0004691); carpal–tarsal coalition (HP:0005048); elbow ankylosis/synostosis (HP:0003031); vertebral fusion (HP:0002948); conductive hearing loss (HP:0000405). (tang2017apointmutation pages 9-10, wang2016anewsubtype pages 3-5, terhal2018furtherdelineationof pages 1-2)

Recent developments (2023–2024 priority)
- FGF9/SYNS3 spectrum expanded: conductive hearing loss and cleft palate reported in a large multigenerational family; total known FGF9 missense variants and affected individuals summarized, underscoring rarity and variable expressivity (Genes, Mar 2023; https://doi.org/10.3390/genes14030724). (schmetz2023fgf9associatedmultiplesynostoses pages 11-12)

Limitations and open questions
- Though noggin-resistance is clearly demonstrated for selected GDF5/GDF6 variants, quantitative maps of NOG–BMP–FGF crosstalk across all human SYNS alleles remain incomplete. Site-specific vulnerability (e.g., elbow/knee) needs deeper integration of spatiotemporal expression and biomechanics to predict phenotype. (tang2017apointmutation pages 9-10, wang2016anewsubtype pages 3-5)

References with URLs and dates (subset, keyed to citations above)
- Wang et al., Journal of Bone and Mineral Research, Apr 2016. “A new subtype of multiple synostoses syndrome is caused by a mutation in GDF6 that decreases its sensitivity to noggin and enhances its potency as a BMP signal.” DOI:10.1002/jbmr.2761. URL: https://doi.org/10.1002/jbmr.2761 (wang2016anewsubtype pages 5-7, wang2016anewsubtype pages 3-5)
- Tang et al., Human Molecular Genetics, Apr 2017. “A point mutation in Fgf9 impedes joint interzone formation leading to multiple synostoses syndrome.” DOI:10.1093/hmg/ddx029. URL: https://doi.org/10.1093/hmg/ddx029 (tang2017apointmutation pages 9-10, tang2017apointmutation pages 1-2)
- Wu et al., American Journal of Human Genetics, Jul 2009. “Multiple synostoses syndrome is due to a missense mutation in exon 2 of FGF9 gene.” DOI:10.1016/j.ajhg.2009.06.007. URL: https://doi.org/10.1016/j.ajhg.2009.06.007 (wu2009multiplesynostosessyndrome pages 7-8)
- Terhal et al., American Journal of Medical Genetics Part A, Jan 2018. “Further delineation of the GDF6 related multiple synostoses syndrome.” DOI:10.1002/ajmg.a.38503. URL: https://doi.org/10.1002/ajmg.a.38503 (terhal2018furtherdelineationof pages 1-2)
- Schmetz et al., Genes, Mar 2023. “FGF9-Associated Multiple Synostoses Syndrome Type 3 in a Multigenerational Family.” DOI:10.3390/genes14030724. URL: https://doi.org/10.3390/genes14030724 (schmetz2023fgf9associatedmultiplesynostoses pages 11-12)

References

1. (wu2009multiplesynostosessyndrome pages 7-8): Xiao-lin Wu, Ming-min Gu, Lei Huang, Xue-song Liu, Hong-xin Zhang, Xiao-yi Ding, Jian-qiang Xu, Bin Cui, Long Wang, Shun-yuan Lu, Xiao-yi Chen, Hai-guo Zhang, Wei Huang, Wen-tao Yuan, Jiang-ming Yang, Qun Gu, Jian Fei, Zhu Chen, Zhi-min Yuan, and Zhu-gang Wang. Multiple synostoses syndrome is due to a missense mutation in exon 2 of fgf9 gene. American journal of human genetics, 85 1:53-63, Jul 2009. URL: https://doi.org/10.1016/j.ajhg.2009.06.007, doi:10.1016/j.ajhg.2009.06.007. This article has 104 citations and is from a highest quality peer-reviewed journal.

2. (tang2017apointmutation pages 9-10): Lingyun Tang, Xiaolin Wu, Hongxing Zhang, Shun-yuan Lu, Min Wu, Chunling Shen, Xuejiao Chen, Yicheng Wang, Wei-gang Wang, Yan Shen, Ming-min Gu, Xiaoyi Ding, Xiaolong Jin, J. Fei, and Zhugang Wang. A point mutation in fgf9 impedes joint interzone formation leading to multiple synostoses syndrome. Human Molecular Genetics, 26:1280–1293, Apr 2017. URL: https://doi.org/10.1093/hmg/ddx029, doi:10.1093/hmg/ddx029. This article has 34 citations and is from a domain leading peer-reviewed journal.

3. (wang2016anewsubtype pages 3-5): Jian Wang, Tingting Yu, Zhigang Wang, Satoshi Ohte, Ru-en Yao, Zhaojing Zheng, Juan Geng, Haiqing Cai, Yihua Ge, Yuchan Li, Yunlan Xu, Qinghua Zhang, James F Gusella, Qihua Fu, Steven Pregizer, Vicki Rosen, and Yiping Shen. A new subtype of multiple synostoses syndrome is caused by a mutation in gdf6 that decreases its sensitivity to noggin and enhances its potency as a bmp signal. Journal of Bone and Mineral Research, Apr 2016. URL: https://doi.org/10.1002/jbmr.2761, doi:10.1002/jbmr.2761. This article has 40 citations and is from a highest quality peer-reviewed journal.

4. (terhal2018furtherdelineationof pages 1-2): Paulien A. Terhal, Nienke E. Verbeek, Nine Knoers, Rutger J. A. J. Nievelstein, Ans van den Ouweland, Ralph J. Sakkers, Lucienne Speleman, and Gijs van Haaften. Further delineation of the gdf6 related multiple synostoses syndrome. American Journal of Medical Genetics Part A, 176:225-229, Jan 2018. URL: https://doi.org/10.1002/ajmg.a.38503, doi:10.1002/ajmg.a.38503. This article has 15 citations.

5. (wang2016anewsubtype pages 5-7): Jian Wang, Tingting Yu, Zhigang Wang, Satoshi Ohte, Ru-en Yao, Zhaojing Zheng, Juan Geng, Haiqing Cai, Yihua Ge, Yuchan Li, Yunlan Xu, Qinghua Zhang, James F Gusella, Qihua Fu, Steven Pregizer, Vicki Rosen, and Yiping Shen. A new subtype of multiple synostoses syndrome is caused by a mutation in gdf6 that decreases its sensitivity to noggin and enhances its potency as a bmp signal. Journal of Bone and Mineral Research, Apr 2016. URL: https://doi.org/10.1002/jbmr.2761, doi:10.1002/jbmr.2761. This article has 40 citations and is from a highest quality peer-reviewed journal.

6. (tang2017apointmutation pages 1-2): Lingyun Tang, Xiaolin Wu, Hongxing Zhang, Shun-yuan Lu, Min Wu, Chunling Shen, Xuejiao Chen, Yicheng Wang, Wei-gang Wang, Yan Shen, Ming-min Gu, Xiaoyi Ding, Xiaolong Jin, J. Fei, and Zhugang Wang. A point mutation in fgf9 impedes joint interzone formation leading to multiple synostoses syndrome. Human Molecular Genetics, 26:1280–1293, Apr 2017. URL: https://doi.org/10.1093/hmg/ddx029, doi:10.1093/hmg/ddx029. This article has 34 citations and is from a domain leading peer-reviewed journal.

7. (wang2016anewsubtype pages 8-8): Jian Wang, Tingting Yu, Zhigang Wang, Satoshi Ohte, Ru-en Yao, Zhaojing Zheng, Juan Geng, Haiqing Cai, Yihua Ge, Yuchan Li, Yunlan Xu, Qinghua Zhang, James F Gusella, Qihua Fu, Steven Pregizer, Vicki Rosen, and Yiping Shen. A new subtype of multiple synostoses syndrome is caused by a mutation in gdf6 that decreases its sensitivity to noggin and enhances its potency as a bmp signal. Journal of Bone and Mineral Research, Apr 2016. URL: https://doi.org/10.1002/jbmr.2761, doi:10.1002/jbmr.2761. This article has 40 citations and is from a highest quality peer-reviewed journal.

8. (schmetz2023fgf9associatedmultiplesynostoses pages 11-12): Ariane Schmetz, Jörg Schaper, Simon Thelen, Majeed Rana, Thomas Klenzner, Katharina Schaumann, Jasmin Beygo, Harald Surowy, Hermann-Josef Lüdecke, and Dagmar Wieczorek. Fgf9-associated multiple synostoses syndrome type 3 in a multigenerational family. Genes, 14:724, Mar 2023. URL: https://doi.org/10.3390/genes14030724, doi:10.3390/genes14030724. This article has 4 citations and is from a poor quality or predatory journal.