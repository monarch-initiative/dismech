# Findings: Graphical Abstract Prompt-Engineering Pilot

## Subjects Tested

1. **Primary Module Pilot (5 prompt iterations)**:
   [`kb/modules/cgas_sting_pathway_activation.yaml`](../../../../kb/modules/cgas_sting_pathway_activation.yaml) — an intracellular DNA-sensing pathway with four subcellular compartments (`Cytosol` → `ER` → `COPII/COPI Vesicular Shuttle` → `Golgi` → `Nucleus`), three monogenic interferonopathy lesions (`TREX1/RNASEH2A` in AGS, `STING1` GOF in SAVI, `COPA` retrograde retrieval failure), pharmacologic agonists (`2'3'-cGAMP`, `MSA-2`), a non-canonical `PERK → eIF2α` translational arrest branch, and a 3-way signal-strength bifurcation (`APC maturation / Th1 & CD8+ antitumor immunity` vs `Constitutive type I IFN vasculopathy & lung fibrosis` vs `T-cell apoptosis & IL-35+ regulatory B-cell induction`).
2. **Transfer Module Pilot (Tissue/Multi-Organ Scale)**:
   [`kb/modules/fibrotic_response.yaml`](../../../../kb/modules/fibrotic_response.yaml) — a 5-stage cross-organ cascade (`Parenchymal Injury` → `Inflammatory Macrophage Recruitment` → `Resident Fibroblast to α-SMA+ Myofibroblast Transdifferentiation` → `Excessive Collagen I/III & TIMP ECM Deposition` → `Architectural Distortion` across Liver, Lung, Heart, and Kidney).
3. **Transfer Project Pilot (Multi-Organelle Hub + Disease Mapping)**:
   [`projects/MEMBRANE_CONTACT_SITES.md`](../../../../projects/MEMBRANE_CONTACT_SITES.md) & [`kb/modules/membrane_contact_site_dysfunction.yaml`](../../../../kb/modules/membrane_contact_site_dysfunction.yaml) — a radial organelle-interactome hub (`ER/SR` tethered at 10–30 nm without fusion to Mitochondria, Peroxisomes, Lipid Droplets, Golgi, Lysosomes, and Plasma Membrane) coupled to its downstream lipid/Ca²⁺ transfer, 6-organelle spectral signature, and neuronal/cardiac outcomes.

---

## Detailed Audit Across the 5 Prompt Iterations (`cgas_sting_pathway_activation`)

| Metric | Iter 1: Narrative (`narrative`) | Iter 2: 3-Col Storyboard (`storyboard`) | Iter 3: Subcellular Cutaway (`cutaway`) | Iter 4: Multi-Card Dismech DSL (`dismech-dsl`) | Iter 5: Hybrid Cutaway + Dismech DSL (`hybrid`) |
|---|---|---|---|---|---|
| **Spelling & Typography** | ❌ `"Eukaryotic Cell Pativation"` typo; random `ACCVCXCAGUGGGCGAC` sequence | ✅ 100% legible, zero typos | ✅ 100% legible, zero typos | ✅ 100% legible, zero typos | ✅ 100% legible, zero typos |
| **Chemical / Molecular Accuracy** | ❌ Hallucinated bicyclic sulfur ring for `2'3'-cGAMP`; wrong Breg cytokines (`IL-10, TGF-β` instead of `IL-35+`) | ✅ Schematic cyclic ring; accurate `IL-35+ Breg` | ✅ Schematic cyclic ring; accurate `IL-35+ Breg` | ✅ Schematic hexagon; accurate `IL-35+ Breg` | ✅ Schematic cyclic ring; accurate `IL-35+ Breg` |
| **Causal Arrow Polarity** | ❌ Inverted `dsDNA + cGAS -> TREX1/RNASEH2A Deficiency` arrow | ✅ Correct `TREX1/RNASEH2 Loss` red X blocking DNA clearance | ✅ Correct `TREX1 Loss` red X above `dsDNA` | ❌ Floating `TREX1` badge; inverted `Golgi ⊣ PERK` inhibitory T-bar | ✅ `TREX1` red T-bar on `dsDNA`; activating `ER-STING → PERK → p-eIF2α ⊣ Ribosome` |
| **Organelle Continuity** | ✅ Single ER, single Golgi, single Nucleus | ⚠️ Omitted Nucleus; no arrows connecting columns 1→2→3 | ✅ Continuous cell cutaway with plasma membrane secretion | ❌ Duplicated Golgi in both Zone 2 and Zone 3 cards | ✅ Single ER, COPII/COPI shuttle, single Golgi, single Nucleus across 3 tinted sub-zones |
| **Dismech Editorial Identity** | ❌ Generic textbook colors | ⚠️ Partial (header box only) | ❌ No module header or legend | ✅ Full `#00838f` header, category pills, scale tags, bottom legend | ✅ Full `#00838f` header, category pills, numbered sub-zones, bottom legend |

---

## Key Design Rules for Dismech Graphical Abstract Prompts

1. **Ban structural chemical formulas and raw nucleotide sequences explicitly.**
   Image models cannot render complex chemical structures (like `2'3'-cGAMP`) or valid gene sequences; instructing the model to use labeled schematic icons (`cyclic ring icon '2,3-cGAMP'`) and explicitly forbidding chemical formulas or letter sequences eliminates 100% of pseudo-chemistry hallucinations.
2. **Keep shared anatomical or cellular compartments inside a single container card.**
   When two pathophysiology nodes share a physical boundary (such as ER-to-Golgi trafficking and Golgi-to-Nucleus signaling inside one cell), splitting them into separate cards causes the image generator to draw duplicate organelles and misroute cross-card arrows. Using background tint bands (`SUB-ZONE 1`, `SUB-ZONE 2`, `SUB-ZONE 3`) inside a single continuous cell cutaway preserves both the node boundaries and the biological topology.
3. **Specify arrow polarity and endpoint symbols in the prompt text (`→` vs `⊣` vs `✕`).**
   Prose words like *"suppresses"*, *"loss of"*, or *"retrains"* frequently get drawn as forward activating arrows (`→`) or inverted T-bars (`⊣`). Writing the explicit symbol grammar (`'ER STING' -> solid activating arrow (→) to 'PERK → p-eIF2α', followed by a flat inhibitory T-bar (⊣) blocking 'Ribosome'`) and reinforcing it in a bottom Legend Bar locks the visual semantics.
4. **Give each distinct entity its own bullet in radial hubs.**
   In Pilot 3 v1 (`MEMBRANE_CONTACT_SITES`), grouping `"Lysosome / Plasma Membrane tethered via PDZD8 / XK–VPS13A"` into a single prompt line caused the model to attach `XK–VPS13A` (an ER–plasma membrane tether in McLeod syndrome) directly to the Lysosome. Splitting them into six explicit bullets in v2 resolved the mis-attachment.
