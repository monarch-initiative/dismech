# OpenScientist hypothesis report review: canonical autoimmune thyrocyte destruction model

**Disease:** Hashimoto's Thyroiditis
**Hypothesis:** `canonical_autoimmune_thyrocyte_destruction_model` (status CANONICAL)
**Report:** `../openscientist.md` (558 lines, 41 cited PMIDs, run 2026-05-23)
**Assessor:** claude-opus-5, 2026-09-02
**Verdict:** SUPPORTED

## What the report gets right

The central mechanism holds. More usefully, this run does not simply agree with
the seed — it brings primary sources the disease entry had never cited. Not one
of its 41 PMIDs appeared anywhere in `kb/disorders/Hashimotos_Thyroiditis.yaml`
before this review.

I fetched and read 16 of the 41. Every one resolved to a real paper broadly
saying what the report says it says, including the seven identifiers above
PMID 41000000 that look implausible at a glance and are simply recent
(PMID:41748903 is *Nature Genetics* 2026; PMID:42039112 is *JCEM Case Reports*
2026). Four findings are strong enough to curate:

- **Intrathyroidal lymphoid follicles are functional germinal centres.**
  Armengol et al. compared them directly against tonsil and lymph node
  follicles, found complete mantle/light/dark zone architecture with follicular
  dendritic cells and high endothelial venules, showed most bind thyroglobulin
  and thyroperoxidase, and found unexpected RAG1/RAG2 expression implying local
  receptor revision (PMID:11549579).
- **Fas killing of thyrocytes is cytokine-gated.** Normal human thyrocytes
  block Fas signalling downstream of the proximal caspases; interferon gamma
  plus interleukin 1 beta lifts the block by raising surface Fas, procaspases
  7/8/10 and Bid (PMID:15563545).
- **The susceptibility architecture is far more polygenic than the entry
  implied.** 418 independent genome-wide significant signals across 81,718
  autoimmune hypothyroidism cases, with coding variants in LAG3, ZAP70 and TG
  among the leads (PMID:41748903) — which converges with the LAG3 variant the
  entry already curated from an independent source.
- **Two clinically real subtypes the entry did not address**: IgG4 thyroiditis
  (PMID:22555173) and seronegative disease (PMID:35377135, PMID:24743395).

## What is overstated, and one misread

**The checkpoint-inhibitor "natural experiment" misreads its source.** The
report says checkpoint blockade "produces thyroid destruction via the exact
pathways described in the canonical model" and calls this "powerful causal
validation". Pollack et al. conclude the opposite: the comparison "revealed
marked differences in pathway enrichment as well as in the predicted upstream
regulators", supporting the view that checkpoint-inhibitor thyroid disease
"represents a novel form of immune thyroid disease with distinct underlying
biological pathways and regulators" (PMID:37445704). Only the apoptosis arm
converged, and this is a murine lung-cancer model, not human Hashimoto tissue.
The clinical arm of the same argument — 92.9% of PD-1-inhibitor destructive
thyroiditis being TPOAb or TgAb positive — is reported accurately
(PMID:39216687).

**"Fas/FasL is the dominant killing pathway" is not what the cited papers
say.** Perforin independence holds. Dominance does not: PMID:11716038 found
killing "only partially dependent on Fas/Fas ligand" with a probable coexisting
caspase-independent route, and PMID:9274519 is a hedged one-paragraph
commentary. The same paper does establish something the report states once and
then drops — in Hashimoto glands the *lymphocytes*, not the thyrocytes, are the
effector killers, which argues against thyrocyte fratricide.

**The Th17 temporal claim outruns its evidence.** The Treg/Th17 imbalance and
its inverse correlation with autoantibody titres is solid human data
(PMID:25771887). "Th17 predominance precedes Th1-mediated tissue destruction"
is one sentence of a 2025 review's synthesis, and the report's own GAP 1
concedes the transition "lacks longitudinal human evidence" — which contradicts
the executive judgment calling the axis "now established as a critical upstream
event".

**418 signals and 5.4% of variance do not belong in one parenthesis.** The
5.48% figure is a seven-variable candidate-SNP model in 147 Polish cases and 147
controls, published six years before the meta-analysis and not derived from it
(PMID:29931474). Reeve et al. publish no such figure. As written the sentence
reads as though 418 signals jointly explain 5.4%, which nobody reported.

**The 88/12 seronegative split is one paediatric cohort.** 12.3% is 19 of 154
Italian children; the adult series reports no prevalence. Reading
antibody-negative serology as an "antibody-independent pathway" also goes past
the sources — and that paediatric paper notes its seronegative group is
clinically superimposable on overweight children with the same ultrasound
changes and no antibodies, a reversible condition.

