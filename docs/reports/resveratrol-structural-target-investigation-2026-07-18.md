# Resveratrol as a "treatment": what the direct structural evidence actually shows

*Investigation report — 2026-07-18*

## TL;DR

Resveratrol is the textbook case of a compound whose **popular therapeutic
narrative (a SIRT1-activating, caloric-restriction-mimetic geroprotector) is the
part with the weakest direct evidence**, while its best-validated molecular fact —
a 1.5 Å co-crystal with **quinone reductase 2 (NQO2/QR2), Kd ≈ 34 nM** (PDB
[1SG0](https://www.rcsb.org/structure/1SG0)) — is rarely what it is marketed for.
Starting from the structural layer, as requested, resveratrol looks less like a
targeted drug and more like a **promiscuous, low-affinity polypharmacology probe**
with a bioavailability problem that has produced a largely null/mixed human
clinical record.

**Recommendation for dismech:** do **not** attach resveratrol to the
`deregulated_nutrient_sensing` / `cellular_senescence` geroprotector modules as a
"SIRT1 activator" — that would import exactly the contested downstream theory those
modules deliberately exclude. If resveratrol is curated at all, the only
structurally-defensible home is as a **transthyretin (TTR) tetramer stabilizer**,
an instance of the existing `amyloidogenesis` module's tafamidis drug-target
pattern (see [§5](#5-the-one-clean-dismech-fit-ttr-stabilization)). The NQO2 and
TyrRS axes are the two cleanest *direct* targets but have no current dismech
disorder home.

---

## 1. The structural evidence layer (start here)

Resveratrol (C₁₄H₁₂O₃; a stilbenoid polyphenol, three hydroxyls) has an unusually
large set of solved protein co-crystal structures. The Frontiers 2018 review
*"Polypharmacology or Promiscuity?"* (Saqib et al., PMID:30405417 / PMC6207623)
catalogs them. The key point is that these targets **share no common fold, sequence
motif, or binding-site chemistry** — resveratrol simply exploits its flat,
H-bond-capable stilbene scaffold opportunistically.

| Target | PDB | Direction | Notes |
|---|---|---|---|
| **Quinone reductase 2 (NQO2/QR2)** | [1SG0](https://www.rcsb.org/structure/1SG0) | **inhibitor** | **Highest measured affinity, Kd 34 ± 15 nM**; sits parallel to FAD isoalloxazine, all 3 –OH H-bonded. Buryanovskyy 2004, PMID:15350128 |
| Tyrosyl-tRNA synthetase (TyrRS/YARS1) | [4Q93](https://www.rcsb.org/structure/4Q93) | active-site mimic | Tyr-mimetic; redirects TyrRS to nuclear PARP1 activation. Sajish & Schimmel 2015, PMID:25533949 |
| Leukotriene A4 hydrolase | 3FTS | inhibitor | |
| Phospholipase A2 | 4QER | inhibitor | |
| F1-ATPase | 2JIZ | inhibitor | |
| Sulfotransferase 1B1 | 3CKL | inhibitor | (also a resveratrol *metabolizer*) |
| PPAR-γ | 4JAZ | inhibitor/modulator | |
| Transthyretin (TTR) | 5CR1 / [8W42](https://www.rcsb.org/structure/8W42) | **stabilizer** | Binds T4 pocket, stabilizes tetramer (tafamidis-like) |
| Troponin C | 2L98 | modulator | |
| Myosin-2 motor domain | 3MNQ | inhibitor | |
| Methionine adenosyltransferase 2B | 2YDX | inhibitor | |
| Sirtuin-5 | 4HDA | weak activator | |
| **Sirtuin-1** | [5BTR](https://www.rcsb.org/structure/5BTR) | **allosteric, substrate-dependent** | Two NTD-bound resveratrol molecules tighten SIRT1–peptide binding. Cao 2015, PMID:26109052 |
| Estrogen receptor α | 4PP6 / 4PPP | modulator | phytoestrogen activity |

Two direct targets outrank SIRT1 on the structural/affinity evidence:

- **NQO2/QR2 (1SG0)** — the flagship. High-affinity (nM), clean competitive
  active-site occupancy. Functional knockdown of QR2 phenocopies resveratrol
  (increased antioxidant/detoxification enzyme expression, reduced proliferation),
  supporting QR2 inhibition as a *bona fide* mechanism (Buryanovskyy 2004).
- **TyrRS (4Q93)** — Sajish & Schimmel showed resveratrol occupies the TyrRS
  active site as a tyrosine mimic and drives an NAD⁺-dependent auto-poly-ADP-
  ribosylation of **PARP1**, a stress-signaling axis **activatable at ~1000× lower
  concentrations than the SIRT1 assays** — i.e. within a plausible physiological
  range (Nature 2015, PMID:25533949).

## 2. The SIRT1 story is the contested one

The marketed mechanism — resveratrol as a **direct** SIRT1 activator and
caloric-restriction mimetic — is the weakest link:

- The original activation was measured with the **Fluor-de-Lys** fluorophore-tagged
  peptide. Resveratrol (and the "STAC" compounds SRT1720/2183/1460) do **not**
  activate SIRT1 against **native, unlabeled** substrates; the effect tracks the
  **fluorophore**, not the enzyme (Beher 2009, PMID:19843076; Pacholec 2010 —
  NMR/SPR/ITC showed compound–fluorophore, not compound–SIRT1, binding).
- The rehabilitated view (Hubbard 2013; Cao 2015, PMID:26109052, PDB 5BTR) is
  **allosteric and substrate-sequence-selective**: two N-terminal-domain-bound
  resveratrol molecules *stabilize* the SIRT1–peptide complex for substrates that
  happen to carry bulky hydrophobic (fluorophore-like) residues at the +1 position.
  This is real but is **not** the clean, general "turn up sirtuin activity" story —
  and it is exactly why `kb/modules/deregulated_nutrient_sensing.yaml` lists
  rapamycin and metformin as its geroprotector treatments and pointedly leaves
  resveratrol out, mentioning it only inside a review-snippet.

## 3. Bioavailability and clinical translation: mostly null

- Extensive first-pass **glucuronidation and sulfation** → very low, transient
  plasma parent-drug levels; the in-vitro efficacious 3–30 µM range is essentially
  never reached in vivo by oral dosing.
- 2024 systematic reviews (e.g. *IJMS* 25(2):747) and bioavailability meta-analyses
  report **heterogeneous, mostly modest/mixed** effects on intermediate biomarkers
  (vascular function, inflammation, insulin sensitivity) and **no replicated
  longevity or hard-outcome benefit** in humans.
- dismech has already hit this in practice: PR #3924 (Multiple Epiphyseal
  Dysplasia) explicitly excluded the **resveratrol pseudoachondroplasia trial
  (NCT03866200)** because it was **terminated with no efficacy result**.

## 4. So is resveratrol a "treatment"?

At the mechanism-of-disease altitude dismech curates: **not for any specific
disorder on current evidence.** It is a promiscuous polyphenol whose:

- **molecular structure evidence is strong** (many co-crystals; NQO2 genuinely
  high-affinity),
- **marketed mechanism (SIRT1 CR-mimetic) is contested/assay-dependent**, and
- **clinical-outcome evidence is weak** (bioavailability, mixed/failed trials).

The correct dismech posture is to treat it as a **cautionary structural probe**,
not to bolt it onto an aging module where it would smuggle in the very theory that
module was written to avoid.

## 5. The one clean dismech fit: TTR stabilization

If resveratrol should appear anywhere in the KB with defensible *direct structural*
evidence, it is as a **transthyretin tetramer stabilizer** (PDB 5CR1 / 8W42):
resveratrol binds the T4 thyroxine pocket and kinetically stabilizes the TTR
tetramer against the rate-limiting dissociation step of amyloidogenesis — the
**identical mechanism** to tafamidis, which the `amyloidogenesis` module already
encodes as a `target_mechanisms` `INHIBITS` edge on the amyloid-precursor node.
This is the only place resveratrol slots into an existing dismech drug-target
*design pattern* backed by a co-crystal rather than by a contested phenotypic
assay. It would still warrant a caveat that TTR stabilization by resveratrol is
weaker than tafamidis and not a clinically established ATTR therapy.

## 6. Recommended next actions

1. **Do not** curate resveratrol into `deregulated_nutrient_sensing` or
   `cellular_senescence` as a SIRT1 activator / CR mimetic.
2. If a concrete KB action is wanted, add resveratrol as a **secondary,
   caveated TTR-stabilizer** exemplar in the `amyloidogenesis` module
   (structural evidence: PDB 5CR1/8W42), explicitly ranked below tafamidis.
3. Optionally record NQO2 (1SG0) and TyrRS/PARP1 (4Q93) as the two
   structurally-validated *direct* targets in a note, since both outrank SIRT1
   on the evidence but have no current disorder home.

## Key references

- Buryanovskyy L, et al. *Crystal Structure of Quinone Reductase 2 in Complex with
  Resveratrol.* Biochemistry 2004;43(36):11417–26. **PMID:15350128** (PDB 1SG0)
- Sajish M, Schimmel P. *A human tRNA synthetase is a potent PARP1-activating
  effector target for resveratrol.* Nature 2015;519:370–3. **PMID:25533949** (PDB 4Q93)
- Cao D, et al. *Structural basis for allosteric, substrate-dependent stimulation
  of SIRT1 activity by resveratrol.* Genes Dev 2015;29:1316–25. **PMID:26109052** (PDB 5BTR)
- Beher D, et al. *Resveratrol is not a direct activator of SIRT1 enzyme activity.*
  Chem Biol Drug Des 2009;74:619–24. **PMID:19843076**
- Saqib U, et al. *Polypharmacology or Promiscuity? Structural Interactions of
  Resveratrol With Its Bandwagon of Targets.* Front Pharmacol 2018;9:1201.
  **PMID:30405417** / PMC6207623
