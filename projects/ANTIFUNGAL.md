---
title: 'Antifungal Therapy: Drug–Fungus Mechanism Design Pattern'
status: PLANNED
description: 'Extends the antimicrobial drug–bug mechanism layer to antifungal therapy: ergosterol-synthesis (azoles/allylamines), membrane-ergosterol-binding (polyenes), cell-wall glucan-synthesis (echinocandins), and antimetabolite (flucytosine) target modules, plus intrinsic-resistance and CNS-penetration gating axes.'
diseases:
- Chromoblastomycosis
- Coccidioidomycosis
- Mycetoma
- Otomycosis
---

# Antifungal Therapy: Drug–Fungus Mechanism Design Pattern

## Status: Phase 0 — Strategy / Module Set Proposed

This project extends the [`ANTIMICROBIAL`](ANTIMICROBIAL.md) drug–bug mechanism
design pattern to **antifungal therapy**. Same machinery — a `Treatment` links
via `target_mechanisms` to the specific pathophysiology node (a fungal
biosynthetic target or a gating principle) that makes the drug work, and
recurrent *fungus-property × drug-class* interactions are captured once as
`kb/modules/` that disease entries `conforms_to`. **No antifungal modules exist
yet**; the worked examples below build on existing fungal entries
(Otomycosis, Coccidioidomycosis, Chromoblastomycosis, Mycetoma).

Antifungal pharmacology has a tighter, more conserved target set than antivirals
because fungi are eukaryotes — selective toxicity hinges on a handful of
fungal-specific structures (ergosterol instead of cholesterol; a β-1,3-glucan
cell wall mammalian cells lack).

| Proposed module | Target / principle | Drug classes | Candidate conformers (existing entries) |
|---|---|---|---|
| `fungal_ergosterol_synthesis_inhibition` | Ergosterol biosynthesis: lanosterol 14α-demethylase (CYP51/ERG11, azole target) and squalene epoxidase (ERG1, allylamine target) | triazoles, imidazoles, allylamines | Otomycosis (clotrimazole, fluconazole), Coccidioidomycosis (fluconazole/itraconazole), Chromoblastomycosis (itraconazole/terbinafine), Mycetoma (itraconazole) |
| `fungal_membrane_ergosterol_binding` | Direct ergosterol binding → membrane pore / oxidative damage | polyenes | Coccidioidomycosis (amphotericin B for severe/disseminated), Mycetoma |
| `fungal_cell_wall_glucan_synthesis_inhibition` | β-1,3-glucan synthase (FKS1) — fungal-specific wall target, cleanest selectivity story | echinocandins | (candidemia/invasive candidiasis entry needed — see Next Steps) |
| `fungal_nucleic_acid_antimetabolite` | Intracellular conversion to 5-FU by fungal cytosine deaminase → DNA/RNA synthesis disruption (mammals lack the enzyme → selectivity) | flucytosine | (cryptococcal meningitis entry needed — AmB + flucytosine induction) |
| `antifungal_intrinsic_resistance_gating` | **Gating, not a drug target.** Species-level target absence/insensitivity excludes whole drug classes | (explains why empiric choice depends on organism ID) | Otomycosis (Aspergillus is intrinsically fluconazole-resistant) |

**Multi-module conformers** (the payoff — one disease constrained by several
independent antifungal mechanisms, mirroring Leprosy/Whipple on the
antibacterial side):
- **Cryptococcal meningitis** (entry to be created): ergosterol binding
  (`fungal_membrane_ergosterol_binding`, amphotericin B) + antimetabolite
  (`fungal_nucleic_acid_antimetabolite`, flucytosine) for induction, then
  azole (`fungal_ergosterol_synthesis_inhibition`, fluconazole) consolidation —
  **and** `antifungal_intrinsic_resistance_gating` because *Cryptococcus* is
  intrinsically echinocandin-resistant (β-glucan synthase is present but not a
  viable target), explaining why the cell-wall module does **not** apply.
