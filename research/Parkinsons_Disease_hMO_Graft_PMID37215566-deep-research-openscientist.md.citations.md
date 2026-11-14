# Citations for Research Query

**Query:** # NAM mining: model-to-mechanism of hiPSC midbrain organoids grafted into 6-OHDA Parkinson mice

## The single paper under study

- **Reference:** PMID:37215566; DOI 10.7150/thno.80271; PMC10196819; *Theranostics* 2023;13(8):2673-2692.
- Open access. The full text is quotable. **Confine the research to THIS paper's own
  findings.** Use other literature only to judge validity/divergence, and when you do,
  cite it separately and say so. Do not attribute another paper's result to this one.

The paper transplants human induced pluripotent stem cell (hiPSC)-derived midbrain
organoids (hMOs) into a unilateral 6-OHDA-lesioned mouse striatum, as a **cell therapy**.
The organoids are from healthy hiPSC lines and carry no Parkinson's disease (PD) genotype;
the dopaminergic insult is in the host, from 6-OHDA.

## Goal

Decide, from this paper, **what each of three distinct biological systems models about
Parkinson's disease, what it does not, and how faithfully** — so a disease knowledge base
can link each system to the mechanism nodes it informs, with a fidelity tier and the
translational caveats that must travel with each link.

The three systems, which must be kept separate in your answer:

1. **hMO** — the hiPSC-derived human midbrain organoid, on its own, in vitro.
2. **6-OHDA mouse** — the unilateral 6-OHDA-lesioned mouse, before/without a graft.
3. **Grafted chimera** — the hMO transplanted into the 6-OHDA mouse striatum (graft + host together).

## The candidate mechanism nodes to test each system against

Report, for each system, which of these it bears on and how. Use these exact node names:

- **Dopaminergic Neuron Loss** — the A9 nigral dopaminergic population whose loss defines PD.
- **Striatal Dopamine Deficiency** — striatal dopamine content/release.
- **Basal Ganglia Circuit Dysfunction** — nigrostriatal/basal-ganglia circuit function and motor output.
- **Neuroinflammation** — striatal inflammatory state (e.g. IL-1β, IL-6).
- **Oxidative Stress** — striatal oxidative/antioxidant state (e.g. Nrf2, Hmox1/HO-1).

(These are nodes in the PD entry; a module also carries "Nigrostriatal Dopaminergic
Neurodegeneration" and "Striatal Dopamine Deficiency and Basal Ganglia Circuit
Dysfunction", which may fit the 6-OHDA lesion better. Note where that is so.)

## What each pairing row must contain

For every (system → node) pairing you assert, give:

1. **relationship** — pick the single best of: RECAPITULATES (reproduces the human
   mechanism), PARTIALLY_RECAPITULATES (reproduces it in part), FAILS_TO_RECAPITULATE
   (a substantive negative — the system does NOT reproduce it), PERTURBS (manipulates
   the node), MEASURES (reads the node out without reproducing it), RESCUES (restores
   the node) — and say in one line why that verb and not the neighbours.
2. **fidelity** — HIGH / MODERATE / LOW / UNKNOWN, with the reason.
3. **model_scale** — the scale the system actually *observes* for this readout:
   MOLECULAR / CELLULAR / TISSUE / ORGANISM. State it even when it differs from the
   node's own scale; if the system observes a scale below the node it is cited for,
   that is an upward extrapolation and must be flagged.
4. **readouts** — the concrete outcome measure(s) grounding the pairing, each with a
   direction (INCREASED / DECREASED / UNCHANGED / RESTORED / ABOLISHED / ALTERED) and
   the measured value where the paper gives one.
5. **limitations** — the specific translational caveat for this pairing.
6. **a verbatim quote** — an exact substring from the paper (abstract or full text)
   that supports the pairing, with its PMID/DOI. Do not paraphrase. If a claim is
   supported only by the full text and not the abstract, say so. Never invent an
   identifier or a quote.

Treat a **RESCUE** (the graft restoring a host node) as a first-class, positive finding:
the grafted chimera restoring striatal dopamine, circuit function or motor behaviour is
exactly the kind of pairing to capture, with its verb set to RESCUES or RESTORED readouts.

## Specific claims from the paper to find, quote and verify

For each, give the exact supporting sentence and its location (abstract vs full text):

- Day 15 is the optimal transplantation stage; day 10 organoids survive but yield few
  TH+ cells, and day 25 grafts largely die.
- At 12 weeks post-graft, 14.11% of surviving human (hNA+) cells are TH+, and over 90%
  of GIRK2+ cells are TH+ (read by the authors as A9 midbrain dopaminergic identity).
- Grafted mice improve on apomorphine-induced rotation, open field and rotarod; the
  vehicle group does not.
- No teratoma or graft overgrowth (teratoma assay with neuroblastoma positive control).
- Striatal IL-1β and IL-6 mRNA fall ~7.85-fold and ~36.66-fold in grafted vs control
  mice; Nrf2 and Hmox1 rise ~1.2-fold and ~3.6-fold.
- The hMOs express dopamine (HPLC after high-K+), show network-wide synchronous bursts
  (MED64, day 60), contain neuromelanin (Fontana-Masson, day 45), and carry **no**
  serotonergic, GABAergic, glutamatergic or cholinergic markers (the authors tie the
  absence to a lower graft-induced dyskinesia risk).
- Quercetin removes >99.99% of residual undifferentiated hiPSCs at ≥40 µM for ≥16 h.
- Whole-cell patch clamp shows graft neurons fire; G-deleted rabies tracing shows
  host-to-graft presynaptic input.

## What the systems do NOT model (for limitations / divergences / fidelity)

State these explicitly and attribute each to the right system:

- The hMO and graft carry **no PD genotype** and show **no alpha-synuclein pathology**
  and **no progressive degeneration within the organoid itself** — so neither models PD
  aetiology or the degenerative process; they model the *dopaminergic cell population and
  its functions* and the *restoration* of host deficits.
- The 6-OHDA lesion is an acute neurotoxin insult, not the slow synucleinopathy of
  idiopathic PD — construct-validity caveat for the "Dopaminergic Neuron Loss" link.
- Neuroinflammation and Oxidative Stress changes are in the **host striatum after
  grafting**, not properties of the organoid — attribute them to the grafted-chimera /
  6-OHDA-host system, not to the hMO.

## Output

A structured report with one section per biological system, each containing its
model-to-mechanism pairing rows as specified above, a short "does not model" subsection,
and an overall fidelity assessment. Then a consolidated table of every (system → node →
relationship → fidelity → model_scale → quote) row. Every factual claim carries a
PMID/DOI and a verbatim quote.
**Provider:** openscientist
**Generated:** 2026-11-14T01:03:00.604791

1. PMID:37215566
2. PMID:20592420
3. PMID:21611977
4. PMID:40307147