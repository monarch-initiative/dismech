---
title: 'Antifungal Therapy: Drug–Fungus Mechanism Design Pattern'
status: IN_PROGRESS
description: 'Extends the antimicrobial drug–bug mechanism layer to antifungal therapy: ergosterol-synthesis (azoles/allylamines), membrane-ergosterol-binding (polyenes), cell-wall glucan-synthesis (echinocandins), and antimetabolite (flucytosine) target modules, plus an intrinsic-resistance gating axis. All five modules are now built and validated.'
diseases:
- Chromoblastomycosis
- Coccidioidomycosis
- Invasive Candidiasis
- Mycetoma
- Otomycosis
modules:
- fungal_ergosterol_synthesis_inhibition
- fungal_membrane_ergosterol_binding
- fungal_cell_wall_glucan_synthesis_inhibition
- fungal_nucleic_acid_antimetabolite
- antifungal_intrinsic_resistance_gating
---

# Antifungal Therapy: Drug–Fungus Mechanism Design Pattern

## Status: Phase 1 — Antifungal Mechanism Module Set Built

This project extends the [`ANTIMICROBIAL`](ANTIMICROBIAL.md) drug–bug mechanism
design pattern to **antifungal therapy**. Same machinery — a `Treatment` links
via `target_mechanisms` to the specific pathophysiology node (a fungal
biosynthetic target or a gating principle) that makes the drug work, and
recurrent *fungus-property × drug-class* interactions are captured once as
`kb/modules/` that disease entries `conforms_to`.

**All five antifungal mechanism modules are now built and validated** (schema +
term + independent snippet-substring verification of every evidence quote): four
drug-target modules (ergosterol synthesis, polyene membrane binding, echinocandin
β-glucan synthesis, flucytosine antimetabolite) plus the species-level
intrinsic-resistance gating module. Invasive candidiasis is the first target-only
echinocandin conformer, Coccidioidomycosis is the first full
ergosterol-synthesis conformer, and Otomycosis is the first intrinsic-resistance
conformer. The ergosterol-synthesis tranche now wires all four named existing
candidates; the remaining missing flagship is cryptococcal meningitis, tracked
with the other follow-up modules in §7.

Antifungal pharmacology has a tighter, more conserved target set than antivirals
because fungi are eukaryotes — selective toxicity hinges on a handful of
fungal-specific structures (ergosterol instead of cholesterol; a β-1,3-glucan
cell wall mammalian cells lack).

| Module (built ✓) | Target / principle | Drug classes | Worked conformers / remaining candidates |
|---|---|---|---|
| `fungal_ergosterol_synthesis_inhibition` | Parallel ergosterol-biosynthesis entry points: lanosterol 14α-demethylase (CYP51/ERG11, azole target) and squalene epoxidase (ERG1, allylamine target) converge on ergosterol production and membrane organization | triazoles, imidazoles, allylamines | Wired: Coccidioidomycosis (fluconazole/itraconazole), Otomycosis (clotrimazole/itraconazole), Chromoblastomycosis (itraconazole component of combination therapy), and Mycetoma's Eumycetoma subtype (itraconazole) |
| `fungal_membrane_ergosterol_binding` | Direct ergosterol binding → membrane pore / oxidative damage | polyenes | Coccidioidomycosis (amphotericin B for severe/disseminated), Mycetoma |
| `fungal_cell_wall_glucan_synthesis_inhibition` | β-1,3-glucan synthase (principally FKS1; FKS2 additionally in species such as *C. glabrata*) — fungal-specific wall target | echinocandins | Invasive Candidiasis / Candidemia (anidulafungin) |
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
- **Invasive candidiasis**: the target-only first tranche now models
  anidulafungin inhibition of Fks glucan synthase via
  `fungal_cell_wall_glucan_synthesis_inhibition`. Azole step-down and
  species/*C. auris* resistance gating remain future multi-module extensions.

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

- **Otomycosis** now keeps its existing biofilm and Aspergillus-specific
  fluconazole-resistance nodes separate from a complete Cyp51 → ergosterol →
  membrane-organization slice. Topical clotrimazole and systemic itraconazole
  carry agent-specific `INHIBITS` edges to Cyp51, while clotrimazole separately
  `BYPASSES` only the fluconazole exclusion; this does not assert universal
  isolate susceptibility.
- **Coccidioidomycosis** now carries a complete Cyp51 → ergosterol → membrane
  organization slice, with agent-specific `target_mechanisms` edges from
  fluconazole and itraconazole. Its rich host-immunity pathophysiology (CLEC7A/
  dectin-1 β-glucan recognition, CARD9, Th1/Th17) remains distinct. Note the
  elegant duality: the same
  β-glucan that **dectin-1 recognizes** for host defense is the polymer
  **echinocandins block the synthesis of** — a candidate cross-link between the
  host-immunity nodes and a future cell-wall drug-target node.

A single `target_mechanisms` edge encodes *why this drug*, and it predicts
failure modes: an echinocandin has a viable target only where β-1,3-glucan
synthase is essential and accessible (Candida, Aspergillus) — not in
*Cryptococcus* or the Mucorales, which it cannot treat.

## 3. Three-Tier Encoding

**Tier 1 — crude baseline.** `treatment_term: NCIT:C15986` (Pharmacotherapy/antimicrobial
agent therapy as appropriate) or `NCIT:C15986` (Pharmacotherapy) /
`NCIT:C15986` (Pharmacotherapy) + `therapeutic_agent` (CHEBI for the
drug, e.g. `CHEBI:3764` clotrimazole, plus fluconazole/itraconazole/amphotericin
B/caspofungin/flucytosine) + the modality appropriate to that agent (usually
`SMALL_MOLECULE`; echinocandins such as anidulafungin are `PEPTIDE`). Says
"clotrimazole is used for otomycosis."

**Tier 2 — the mechanistic edge (the depth).** Add a pathophysiology node for the
targeted fungal step and link `target_mechanisms` to it: an azole → "Lanosterol
14-alpha-Demethylation by CYP51 (ERG11)"; terbinafine → "Squalene Epoxidation by
Squalene Epoxidase (ERG1)"; amphotericin B →
"Ergosterol Membrane Integrity"; an echinocandin → "β-1,3-Glucan Cell-Wall
Synthesis by Fks glucan synthase"; flucytosine → "Fungal DNA/RNA Synthesis (cytosine-deaminase
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
| **β-1,3-glucan cell wall (Fks glucan synthase)** | fungal-specific echinocandin target — encoded principally by FKS1, with FKS2 additionally important in species such as *C. glabrata*; present/essential in *Candida*/*Aspergillus*, **not** a viable target in *Cryptococcus* or the Mucorales | Invasive Candidiasis; target non-viability explains echinocandin failure in cryptococcosis |
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
(**recommended** — both normal dependencies converge on ergosterol production
and membrane organization) or two modules. Recommendation: one
`fungal_ergosterol_synthesis_inhibition` module with distinct, parallel CYP51 and
squalene-epoxidase target nodes, analogous to the bacterial folate module holding
distinct DHPS and DHFR targets.

