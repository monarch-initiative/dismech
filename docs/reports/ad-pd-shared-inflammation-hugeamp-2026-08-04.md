# Alzheimer and Parkinson Disease: Shared Genetics of Inflammation (HuGeAMP, 2026-08-04)

An exploration of the AD–PD relationship using the [HuGeAMP / Knowledge Portal
Network](../../projects/HUGEAMP_PARTNERSHIP.md) open API, focused on whether the
"neuroinflammation" node that both `Alzheimer_Disease` and `Parkinsons_Disease`
carry in dismech is one shared mechanism or two different ones.

**Headline: it is two different ones, joined at a single point.** The shared
inflammatory axis is MHC class II antigen presentation (`HLA-DRB1`, HuGE 45 in
both). Downstream of it the effector arms diverge cleanly — AD's genetic signal
is **innate/myeloid** (microglia, monocytes, macrophages), PD's is
**adaptive/T-cell**. And the cytokine genes that dominate the neuroinflammation
literature (`TNF`, `IL1B`, `IL6`, `NLRP3`, `TLR4`, `C1QA`) have **no human
genetic support in either disease**.

> **Scope caveat.** This is a genetic-architecture analysis. Common-variant
> heritability enrichment supports where the *causal susceptibility* acts; it
> says nothing about downstream or reactive processes, which is exactly where
> most neuroinflammation biology lives. A null here is evidence against a
> *causal genetic* role, not against involvement in disease. See
> [Interpretation limits](#interpretation-limits).

## Method

All figures came from direct queries against `https://bioindex.hugeamp.org`
(open, unauthenticated) on 2026-08-04, using the phenotypes `AD`, `LateAD`,
`Parkinsons`, `PDAndFirstDegree`, and `LBD` from the Neurodegenerative Diseases
Portal (NDKP). Indexes used: `genetic-correlation`, `gene-finder`, `huge`,
`global-enrichment`, `partitioned-heritability`.

Raw data:

- [`data/ad-pd-hugeamp-huge-scores-2026-08-04.tsv`](data/ad-pd-hugeamp-huge-scores-2026-08-04.tsv)
- [`data/ad-pd-hugeamp-biosample-enrichment-2026-08-04.tsv`](data/ad-pd-hugeamp-biosample-enrichment-2026-08-04.tsv)

## 1. AD and PD are weakly but positively genetically correlated

| Pair | rg | SE | p |
|---|---|---|---|
| AD ↔ Parkinsons | **+0.117** | — | 0.016 |
| AD ↔ LBD | +0.633 | 0.195 | 1.1e-03 |
| Parkinsons ↔ LBD | +0.659 | 0.201 | 1.0e-03 |
| AD ↔ LateAD | +0.901 | 0.051 | 1.2e-70 |

The direct AD–PD correlation is real but small — an order of magnitude below
either disease's correlation with **Lewy body dementia**. LBD is the genetic
bridge: it correlates ~+0.65 with *both*, which is the quantitative version of
the clinical observation that LBD sits between the two.

> **Data-quality flag.** `PDAndFirstDegree` (PD with proxy cases) reports
> rg = **−1.13** against `Parkinsons`, which is not biologically interpretable
> and indicates inverted sign coding in that dataset. Its AD correlation
> (−0.181) flips to **+0.181** under that correction, which is consistent with
> the +0.117 from `Parkinsons` — a useful internal replication, but the
> phenotype should not be used as-is.

## 2. Heritability enrichment: AD is immune-tissue, PD is not

Tissue-level enrichment of common-variant heritability, best record per tissue:

| Trait | Records at p<1e-4 | In immune tissue | In brain tissue |
|---|---|---|---|
| **AD** | 9 | **9** | 0 |
| **Parkinsons** | 6 | 2 | 0 |
| LBD | 0 | 0 | 0 (underpowered) |

**Every single AD record passing p<1e-4 is an immune tissue** — blood
(enrichment 1.96, p=1.1e-07), lymphoid tissue (6.65, p=8.3e-07), spleen (5.06,
p=8.2e-07), thymus (5.42, p=1.7e-05). Central nervous system enhancers rank
*eleventh* for AD (1.82, p=3.6e-03).

PD's top tissue is pancreas (2.30, p=5.9e-07), followed by **central nervous
system** (2.06, p=6.9e-06) — a genuine CNS signal that AD lacks at that
significance — then blood (1.74, p=1.2e-05).

So the crude reading is: AD susceptibility is enriched in immune regulatory
elements to a degree PD's is not, and PD retains a neuronal signal AD does not.

## 3. Biosample resolution: innate (AD) vs adaptive (PD)

This is where the two inflammation stories separate. Top biosample-resolved
enrichments:

**AD — myeloid and B-cell dominant**

| Biosample | Enrichment | p |
|---|---|---|
| germinal_center | 6.65 | 8.3e-07 |
| B_cell | 5.45 | 1.0e-06 |
| thymus | 4.44 | 2.0e-05 |
| **inflammatory_macrophage** | 5.89 | 2.7e-05 |
| **tissue-resident_macrophage** | 32.78 | 3.0e-05 |
| alternatively_activated_macrophage | 4.53 | 3.0e-05 |
| natural_killer_cell | 5.63 | 3.3e-05 |
| **microglial_cell** | 26.86 | 5.6e-05 |
| substantia_nigra | 4.92 | 7.9e-05 |
| **CD14+/CD16− classical monocyte** | 5.77 | 1.4e-04 |
| mature_neutrophil | 5.91 | 1.7e-04 |

**PD — CNS and T-cell**

| Biosample | Enrichment | p |
|---|---|---|
| islet_of_Langerhans | 3.16 | 1.2e-06 |
| **caudate_nucleus** | 3.52 | 4.6e-06 |
| **CD4+ αβ memory T cell** | 3.33 | 7.3e-06 |
| B_cell | 3.36 | 8.1e-06 |
| natural_killer_cell | 3.50 | 8.7e-05 |
| memory_B_cell | 6.18 | 1.3e-04 |
| thymus | 2.94 | 2.0e-04 |
| common_myeloid_progenitor | 3.33 | 2.0e-04 |

AD's list is macrophage/microglia/monocyte/neutrophil — **innate myeloid**. PD's
top immune hit is **CD4+ memory T cells**, with no macrophage population until
alternatively-activated macrophage far down the list. PD also puts a striatal
region (caudate nucleus) near the top, which AD does not.

The PD CD4+ T-cell result independently recovers the known α-synuclein-specific
T-cell response, and it is mechanistically coherent with the HLA class II
association in §4 — class II presents to CD4+ T cells.

> **Metadata artifact.** HuGeAMP maps `microglial_cell` and
> `tissue-resident_macrophage` to tissue `pancreas`, which is wrong. The
> biosample labels are usable; the `tissue` field on those rows is not.

## 4. Gene level: one shared immune locus, two disjoint gene sets

HuGE scores (Bayes-factor-derived gene-level genetic evidence; **1.0 = no
evidence**):

| Gene | Function | AD | PD | LBD |
|---|---|---:|---:|---:|
| **TREM2** | microglial innate receptor | **407.9** | 1.0 | 1.0 |
| **ABCA7** | myeloid lipid transport | **200.1** | 1.0 | 1.0 |
| **CLU** | complement regulator | **46.1** | 1.0 | 1.0 |
| **CD33** | myeloid Siglec receptor | **45.0** | 1.0 | 1.0 |
| **MS4A4A** | myeloid membrane protein | **45.0** | 1.0 | 1.0 |
| **INPP5D** (SHIP1) | myeloid signaling brake | **45.0** | 1.0 | 1.0 |
| **CR1** | complement receptor 1 | **45.0** | 1.0 | 1.0 |
| **SPI1** (PU.1) | master myeloid TF | **20.0** | 1.6 | 1.0 |
| MS4A6A | myeloid membrane protein | 20.0 | 1.0 | 1.0 |
| TYROBP (DAP12) | TREM2 adaptor | 5.5 | 1.0 | 1.0 |
| PLCG2 | myeloid signaling | 3.0 | 1.0 | 1.0 |
| **HLA-DRB1** | **MHC class II** | **45.0** | **45.0** | 1.0 |
| HLA-DRA / HLA-DRB5 | MHC class II | 3.0 | 3.0 | 1.0 |
| **LRRK2** | kinase, lysosomal + immune | 1.0 | **713.2** | 1.0 |
| **TMEM175** | lysosomal K⁺ channel | 8.6 | **350.0** | 45.0 |
| **GBA1** | lysosomal glucocerebrosidase | 1.0 | 45.0 | **350.0** |
| **SNCA** | α-synuclein | 1.0 | 45.8 | 3.0 |
| VPS13C | lysosomal lipid transfer | 1.0 | 8.9 | 1.0 |
| APOE | lipid transport | 24.4 | 1.0 | **45.0** |
| **TNF** | cytokine | **1.0** | **1.0** | 1.0 |
| **IL1B** | cytokine | **1.0** | **1.0** | 1.0 |
| **IL6** | cytokine | **1.1** | **1.0** | 1.0 |
| **NLRP3** | inflammasome sensor | **1.0** | **1.2** | 1.0 |
| **TLR4** | innate PRR | **1.0** | **1.0** | 1.0 |
| **C1QA** / **C3** | complement | **1.0** | 1.2 / 1.0 | 1.0 |
| **AIF1** (Iba1) / **CSF1R** / **SYK** | microglial | **1.0** | **1.0** | 1.0 |

Three things fall out:

1. **The AD microglial panel is completely PD-null.** Ten genes with HuGE 3–408
   in AD sit at exactly 1.0 in PD. This is not a gradient; it is disjoint.
2. **PD's panel is lysosomal/autophagic**, and equally AD-null. `LRRK2` is the
   crossover candidate — it is a genuine immune-expressed kinase — but its
   genetic evidence is entirely on the PD side.
3. **`HLA-DRB1` is the only gene with substantial evidence in both** (45/45).
   That single locus carries the shared inflammatory signal.
4. **The canonical inflammatory mediators are flat at ~1.0 in both.** No
   detectable common-variant support for `TNF`, `IL1B`, `IL6`, `NLRP3`, `TLR4`,
   `C1QA`, `CSF1R`, `AIF1`, `SYK` in either disease.

LBD again bridges: it takes `APOE` (45) from the AD side and `GBA1` (350) plus
`TMEM175` (45) from the PD side.

## 5. Locus-level check on shared genes

Naive gene-level overlap at p<2.5e-6 gives 28 "shared" genes, but clustering by
position collapses them to **6 loci**, and two LD blocks account for 23 of the 28:

| Locus | n genes | AD p | PD p | Note |
|---|---:|---|---|---|
| chr17:42.4Mb | 10 | 1.3e-10 | 6.0e-54 | **17q21.31 MAPT inversion** — one haplotype |
| chr16:30.7Mb | 13 | 1.8e-10 | 2.6e-23 | **16p11.2** — one LD block |
| **chr6:32.3Mb** | 2 | 5.1e-09 | 1.8e-12 | **MHC class II** (`HLA-DRA`, `C6orf10`) |
| chr4:1.0Mb | 1 | 8.9e-09 | 6.4e-31 | `DGKQ` |
| chr2:135.6Mb | 1 | 1.6e-08 | 4.9e-13 | `ACMSD` |
| chr7:100.1Mb | 1 | 1.1e-06 | 3.2e-07 | `NYAP1` |

Anyone reading the raw gene list would report 28 shared genes and 10 shared
tau-pathway genes at 17q21.31. There is **one** shared signal there — the MAPT
inversion haplotype. Of the six real loci, only the MHC is immune.

## 6. What this means for the dismech entries

Both `Alzheimer_Disease` and `Parkinsons_Disease` carry a pathophysiology node
named exactly `Neuroinflammation`. The genetics say these are **not the same
node** and should not be curated as though a future shared module would cover
both.

### Concrete gaps found

| Gap | Detail |
|---|---|
| **`HLA-DRB1` absent from both** | The one locus with genetic support in AD *and* PD appears in neither `genetic:` list. This is the highest-value single addition. |
| **`relationship_type` unset on all 9 AD genes** | `APP`, `PSEN1`, `PSEN2`, `APOE`, `BIN1`, `TREM2`, `NLRP3`, `PYCARD`, `LRP1` all lack `relationship_type`. HuGE cleanly separates them: `APP`/`PSEN1`/`PSEN2` are `CAUSATIVE`; `TREM2` (408), `ABCA7` (200), `APOE` (24) are `RISK_FACTOR`/`SUSCEPTIBILITY`. |
| **`NLRP3` and `PYCARD` are curated but genetically null** | HuGE `NLRP3` = 1.0 in AD. Whatever supports them is inflammasome biology, not human genetics — they must not be typed `RISK_FACTOR`/`SUSCEPTIBILITY` on that basis. |
| **AD myeloid panel missing** | `ABCA7`, `CD33`, `MS4A4A`, `MS4A6A`, `INPP5D`, `CR1`, `SPI1`, `CLU`, `PICALM` — HuGE 20–200, none curated. |
| **PD lysosomal panel incomplete** | `TMEM175` (350) and `VPS13C` (8.9) not in the PD `genetic:` list. |
| **PD has no inflammation hypothesis group** | AD has `neuroimmune_glial_amplification_model` (ALTERNATIVE). PD's `mechanistic_hypotheses` has no immune entry despite the CD4+ T-cell and HLA class II signal. |
| **No AD–PD comorbidity entry** | `kb/comorbidities/` has 19 entries, none for this pair. |

### Suggested curation

1. **Add `HLA-DRB1` to both entries** as `relationship_type: SUSCEPTIBILITY`,
   with the mechanism annotated as MHC class II antigen presentation — the same
   locus, two different downstream effector arms.
2. **Split the AD `Neuroinflammation` node** into a myeloid/microglial arm
   (`TREM2`/`TYROBP`/`SPI1`/`CD33`/`INPP5D`) and keep the existing adaptive
   `Adaptive Immune T Cell Response to Tau Pathology` node distinct. AD already
   has both; the genetics says the myeloid arm carries the causal weight.
3. **Add a PD adaptive-immune hypothesis group** (`EMERGING`) covering HLA class
   II → CD4+ T-cell recognition of α-synuclein, attached to PD's existing
   `Neuroinflammation` node.
4. **Do not create a shared "neuroinflammation" module** spanning AD and PD. The
   only defensible shared abstraction is narrower — MHC class II antigen
   presentation — and it is a single locus, not a pathway chain. A module needs
   more conformers than this.
5. **Consider an `Alzheimer_Disease__Parkinsons_Disease` comorbidity entry**
   carrying the rg = +0.117 signal, with LBD as the `UpstreamConditionHypothesis`
   — the rg ≈ +0.65 to both is a strong structured argument for exactly that
   shape.

## Interpretation limits

- **Association is not mechanism.** Nothing here supports a `downstream:` causal
  edge. These findings support gene–disease `SUSCEPTIBILITY` typing and node
  annotation only.
- **A null HuGE score is not "not involved."** `TNF` at 1.0 means common variation
  in `TNF` does not measurably alter AD risk. TNF may still be a central
  downstream effector — this analysis cannot see reactive processes, and most
  neuroinflammation is reactive. The correct claim is narrow: these genes are not
  *upstream genetic drivers*.
- **Power is unequal.** PD's GWAS is smaller than AD's; some AD-vs-PD contrasts
  partly reflect sample size, not biology. The disjointness in §4 is too clean to
  be power alone (PD detects `LRRK2` at 713, so it is not underpowered in general),
  but marginal comparisons should not be over-read.
- **Ancestry.** Results are `Mixed` or European-dominant. Not generalizable.
- **LBD is underpowered** — 0 records at p<1e-4. Its rg values are usable; its
  enrichment results are not.
- **The `SysBio_ADvPD` phenotype** ("Alzheimers disease (case) vs Parkinsons
  disease (control)") exists in the phenotype list and would be the ideal direct
  contrast, but returns no data on this BioIndex deployment. Worth asking the
  Flannick lab about — it is the single most relevant phenotype for this question.
- **PIGEAN gene-set indexes** (`pigean-*`) are registered but empty on this
  deployment, so the gene-set/latent-factor layer of this analysis could not be
  run. It would be the natural next step.

## Reproducing

```bash
BI=https://bioindex.hugeamp.org/api/bio/query
curl -sS "$BI/genetic-correlation?q=AD&limit=400"
curl -sS "$BI/gene-finder?q=Parkinsons&limit=1200"
curl -sS "$BI/huge?q=TREM2&limit=2000"
curl -sS "$BI/global-enrichment?q=AD&limit=6000"
curl -sS "$BI/partitioned-heritability?q=Parkinsons&limit=20000"
```

No API key required. See
[`projects/HUGEAMP_PARTNERSHIP.md`](../../projects/HUGEAMP_PARTNERSHIP.md) for the
platform survey and integration plan.
