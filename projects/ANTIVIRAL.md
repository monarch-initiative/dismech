---
title: 'Antiviral Therapy: Drug–Virus Mechanism Design Pattern'
status: PLANNED
description: 'Extends the antimicrobial drug–bug mechanism layer to antiviral therapy: viral-target modules (polymerase, protease, entry/fusion, integrase, release) plus the latency/reservoir and quasispecies-resistance gating axes.'
diseases:
- Acquired_Immunodeficiency_Syndrome
- Acute_Hepatitis_C_Virus_Infection
- COVID-19
- Hepatitis_B
- Hepatitis_C
- Influenza
modules:
- parp_parg_macrodomain_viral_evasion
---

# Antiviral Therapy: Drug–Virus Mechanism Design Pattern

## Status: Phase 0 — Strategy / Module Set Proposed

This project extends the [`ANTIMICROBIAL`](ANTIMICROBIAL.md) drug–bug mechanism
design pattern to **antiviral therapy**. The same machinery applies — a
`Treatment` links via `target_mechanisms` to the specific pathophysiology node
(a viral enzyme/step or a gating principle) that makes the drug work, and
recurrent *virus-property × drug-class* interactions are captured once as
`kb/modules/` that disease entries `conforms_to`. The worked examples below are
already partly in the KB; the **antiviral target-class modules are proposed, not
yet built**.

| Proposed module | Target / principle | Drug classes | Candidate conformers (existing entries) |
|---|---|---|---|
| `viral_polymerase_inhibition` | RdRp / reverse transcriptase / viral DNA polymerase; nucleos(t)ide chain termination + non-nucleoside allosteric block | NRTIs, NNRTIs, nucleotide analogs | Hepatitis_B (tenofovir, entecavir), Hepatitis_C (sofosbuvir), COVID-19 (remdesivir, molnupiravir), Acquired_Immunodeficiency_Syndrome (tenofovir/emtricitabine) |
| `viral_protease_inhibition` | Viral polyprotein maturation protease (HIV PR, HCV NS3/4A, SARS-CoV-2 Mpro/3CLpro) | protease inhibitors | COVID-19 (nirmatrelvir), Hepatitis_C (glecaprevir/grazoprevir), Acquired_Immunodeficiency_Syndrome (atazanavir/darunavir, ritonavir boost) |
| `viral_entry_fusion_inhibition` | Receptor attachment / co-receptor / membrane fusion / host-factor uptake | gp41 fusion, CCR5 antagonist, attachment, NTCP | Acquired_Immunodeficiency_Syndrome (maraviroc, enfuvirtide, fostemsavir) |
| `viral_integrase_inhibition` | Retroviral integrase strand transfer (provirus formation) | INSTIs | Acquired_Immunodeficiency_Syndrome (dolutegravir, bictegravir) |
| `viral_assembly_release_inhibition` | Virion assembly / budding / egress (influenza neuraminidase, HCV NS5A replication complex, HBV capsid) | NA inhibitors, NS5A inhibitors, capsid assembly modulators | Influenza (oseltamivir, baloxavir target is endonuclease — see notes), Hepatitis_C (velpatasvir/ledipasvir) |
| `viral_latency_reservoir_persistence` | **Gating, not a drug target.** Latent/integrated/episomal genome (HIV provirus, HSV latency, HBV cccDNA) that replication inhibitors cannot clear → suppression ≠ cure | (explains why lifelong therapy / why "functional cure" is the frontier) | Acquired_Immunodeficiency_Syndrome (HIV reservoir), Hepatitis_B (cccDNA) |

**Multi-module conformers** (the payoff — one disease constrained by several
independent antiviral mechanisms, mirroring Leprosy/Whipple on the antibacterial
side):
- **Acquired_Immunodeficiency_Syndrome (HIV/ART)**: reverse transcriptase
  (`viral_polymerase_inhibition`) + integrase (`viral_integrase_inhibition`) +
  protease (`viral_protease_inhibition`) + entry (`viral_entry_fusion_inhibition`)
  + latent reservoir (`viral_latency_reservoir_persistence`). The canonical
  combination-therapy story.
