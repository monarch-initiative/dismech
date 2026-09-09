# Lead (Pb) AOP Network: Shared Key Events, Consensus Nodes, and Network Unification

## Summary

Lead (Pb) is aggregated on AOP-Wiki stressor page 59 as a prototypical stressor for eight Adverse Outcome Pathways: **AOP 12, 499, 500, 552, 555, 556, 558, and 560**. The central question of this investigation was whether these eight AOPs share Key Events (KEs) and Key Event Relationships (KERs) that can be assembled into a coherent AOP network, and whether **consensus Key Event nodes** are needed in place of the fragmented, author-selected nodes that currently prevent the network from cohering.

The principal result is that **as authored, the eight Lead AOPs do not form a connected network.** Their union comprises 35 unique KEs and 36 unique KERs, but only 8 KEs and 4 KERs are reused by more than one AOP, and — critically — **every instance of reuse is strictly intra-organ.** There is zero Key Event and zero Key Event Relationship overlap between the neurodevelopmental cluster (AOPs 12, 499, 500) and the cardiac cluster (AOPs 552, 555, 556, 558, 560). Consequently, the authored union collapses into three disconnected weakly-connected components: a 14-KE neurodevelopmental cluster, a 17-KE cardiac contractility/electrophysiology cluster, and a 4-KE chronotropic/conduction branch (AOP 560).

The investigation identified three **literature-supported consensus Key Event nodes** that knit these disconnected components into a single connected network without violating the underlying biology. First, a directional **"increased intracellular Ca²⁺"** node that merges the synonymous author-chosen calcium KEs (KE1339 and KE389), justified by lead's ionic mimicry of calcium at calmodulin (Pb²⁺ binds with ~8-fold higher affinity than Ca²⁺). Second, a consensus **"cardiac arrhythmia"** node (KE1106) that receives the cluster's bespoke arrhythmic KEs (KE2283, KE1963), justified by an existing wiki KER. Third, an **oxidative-stress/ROS** node (KE1115/KE177) — conspicuously absent from all cardiac Lead AOPs despite lead being an established cardiac oxidant — wireable into the cardiac RyR2/Ca²⁺ arm. Applying these three consensus operations collapses the eight AOPs from three disconnected components into **one connected component of 34 KEs and 39 KERs**, revealing an asymmetric architecture: seven divergent Pb²⁺ ionic-mimicry/channel-blockade Molecular Initiating Events (MIEs) fan out, then mid- and late-pathway events reconverge on calcium dyshomeostasis and reactive oxygen species before diverging again to organ-specific adverse outcomes.

---

## Key Findings

### Finding 1 — The eight Lead AOPs form three disconnected sub-networks

Merging AOPs 12, 499, 500, 552, 555, 556, 558, and 560 yields **35 unique KEs and 36 unique KERs**. When rendered as a directed graph, the union does not form a single connected structure; it decomposes into three weakly-connected components:

| Component | Member AOPs | # KEs | Character |
|-----------|-------------|-------|-----------|
| Neurodevelopmental | 12, 499, 500 | 14 | Learning/memory, neurodegeneration |
| Cardiac contractility/electrophysiology | 552, 555, 556, 558 | 17 | QT prolongation, contractility, heart failure |
| Chronotropic/conduction | 560 | 4 | Funny-current, conduction, arrhythmia |

The only KEs shared by two or more AOPs (with the number of AOPs using each) are: **KE1535 Heart failure** (4 AOPs: 552, 555, 556, 558); **KE341 Impairment of learning & memory** (3 AOPs: 12, 499, 500); **KE352 Neurodegeneration** (2: 12, 500); **KE1339 Increase intracellular Ca²⁺** (2: 499, 500); **KE2146 MAPKK/ERK1/2 activation** (2: 499, 500); **KE1962 QT prolongation** (2: 552, 555); **KE1532 Decrease cardiac contractility** (2: 556, 558); and **KE389 Intracellular Ca²⁺ overload** (2: 556, 558). The shared KERs are 352→341, 2146→1339 (neuro) and 389→1532, 1532→1535 (cardiac).

