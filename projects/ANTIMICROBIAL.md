# Antimicrobial Therapy: Drug–Bug Mechanism Design Pattern

## Status: Phase 1 — Strategy Note + 3 Modules + Conforming Entries

## 0. Scope and Positioning (what this is and is NOT)

This work is an **explanatory mechanism layer**, not a drug–indication database and
not a clinical decision support system (DSS):

- **Not duplicating drug-indication curation.** Other efforts already enumerate
  *which* drugs treat *which* conditions (drug labels, DrugBank, DrugCentral,
  ChEMBL indications, RxNorm/NDF-RT may-treat, DailyMed). dismech does not try to
  recapitulate that catalogue. Its contribution is to *explain* those
  associations mechanistically — linking a treatment, via `target_mechanisms`, to
  the specific pathophysiology node (drug target or gating principle) that makes
  it work, and to make that explanation queryable and consistency-checkable
  across diseases via shared modules.
- **Not a DSS — claims must stay moderated.** Antibiotic decision support already
  exists (institutional antibiograms/stewardship tools, IDSA guidelines, Sanford
  Guide, UpToDate, local empiric-therapy pathways, CLSI/EUCAST breakpoints). We
  should not position these modules as point-of-care prescribing guidance. At
  most this is a *mechanistic substrate* that such tools could cite or build on;
  the deliverable here is explanation and structured knowledge, not a
  recommendation engine.
- **Open question worth a short survey:** look at how existing DSSs and
  knowledge bases (DrugMechDB for mechanism paths; guideline/stewardship tools
  for drug–bug logic) represent this, to (a) borrow vocabulary and avoid
  reinventing, and (b) sharpen where the *mechanistic-explanation* niche is
  genuinely additive rather than overlapping. Tracked as a follow-up, not a
  blocker.

Recording the strategy for the treatment/action block of **bacterial infectious
disease** entries. The same pattern generalizes to antifungal, antiparasitic, and
antiviral therapy, but the worked examples here are antibacterial.

## 1. The Problem

Crudely, *any* broad-spectrum antibiotic is "good against any bacterial
infection," so the naive treatment block for every bacterial entry collapses to
a single generic edge: `Pharmacotherapy → some antibiotic → disease`. That throws
away the knowledge clinicians actually use: **particular mechanisms in particular
antibiotics are better (or useless) for particular diseases.** We want to encode
that depth.

## 2. The Core Principle: Target the Pathogen Mechanism Node, Not the Disease

dismech already has the machinery. A `Treatment` links to specific
pathophysiology nodes via `target_mechanisms` (`TreatmentMechanismTarget`,
schema). This is the same pattern as `immune_checkpoint_blockade` and
`fibrotic_response` — describe the same biology from both the disease side and
the treatment side, and connect them with a `target_mechanisms` edge.

For antibacterials, the edge should point at the **pathogen's druggable biology**,
which lives as pathophysiology nodes:

- **Leprosy** already does this for *adjunctive* therapy: corticosteroids →
  "Type 1 Delayed-Type Hypersensitivity Response"; thalidomide → "Immune-Complex
  Formation in Type 2 Reaction". The antibacterial agents (rifampicin, dapsone,
  clofazimine) currently lack `target_mechanisms` edges — that is the gap.
- **Lyme Disease** is the model for laying the substrate: it already treats
  pathogen biology as first-class pathophysiology nodes (Complement Evasion via
  BBK32, Antigenic Variation via vlsE, Host Lipid Scavenging and Membrane
  Biogenesis). The same entries should carry **drug-target nodes** (peptidoglycan
  synthesis, ribosomal translation, RNA polymerase, folate synthesis) that the
  antibiotic's `target_mechanisms` points at.

A single `target_mechanisms` edge encodes *why this drug*, not just *that this
drug* — and it predicts failure modes (a cell-wall-less organism has no PBP node,
so β-lactams have nothing to point at).

## 3. Three-Tier Encoding

**Tier 1 — crude baseline (already in use).**
`treatment_term: NCIT:C15986` (Pharmacotherapy) + `therapeutic_agent` (CHEBI for
the specific drug, e.g. `CHEBI:28077` rifampicin) + `therapeutic_modality:
SMALL_MOLECULE`. Says "rifampicin is used for leprosy."