- **Hepatitis_C (DAA regimens)**: NS5B polymerase
  (`viral_polymerase_inhibition`) + NS3/4A protease
  (`viral_protease_inhibition`) + NS5A replication-complex
  (`viral_assembly_release_inhibition`). The three-target DAA cure.
- **Hepatitis_B**: reverse transcriptase suppression
  (`viral_polymerase_inhibition`) gated by the cccDNA reservoir
  (`viral_latency_reservoir_persistence`) — explains indefinite suppression
  without cure.

## 0. Scope and Positioning (what this is and is NOT)

This is an **explanatory mechanism layer**, not a drug–indication database and
not a clinical decision support system (DSS). Identical positioning to
[`ANTIMICROBIAL`](ANTIMICROBIAL.md) §0:

- **Not duplicating drug-indication curation.** DrugBank, DrugCentral, ChEMBL,
  RxNorm/NDF-RT, and antiviral drug labels already enumerate *which* antivirals
  treat *which* infections. dismech's contribution is to *explain* those
  associations mechanistically — linking a treatment, via `target_mechanisms`,
  to the viral step it blocks — and to make that explanation queryable and
  consistency-checkable across diseases via shared modules.
- **Not a DSS.** HIV/HCV/HBV treatment guidelines (DHHS, AASLD/IDSA, EASL),
  resistance-interpretation tools (Stanford HIVdb), and stewardship pathways
  already give point-of-care guidance. These modules are at most a *mechanistic
  substrate* such tools could cite, not a prescribing engine.
- **Open question worth a short survey:** how DrugMechDB and antiviral
  resistance databases represent viral drug-target mechanism paths — borrow
  vocabulary, avoid reinventing, and sharpen where mechanistic explanation is
  additive. Tracked as a follow-up, not a blocker.

## 1. The Problem

Naively, the treatment block for every viral entry collapses to
`Pharmacotherapy → some antiviral → disease`. That discards the knowledge
clinicians actually use: **viruses are far more target-divergent than bacteria**
— there is no broad-spectrum antiviral analogous to a broad-spectrum antibiotic,
because each virus family carries its own polymerase, protease, and entry
machinery. *Which* mechanism a drug hits, and *whether that target even exists*
in a given virus, is the whole game. We want to encode that depth.

## 2. The Core Principle: Target the Viral Step Node, Not the Disease

A `Treatment` links to specific pathophysiology nodes via `target_mechanisms`
(`TreatmentMechanismTarget`). For antivirals, the edge should point at the
**virus's druggable step**, which lives as a pathophysiology node:

- **Acute_Hepatitis_C_Virus_Infection** is the model already laid down: its
  direct-acting antiviral treatment carries a `target_mechanisms` edge
  (`INHIBITS`) onto an "Early HCV infection of hepatocytes" node and explains
  that the NS5B polymerase inhibitor sofosbuvir plus NS5A inhibitor velpatasvir
  "suppress HCV replication during the early-infection phase." That is the
  target — a finer-grained "NS5B RNA-Dependent RNA Polymerase" node would let
  the polymerase module attach.
- **COVID-19** already carries the host/viral-evasion biology as first-class
  pathophysiology and `conforms_to` the `parp_parg_macrodomain_viral_evasion`
  module, and lists nirmatrelvir (Mpro inhibitor) and remdesivir (RdRp
  inhibitor) as treatments — but **without** `target_mechanisms` edges onto
  explicit "SARS-CoV-2 Main Protease (Mpro/3CLpro)" and "SARS-CoV-2
  RNA-Dependent RNA Polymerase" drug-target nodes. That is the gap to close and
  the cleanest first proof-of-concept.

A single `target_mechanisms` edge encodes *why this drug*, and it predicts
failure modes: a DNA-virus polymerase inhibitor has nothing to point at in an
RNA virus, and an integrase inhibitor is meaningless outside the retroviruses.

## 3. Three-Tier Encoding