{{figure:lead_aop_network.png|caption=Merged authored network of the eight Lead AOPs. Shared KEs are highlighted in orange and shared KERs in red. The graph visibly separates into distinct neurodevelopmental and cardiac clusters, with AOP 560 isolated.}}

### Finding 2 — Literal overlap is strictly intra-organ; consensus nodes are mandatory

Extending Finding 1, of the 35 unique KEs, **only 8 are reused by ≥2 AOPs and 27 (77%) appear in a single AOP.** Only 4 KERs are reused. Decisively, **every shared KE and KER lies within a single organ system.** On the cardiac side the shared nodes are KE1535, KE389, KE1532, and KE1962; on the neuro side they are KE341, KE1339, KE2146, and KE352. **Zero KEs and zero KERs bridge the neuro and cardiac clusters.** This is the structural reason the authored union has ≥3 disconnected components, and it establishes that connectivity between organ systems can only be achieved through consensus nodes — the AOPs share no literal connective tissue.

### Finding 3 — Redundant calcium KE nodes are the prime consensus candidate

Calcium dyshomeostasis is represented across the eight AOPs by at least **three distinct KE nodes** that describe the same underlying biology (Pb²⁺-driven perturbation of intracellular calcium) but do not merge in the graph:

| KE | Title | AOP(s) | Direction |
|----|-------|--------|-----------|
| KE52 | Decreased, Calcium influx | 12 | ↓ |
| KE1339 | Increase, intracellular calcium | 499, 500 | ↑ |
| KE389 | Increased, Intracellular Calcium overload | 556, 558 | ↑ |

