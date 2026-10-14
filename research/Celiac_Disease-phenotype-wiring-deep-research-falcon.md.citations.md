# Citations for Research Query

**Query:** # Mechanism-to-Phenotype Wiring Research Template

## Target Disease
- **Disease Name:** Celiac Disease
- **MONDO ID:** MONDO:0005130 (if available)

## Context: What Is Already Curated

This disease's knowledge base entry already models the following pathophysiology
mechanism nodes:

1. Gluten-Triggered Immune Response (TG2 deamidation of gliadin, HLA-DQ2/DQ8 presentation, CD4 T-cell activation); 2. Mixed Th1/Th17/IL-21 Mucosal Cytokine Response; 3. Intestinal Epithelial Damage (IL-15/NKG2D-MICA intraepithelial lymphocyte cytotoxicity, villous atrophy, crypt hyperplasia); 4. Autoantibody Production (anti-TG2 IgA, anti-deamidated-gliadin-peptide antibodies, plasma cells); 5. Barrier Dysfunction (zonulin, tight junction disruption, increased permeability); 6. Microbiome Dysbiosis

It also records the following clinical phenotypes, each already evidenced as
occurring in the disease:

Chronic Diarrhea; Abdominal Pain; Bloating; Constipation; Villous Atrophy; Weight Loss; Iron Deficiency Anemia; Fatigue; Growth Failure in Children; Dermatitis Herpetiformis; Reduced Bone Mineral Density; Dental Enamel Defects; Recurrent Aphthous Stomatitis; Peripheral Neuropathy; Cerebellar Ataxia; Elevated Hepatic Transaminases; Vitamin D Deficiency; Small intestinal lymphoma; Osteoporosis; Arthritis; Short stature; Female infertility

The core disease mechanism is already curated in depth and is NOT the subject of
this report. Treat it as established context and do not re-derive, re-survey, or
re-justify it:

Dietary gluten leads to TG2-mediated deamidation of gliadin peptides, which bind HLA-DQ2/DQ8 with high affinity and activate gluten-reactive CD4 T cells; the resulting mixed Th1/Th17/IL-21 cytokine response, together with IL-15-driven innate epithelial activation, licenses NKG2D/MICA-mediated intraepithelial lymphocyte cytotoxicity, producing villous atrophy and crypt hyperplasia, with anti-TG2 autoantibody production by B cells. Corroborated by the ZED1227 TG2-inhibitor randomized trial, HLA-DQ2 tetramer studies, and gluten-free-diet remission.

## Research Objective

The missing layer is the **causal wiring between the mechanism nodes and the
clinical phenotypes**: which pathophysiological process produces which clinical
manifestation, through what intermediates. For **each phenotype listed above**,
report:

1. **The mechanistic chain** from the established disease process to that
   phenotype, as an ordered sequence of steps, one per line, with explicit
   causal verbs ("leads to", "results in"). Start each chain from whichever of
   the existing mechanism nodes is the true proximal upstream step.
2. **Missing intermediate processes**: where the chain passes through a
   process that is NOT in the mechanism node list above (for example a
   malabsorption step, a distinct autoantibody specificity, a clonal expansion
   step), name it explicitly and flag it as a proposed new node.
3. **Primary human evidence** for each causal step: PMIDs with exact quotes
   from the abstracts. Prefer human clinical and interventional studies
   (dietary-withdrawal reversal counts as interventional evidence for a causal
   link). Distinguish evidence source types: human clinical, model organism,
   in vitro, computational.
4. **An evidence grade for the chain as a whole**, one of:
   - ESTABLISHED — causal chain demonstrated in humans, widely accepted
   - SUPPORTED — plausible chain with direct human evidence for most steps
   - PROPOSED — hypothesis in the literature, key steps not demonstrated
   - NOT_ESTABLISHED — the association is documented but no mechanistic chain
     has been demonstrated; competing explanations remain open
5. **Non-causal alternatives** where they are live: if the phenotype may be
   associated through shared genetic background (for example shared HLA
   haplotypes), coincident autoimmunity, or ascertainment rather than through
   downstream causation, say so explicitly.

**Honesty requirement:** "NOT_ESTABLISHED, mechanism unknown" is a correct and
valuable answer. Do NOT manufacture a mechanistic chain to satisfy the request.
A phenotype with no settled mechanism should be reported as exactly that, with
the competing hypotheses named and graded. It is expected that several
phenotypes in the list will end up NOT_ESTABLISHED.

## Priority Hubs

The following convergence hubs are anticipated to route several phenotypes and
must NOT be given shallow treatment. For each, report the full mechanistic
detail and per-branch citations:

(a) Nutrient malabsorption cascade: villous atrophy leads to reduced absorptive surface area and loss of brush-border transporters, producing deficiency of iron, folate, vitamin B12, vitamin D, calcium, zinc and fat-soluble vitamins, which in turn produce iron deficiency anemia, reduced bone mineral density and osteoporosis (also via secondary hyperparathyroidism), growth failure and short stature in children, weight loss, and fatigue. Detail which nutrient deficit drives which phenotype and where deficiency-independent (inflammatory, e.g. RANKL/OPG or cytokine-mediated) contributions are documented, especially for bone disease. (b) Extraintestinal autoimmunity by epitope spreading: anti-transglutaminase-3 (TG3) IgA and dermal IgA-TG3 deposits leading to dermatitis herpetiformis; anti-transglutaminase-6 (TG6) antibodies and cerebellar Purkinje cell injury leading to gluten ataxia; the disputed role of humoral versus T-cell mechanisms in gluten neuropathy. (c) Lymphomagenesis: chronic IL-15-driven activation and clonal expansion of intraepithelial lymphocytes leading to refractory celiac disease type II (aberrant clonal IELs, often with JAK1/STAT3 mutations) progressing to enteropathy-associated T-cell lymphoma, and the epidemiological protection conferred by gluten-free diet adherence.