**Tier 1 — crude baseline.** `treatment_term: MAXO:0000168` (antiviral agent
therapy) or `NCIT:C15986` (Pharmacotherapy) + `therapeutic_agent` (CHEBI for the
drug, e.g. `CHEBI:85083` sofosbuvir, `CHEBI:145994` remdesivir,
`CHEBI:170007` nirmatrelvir) + `therapeutic_modality: SMALL_MOLECULE`. Says
"remdesivir is used for COVID-19."

**Tier 2 — the mechanistic edge (the depth).** Add a pathophysiology node for the
targeted viral step and link `target_mechanisms` to it: remdesivir → "SARS-CoV-2
RdRp"; nirmatrelvir → "SARS-CoV-2 Mpro"; sofosbuvir → "HCV NS5B polymerase";
dolutegravir → "HIV integrase strand transfer"; oseltamivir → "Influenza
neuraminidase-dependent virion release". Use `target_phenotypes` for host-directed
adjuncts (e.g. dexamethasone → COVID hyperinflammation), exactly as the
antibacterial entries do for anti-inflammatory adjuncts.

**Tier 3 — conserved generalizations as modules.** The reasons "some mechanisms
are better/useless for some viruses" are conserved *virus-property × drug-class*
interactions — `kb/modules/` + `conforms_to`. See the proposed module table
above. The host-side `parp_parg_macrodomain_viral_evasion` module already exists
and is complementary: it captures the **host antiviral / viral-evasion** axis
(IFN-induced PARP ADP-ribosylation vs viral macrodomain countermeasures),
whereas the proposed modules capture the **direct antiviral drug-target** axis.

## 4. The Axes That Make Specific Drugs Better for Specific Viruses

| Determinant | Why it gates drug choice | dismech examples |
|---|---|---|
| **Genome/polymerase type** | RNA vs DNA virus; RdRp vs reverse transcriptase vs DNA pol — a given nucleos(t)ide analog only fits one | Hepatitis_C (NS5B RdRp) vs Hepatitis_B / HIV (reverse transcriptase) vs herpesviruses (DNA pol, acyclovir) |
| **Presence of a viral protease** | maturation-protease inhibitors need a polyprotein-processing protease to exist | Acquired_Immunodeficiency_Syndrome (HIV PR), Hepatitis_C (NS3/4A), COVID-19 (Mpro) |
| **Retroviral integration** | integrase strand-transfer inhibitors are retrovirus-only | Acquired_Immunodeficiency_Syndrome (dolutegravir) — meaningless for HCV/influenza |
| **Entry receptor / co-receptor / host factor** | entry inhibitors are exquisitely virus- and even tropism-specific | Acquired_Immunodeficiency_Syndrome (CCR5-tropic only → maraviroc); HDV/HBV (NTCP → bulevirtide) |
| **Latency / integrated provirus / cccDNA reservoir** | replication inhibitors suppress but cannot clear a latent genome → lifelong therapy, "functional cure" frontier | Acquired_Immunodeficiency_Syndrome (proviral reservoir), Hepatitis_B (cccDNA) — contrast Hepatitis_C, which is curable (no integration/reservoir) |
| **High mutation rate / quasispecies** | error-prone RdRp/RT → resistance escape → mandates combination therapy or high-barrier agents | HIV (3-drug ART), HCV (multi-DAA); high genetic barrier of dolutegravir/sofosbuvir |
| **Resistance mutation** | specific target mutations abolish a drug (M184V, NS5A RASs, Mpro/RdRp mutations) | resistance as its own pathophysiology node the drug must overcome |
| **Tissue/compartment penetration (PK)** | CNS sanctuary (HIV), genital reservoir, intracellular activation of prodrugs | site-specific `target_phenotypes`; prodrug-activation nodes |
| **Host-directed vs direct-acting** | immunomodulation (corticosteroids, IFN) acts on host response, not the virion | COVID-19 (dexamethasone), chronic hepatitis (pegylated IFN historically) |
| **Window of action** | many antivirals only work early (before peak replication / irreversible immunopathology) | Influenza (NA inhibitors within 48 h), Acute_Hepatitis_C (early DAA before chronicity) |

## 5. Recommended Encoding Pattern (per viral entry)

1. Populate `infectious_agent` (`InfectiousAgent`, NCBITaxon term) — the virus
   identity anchor.