**Provenance is thin.** "145 papers reviewed" against 41 cited, with no search
string, date filter or screening log; the "12 of 13 claims established" tally
never enumerates the 13 claims; all three referenced figures are unresolved
template placeholders with no committed artifact. The GenCC/ClinGen absence in
GAP 6 is asserted without any search record, and is in any case closer to a
scope boundary than a curation gap: those panels curate Mendelian gene-disease
validity, so an empty result for a complex polygenic trait is expected.

## Integration into the disease YAML

All changes are in `kb/disorders/Hashimotos_Thyroiditis.yaml`.

**Added.**

1. Two evidence items on the `canonical_autoimmune_thyrocyte_destruction_model`
   entry (PMID:41748903, PMID:29931474). The entry's `notes` already asserted
   the polygenicity refinement in prose with nothing behind it; these
   substantiate it, and the second carries an explicit scope caveat so the two
   numbers are not read as one result.
2. New pathophysiology node **Th17/Treg Imbalance**, bound to CL:0000899,
   CL:0000815, GO:0072539 (INCREASED) and GO:0045066 (DECREASED), with four
   evidence items and a downstream edge to `Lymphocytic Infiltration` carrying
   its own IL-17/IL-17RA evidence. An incoming edge was added from `Loss of
   Immune Tolerance to Thyroid Antigens`. Curated as an amplifier, not the
   initiating lesion; the precedence claim is graded `OTHER` as a review-level
   synthesis and the reason is recorded in the node `notes`.
3. New pathophysiology node **Cytokine-Sensitized Fas-Mediated Thyrocyte
   Apoptosis**, bound to CL:0002258 and GO:0008625, with three evidence items,
   an incoming edge from `Lymphocytic Infiltration` and an outgoing edge to
   `Autoimmune Thyroid Destruction`. Its `notes` record why "dominant killing
   pathway" was not carried over.
4. Two evidence items on `Lymphocytic Infiltration` for the germinal-centre and
   RAG claims, plus GO:0002467 on its `biological_processes`.
5. One evidence item plus a `notes` block on `Autoimmune Thyroid Destruction`
   recording the checkpoint-inhibitor transcriptomic result *with* the source's
   own distinct-pathways conclusion, so the existing ICI evidence item is not
   left implying a stronger parallel than the data support.
6. A new `discussions:` block (the entry had none) with five entries: the
   tolerance-breaking initiating event (KNOWLEDGE_GAP), the seronegative
   effector mechanism (KNOWLEDGE_GAP), IgG4 thyroiditis entity status
   (OPEN_QUESTION), sex-biased CXCL13-CXCR5 plasma B cell homing
   (EMERGING_HYPOTHESIS), and the absence of disease-modifying therapy
   (KNOWLEDGE_GAP, carrying the JAK-inhibitor case as the lead it is).

**Deliberately not done.**

- **No `status:` change.** The report recommends retaining CANONICAL, and the
  entry's `notes` already record all six qualifications the report raises.
- **No `has_subtypes` entries for IgG4 or seronegative disease.** Both are
  supported enough to record and not settled enough to model as subtypes: the
  IgG4 proportion comes from one thyroidectomy series, the seronegative
  proportion from one paediatric cohort, and whether either is a subtype of
  Hashimoto's thyroiditis or a separate entity is exactly the open question.
  Discussions are the honest home until comparative data exist.
- **No gut-thyroid-axis node.** The supporting citations are two narrative
  reviews and a mathematical model; the report itself grades the evidence
  "Low-Moderate". I did not verify the primary molecular-mimicry data and
  will not wire an edge on review-level assertion alone.
- **No NETosis, epigenetic-interface, or SARS-CoV-2 node.** Each rests on a
  review or a single case report in this run. The entry's HCV node already
  records in its `notes` that other candidate viruses including SARS-CoV-2 are
  proposed but not substantiated by its cited source, which remains accurate.
- **No JAK inhibitor treatment entry.** One patient, and the source claims only
  "possible reversal". It is recorded as the lead inside the
  disease-modifying-therapy knowledge gap instead.
- **Nothing from the GenCC/ClinGen absence.** An undocumented negative about
  panels whose remit does not cover complex polygenic traits.
- **The report's candidate ontology terms were not used as given.** GO:0002286
  and GO:0002504 were not needed; the terms actually bound were selected against
  the node claims and checked against this repository's term caches.
