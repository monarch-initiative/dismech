# Antimicrobial Therapy: Drug–Bug Mechanism Design Pattern

## Status: Phase 0 — Strategy / Design Note

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

- [ ] Draft a `bacterial_cell_wall_synthesis_inhibition` and/or
      `intracellular_pathogen_persistence` module as proof-of-concept.
- [ ] Retrofit one existing entry (Leprosy or Murine_Typhus) with Tier-2
      `target_mechanisms` edges to demonstrate the pattern end-to-end.
- [ ] Audit existing bacterial entries (Leprosy, Lyme_Disease, Murine_Typhus,
      Oroya_Fever, Paratyphoid_Fever, Ainhum) for the drug-target node gap.
- [ ] Record the per-disease-vs-module decision in the design register.