- **Invasive candidiasis** (entry to be created): echinocandin
  (`fungal_cell_wall_glucan_synthesis_inhibition`) first-line vs azole
  (`fungal_ergosterol_synthesis_inhibition`) step-down, gated by *Candida*
  species / *C. auris* resistance.

## 0. Scope and Positioning (what this is and is NOT)

This is an **explanatory mechanism layer**, not a drug–indication database and
not a clinical decision support system (DSS). Identical positioning to
[`ANTIMICROBIAL`](ANTIMICROBIAL.md) §0:

- **Not duplicating drug-indication curation.** DrugBank, DrugCentral, ChEMBL,
  and antifungal labels already enumerate *which* antifungals treat *which*
  mycoses. dismech's contribution is to *explain* those associations
  mechanistically — linking a treatment, via `target_mechanisms`, to the fungal
  biosynthetic step it blocks — and to make that explanation queryable and
  consistency-checkable across diseases via shared modules.
- **Not a DSS.** IDSA antifungal guidelines, CLSI/EUCAST breakpoints, and
  stewardship pathways already give point-of-care guidance. These modules are at
  most a *mechanistic substrate* such tools could cite, not a prescribing engine.
- **Open question worth a short survey:** how DrugMechDB and antifungal
  resistance/MIC databases represent fungal drug-target mechanism paths — borrow
  vocabulary, avoid reinventing, sharpen where mechanistic explanation is
  additive. Tracked as a follow-up, not a blocker.

## 1. The Problem

Naively, the treatment block for every mycosis collapses to
`Pharmacotherapy → some antifungal → disease`. That discards the knowledge
clinicians actually use: **the small antifungal armamentarium is sharply gated
by organism**. Whether a class works depends on conserved fungal-cell properties
— does the organism have an azole-druggable CYP51, an echinocandin-druggable
β-glucan wall, a polyene-bindable ergosterol membrane, and does intrinsic
resistance exclude a class outright? We want to encode that depth.

## 2. The Core Principle: Target the Fungal Biosynthetic Node, Not the Disease

A `Treatment` links to specific pathophysiology nodes via `target_mechanisms`
(`TreatmentMechanismTarget`). For antifungals, the edge should point at the
**fungus's druggable biology**, which lives as a pathophysiology node:

- **Otomycosis** is the closest existing substrate: it already models a "Biofilm
  formation and antifungal resistance" pathophysiology node and lists topical
  azoles (clotrimazole, miconazole) and acidifying agents as treatments — but
  **without** `target_mechanisms` edges onto an explicit "Ergosterol Biosynthesis
  (CYP51/ERG11)" target node. Adding that node and edge is the cleanest first
  proof-of-concept, and the existing biofilm/resistance node is a ready-made
  gating node.
- **Coccidioidomycosis** carries rich host-immunity pathophysiology (CLEC7A/
  dectin-1 β-glucan recognition, CARD9, Th1/Th17) and uses azoles and
  amphotericin B clinically — but the antifungal agents lack `target_mechanisms`
  edges onto fungal drug-target nodes. Note the elegant duality: the same
  β-glucan that **dectin-1 recognizes** for host defense is the polymer
  **echinocandins block the synthesis of** — a candidate cross-link between the
  host-immunity nodes and a future cell-wall drug-target node.

A single `target_mechanisms` edge encodes *why this drug*, and it predicts
failure modes: an echinocandin has a viable target only where β-1,3-glucan
synthase is essential and accessible (Candida, Aspergillus) — not in
*Cryptococcus* or the Mucorales, which it cannot treat.

## 3. Three-Tier Encoding

**Tier 1 — crude baseline.** `treatment_term: MAXO:0000168` (antiviral/antimicrobial
agent therapy as appropriate) or `NCIT:C15986` (Pharmacotherapy) /
`MAXO:0001573` (topical pharmacotherapy) + `therapeutic_agent` (CHEBI for the
drug, e.g. `CHEBI:3764` clotrimazole, plus fluconazole/itraconazole/amphotericin
B/caspofungin/flucytosine) + `therapeutic_modality: SMALL_MOLECULE`. Says
"clotrimazole is used for otomycosis."