## Output Format

- One subsection per phenotype, headed by the phenotype name exactly as listed
  above, containing: the numbered causal chain, the evidence grade, PMIDs with
  exact abstract quotes per step, and suggested ontology terms (GO for
  biological processes, CL for cell types, HP for the phenotype itself).
- A final section titled **Proposed New Mechanism Nodes** listing every
  intermediate process flagged in item 2, each with: a suggested node name, its
  upstream node (from the existing list or another proposed node), its
  downstream phenotypes, and the strongest single citation for its causal
  placement.
- A final section titled **Unwired Phenotypes** listing every phenotype graded
  NOT_ESTABLISHED, with one sentence each on what evidence would settle it.

## Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Include direct quotes from abstracts to support key statements
- Never cite a paper for a claim its abstract does not make

**Provider:** falcon
**Generated:** 2026-09-25T16:58:42.267757

1. montorohuguet2021smallandlarge pages 10-13
2. montorohuguet2021smallandlarge pages 24-25
3. barton2008celiacdiseaseand pages 14-16
4. patt2023unravelingtheimmunopathological pages 14-15
5. cording2022oncogeneticlandscapeof pages 1-1
6. kaunisto2022antibodyresponsesto pages 1-3
7. rouvroye2020theneuropathologyof pages 13-15
8. montorohuguet2021smallandlarge pages 22-24
9. merlotti2022bonefragilityin pages 5-7
10. patt2023unravelingtheimmunopathological pages 7-8
11. krupakozak2014pathologicbonealterations pages 4-5
12. altoma2022thedietaryand pages 2-4
13. lungaro2023osteoporosisandceliac pages 2-4
14. lauret2013celiacdiseaseand pages 6-7
15. chander2018pathogenesisofenteropathyassociated pages 1-2
16. botosso2023theroleof pages 6-8
17. hue2022cellularoriginsand pages 14-16
18. gracefarfaglia2015bonesofcontention pages 13-15
19. pelizzaro2021theriskof pages 2-4
20. stefano2013bonemassand pages 10-12
21. patt2023unravelingtheimmunopathological pages 5-7
22. Human clinical synthesis; DOI 10.3390/nu13041254; April 2021; PMID not exposed
23. Human clinical synthesis; DOI 10.3390/nu13041254
24. Primary human cross-sectional study; DOI 10.3390/nu5103975; September 2013; PMID not exposed
25. Human clinical review integrating intervention cohorts; DOI 10.3390/nu13051695; May 2021; PMID not exposed
26. Primary human prospective intervention-follow-up; DOI 10.3389/fmed.2023.1242512; September 2023; trial NCT01551563
27. Primary human case-control study; DOI 10.3390/children11091042; August 2024
28. Primary human serologic/tissue study; Sárdy et al.; DOI 10.1084/jem.20011299; March 2002
29. Human systematic review; DOI 10.3390/jcm13051382; February 2024
30. Primary human comparative study; DOI 10.17796/1053-4625-43.4.9; 2019
31. Systematic neuropathology review; DOI 10.3390/nu12030822; March 2020
32. Primary human retrospective intervention-follow-up; DOI 10.5114/ceh.2021.111003; December 2021
33. Primary human genomic study plus functional validation; DOI 10.1136/gutjnl-2020-322935; online 2021/issue 2022
34. Primary human retrospective cohort; DOI 10.1186/s12969-023-00822-x; May 2023
35. Mechanistic review incorporating in-vitro human cells and murine evidence; DOI 10.3390/antib12040079; December 2023
36. https://doi.org/10.3390/nu13041254
37. https://doi.org/10.3390/nu5103975
38. https://doi.org/10.3390/nu13051695
39. https://doi.org/10.3389/fmed.2023.1242512
40. https://doi.org/10.3390/children11091042
41. https://doi.org/10.1084/jem.20011299
42. https://doi.org/10.3390/jcm13051382
43. https://doi.org/10.17796/1053-4625-43.4.9
44. https://doi.org/10.3390/nu12030822
45. https://doi.org/10.5114/ceh.2021.111003
46. https://doi.org/10.1136/gutjnl-2020-322935
47. https://doi.org/10.1186/s12969-023-00822-x
48. https://doi.org/10.3390/antib12040079
49. https://doi.org/10.3390/nu13041254,
50. https://doi.org/10.3390/ijms23052713,
51. https://doi.org/10.3390/ijms242015482,
52. https://doi.org/10.3390/ijms23062910,
53. https://doi.org/10.1016/j.nut.2013.05.027,
54. https://doi.org/10.3390/nu14214554,
55. https://doi.org/10.3390/nu15051089,
56. https://doi.org/10.1155/2013/127589,
57. https://doi.org/10.3390/nu12030822,
58. https://doi.org/10.1016/j.gtc.2008.02.001,
59. https://doi.org/10.1136/gutjnl-2020-322935,
60. https://doi.org/10.1007/s11899-018-0459-5,
61. https://doi.org/10.5772/intechopen.110858,
62. https://doi.org/10.3390/cancers14102483,
63. https://doi.org/10.3390/nu7053347,
64. https://doi.org/10.3390/cancers13215288,
65. https://doi.org/10.3390/nu5114786,