# DNT in vitro battery coverage of the dismech pathograph

How far the endpoints of the developmental neurotoxicity in vitro battery (DNT-IVB) reach into the dismech pathograph, counted by node, by entry, and by whether any model is linked to the node. The battery is a set of assays, each scoring one process in nervous-system development, assembled so a chemical can be screened against all of them at once. Its two generations are set out in Figure 1 of Tal et al., *New approach methods to assess developmental and adult neurotoxicity for regulatory use: a PARC work package 5 project*, Frontiers in Toxicology 2024;6:1359507, [doi:10.3389/ftox.2024.1359507](https://doi.org/10.3389/ftox.2024.1359507) (CC BY 4.0). That figure shows 20 boxes; neurite outgrowth, synaptogenesis and neural network formation appear in both versions, leaving **17 distinct processes**.

A name match is a **candidate**, never a mapping. dismech records no crosswalk to this battery, so a match says a node's name carries an endpoint's vocabulary. It does not say the node measures what the assay measures, at the same scale, in the same direction, or at the same life stage. Every figure below is an upper bound on what could be mapped.

`kb/disorders` and `kb/modules` as of commit `093f725c24`, read on **2026-10-02**. The counts move with every curation PR, so treat them as a dated snapshot and the script as the deliverable; regenerate with `just dnt-ivb-coverage`.

## How the match is made

Each endpoint owns a set of substring patterns, applied to `pathophysiology[].name` and `phenotypes[].name` across every disorder entry and mechanism module. Rows prone to collision carry a second filter requiring neural vocabulary somewhere in the node's name, GO labels, cell types or file stem, which is what keeps immunological memory out of *Learning and memory* and cancer cell migration out of *Cell migration*. Model and method properties are read from the `modeled_mechanisms` links that experimental, animal and computational models attach to a node.

Every node is emitted with a deep link to its own card on the published page. The page filename comes from the entry's `name`, not its file stem, and the two differ for roughly a sixth of the matched entries, so building a link from the stem produces pages that do not exist. `just dnt-ivb-coverage --check-anchors pages` re-checks both halves of every link, because a fragment matching no element on the page is a silent failure: the browser loads the page, stays at the top and reports no error. At this commit all 1,157 distinct links resolve to the node they name.

## Coverage

Assay substrate records what Figure 1's caption states. Blue boxes are human cells, yellow are rat primary cells, green are early life-stage zebrafish; the caption does not explain the remaining v2.0 box colours, so those are left unstated rather than guessed at.

| Endpoint | Battery | Assay substrate | Nodes | Model-linked | Entries |
|---|---|---|---:|---:|---:|
| NPC proliferation | v1.0 | human cells | 32 | 12 | 31 |
| NPC apoptosis | v1.0 | human cells | 14 | 4 | 14 |
| NP-neuronal differentiation | v1.0 | human cells | 58 | 17 | 57 |
| NP-glial differentiation | v1.0 | human cells | 13 | 3 | 13 |
| Neurite outgrowth | v1.0+v2.0 | human cells | 44 | 18 | 41 |
| Cell migration | v1.0 | human cells | 80 | 18 | 75 |
| Synaptogenesis | v1.0+v2.0 | rat primary cells | 37 | 10 | 35 |
| Neural network formation | v1.0+v2.0 | rat primary cells | 50 | 13 | 44 |
| Myelination | v2.0 | unstated | 271 | 27 | 179 |
| BBB function | v2.0 | unstated | 37 | 5 | 36 |
| Mitochondrial dysfunction | v2.0 | unstated | 132 | 29 | 95 |
| Motorneuron development | v2.0 | zebrafish | 137 | 22 | 92 |
| Learning and memory | v2.0 | zebrafish | 242 | 1 | 221 |
| Escape response | v2.0 | zebrafish | 2 | 0 | 2 |
| Anxiety-like behavior | v2.0 | zebrafish | 15 | 0 | 15 |
| Epigenetic markers | v2.0 | unstated | 16 | 0 | 16 |
| Sub-cellular morphology | v2.0 | unstated | 7 | 3 | 7 |

1,187 matched node rows over 1,157 distinct links. `--format tsv --table nodes` prints every one.

## What the counts show

**The network row skews to epilepsy.** Coverage is not the problem: neural network formation matches 50 nodes across 44 entries. The framing is. Thirty-one of those nodes describe hyperexcitability or hypersynchrony, and 24 of the 44 entries are epilepsies or developmental and epileptic encephalopathies, read out by EEG. Those describe a circuit that already exists and has gone wrong, not one being built. Nine nodes do describe network assembly or formation, and those are the genuine counterparts to the assay. Cockayne syndrome and PCDH19 clustering epilepsy carry the closest two.

**The v2.0 behavioural endpoints have no method attached.** Escape response, anxiety-like behavior and epigenetic markers return no model-linked node at all, and learning and memory returns one in 242. Most of these are phenotype entries rather than pathophysiology nodes: 197 of the 242 learning-and-memory matches and 14 of the 15 anxiety matches. They record the human clinical feature, which is the opposite end of the translational chain from a zebrafish larval assay, and nothing in dismech currently connects the two.

**Organ-on-chip is in the corpus but barely in this set.** dismech records 40 organ-on-chip models in total. Exactly one falls inside the matched set: the iPSC-derived neurovascular unit under Tuberous Sclerosis Complex, reached through BBB function. Microelectrode arrays appear in 21 files, nearly all cardiac or epilepsy rather than developmental.

## Known limits

**Lexical matching does not know what a node means.** The large rows are the least trustworthy. Myelination and learning and memory each sweep in entries where the word appears for an unrelated reason, and no filter here distinguishes a node that measures a process from one that merely names it.

**Both filters have been wrong, in both directions, three times so far.** The endpoint patterns are substring regexes, and `cognit` matched *re-cognit-ion*, pulling 23 pattern-recognition-receptor nodes into learning and memory before a negative lookbehind was added. The neural filter was then found to be discarding `nmda_receptor_hypofunction` > *Learning and Memory Impairment*, bound to GO `learning` and GO `memory` and the most on-point node in the corpus for that endpoint, because nothing in it says "neuro"; neurotransmitter vocabulary was added to fix it. The same filter was also admitting bare `progenitor`, which let 22 nodes through of which 21 were hematopoietic, intestinal crypt, osteoprogenitor or mesenchymal rather than neural; the word was removed and `microcephal` added to keep the one genuine entry. Each of the three was invisible in the output. `tests/test_dnt_ivb_coverage.py` pins all three, but assume more remain, and audit with `--format tsv --table nodes` rather than trusting the filtered counts.

**Node names are a dated snapshot, not stable identifiers.** A curation round that renames or splits a node breaks the link pointing at it, in the silent way described above. Re-run `--check-anchors` before relying on the links.

**One link failure `--check-anchors` cannot see.** Where two phenotypes on a page share a name, the renderer gives the second a `-2` suffix, and 21 phenotype names collide this way. The script claims anchors exactly as the renderer does so the links are right, but if that ever drifts the check would still pass: the id it looks for exists, on the wrong card. `tests/test_dnt_ivb_coverage.py` pins the suffix behaviour instead.