**Tier 2 — the mechanistic edge (the depth).** Add a pathophysiology node for the
targeted fungal step and link `target_mechanisms` to it: an azole → "Ergosterol
Biosynthesis — Lanosterol 14α-Demethylase (CYP51/ERG11)"; terbinafine →
"Ergosterol Biosynthesis — Squalene Epoxidase (ERG1)"; amphotericin B →
"Ergosterol Membrane Integrity"; an echinocandin → "β-1,3-Glucan Cell-Wall
Synthesis (FKS1)"; flucytosine → "Fungal DNA/RNA Synthesis (cytosine-deaminase
activation)". Use `target_phenotypes` for adjuncts (surgical debridement, immune
reconstitution).

**Tier 3 — conserved generalizations as modules.** The reasons "some classes are
useless against some fungi" are conserved *fungus-property × drug-class*
interactions — `kb/modules/` + `conforms_to`. See the proposed module table
above. Because antifungal selectivity rests on a few fungal-specific structures,
the module set is small and high-coverage.

## 4. The Axes That Make Specific Drugs Better for Specific Fungi

| Determinant | Why it gates drug choice | dismech examples |
|---|---|---|
| **Ergosterol vs cholesterol membrane** | the selective-toxicity basis for both azoles (block synthesis) and polyenes (bind it); also the source of polyene host toxicity | all mycoses — Coccidioidomycosis (amphotericin B) |
| **Druggable CYP51 / ERG11** | azole target; point mutations or overexpression (and environmental TR34/L98H in *Aspergillus*) abolish activity | Otomycosis, Coccidioidomycosis, Chromoblastomycosis |
| **β-1,3-glucan cell wall (FKS1)** | fungal-specific echinocandin target — present/essential in *Candida*/*Aspergillus*, **not** a viable target in *Cryptococcus* or the Mucorales | future invasive-candidiasis entry; absence explains echinocandin failure in cryptococcosis |
| **Cytosine deaminase / permease** | flucytosine needs fungal activation; rapid monotherapy resistance mandates combination use | future cryptococcal-meningitis entry (AmB + flucytosine) |
| **Intrinsic species resistance** | whole classes excluded a priori by organism ID | Otomycosis (*Aspergillus* intrinsically fluconazole-resistant); Mucorales (voriconazole/echinocandin-resistant → isavuconazole/AmB); *Cryptococcus* (echinocandin-resistant) |
| **CNS / compartment penetration (PK)** | fluconazole, flucytosine, voriconazole reach CSF; echinocandins and lipid AmB penetrate poorly | cryptococcal/coccidioidal meningitis → fluconazole consolidation; Coccidioidomycosis (coccidioidal meningitis subtype) |
| **Biofilm / device / dimorphic phase** | biofilms tolerate azoles; echinocandins and lipid AmB retain activity; tissue spherule/sclerotic-body forms are less drug-accessible | Otomycosis (biofilm/resistance node); Chromoblastomycosis (muriform/sclerotic bodies, notoriously refractory) |
| **Mold vs yeast vs dimorphic / thermal dimorphism** | spectrum and dosing differ by morphology and growth | Coccidioidomycosis (dimorphic), Otomycosis (Aspergillus mold vs Candida yeast) |
| **Acquired azole resistance (efflux, target overexpression)** | CDR/MDR efflux pumps and ERG11 changes drive clinical failure | Otomycosis resistance node; *C. auris* multidrug resistance (future entry) |
| **Adjunctive surgery / source control** | many deep mycoses are drug-refractory without debridement/excision | Chromoblastomycosis, Mycetoma (eumycetoma — surgery + prolonged azole) |

## 5. Recommended Encoding Pattern (per fungal entry)

1. Populate `infectious_agent` (`InfectiousAgent`, NCBITaxon term) — the fungal
   identity anchor (already present in Coccidioidomycosis, Chromoblastomycosis,
   Otomycosis, Mycetoma).
2. In `pathophysiology`, add **fungal drug-target nodes** (ergosterol synthesis,
   ergosterol membrane, β-glucan wall synthesis, nucleic-acid antimetabolite)
   **and** **gating-property nodes** (intrinsic resistance, biofilm/dimorphic
   phase, CNS sanctuary) as appropriate.
3. Each `Treatment`: Tier-1 fields **plus** `target_mechanisms` → the specific
   node(s) it inhibits, and `target_phenotypes` for adjuncts (debridement,
   immune reconstitution).
4. Where the mechanism recurs, `conforms_to` a shared antifungal-mechanism
   module.
5. Consider cross-linking host β-glucan recognition (dectin-1/CLEC7A) nodes to
   the β-glucan-synthesis drug-target node where both are modeled — the same
   polymer seen from the host-defense and drug-target sides.

## 6. Open Decision for the Register

Surface to `docs/explanation/design-decisions.md`: the same per-disease-vs-module
decision recorded for antibacterials applies. Antifungal-specific question:
whether the two ergosterol-biosynthesis targets (CYP51 demethylase for azoles,
squalene epoxidase for allylamines) are one module with two target nodes
(**recommended** — they share the ergosterol-depletion endpoint) or two modules.
Recommendation: one `fungal_ergosterol_synthesis_inhibition` module with
distinct CYP51 and squalene-epoxidase target nodes, parallel to how the bacterial
folate module holds distinct DHPS and DHFR nodes.

## 7. Next Steps

- [ ] Draft `fungal_ergosterol_synthesis_inhibition` as the proof-of-concept
      module (CYP51/ERG11 demethylase node + squalene epoxidase node →
      ergosterol depletion / membrane stress → azole-resistance branch: ERG11
      mutation, efflux, TR34/L98H), mirroring the
      `bacterial_cell_wall_synthesis_inhibition` build. Highest-yield module
      (azoles are the workhorse class across nearly every mycosis here).
- [ ] Wire **Otomycosis** end-to-end as the first conformer: add an "Ergosterol
      Biosynthesis (CYP51/ERG11)" drug-target node, `conforms_to` the module,
      add `target_mechanisms` edges from clotrimazole/miconazole/fluconazole,
      and connect the existing biofilm/resistance node to
      `antifungal_intrinsic_resistance_gating` (Aspergillus ↔ fluconazole).
- [ ] Wire **Coccidioidomycosis**: add ergosterol-synthesis (azole) and
      ergosterol-membrane (amphotericin B) target nodes; cross-link the existing
      dectin-1/CLEC7A β-glucan host-recognition node to a future β-glucan
      drug-target node.
- [ ] Draft `fungal_membrane_ergosterol_binding` (polyenes) and
      `fungal_cell_wall_glucan_synthesis_inhibition` (echinocandins, FKS1 —
      the cleanest fungal-specific selectivity story).
- [ ] Draft `fungal_nucleic_acid_antimetabolite` (flucytosine) and
      `antifungal_intrinsic_resistance_gating` (the antifungal analog of
      `intracellular_pathogen_persistence` — species-level class exclusion).
- [ ] Create the missing flagship entries that unlock the multi-module
      conformers: **Cryptococcal_Meningitis** (AmB + flucytosine induction →
      fluconazole consolidation; echinocandin-resistant) and **Invasive
      Candidiasis / Candidemia** (echinocandin first-line; *C. auris* resistance).
      These do not yet exist in `kb/disorders/` and are the worked-example payoff.
- [ ] Wire **Chromoblastomycosis** and **Mycetoma** (eumycetoma) as the
      surgery-plus-prolonged-azole, drug-refractory cases — itraconazole/
      terbinafine `target_mechanisms` onto the ergosterol-synthesis node, with
      debridement/excision as `target_phenotypes` adjuncts.
- [ ] Short survey of antifungal drug-mechanism KBs / resistance databases
      (DrugMechDB, EUCAST/CLSI breakpoint rationales) — see §0; borrow
      vocabulary, sharpen the niche.
- [ ] Record the ergosterol-one-module-two-nodes decision in the design register.
