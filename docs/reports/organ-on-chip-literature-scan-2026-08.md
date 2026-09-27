# Organ-on-chip and lung-on-chip literature scan, 2026

**Date:** 2026-08-27
**Scope:** PubMed, publication date 2026 (lung-specific set) and 2026-02 onward (general
organ-on-chip set).
**Purpose:** survey where this literature is being published, and triage which papers carry
mechanism claims curatable into dismech.

## Search

Two PubMed queries, both restricted to title/abstract:

- **Lung set** — `lung-on-a-chip OR lung-on-chip OR "lung chip" OR airway-on-a-chip OR
  alveolus-on-a-chip OR "alveolus chip"`, 2026. **49 papers**, all retrieved.
- **General set** — `organ-on-a-chip OR organ-on-chip OR organs-on-chips OR
  microphysiological`, 2026-02 onward. **703 papers**, first 500 retrieved and analysed.

The general query's `microphysiological` clause is what makes it large; that word is now
standard in regulatory and toxicology writing, so the set includes many papers that are about
the regulatory status of these models rather than about any disease.

## Where this work is published

**There is no home journal.** This is the single most useful thing the scan establishes.

In the general set, 500 papers are spread across **254 distinct journals**. **175 of those
journals contributed exactly one paper.** The twelve most frequent venues together account for
only **28%** of the set. The lung subset is more extreme still: 49 papers across **43
journals**, with no journal contributing more than two.

Most-frequent venues, general set (2026-02 onward, n=500):

| n | Journal |
|---|---|
| 23 | bioRxiv (preprint) |
| 21 | Lab on a Chip |
| 15 | Frontiers in Bioengineering and Biotechnology |
| 13 | Advanced Healthcare Materials |
| 12 | Biofabrication |
| 12 | Advanced Drug Delivery Reviews |
| 11 | International Journal of Molecular Sciences |
| 9 | Advanced Science |
| 7 | Small |
| 7 | Micromachines |
| 6 | Acta Biomaterialia |
| 6 | Frontiers in Toxicology |

These fall into four groups, and the grouping matters more than the ranking:

1. **Microfabrication and biomaterials** — Lab on a Chip, Biofabrication, Advanced Healthcare
   Materials, Small, Acta Biomaterialia, Materials Today Bio. The largest group. Papers here
   are usually reporting a *device*; the disease application is a validation experiment at the
   end.
2. **Toxicology and drug delivery** — Advanced Drug Delivery Reviews, Frontiers in Toxicology,
   Toxicological Sciences, Journal of Applied Toxicology, Archives of Toxicology,
   International Journal of Pharmaceutics. Driven by the shift away from mandatory animal
   testing; these papers have real exposure–response data.
3. **Clinical and organ-specific journals** — European Respiratory Journal, Thorax, Journal of
   Clinical Investigation, Transplantation, Respiratory Research, American Journal of
   Respiratory Cell and Molecular Biology. The smallest group but the highest mechanistic
   yield.
4. **Preprints** — bioRxiv is the single largest venue in the general set.

**Consequences for how we monitor this field.** Following a journal list will not work; a
keyword-based PubMed sweep is the only viable approach, and it must include bioRxiv. Roughly
half the returned records (259 of 500 in the general set, 22 of 49 in the lung set) are
**reviews**, so any automated scan needs a `Review[pt]` filter or it will spend most of its
budget on secondary literature.

**A caution the scan surfaced directly.** One 2026 record in the lung set is a *retraction
notice* for a lung-on-chip influenza/pneumococcus co-infection paper (PMID:42481340). Anything
harvesting this literature automatically should check publication type before citing.

## Triage: which papers carry curatable mechanism

Of the 49 lung papers, most are device or platform reports whose disease content is a
demonstration rather than a finding. Eleven had a substantive, quotable mechanism claim tied to
a specific disease. Those are listed below with what was done about each.

