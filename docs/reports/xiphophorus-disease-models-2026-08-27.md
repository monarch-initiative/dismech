# Xiphophorus as a Disease Model: Mechanisms It Elucidated (2026-08-27)

Survey of what the platyfish/swordtail genus *Xiphophorus* has actually established about
human disease mechanism, what remains contested inside the model, and what of it is now
curated in dismech.

The anchor reference is Schartl & Lu's 2024 review in *Disease Models & Mechanisms*
([PMID:38299666](https://pubmed.ncbi.nlm.nih.gov/38299666/)), which assesses the genus
against construct, face and predictive validity. Live stocks come from the Xiphophorus
Genetic Stock Center (XGSC) at Texas State University
([stock list](https://imls.txst.edu/stocks.html)).

## Summary

| Mechanism area | What the fish established | Status | In dismech |
|---|---|---|---|
| RTK→Ras/Raf/MAPK as the melanoma driver | Identified ~a decade before human confirmation | Established, predictive hit | `BRAF_V600_Mutant_Melanoma` |
| Osteopontin and the radial→vertical growth transition | First identified here; now a clinical prognostic marker | Established, predictive hit | `Metastatic_Melanoma` |
| Two-locus melanoma genetics (oncogene + tumour suppressor) | `Xmrk` released from `R/Diff` restraint | Established; suppressor identity revised | Partly |
| UV wavelength dependence of melanomagenesis | Direct DNA photoproducts, not melanin photosensitization | **Reversed within the model** | No — see gaps |
| MC4R dominant-negative signalling | Natural allelic series of graded receptor loss | Established | `Obesity_Due_to_MC4R_Pathway_Disruption` |
| Hybrid regulatory dysregulation as gene discovery | Surfaced *CLDN4*, *CASR*, *GCK* | Emerging method | No |
| OCA2 albinism | Phenotype only | Mechanism pending | No |

## 1. Melanoma — the flagship, and the reason the genus matters

Interspecies hybrids of *Xiphophorus* have been known to develop malignant melanoma since
1928 (Häussler; Kosswig; Gordon 1931), making this **the oldest vertebrate cancer model**.
The Gordon–Kosswig–Anders cross mates a spotted *X. maculatus* platyfish to *X. hellerii*
and backcrosses the F1 to the swordtail parent. The offspring segregate into four
Mendelian classes, and

> backcross segregants that have inherited only R/Diff-free chromosomes develop highly
> malignant melanoma due to unobstructed activity of Tu

([PMID:38299666](https://pubmed.ncbi.nlm.nih.gov/38299666/)).

### 1.1 The oncogene: `Xmrk`

Wittbrodt et al. cloned the `Tu` locus in 1989 and found

> The Tu gene codes for a novel receptor tyrosine kinase which is closely related to the
> receptor for epidermal growth factor.

with expression level tracking malignancy grade
([PMID:2797166](https://pubmed.ncbi.nlm.nih.gov/2797166/)). `Xmrk` arose by duplication of
the fish *egfr*; a new promoter plus two amino-acid substitutions made it
ligand-independent and constitutively active.

**The mechanistic payoff.** The dominant effector arm is Ras/Raf/MAPK, and this is the
genus's clearest predictive hit:

> studies of oncogenic Xmrk signaling predicted the role of the receptor tyrosine
> kinase/Ras/Raf/MAPK pathway as the critical driver for melanoma a decade before this was
> confirmed in humans

Because the driver enters the cascade upstream of RAF, the model separates *sustained MAPK
flux* from *the identity of the mutation producing it* — which is exactly why it
generalized to human melanoma, where ~70% of tumours run the same pathway through BRAF or
NRAS instead.

### 1.2 The tumour suppressor: `R/Diff` — and a correction worth noting

The second locus, `R`/`Diff`, restrains `Xmrk`; melanoma requires losing it. Its molecular
identity has moved:

- **`cdkn2ab` (CDKN2X)**, the fish *CDKN2A/p16* homologue, was the long-standing candidate,
  mapped to the implicated interval ([PMID:10753192](https://pubmed.ncbi.nlm.nih.gov/10753192/)).
  Notably it behaves *opposite* to the human locus — it is **overexpressed** in fish
  melanoma rather than silenced, plausibly as a response to `Xmrk` upregulation, and its
  CpG island is unmethylated.
- **Fine-mapping later narrowed `R/Diff` to a ~100 kb interval on linkage group 5
  containing three genes** (`cdkn2ab`, `rab3d`, `adgre5`), and RNA-seq found that *only
  `rab3d`* is expressed in the nevus-like spots and in the benign and malignant lesions
  ([PMID:38299666](https://pubmed.ncbi.nlm.nih.gov/38299666/)).

Curators citing this model should not present `cdkn2ab` as the settled `R/Diff` gene.

### 1.3 Osteopontin and dermal invasion

A melanocyte that leaves the epidermis normally dies in dermal collagen. Using the
`Xmrk`-driven system, Geissinger et al. identified what lets it survive:

> In melanocytes, expression of the secreted adhesion protein OPN was up-regulated by the
> melanoma-inducing receptor tyrosine kinase Xmrk

> Addition of exogenous OPN allowed melanocytes to adhere, spread, and survive in
> three-dimensional collagen gels, whereas in the absence of OPN, the cells underwent
> apoptosis.

([PMID:12183442](https://pubmed.ncbi.nlm.nih.gov/12183442/)). OPN acts through integrin
αvβ3. The review records the translational outcome: osteopontin

> was first identified in Xiphophorus melanoma as a key factor for the transition from
> radial to vertical growth

and is now used clinically as a prognostic marker. This is the genus's second predictive
hit, and the more concrete one — a specific molecule, not a pathway.

### 1.4 Face validity worth knowing

Fish melanomas arise from **epidermal melanocytes** and progress nevus → radial growth →
vertical growth, matching the human sequence. Mouse melanoma models generally initiate in
the hair follicle bulb, so on lesion architecture the fish is closer to human disease than
the mouse is.

## 2. UV etiology — including a reversal inside the model

This is the most instructive episode, and the one most often cited stale.

**The original claim (1993).** Setlow et al. irradiated backcross hybrids at discrete
wavelengths and derived an action spectrum for melanoma induction:

> Heavily pigmented backcross hybrids of the genus Xiphophorus (platyfish and swordtails)
> are very sensitive to melanoma induction by single exposures to UV.

They reported appreciable sensitivity at 365, 405 and possibly 436 nm and concluded that
light absorbed **in melanin** drove melanomagenesis, attributing 90–95% of induction to
wavelengths >320 nm — i.e. UVA and visible
([PMID:8341684](https://pubmed.ncbi.nlm.nih.gov/8341684/)). This result was influential in
sunscreen and tanning-bed policy debate.

**The reversal (2010).** Mitchell et al. re-ran the wavelength dependence in the
Sp-couchianus backcross:

> Whereas ultraviolet B (UVB) irradiation of neonates yielded high frequencies of melanomas
> in pigmented fish, UVA irradiation resulted in melanoma frequencies that were not
> significantly different from unirradiated fish.

> These data are consistent with an essential role for direct DNA damage, including
> cyclobutane dimers and (6-4) photoproducts, in the etiology of melanoma.

([PMID:20439744](https://pubmed.ncbi.nlm.nih.gov/20439744/)). Supporting this, neonatal
UVB followed immediately by visible/blue light — which lets fish photolyase repair
photoproducts *in situ* via photoenzymatic repair — cut melanoma incidence by 50% in this
model and to background levels in others.

**So the model's current position is:** direct UVB-induced pyrimidine dimers, not melanin
photosensitization, initiate melanoma. Cite the 2010 result, not the 1993 action spectrum,
for the mechanism.

**A useful negative result.** Deficient global nucleotide excision repair looked like the
obvious explanation for hybrid susceptibility — F1 hybrids repair (6-4) photoproducts far
worse than either parent (~18% vs ~48–64%). But measured per individual:

> we found no difference in mean NER capacity between fish with and without melanomas, thus
> detaching global NER from melanomagenesis

([PMID:21143485](https://pubmed.ncbi.nlm.nih.gov/21143485/)) — fish with 13% and with 88%
repair capacity both developed melanoma. Individual DNA repair capacity is not the risk
axis, even where the photoproducts clearly are causal. This is a real constraint on the
"DRC predicts melanoma risk" hypothesis in humans.

## 3. MC4R — a natural allelic series for a dominant-negative receptor

*X. multilineatus* and *X. nigrensis* males come in size classes set by a single Mendelian
locus `P` controlling puberty onset. Lampert et al. showed:

> We show that sequence polymorphisms of the melanocortin receptor 4 gene (mc4r) comprise
> both functional and non-signal-transducing versions and that variation in copy number of
> mc4r genes on the Y chromosome underlies the P locus polymorphism.

> Nonfunctional Y-linked mc4r copies in larger males act as dominant-negative mutations and
> delay the onset of puberty.

([PMID:20869245](https://pubmed.ncbi.nlm.nih.gov/20869245/)).

**Why this is useful for human obesity.** Heterozygous *MC4R* variants are found in ~1–5% of
severely obese people, and their severity is not explained by simple haploinsufficiency.
The fish provide a *naturally occurring graded allelic series* in which non-signalling
copies suppress a co-expressed functional receptor — the dominant-negative mechanism, on a
wild-type genetic background rather than an engineered one.

**The honest limitation:** fish do not get fat. The readout is delayed puberty and
prolonged somatic growth, not adiposity. The model speaks to the *receptor-signalling
lesion* and to the energy-balance/reproduction link the authors draw explicitly — not to
the clinical endpoint.

## 4. Emerging and secondary areas

- **Obesity (nuchal hump).** *X. multilineatus* males on high-calorie diets develop a
  nuchal fat deposit; transcriptomics show differential expression of appetite, metabolism
  and lipid-regulation genes. A maladaptation-to-caloric-abundance model, still early.
- **Albinism.** An *X. hellerii* strain shows eye and skin depigmentation resembling human
  OCA2. The review is explicit that the molecular mechanism is still being studied — **do
  not curate a mechanism claim here yet.**
- **Hybrid regulatory dysregulation as a gene-discovery engine.** Epistasis between
  divergent *cis* and *trans* regulatory elements in hybrids produces transgressive
  expression. Screening this surfaced *CLDN4* (ovarian cancer), *CASR* (inflammation,
  hypertension, obesity) and *GCK* (MODY). This is a method for nominating disease genes,
  not a disease model as such.
- **Fin regeneration.** BMP-driven lepidotrichia regeneration with *Tp63* maintaining
  quiescence in the wounded basal epidermis, consistent with mammalian function.
- **Pigment pattern / neural crest.** A chromosome-17 locus for caudal-fin pattern in
  *X. maculatus* × *X. couchianus* intercrosses, hypothesized to act on neural crest
  differentiation and migration.

## 5. The stocks, and why the lines matter

XGSC lines are not interchangeable; the genetics of the cross *is* the model.

| Line | Why it matters |
|---|---|
| *X. maculatus* Jp163A / Jp163B | The `Tu`-carrying parents. 122nd / 113th generation inbred, maintained for defined segregating sex-linked and autosomal traits. Jp163B is the Sp (spotted-side) source for the UVB model. |
| *X. couchianus* | `Tu`-free partner, 71st generation full-sib inbred and effectively homozygous throughout. **Extinct in the wild** — the stock is the species. Recurrent parent of the Sp-couchianus UVB backcross. |
| *X. hellerii* Cd | Recurrent parent of the classical Gordon–Kosswig–Anders cross; >50 generations inbred. |
| *X. variatus* Zarco | Develops melanoma **without hybridization** — P-2 homozygotes form melanotic nodules from ~1.5 years. A spontaneous, non-hybrid comparator. |
| *X. cortezi* | Some Sc males develop melanosis and small melanomas. |
| HeLi (*X. variatus* Lineatus × *X. hellerii* Lancetilla backcross) | Constructed backcross hybrid line. |

The inbreeding depth is the point: an effectively isogenic `Tu`-free recipient makes the
one-locus-at-a-time genetics tractable in a way an outbred stock would not.

## 6. What was curated into dismech from this survey

| Entry | Added | Node | Relationship |
|---|---|---|---|
| `BRAF_V600_Mutant_Melanoma` | `animal_models`: Gordon–Kosswig–Anders backcross hybrid | `Sustained MEK-ERK Signaling` | `PARTIALLY_RECAPITULATES` |
| `Metastatic_Melanoma` | `experimental_models`: Xmrk-activated melanocytes in 3D dermal collagen | `Invasive Plasticity and Migration` | `PARTIALLY_RECAPITULATES` |
| `Obesity_Due_to_MC4R_Pathway_Disruption` | `animal_models`: Y-linked `mc4r` copy-number polymorphism (P locus) | `MC4R pathway signaling failure` | `PARTIALLY_RECAPITULATES` |

All three are `PARTIALLY_RECAPITULATES` deliberately: in each case the model reproduces the
*mechanism node* while diverging from the human disease on the driver (Xmrk vs BRAF), the
compartment (collagen gel vs vascularized dermis), or the endpoint (puberty timing vs
adiposity). Each link carries explicit `limitations`.

## 7. Gaps this survey opened

1. **No home for the UV melanoma etiology finding.** The KB has BRAF/NRAS/KIT-mutant,
   metastatic, uveal and ocular melanoma entries, plus melanoma in congenital melanocytic
   nevus — but no general cutaneous melanoma entry carrying UV etiology. The CMN entry's
   `UV Exposure` node is explicitly weak (its own evidence notes CMN melanoma has a distinct,
   largely non-UV pathogenesis), so attaching the Xiphophorus UVB result there would be
   wrong. This is the single strongest uncurated Xiphophorus contribution.
2. **The NER negative result has no natural home either.** `Xeroderma_Pigmentosum` has
   `UV-induced DNA photoproduct formation` and `Impaired nucleotide-excision repair` nodes,
   but the fish finding *detaches* individual repair capacity from melanoma risk. It would
   belong as a `discussions` entry of kind `KNOWLEDGE_GAP` or `HUMAN_MODEL_MISMATCH` rather
   than as a model link.
3. **`R/Diff` is not curated anywhere,** despite the two-locus oncogene/suppressor logic
   being the model's core genetic insight — and its molecular identity is unsettled
   (`rab3d` now better supported than `cdkn2ab`).
4. **Albinism is deliberately excluded** pending a published mechanism.

## References

| ID | Use |
|---|---|
| [PMID:38299666](https://pubmed.ncbi.nlm.nih.gov/38299666/) | Schartl & Lu 2024, *Dis Model Mech* — validity review, anchor for the whole survey |
| [PMID:2797166](https://pubmed.ncbi.nlm.nih.gov/2797166/) | Wittbrodt et al. 1989, *Nature* — `Xmrk` is an EGFR-related RTK |
| [PMID:10753192](https://pubmed.ncbi.nlm.nih.gov/10753192/) | Kazianis et al. 2000, *Carcinogenesis* — fish CDKN2 overexpressed in melanoma |
| [PMID:12183442](https://pubmed.ncbi.nlm.nih.gov/12183442/) | Geissinger et al. 2002, *Cancer Res* — osteopontin and dermal survival |
| [PMID:8341684](https://pubmed.ncbi.nlm.nih.gov/8341684/) | Setlow et al. 1993, *PNAS* — original melanoma action spectrum (superseded) |
| [PMID:20439744](https://pubmed.ncbi.nlm.nih.gov/20439744/) | Mitchell et al. 2010, *PNAS* — UVA does not induce melanoma; UVB does |
| [PMID:21143485](https://pubmed.ncbi.nlm.nih.gov/21143485/) | Fernandez et al. 2011, *Photochem Photobiol* — global NER is not the risk axis |
| [PMID:20869245](https://pubmed.ncbi.nlm.nih.gov/20869245/) | Lampert et al. 2010, *Curr Biol* — `mc4r` dominant-negative copies and puberty |