2. In `pathophysiology`, add **viral-step drug-target nodes** (polymerase,
   protease, entry/fusion, integrase, assembly/release) **and**
   **gating-property nodes** (latency/reservoir, quasispecies/resistance,
   compartment sanctuary) as appropriate.
3. Each `Treatment`: Tier-1 fields **plus** `target_mechanisms` → the specific
   node(s) it inhibits, and `target_phenotypes` for host-directed adjuncts.
4. Where the mechanism recurs, `conforms_to` a shared antiviral-mechanism module.
5. Keep direct-acting antivirals distinct from host-directed therapy — they
   target different node types (viral step vs host phenotype).

## 6. Open Decision for the Register

Surface to `docs/explanation/design-decisions.md`: the same per-disease-vs-module
decision recorded for antibacterials applies here, plus an antiviral-specific
question — whether **host-directed antiviral mechanisms** (IFN signaling,
restriction factors, the existing `parp_parg_macrodomain_viral_evasion` module)
should be modeled as the same kind of object as **direct-acting viral-target
modules**, or kept as a distinct host-axis layer. Recommendation: keep both as
`kb/modules/`, but tag direct-acting (virus-target) vs host-directed so queries
can separate them.

## 7. Next Steps

- [ ] Draft `viral_polymerase_inhibition` as the proof-of-concept module
      (nucleos(t)ide chain termination + non-nucleoside allosteric block across
      RdRp / reverse transcriptase / viral DNA polymerase), mirroring the
      `bacterial_cell_wall_synthesis_inhibition` build: target node →
      chain-termination/inhibition mechanism → resistance-mutation branch. It is
      the highest-yield module (covers HCV, HBV, HIV, SARS-CoV-2, herpesviruses).
- [ ] Wire **COVID-19** end-to-end as the first conformer: add explicit
      "SARS-CoV-2 RdRp" and "SARS-CoV-2 Main Protease (Mpro)" drug-target nodes,
      `conforms_to` the polymerase/protease modules, and add `target_mechanisms`
      edges from remdesivir/molnupiravir and nirmatrelvir. (The host-evasion
      `parp_parg_macrodomain_viral_evasion` conformance is already present.)
- [ ] Refine **Acute_Hepatitis_C_Virus_Infection** / **Hepatitis_C**: split the
      coarse "Early HCV infection of hepatocytes" target into explicit NS5B
      polymerase, NS3/4A protease, and NS5A replication-complex nodes so all
      three DAA classes attach.
- [ ] Draft `viral_protease_inhibition` and wire the multi-target HCV and HIV
      regimens plus COVID-19 Mpro.
- [ ] Draft `viral_latency_reservoir_persistence` (gating, not a drug target —
      the antiviral analog of `intracellular_pathogen_persistence`). Wire
      **Acquired_Immunodeficiency_Syndrome** (proviral reservoir) and
      **Hepatitis_B** (cccDNA) as the worked "suppression ≠ cure" examples.
- [ ] Draft `viral_integrase_inhibition` and `viral_entry_fusion_inhibition`;
      build out **Acquired_Immunodeficiency_Syndrome** as the flagship
      multi-module conformer (RT + integrase + protease + entry + reservoir).
- [ ] Decide how to model **Influenza** baloxavir (cap-dependent endonuclease,
      PA subunit) vs oseltamivir (neuraminidase release): endonuclease is closer
      to a polymerase-complex target than to assembly/release — may warrant its
      own node rather than forcing it into `viral_assembly_release_inhibition`.
- [ ] Short survey of antiviral drug-mechanism KBs / resistance databases
      (DrugMechDB, Stanford HIVdb) — see §0; borrow vocabulary, sharpen the niche.
- [ ] Record the host-directed-vs-direct-acting module decision in the design
      register.

> **Note on Influenza/baloxavir and "endonuclease":** influenza lacks an RdRp of
> the picornavirus type; its polymerase is a heterotrimer (PB1/PB2/PA), and
> baloxavir inhibits the PA cap-dependent endonuclease. Model it as a polymerase-
> complex subunit target, not a generic release inhibitor.