## 7. Next Steps

- [x] Draft `fungal_ergosterol_synthesis_inhibition` as the proof-of-concept
      module. Built at `kb/modules/fungal_ergosterol_synthesis_inhibition.yaml`:
      five nodes: parallel CYP51/ERG11-demethylase and ERG1-squalene-epoxidase
      targets converge on normal ergosterol production and plasma-membrane
      organization; target alteration/overexpression and efflux are recorded as
      a standalone resistance state. Evidence: 33374996 and 31643715 (CYP51),
      1543672 (ERG1, ergosterol, and membrane dependency). Key target:
      `#Lanosterol 14-alpha-Demethylation by CYP51 (ERG11)`.
- [x] Draft `fungal_membrane_ergosterol_binding` (polyenes). Built: three nodes
      (membrane ergosterol as the polyene binding target → permeabilization /
      fungicidal killing → rare resistance via reduced ergosterol). Evidence:
      31643715 (LiverTox), Anderson 24681535 (sterol-sponge), Czajka 37998390.
- [x] Draft `fungal_cell_wall_glucan_synthesis_inhibition` (echinocandins,
      Fks glucan synthase). Built: five nodes (β-1,3-glucan synthase target → normal
      cell-wall assembly, plus intervention-conditional integrity failure /
      osmotic lysis, FKS-mediated resistance, and intrinsic resistance in
      Cryptococcus). Evidence: Perlin 26190298 / 26567278, Emri
      23463246, Aruanno 31138565, Cappelletty 21694887, Iyer 33558691.
- [x] Draft `fungal_nucleic_acid_antimetabolite` (flucytosine). Built: three
      nodes (fungal cytosine-deaminase activation of 5-FC to 5-FU → disruption of
      fungal RNA/DNA synthesis → rapid monotherapy resistance mandating
      combination). Evidence: Vermes 10933638, Houšť 32178468, Noël 12654658.
- [x] Draft `antifungal_intrinsic_resistance_gating` (the antifungal analog of
      `intracellular_pathogen_persistence` — species-level class exclusion).
      Built: three nodes forming parallel intrinsic and acquired resistance arms
      that converge on resistance-gated narrowing of antifungal options; neither
      resistance arm causes the other. Otomycosis now conforms on the
      Aspergillus/fluconazole intrinsic arm. Evidence: 33558691, 38445857,
      31159914, 33091071, and 28911043.
- [x] **Wire additional ergosterol-synthesis conformers.** Coccidioidomycosis is
      the first full conformer, with Cyp51 → ergosterol → membrane nodes and
      fluconazole/itraconazole target edges. Otomycosis duplicates the same
      Cyp51 slice for clotrimazole and persistent-disease itraconazole while
      preserving its separate Aspergillus/fluconazole intrinsic-resistance gate.
      A later, separate module tranche can add Coccidioidomycosis's
      amphotericin-B ergosterol-membrane target without conflating the two
      modules.
- [ ] Create **Cryptococcal_Meningitis**, the remaining missing flagship
      conformer (AmB + flucytosine induction → fluconazole consolidation;
      echinocandin-resistant).
- [x] Create **Invasive_Candidiasis** with Candidemia as a subtype and the
      minimal Fks glucan-synthase target-only conformer: anidulafungin → INHIBITS
      → fungal beta-1,3-glucan synthase. Azole step-down and acquired-resistance
      wiring remain later extensions.
- [x] Wire **Chromoblastomycosis** and **Mycetoma** (Eumycetoma subtype) on the
      high-precision Cyp51 branch. Chromoblastomycosis models the itraconazole
      component of documented combination therapy without asserting
      monotherapy; Mycetoma limits the fungal target chain and itraconazole edge
      to Eumycetoma and anchors it to *Madurella mycetomatis*. Terbinafine/Erg1
      branches and surgical-adjunct targeting remain optional extensions.
- [ ] Short survey of antifungal drug-mechanism KBs / resistance databases
      (DrugMechDB, EUCAST/CLSI breakpoint rationales) — see §0; borrow
      vocabulary, sharpen the niche.
- [x] Record the ergosterol-one-module-two-target-branches decision in the design
      register, including branch-specific conformance.