Lead is a well-documented calcium mimic, so these author-chosen nodes fragment what is biologically one process. Literature directly supports Pb-induced calcium influx disruption as the mechanistic driver of cognitive/memory impairment ([PMID: 41486071](https://pubmed.ncbi.nlm.nih.gov/41486071/)): *"lead interferes with the synaptic pathways by inhibiting calcium influx, leading to cognitive impairments and memory issues."*

### Finding 4 — Ontology annotations objectively confirm three calcium KEs are one entity

Extracting AOP-Wiki structured `BiologicalEvent` annotations (`hasProcess`/`hasObject`/`hasAction`) for all 35 KEs provides objective, machine-readable confirmation. **KE389 "Ca²⁺ overload" and KE52 "Decreased Calcium influx" carry the IDENTICAL ontology pair** — process GO:0006816 (calcium ion transport) + object CHEBI:39124 (calcium ion) — differing only in the action term (increased vs decreased). **KE1339 "Increase, intracellular calcium"** targets the same ion (CHEBI:29108, calcium 2+) but under a different process ontology (VT:0010499). Thus three author-chosen KEs (52, 389, 1339) resolve to the same biological object — the calcium ion — under inconsistent process ontologies. This is direct, structured evidence that these nodes should be consolidated.

### Finding 5 — 15 of 35 KEs (mostly cardiac electrophysiology) lack any structured ontology annotation

Only 20 of the 35 KEs carry `hasProcess`/`hasObject` `BiologicalEvent` annotations. The 15 unannotated KEs are almost entirely the higher-ID cardiac events: 1321, 1529, 1532, 1961, 1962, 1963, 2281, 2283, 2287, 2288, 2289, 2290, 2291, 2292, plus MIE 201. By contrast, most neurodevelopmental KEs (188, 195, 341, 352, 381, 1115, 1262, 177, 2146, 2151) are fully annotated with GO/CHEBI/PR/MP terms. This annotation gap makes automated cross-organ node matching harder precisely where consensus bridges are most needed, and represents a curation priority.

### Finding 6 — KE389 is the community-consensus calcium node by wiki-wide reuse

Wiki-wide reuse counts (number of AOPs using each KE) reveal a clear community preference for a single calcium node: **KE389 "Increased, Intracellular Calcium overload" is used in 7 AOPs — the most-reused calcium KE in the entire AOP-Wiki.** KE1339 is used in 4 AOPs, and KE52 in only 2. Among 13 calcium-related KEs wiki-wide, KE389 ranks #1 by reuse. Combined with the identical ontology annotation shared with KE52 (Finding 4), KE389 is the natural consensus target onto which the synonymous calcium nodes should consolidate.

### Finding 7 — A single consensus calcium node reconnects the network (3 → 2 components)

Relabelling the synonymous calcium KEs onto the consensus node — **with no added edges** — reduces the merged network from three weakly-connected components to two. A single 29-node component now contains **all of the neurodevelopmental AND cardiac contractility/electrophysiology events**, leaving only AOP 560 (the 4-node chronotropic branch) isolated. The consensus calcium node becomes a genuine cross-organ hub: its predecessors span both organ systems (KE195 NMDAR inhibition, KE2146 MAPKK/ERK from neuro; KE2287 Na-Ca exchange, KE2289 RyR2 hyperphosphorylation from cardiac), and its successors likewise span both (KE177 mitochondrial dysfunction, KE381 reduced BDNF, KE1262 apoptosis, KE2151 neurotransmitter release on the neuro side; KE1532 decreased cardiac contractility on the cardiac side).

{{figure:lead_aop_consensus_network.png|caption=Side-by-side comparison of the fragmented authored network (3 components) versus the consensus-unified network after merging synonymous calcium nodes and adding the arrhythmia node. The consensus calcium node acts as a cross-organ hub connecting neurodevelopmental and cardiac events.}}

### Finding 8 — A consensus arrhythmia node plus the calcium node fully unifies all 8 AOPs

The last isolated fragment (AOP 560) is joined by adding a consensus **cardiac arrhythmia node (KE1106)**. A wiki-wide KER query shows KE1106 is reached from KE2285 "delayed/early afterdepolarizations," KE2280 "delay in electrical conduction," KE2292 "Altered Cardiac Electrical Conduction," and KE1098 "blood potassium," and leads on to KE351 mortality. The cardiac cluster uses near-synonymous bespoke nodes — KE2283 "early premature depolarizations" (≈ KE2285) and KE1963 "Torsades de Pointes"/KE2281 "uncoordinated contraction" (arrhythmic manifestations) — while AOP 560 already terminates in KE1106 via KE2292. Adding consensus edges **KE2283 → KE1106** and **KE1963 → KE1106** (both justified by the existing wiki KER KE2285 → KE1106), on top of the calcium merge, collapses the network from 2 components to **1 single 33-node component** in which the learning-and-memory adverse outcome (KE341) and the cardiac arrhythmia adverse outcome (KE1106) reside in the same connected component.

### Finding 9 — The neuro NMDAR calcium arm is directionally OPPOSITE the cardiac overload arm

A crucial biological nuance: the three calcium KEs are not all directionally concordant. KE52 "Decreased, Calcium influx" (AOP 12, downstream of KE195 NMDAR inhibition) describes **reduced** calcium influx, whereas KE1339 and KE389 both describe **increased** intracellular calcium. Therefore the defensible merge is **KE1339 → KE389** (an "increased intracellular Ca²⁺" node), keeping the opposite-sign KE52 distinct. This nuance reflects real dual biology: lead both blocks NMDAR-mediated Ca²⁺ entry (reducing influx in the developing synapse) and drives cytosolic Ca²⁺ overload elsewhere. The unifying molecular rationale is ionic mimicry at the calcium sensor: Pb²⁺ binds calmodulin with **~8-fold higher affinity than Ca²⁺** in the N-terminal domain ([PMID: 23692958](https://pubmed.ncbi.nlm.nih.gov/23692958/): *"Ca(2+) binding proteins such as calmodulin (CaM) are often reported to be molecular targets for Pb(2+)-binding and lead toxicity"* and *"Pb(2+) binds with 8-fold higher affinity than Ca(2+) in the N-terminal domain"*), making perturbed Ca²⁺/calmodulin signalling a plausible shared molecular target across organs regardless of the direction of the flux change.

### Finding 10 — Literature supports adding an oxidative-stress/ROS consensus node to the cardiac AOPs

Within the eight Lead AOPs, the ROS/mitochondrial module — **KE1115 ROS, KE177 mitochondrial dysfunction, KE1262 apoptosis** — appears ONLY in the neurodevelopmental cluster (AOP 500). None of the four cardiac AOPs (552, 555, 556, 558) nor AOP 560 contain a ROS/mitochondrial KE, even though **KE1115 (ROS) is the single most-reused KE across the entire AOP-Wiki (63 AOPs)**, KE177 is used in 43, KE55 in 29, and KE1262 in 21. This is a striking omission, because lead is a well-established systemic pro-oxidant. Lead exposure increases ROS/RNS production via δ-aminolevulinic acid (ALA) auto-oxidation and xanthine oxidase upregulation while inhibiting antioxidant enzymes ([PMID: 37495800](https://pubmed.ncbi.nlm.nih.gov/37495800/): *"Pb-exposure increases reactive oxygen/nitrogen species (ROS/RNS) production by δ-aminolevulinic acid auto-oxidation, xanthine dehydrogenase, and xanthine oxidase upregulation"* and *"Pb exposure also inhibits antioxidant enzymes, potentiating ROS/NOS levels and reactive cell damage"*), and increases lipid peroxidation and H₂O₂ dose-dependently ([PMID: 21858511](https://pubmed.ncbi.nlm.nih.gov/21858511/): *"Lipid peroxidation and hydrogen peroxide concentration both in roots and leaves increased with increasing Pb levels"*). An oxidative-stress consensus node is therefore biologically justified as a bridge into the cardiac AOPs that currently omit it.

### Finding 11 — A ROS → RyR2/CaMKII → Ca²⁺-leak edge wires oxidative stress into the cardiac calcium arm

The consensus ROS node is not merely appended; there is a direct mechanistic route by which it feeds the cardiac calcium arm. The cardiac AOPs 556/558 route through **KE2289 "RyR2 hyperphosphorylation"** and **KE2287 "Impaired Na-Ca exchange"** to KE389 "Ca²⁺ overload." Literature provides an oxidative mechanism for exactly this step: mitochondrial ROS enhances SR Ca²⁺-release-channel (RyR2) oxidation and activity, and RyR2 Ca²⁺ leak itself further drives mito-ROS in a feed-forward loop ([PMID: 32444920](https://pubmed.ncbi.nlm.nih.gov/32444920/): *"Cardiac disease is associated with deleterious emission of mitochondrial reactive oxygen species (mito-ROS), as well as enhanced oxidation and activity of the sarcoplasmic reticulum"*). ROS-driven oxidation of PKA and CaMKII increases RyR2 phosphorylation and diastolic Ca²⁺ leak, and reducing ROS reduces RyR2 phosphorylation ([PMID: 38198753](https://pubmed.ncbi.nlm.nih.gov/38198753/): *"reducing ryanodine receptor 2 (RyR2) phosphorylation to decrease diastolic Ca²⁺"*). Combined with lead's established pro-oxidant action, this supports a consensus edge **ROS (KE1115)/mitochondrial dysfunction (KE177) → RyR2 hyperphosphorylation (KE2289)/Ca²⁺ overload (KE389)** — a second cross-organ bridge complementing the calcium hub.

### Finding 12 — Seven divergent, non-overlapping Molecular Initiating Events form an "ionic-mimicry MIE cluster"

Querying `aopo:has_molecular_initiating_event` returns **7 distinct MIEs** across the 8 AOPs (only KE2146 is shared, by AOPs 499+500):

| MIE (KE) | Title | AOP |
|----------|-------|-----|
| KE201 | NMDAR antagonist binding | 12 |
| KE2146 | MEK/ERK activation | 499, 500 |
| KE1529 | L-type Ca²⁺ channel blockade | 552 |
| KE593 | ERG K⁺ channel inhibition | 555 |
| KE1562 | Decreased Na/K-ATPase activity | 556 |
| KE2288 | Phosphodiesterase inhibition | 558 |
| KE2290 | Funny-current (I_f) inhibition | 560 |

Four of these act directly on cation-handling membrane proteins where lead is a documented ligand: Pb is *"a potent blocker of calcium channel"* and blocks L-type Ca²⁺ channels ([PMID: 29939358](https://pubmed.ncbi.nlm.nih.gov/29939358/)), antagonizes NMDARs, and inhibits Na/K-ATPase. The adverse outcomes are convergent by organ (neuro: KE341 learning/memory in AOPs 12, 499, 500; cardiac: KE1535 heart failure in 552, 555, 556, 558; KE1106 arrhythmia in 560), but **the MIEs are divergent** — supporting the notion of a consensus MIE *cluster* ("Pb²⁺ substitution/blockade at cation-handling membrane proteins") rather than a single consensus MIE node.

### Finding 13 — Deliverable: three consensus nodes collapse 8 disconnected AOPs into one 34-KE network

Integrating all findings, three literature-supported consensus operations unify the set into a single connected component (34 KEs, 39 KERs):

- **(A)** Merge KE1339 → KE389 as a directional "increased intracellular Ca²⁺" node (Pb²⁺/calmodulin mimicry, ~8× Ca²⁺ affinity), keeping the opposite-sign KE52 "decreased Ca²⁺ influx" distinct.
- **(B)** Consensus "cardiac arrhythmia" node KE1106 receiving KE2283 and KE1963 (justified by wiki KER KE2285 → KE1106).
- **(C)** Oxidative-stress node KE1115/KE177 wired via ROS → RyR2 (KE2289) → Ca²⁺ overload (KE389), filling the gap where no cardiac Lead AOP contains a ROS KE.

The resulting architecture is asymmetric: 7 divergent MIEs fan out; mid/late KEs reconverge on calcium and ROS before organ-specific adverse outcomes (KE341 learning/memory, KE1535 heart failure, KE1106 arrhythmia).

{{figure:lead_aop_final_consensus_network.png|caption=Definitive full-consensus Lead AOP network. Seven divergent ionic-mimicry/channel-blockade MIEs (left) fan out, reconverge on the calcium and ROS consensus hubs (center), and diverge to organ-specific adverse outcomes (right). Calcium, arrhythmia, and ROS consensus edges are highlighted.}}

---

## Mechanistic Model / Interpretation

The eight Lead AOPs, when unified through consensus nodes, describe a coherent **"divergent-initiation, convergent-core, divergent-outcome"** toxicological architecture. The unifying biological principle is lead's **ionic mimicry of divalent cations**, particularly calcium, which allows a single stressor to perturb many cation-handling proteins and converge on a small number of downstream disturbances.

```
   MOLECULAR INITIATING EVENTS            CONVERGENT CORE              ADVERSE OUTCOMES
   (7 divergent, ionic mimicry)        (consensus hubs)            (organ-specific)

   KE201  NMDAR antagonism  ──┐
                             ├─► [KE52 ↓Ca influx]───► synaptic ──► KE341 Learning/
   KE2146 MEK/ERK  ──────────┘                          deficit      memory impairment
                                                                     (AOPs 12,499,500)
   KE2146 MEK/ERK  ──────────► [Ca²⁺ ↑ CONSENSUS]◄─┐
                                KE1339 ⇒ KE389      │
                                   │                │
   KE1529 L-type Ca block ──┐      ▼                │
   KE593  ERG K⁺ block ─────┤   mito dysfunction    │
   KE1562 Na/K-ATPase ↓ ────┤   KE177 / apoptosis   │
   KE2288 PDE inhibition ───┤      ▲                │
                            │      │                │
                            └─► [ROS CONSENSUS]─────┘  ──► KE1532 ↓contractility
                                KE1115 / KE177           ──► KE1535 Heart failure
                                   │  ROS→RyR2(KE2289)       (AOPs 552,555,556,558)
                                   ▼  →Ca overload
   KE2290 Funny-current ─────► [ARRHYTHMIA CONSENSUS]──► KE1106 Cardiac arrhythmia
                                KE1106 ◄ KE2283,KE1963        (AOP 560 + cardiac)
```

The model has three tiers:

1. **Divergent initiation.** Lead does not have one molecular target; it has many. Seven distinct MIEs — NMDAR antagonism, L-type Ca²⁺ channel blockade, ERG K⁺ channel inhibition, Na/K-ATPase inhibition, phosphodiesterase inhibition, funny-current inhibition, and MEK/ERK activation — reflect lead's promiscuous binding to cation-handling and signalling proteins. This promiscuity is the toxicological signature of an ionic mimic.

2. **Convergent core.** Despite the divergent starts, the pathways reconverge on **calcium dyshomeostasis** and **oxidative stress**. Calcium is the biological pivot: Pb²⁺ binds calmodulin with ~8-fold higher affinity than Ca²⁺, so perturbed Ca²⁺/calmodulin signalling is a shared molecular consequence across organs. Oxidative stress is the second pivot: lead generates ROS through δ-ALA auto-oxidation and antioxidant enzyme inhibition, and ROS feeds back onto RyR2/CaMKII to worsen calcium leak. Notably, this convergent core is only partially represented in the authored AOPs — the calcium node is fragmented into three synonyms, and the ROS node is entirely absent from the cardiac AOPs. The consensus nodes make the convergence explicit.

3. **Divergent outcome.** From the shared core, the network diverges again to organ-specific adverse outcomes: learning and memory impairment (neuro), heart failure via decreased contractility (cardiac contractility), and cardiac arrhythmia (cardiac electrophysiology).

The bidirectional calcium biology (Finding 9) is a genuine subtlety worth preserving rather than papering over. In the developing neuron, lead's NMDAR antagonism **reduces** activity-dependent Ca²⁺ influx (KE52), impairing the calcium signalling needed for synaptic plasticity and BDNF/CREB-dependent learning. In the cardiomyocyte, lead drives cytosolic and SR Ca²⁺ **overload** (KE389) via impaired Na-Ca exchange and RyR2 hyperphosphorylation. Both are "calcium dysregulation," and both trace to Pb²⁺/calmodulin mimicry, but they are directionally opposite. The recommended consensus therefore merges only the concordant nodes (KE1339 → KE389) and keeps KE52 as a distinct, oppositely-signed node — a network that is both connected and biologically faithful.

---

## Evidence Base

| PMID | Title (abbreviated) | Role in this investigation |
|------|--------------------|---------------------------|
| [41486071](https://pubmed.ncbi.nlm.nih.gov/41486071/) | Lead-induced neurotoxic effects on synaptic signalling & ASD | Supports Pb inhibition of calcium influx as driver of cognitive/memory impairment (Finding 3) |
| [23692958](https://pubmed.ncbi.nlm.nih.gov/23692958/) | Metal toxicity and opportunistic binding of Pb²⁺ in proteins | Establishes calmodulin as a shared Pb²⁺ target; quantifies ~8× Ca²⁺ affinity — the molecular rationale for the calcium consensus node (Finding 9) |
| [37495800](https://pubmed.ncbi.nlm.nih.gov/37495800/) | Plant extracts on hepatic redox metabolism upon lead exposure | Documents Pb ROS-generation routes (δ-ALA auto-oxidation, xanthine oxidase) and antioxidant inhibition (Findings 10, 11) |
| [21858511](https://pubmed.ncbi.nlm.nih.gov/21858511/) | Effects of lead on physiological responses of *Pluchea sagittalis* | Dose-dependent Pb-induced lipid peroxidation and H₂O₂ (Finding 10) |
| [32444920](https://pubmed.ncbi.nlm.nih.gov/32444920/) | Increased RyR2 activity exacerbated by Ca leak-induced mito-ROS | Mito-ROS enhances SR/RyR2 oxidation and activity — mechanistic basis for ROS→RyR2 edge (Finding 11) |
| [38198753](https://pubmed.ncbi.nlm.nih.gov/38198753/) | Cardiac MAO-A inhibition protects via diastolic calcium control | ROS/CaMKII-PKA → RyR2 phosphorylation → diastolic Ca²⁺ leak is causal (Finding 11) |
| [29939358](https://pubmed.ncbi.nlm.nih.gov/29939358/) | Pb exposure and AMPA receptor surface trafficking | Documents lead as a potent calcium-channel blocker (Finding 12) |
| [42001927](https://pubmed.ncbi.nlm.nih.gov/42001927/) | Metal exposure in heart disease | Confirms lead promotes oxidative stress and mitochondrial injury in the cardiovascular system (Finding 10 support) |

The literature base is strongly convergent on two points central to the proposed consensus nodes: (1) lead's mechanism is fundamentally **ionic mimicry of calcium**, which unifies its otherwise disparate molecular targets, and (2) lead is a **systemic pro-oxidant**, which justifies inserting an oxidative-stress node into pathways (the cardiac ones) that omit it. No retrieved paper contradicted the consensus-node proposal; the RyR2/ROS papers ([PMID: 32444920](https://pubmed.ncbi.nlm.nih.gov/32444920/), [PMID: 38198753](https://pubmed.ncbi.nlm.nih.gov/38198753/)) were not lead-specific but establish the general cardiomyocyte mechanism that lead's pro-oxidant action would engage.

---

## Limitations and Knowledge Gaps

1. **Annotation incompleteness.** 15 of 35 KEs — almost all cardiac electrophysiology events — lack structured `BiologicalEvent` (GO/CHEBI/PR/MP) annotations (Finding 5). Consensus-node matching for the cardiac cluster therefore relied more on KE titles and expert reasoning than on machine-readable ontology terms, introducing subjectivity. Curating these annotations is a prerequisite for fully automated network assembly.

2. **The ROS consensus node is inferential for the cardiac AOPs.** No cardiac Lead AOP currently contains a ROS or mitochondrial KE. The proposed insertion rests on general cardiomyocyte biology plus lead's known pro-oxidant action, not on a Pb-specific, cardiac-tissue empirical KER. The mechanistic RyR2/ROS papers are not lead-specific.

3. **Directional heterogeneity of calcium.** The neuro NMDAR arm (decreased Ca²⁺ influx, KE52) is directionally opposite the cardiac overload arm (KE389). This was handled by keeping KE52 distinct, but it means "calcium dysregulation" is not a single monotonic node — a caveat for any downstream quantitative AOP modelling.

4. **Weight-of-evidence not assessed.** This analysis addressed network topology and node identity, not the empirical support (essentiality, biological plausibility, dose-response concordance) for individual KERs. Some author-selected KERs may be better supported than the proposed consensus edges.

5. **No quantitative dose-response integration.** The unified network is qualitative. Lead's dual, dose-dependent effects on calcium (block vs overload) likely depend on exposure level, developmental stage, and tissue — dimensions not captured here.

6. **Stressor breadth of consensus KEs.** KE389 and KE1115 are used across dozens of non-lead AOPs. Their strength as consensus hubs is also a caveat: they are generic stress nodes, so their presence does not by itself establish lead-specificity of the pathway.

---

## Proposed Follow-up Experiments / Actions

1. **Submit consensus-node curation proposals to AOP-Wiki.** Concretely: (a) consolidate KE1339 onto KE389 as a directional "increased intracellular Ca²⁺" node, retaining KE52 as a distinct decreased-influx node; (b) add KERs KE2283 → KE1106 and KE1963 → KE1106 to route bespoke arrhythmic nodes into the consensus arrhythmia node; (c) propose insertion of an oxidative-stress KE (KE1115) and RyR2 edge (KE1115/KE177 → KE2289 → KE389) into cardiac AOPs 556/558.

2. **Complete ontology annotation of the 15 unannotated cardiac KEs** with GO/CHEBI/PR/MP terms, enabling automated cross-organ node matching and reproducible network assembly.

3. **Empirically test the ROS → cardiac Ca²⁺ arm under lead.** Measure, in lead-exposed cardiomyocytes, whether antioxidant co-treatment reduces RyR2 phosphorylation, diastolic Ca²⁺ leak, and contractile dysfunction — validating the proposed ROS consensus edge specifically for lead.

4. **Dose-response mapping of lead's bidirectional calcium effect.** Determine the exposure thresholds at which lead transitions from NMDAR-mediated Ca²⁺-influx blockade (neuro) to Ca²⁺ overload (cardiac), to quantitatively parameterize the divergent calcium nodes.

5. **Extend the consensus-node approach to other metal stressors.** Because ionic mimicry and oxidative stress are shared by cadmium, arsenic, and mercury, test whether the same three consensus hubs (calcium, ROS, arrhythmia) unify those stressors' AOP sets — aligning with the user's broader AOP-network program.

6. **Weight-of-evidence evaluation** of the proposed consensus KERs versus the author-selected KERs, using the OECD tailored Bradford-Hill criteria, before formal adoption.

---

## Supported and Refuted Hypotheses

**Supported**
- The Lead AOPs share KEs only *within* organ systems and are disconnected across organs (Findings 1, 2). ✔
- A directional "increased intracellular Ca²⁺" consensus node bridges neuro ↔ cardiac (Findings 3, 4, 6, 7, 9). ✔
- A consensus arrhythmia node (KE1106) unifies the cardiac cluster's bespoke arrhythmic KEs (Finding 8). ✔
- An oxidative-stress consensus node is biologically warranted and mechanistically insertable into the cardiac arm (Findings 10, 11). ✔
- Lead's MIEs are divergent (ionic-mimicry/channel-blockade), outcomes convergent (Finding 12). ✔

**Refuted / qualified**
- "All calcium KEs can be merged into one node." **Refuted** — KE52 (decreased influx) is directionally opposite to KE389/KE1339 (increased); only same-direction KEs may merge (Finding 9).
- "A single consensus MIE unifies the set." **Refuted** — 7 distinct MIEs; at best a consensus MIE *cluster* (cation-handling membrane proteins), not one node (Finding 12).

---

## Conclusion

As authored, the eight Lead AOPs (12, 499, 500, 552, 555, 556, 558, 560) do **not** form a connected AOP network: their 35 KEs and 36 KERs share only 8 KEs and 4 KERs, all strictly intra-organ, producing three disconnected components. The shared Key Events that do exist are KE1535 (Heart failure), KE341 (Learning/memory impairment), KE352 (Neurodegeneration), KE1339 and KE389 (calcium), KE2146 (MEK/ERK), KE1962 (QT prolongation), and KE1532 (Decreased contractility); shared KERs are 352→341, 2146→1339, 389→1532, and 1532→1535. Three literature-supported consensus nodes — a directional "increased intracellular Ca²⁺" node (KE1339+KE389; Pb²⁺/calmodulin ionic mimicry), a "cardiac arrhythmia" node (KE1106), and an "oxidative-stress/ROS" node (KE1115/KE177) — collapse the eight AOPs into a single connected component of 34 KEs, revealing a divergent-initiation (7 ionic-mimicry MIEs), convergent-core (calcium + ROS), divergent-outcome architecture.

---

*Analysis performed against the live AOP-Wiki SPARQL endpoint; 14 findings recorded across 10 iterations; 36 literature abstracts reviewed.*