| PMID | Journal | Claim | Disposition |
|---|---|---|---|
| 41477823 | Science Advances | Autologous iPSC alveolus-chip; macrophage-restricted ATG14 knockout raises necrosis without bacterial replication | Curated → `Tuberculosis` |
| 40987954 | Nature Biomedical Engineering | IL-1β and TNF-α act in *opposite* directions on the influenza cytokine storm; fibroblast CXCL12–CXCR4 axis | Curated → `Influenza` |
| 41252215 | J Clinical Investigation | Hyperphysiological strain worsens *Pseudomonas* infection and bacterial translocation | Curated → `Acute_Respiratory_Distress_Syndrome` |
| 41442163 | Toxicological Sciences | Chlorine gas: epithelial junction loss immediate, endothelial loss delayed to 72 h | Curated → `Acute_Respiratory_Distress_Syndrome` |
| 42473541 | Materials Today Bio | Whole cigarette smoke destroys alveolar microvasculature only when alveolar epithelium is present | Curated → `Chronic_Obstructive_Pulmonary_Disease` |
| 42475431 | J Visualized Experiments | COPD patient-derived chip shows mucus hypersecretion with barrier intact | Curated → `Chronic_Obstructive_Pulmonary_Disease` |
| 41406599 | Biofabrication | Cyclic stretch amplifies TGF-β1 fibrotic signalling; reversed by nintedanib | Curated → `Idiopathic_Pulmonary_Fibrosis` |
| 41786071 | Eur J Pharmacology | Hypoxia degrades blood-gas barrier proteins via HIF-1α/HO-1; canine + chip | Curated → new `High_Altitude_Pulmonary_Edema` |
| 42546767 | Biofabrication | Diesel particulate injures the *unexposed* endothelial layer — "trans-barrier propagation" | Curated → new module (see below) |
| 42083145 | Transplantation | Cold-storage IRI alveolus-chip: barrier loss plus compartment-specific adhesion-molecule shedding | Curated → new module |
| 42204607 | Respiratory Research | Isothiazolinone humidifier disinfectant disrupts the alveolar barrier | Curated → new module |

### The cross-cutting finding

Five of these papers, using five unrelated insults — diesel particulate, chlorine gas, cigarette
smoke, isothiazolinone, and cold-storage ischemia — independently report the same thing: an
exposure confined to **one** side of the blood-gas barrier produces measurable injury in the
**other**, unexposed side. The chlorine paper times it (epithelial injury immediate, endothelial
at 72 h). The cigarette-smoke paper controls it (vascular networks exposed to smoke *without*
overlying epithelium stay intact).

This is a mechanism claim, not a device observation, and it is the kind of thing only a
compartmentalised model can establish — you cannot expose one side of the alveolar barrier and
not the other in a patient or an animal. It recurs across enough diseases to meet the module bar,
so it was curated as one:

- **`kb/modules/alveolar_capillary_barrier_failure.yaml`** — five nodes,
  `trigger → amplifier → central_effector → effector → consequence`, with
  *Alveolar Epithelial and Endothelial Junctional Disruption* as the key conformance target.
  `Acute_Respiratory_Distress_Syndrome` (4 nodes) and `High_Altitude_Pulmonary_Edema` (3 nodes)
  conform to it.

### Not curated, and why

- **Reviews (22 of 49).** Useful for orientation, not for evidence snippets.
- **Pure device and materials papers** — PLGA/PCL membrane chemistry (42546767's primary
  contribution), LCD 3D printing (42480620), inkjet pH sensors (41590290), extracellular-vesicle
  isolation chips (41500804). Where these carried a disease finding it was extracted; the
  fabrication content has no dismech home.
- **PMID:42481340** — retracted.
- **PMID:41982094** (mechanical stretch reduces SARS-CoV-2 pseudovirus membrane fusion) — a real
  finding, but pseudovirus fusion on stretched AT2 cells does not map cleanly onto any existing
  node in `Long_COVID` or a COVID entry. Left for a curator who knows that entry.
- **PMID:42138232** (benzene VOC cumulative cytokine response, reversed by montelukast) — an air-quality
  risk-assessment result rather than a disease mechanism; would need an entry for benzene
  inhalation exposure that does not yet exist.

## Curation output

| Path | Change |
|---|---|
| `kb/modules/alveolar_capillary_barrier_failure.yaml` | new module, 13 evidence snippets |
| `kb/disorders/High_Altitude_Pulmonary_Edema.yaml` | new disorder (MONDO:0031257), 33 snippets |
| `kb/disorders/Tuberculosis.yaml` | iPSC alveolus-chip, 5 mechanism links incl. one `FAILS_TO_RECAPITULATE` |
| `kb/disorders/Influenza.yaml` | immune-competent lung-chip, 3 mechanism links |
| `kb/disorders/Chronic_Obstructive_Pulmonary_Disease.yaml` | 2 chips, 4 mechanism links |
| `kb/disorders/Idiopathic_Pulmonary_Fibrosis.yaml` | alveolar array chip, 2 mechanism links |
| `kb/disorders/Acute_Respiratory_Distress_Syndrome.yaml` | 2 chips, 4 mechanism links; 4 `conforms_to` edges to the new module |

## Notes for future scans

- The lung-chip literature is small enough (≈50 papers/year) to read exhaustively. The general
  organ-on-chip literature (≈700 in six months) is not, and needs the `Review[pt]` filter plus a
  disease-term intersection to be tractable.
- Negative results are unusually well reported in this field, because a chip that fails to
  reproduce something is publishable as a limitation. `FAILS_TO_RECAPITULATE` and
  `HUMAN_MODEL_MISMATCH` are the right slots and were under-used before this scan; the
  tuberculosis non-permissiveness result is a good worked example.
- Several groups now publish patient-derived chips (COPD in 42475431 and 42473541). These are
  worth watching: they carry genotype into the model, which is what makes a chip usable for the
  subtype-level claims dismech records.
