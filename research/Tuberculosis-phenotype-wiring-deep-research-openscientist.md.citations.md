# Citations for Research Query

**Query:** # Mechanism-to-Phenotype Wiring Research Template

## Target Disease
- **Disease Name:** Tuberculosis
- **MONDO ID:** MONDO:0018076 (if available)

## Context: What Is Already Curated

This disease's knowledge base entry already models the following pathophysiology
mechanism nodes:

1. Phagocytosis of Mycobacterium tuberculosis by alveolar macrophages, with bacterial resistance to killing (CELLULAR); 2. Immune Evasion (phagosome maturation arrest, type I IFN subversion; CELLULAR); 3. GBP4-mediated autophagy-dependent restriction (host defence; CELLULAR); 4. Granuloma Formation (foamy macrophages, caseous necrosis; TISSUE); 5. Neutrophil Activation and NETosis (type I IFN-linked; CELLULAR); 6. Tissue Damage (granuloma necrosis, cavitation, lung parenchymal destruction and remodeling; TISSUE; currently wired only to Dyspnea and to drug resistance); 7. Drug Resistance Mechanisms; 8. Rv0191 MFS-mediated pyrazinamide efflux

It also records the following clinical phenotypes, each already evidenced as
occurring in the disease:

Chronic Cough; Fever; Night Sweats; Weight Loss; Hemoptysis; Chest Pain; Fatigue; Back Pain (spinal tuberculosis / Pott disease); Lymphadenopathy (tuberculous lymphadenitis). (Dyspnea is already wired from Tissue Damage and need not be covered.)

The core disease mechanism is already curated in depth and is NOT the subject of
this report. Treat it as established context and do not re-derive, re-survey, or
re-justify it:

Tuberculosis is infection with Mycobacterium tuberculosis acquired by inhalation; bacilli are taken up by alveolar macrophages, evade phagolysosomal killing, and drive granuloma formation; granuloma caseous necrosis and liquefaction lead to cavitation and lung tissue destruction. Do NOT re-survey host-pathogen immunology, granuloma biology, drug resistance or diagnostics. Treat this as given and concentrate on how it produces each listed clinical manifestation.

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

(a) CONSTITUTIONAL SYMPTOM HUB: whether fever, night sweats, weight loss/wasting and fatigue in TB are produced by a systemic inflammatory cytokine response (TNF, IL-1beta, IL-6, IFN-gamma; acute-phase response; leptin/appetite suppression, cachexia) - give human studies that measure these cytokines against symptoms or weight loss in TB patients, and say which links are demonstrated vs inferred. (b) CAVITY / AIRWAY HUB: how cavitation and endobronchial disease produce cough and hemoptysis (erosion of bronchial arteries, Rasmussen pseudoaneurysm of pulmonary artery branches in cavity walls, bronchiectasis), with primary human (angiographic, CT, autopsy) evidence. (c) EXTRAPULMONARY HUB: chest pain via pleural involvement (tuberculous pleuritis), lymphadenopathy via lymphatic spread and granulomatous inflammation of nodes, and back pain via haematogenous spread to vertebrae with spondylodiscitis and vertebral destruction - state the proposed new mechanism nodes these require.

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

**Provider:** openscientist
**Generated:** 2026-11-24T19:41:52.708305

1. PMID:42764468
2. PMID:9264292
3. PMID:9625384
4. PMID:27798613
5. PMID:40334195
6. PMID:36742561
7. PMID:34898509
8. PMID:42365784
9. PMID:40590271
10. PMID:34934475
11. PMID:42214607
12. PMID:32642186
13. PMID:32961891
14. PMID:42517191
15. PMID:41871964
16. PMID:30180300
17. PMID:38916387
18. PMID:40607012
19. PMID:22143887
20. PMID:19958757
21. PMID:18664365
22. PMID:35429606
23. PMID:42893161
24. PMID:43031973
25. PMID:42963813
26. PMID:8521296
27. PMID:38163944
28. PMID:16083502
29. PMID:43017321
30. PMID:43001309
31. PMID:42926821
32. PMID:36333017
33. PMID:8603261
34. PMID:23358528
35. PMID:11836317
36. PMID:14535627
37. PMID:42631029
38. PMID:42411357
39. PMID:42525594
40. PMID:42626526
41. PMID:42830033
42. PMID:42377159
43. PMID:42100439
44. PMID:26150911
45. PMID:34221154
46. PMID:35968962
47. PMID:33077054
48. PMID:43023121
49. PMID:33876222
50. PMID:26792471
51. PMID:26136467
52. PMID:29677205
53. PMID:35125696
54. PMID:35909258
55. PMID:31876844
56. PMID:41970748
57. PMID:42638134
58. PMID:42005151
59. PMID:42666708
60. PMID:42079494
61. PMID:42629577
62. PMID:32790739
63. PMID:39172563
64. PMID:29484929
65. PMID:40522188
66. PMID:42469982
67. PMID:22207528