**Tier 2 — the mechanistic edge (the depth).**
Add a pathophysiology node for the targeted bacterial process and link
`target_mechanisms` to it: rifampicin → "Bacterial DNA-dependent RNA Polymerase
(rpoB)"; dapsone → "Folate Synthesis (DHPS)"; a β-lactam → "Peptidoglycan
Transpeptidation (PBPs)". Use `target_phenotypes` for adjuncts (anti-inflammatory,
anti-toxin), as Leprosy already does.

**Tier 3 — conserved generalizations as modules.**
The reasons "some mechanisms are better for some diseases" are largely conserved
*pathogen-property × drug-class* interactions — exactly what `kb/modules/` +
`conforms_to` capture. Proposed modules:
- `bacterial_cell_wall_synthesis_inhibition`
- `bacterial_protein_synthesis_inhibition`
- `intracellular_pathogen_persistence` (lifestyle gating, not a drug target)

Disease nodes `conforms_to` these so a generalization ("β-lactams fail vs
cell-wall-less organisms") lives in one place and is queryable across diseases.

## 4. The Axes That Make Specific Drugs Better for Specific Diseases

Each row is a recurring reason drug choice deviates from "any broad-spectrum
agent." These are the determinants worth encoding as pathophysiology nodes or
agent properties.

| Determinant | Why it gates drug choice | dismech examples |
|---|---|---|
| **Intracellular lifestyle** | β-lactams penetrate cells poorly; macrolides/tetracyclines/fluoroquinolones/rifamycins accumulate intracellularly | Murine_Typhus (*Rickettsia*), Oroya_Fever (*Bartonella*) → doxycycline, **not** a β-lactam |
| **No peptidoglycan cell wall** | β-lactams have no target at all | *Mycoplasma* → macrolide/tetracycline |
| **Mycobacterial cell wall + slow growth + persisters** | mandates multidrug, long-course; specific targets (rpoB, mycolic acid, DHPS) | Leprosy → rifampicin + dapsone + clofazimine |
| **Toxin-mediated pathology** | add a protein-synthesis inhibitor (clindamycin/linezolid) to shut off toxin even when a β-lactam clears the organism — the "Eagle effect" at high inoculum | necrotizing strep/staph, diphtheria |
| **Bactericidal vs bacteriostatic + host/site** | immune-privileged or immune-impaired sites (endocarditis, meningitis, neutropenia) need cidal agents | qualify the treatment edge with a `modifier`/`role` |
| **Anaerobe / O₂-dependent uptake** | aminoglycosides need O₂-driven uptake → useless anaerobically; metronidazole needs anaerobic nitroreductase → *selective* for anaerobes | C. difficile, anaerobic abscess |
| **Tissue penetration (PK)** | CSF (ceftriaxone vs 1st-gen), urine-only (nitrofurantoin/fosfomycin), bone/prostate/biliary | site-specific `target_phenotypes` |
| **Biofilm / device / persisters** | rifampin adjunct for staph prosthetic-device infection; cell-wall agents tolerated in biofilm | add a biofilm pathophysiology node |
| **Synergy** | cell-wall agent + aminoglycoside in enterococcal endocarditis (wall disruption boosts aminoglycoside entry) | two treatments, each with its own mechanism node, plus a combination treatment |
| **Resistance mechanism** | MRSA PBP2a → vancomycin/ceftaroline; ESBL/carbapenemase → carbapenem/novel inhibitor | resistance as its own pathophysiology node the drug must overcome |

## 5. Recommended Encoding Pattern (per bacterial entry)

1. Populate `infectious_agent` (`InfectiousAgent`, NCBITaxon term) — the identity anchor.
2. In `pathophysiology`, add **drug-target nodes** (cell-wall synthesis, ribosome,
   gyrase/topo, RNA pol, folate) **and** **gating-property nodes** (intracellular
   survival, toxin production, biofilm, anaerobic metabolism) as appropriate.
3. Each `Treatment`: Tier-1 fields **plus** `target_mechanisms` → the specific
   node(s) it inhibits, and `target_phenotypes` for adjuncts.
4. Where the mechanism recurs, `conforms_to` a shared antibiotic-mechanism module.

## 6. Open Decision for the Register

Surface to `docs/explanation/design-decisions.md` before building: whether
drug–bug mechanism knowledge lives **per-disease** (treatments hang off the
`Disease`, consistent with current architecture — **recommended**) or whether
antibiotic classes deserve their own module/grouping objects that diseases
reference. The module route (Tier 3) gives both: disease-centric storage with a
conserved-mechanism layer, no new top-level class needed.

## 7. Next Steps

- [x] Draft a `bacterial_cell_wall_synthesis_inhibition` module as proof-of-concept.
      Built at `kb/modules/bacterial_cell_wall_synthesis_inhibition.yaml`: five
      nodes (precursor/lipid II synthesis → PBP cross-linking → bactericidal
      autolysis, plus acquired-resistance and intrinsic cell-wall-deficient
      gating branches). Schema + term validation pass; all evidence snippets are
      verified exact substrings of real abstracts (Typas 22203377, Sauvage
      18266856, Blair 25435309, Pereyre/Tardy 34680797, Kim 18302341). Key
      conformance/treatment target: `#Peptidoglycan Cross-Linking by
      Penicillin-Binding Proteins`.
- [x] Wire conforming entries end-to-end. Ten bacterial-disease entries now carry
      a drug-target pathophysiology node with `conforms_to` the module plus a
      treatment `target_mechanisms` edge to that node:
      - **β-lactam → PBP cross-linking node**: Lyme_Disease (amoxicillin,
        ceftriaxone), Scarlet_Fever (penicillin), Bejel + Pinta (benzylpenicillin),
        Whipple_Disease (ceftriaxone), Paratyphoid_Fever (ceftriaxone),
        Ludwigs_Angina (penicillin), Bacterial_meningitis (ceftriaxone).
      - **glycopeptide → lipid II / precursor node**: Clostridioides_difficile
        (oral vancomycin), Bacterial_meningitis (vancomycin, second node).
      - **acquired-resistance node**: Furunculosis models both the β-lactam target
        (oxacillin/MSSA) and the `Acquired Resistance and Drug Inactivation` node
        (PBP2a/MRSA → vancomycin substitution), the clearest drug-choice gating case.
      All ten pass schema + term validation.
- [ ] Deliberately **excluded** (primary therapy is not a cell-wall agent, so they
      do not conform to this module): Leptospirosis, Yaws (doxycycline/azithromycin
      first-line), Tetanus (metronidazole + antitoxin; β-lactam adjunct only),
      Oroya_Fever (intracellular Bartonella), Folliculitis (often topical/mixed).
      These are candidates for the future `intracellular_pathogen_persistence`
      and protein-synthesis-inhibitor modules instead.
- [x] Draft `bacterial_protein_synthesis_inhibition` module. Built at
      `kb/modules/bacterial_protein_synthesis_inhibition.yaml`: three nodes
      (ribosomal translation target → toxin/exoprotein-synthesis suppression →
      ribosomal target resistance). Evidence: Wilson 24336183 (ribosome target +
      resistance), Sawai 17101685 (clindamycin exoprotein suppression). Schema +
      term validation pass.
- [x] Draft `intracellular_pathogen_persistence` module (lifestyle-gating). Built
      at `kb/modules/intracellular_pathogen_persistence.yaml`: two nodes
      (intracellular niche / beta-lactam exclusion → cell-penetrant-drug
      requirement). Evidence: Maurin & Raoult 18611821, Pea 28639230. Schema +
      term validation pass.
- [x] Multi-module conformers wired: **Murine_Typhus** (doxycycline) and
      **Oroya_Fever** (chloramphenicol) each conform to BOTH the ribosome target
      (`#Bacterial mRNA Translation by the Ribosome`) and the intracellular gating
      node (`#Intracellular Niche and Beta-Lactam Exclusion`), demonstrating
      composition of a target-based module with a pharmacokinetic-gating module.
- [ ] Further ribosome conformers (doxycycline/macrolide first-line): Lyme_Disease,
      Leptospirosis, Yaws, Whipple_Disease (doxycycline alternative regimen),
      Scarlet_Fever (macrolide for penicillin allergy). Not yet wired.
- [ ] The `#Suppression of Toxin and Exoprotein Synthesis` node has no conformer
      yet — needs a toxin-mediated entry (necrotizing fasciitis / strep or staph
      toxic shock), which does not currently exist in `kb/disorders/`.
- [ ] Short survey of existing drug-mechanism KBs / DSSs (DrugMechDB, stewardship
      tooling) — see §0; borrow vocabulary, sharpen the explanatory niche.
- [ ] Record the per-disease-vs-module decision in the design register.
