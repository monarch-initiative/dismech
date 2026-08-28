# PhysioMap: assessment and relevance to dismech (2026-08-23)

**Subject.** Hoehndorf R, Schofield PN, Gkoutos GV. *PhysioMap: an ontology-grounded causal
knowledge graph of human physiology.* bioRxiv preprint, posted 2026-08-07.
[doi:10.64898/2026.08.03.742471](https://doi.org/10.64898/2026.08.03.742471) ·
[code + OWL release](https://github.com/bio-ontology-research-group/physiomap/) ·
[interactive demo](https://bio2vec.net/physiomap/). Code BSD-3-Clause; map, benchmark
data, and docs CC BY 4.0. To appear in a PSB-style proceedings volume (© 2027).

**How to read this document.** It has three layers, kept deliberately separate because
conflating them is misleading:

| Part | Source | What it is |
|---|---|---|
| **I** (§1) | the preprint only | What the authors claim and how they say they built and evaluated it |
| **II** (§2) | their public repo | Their actual working artifacts — curation files, evidence records, the archived expert review |
| **III** (§3) | my own computation | Analyses I ran over the v1.1.1 release that are **not** in the paper |
| **IV–V** (§4–5) | this repo | Comparison with dismech and recommendations |

Nothing here modifies a KB entry, schema file, or cache.

**Bottom line.** PhysioMap and dismech are close to *structural duals*, and the difference
is not subject matter — it is what an edge means and what a node names. dismech has over 11×
PhysioMap's edge count but cannot run PhysioMap's central inference, because dismech causal
edges carry **directness without polarity** and dismech nodes are **file-scoped strings
rather than a shared variable namespace**. Those are two separable gaps, and the first is
much cheaper to close than the second.

Their curation discipline is worth studying independently of the schema question: every
imported edge carries a machine-checkable provenance record, failed checks are recorded
rather than dropped, and the expert review is archived down to the sha256 of the returned
spreadsheet (§2).

---

# Part I — What the paper says

## 1. The claims and method as published

### 1.1 There are five distinct graph objects, not one

The paper is careful about this and it is the part most easily blurred. One knowledge base
is built, and several different graphs are *derived* from it:

| Object | What it is | Size |
|---|---|---|
| **K** | OWL 2 EL TBox. Not a graph — a terminology of trait classes and axioms | 1,699 traits + relation axioms |
| **CKG** | The projected typed causal knowledge graph, produced from K by a versioned pattern registry Π | 1,699 nodes, 2,387 typed relation instances |
| **G∂ = (V, E∂)** | **Signed dependency graph.** Causal influence + production + quantitative identity only. Defines the signed Jacobian | cyclic; largest SCC = 213 traits |
| **Gκ = (V, C)** | **Constitutive dependency graph.** Shares vertices with G∂ but deliberately does **not** enter the causal Jacobian | acyclic by construction |
| **H ⊆ V × Ec** | Modulation — (node, edge) pairs, i.e. hyperedges. The first-order solver does **not** read these | 19 |

At query time two more are derived: **G∂^do(k)**, which is G∂ with the intervention target's
incoming edges cut, and the **condensation** of that into a DAG of strongly connected
components, processed in topological order.

Why constitution is split into its own graph: an intervention on a *whole* must replace the
whole's defining equation, not propagate backwards into its parts. Body weight rising must
not imply adipose mass rose. Determination therefore flows along Gκ in topological order
only, and because scales are strictly hierarchical, Gκ has no cycles.

### 1.2 Trait semantics

A trait is the entity–quality (EQ) pattern used by HPO/MP: a PATO quality borne by an entity
or process in a recorded context —
`Trait ⊓ ∃hasPart.(E ⊓ ∃κ.C ⊓ ∃hasQuality.Qᴱ)`, where `κ` is `contextPartOf` for continuants
and `occursIn` for processes (`occursIn ∘ partOf ⊑ occursIn`, so process location propagates
along parthood). Entity classes come from ChEBI, PR, CL, Uberon, GO; qualities from PATO.
The context conjunct is omitted when no context is recorded.

Causal claims are asserted type-level via the *collection pattern*
(`T_tᵃˡˡ ⊑ ∃hasMember.(∃causedBy.T_s)`) rather than the stronger `T_t ⊑ ∃causedBy.T_s`,
which would claim every instance of the target is so caused. The naive subclass axiom is the
*wrong claim*, not merely an expensive one; the collection form also stays in OWL 2 EL.

### 1.3 The five relation types and their SCM readings

The paper's core claim is that typing a relation determines what an intervention replaces:

| Relation | Quantitative constraint | Enters causal Jacobian? |
|---|---|---|
| Causal influence | target mechanism Ft depends non-constantly on xs; σ = sign(∂Ft/∂xs) | yes |
| Production | Ft = Rt + εpt·qpt(xp), q′ > 0, ε ∈ {−1,+1} | yes |
| Quantitative identity | Xq = Qq(Xa₁…Xaℓ) — a named variable *is* a function of its arguments | yes |
| Constitution | Xw = Cw(Xp₁…Xpr) — a whole determined by its constituents | **no** (separate Gκ) |
| Modulation | mixed partial: sign(∂²F̃t/∂η∂θ) = µ | **no** (retained in H, unread) |

Sign values are `{+, −, 0, ?}`. `?` means non-constant dependence with **no sign constraint**
— it is a positive claim, not a curation gap.

### 1.4 Every example edge the paper actually gives

This is a short list — the paper contains roughly twenty example edges in total.

**Table 1, one per relation type:**

- *Causal influence* — "More plasma ACE directly raises plasma angiotensin II: D_ACE,AngII > 0"
- *Production* — "A higher adrenal aldosterone-secretion rate raises plasma aldosterone"
- *Constitution* — "Adipose-tissue mass contributes positively to total body weight"
- *Quantitative identity* — "Mean arterial pressure = cardiac output × total peripheral
  resistance; both partial derivatives are positive"
- *Modulation* (§2.3 text) — "higher cortisol makes a fixed increase in norepinephrine
  produce a larger increase in total peripheral resistance"

**Figure 1** is the only neighbourhood the paper draws: an intervention `do(plasma ACE↓)`
with incoming edges cut, split into a whole-body loop and an intracellular arm. (The PDF
figure text extracts out of order, so the signs below were verified against the release
rather than read off the figure.)

*Whole-body RAAS / baroreflex loop:*
```
renal perfusion pressure                --[-]--> plasma renin activity
plasma renin activity                   --[+]--> plasma angiotensin II
plasma angiotensin II                   --[+]--> plasma aldosterone
plasma angiotensin II                   --[+]--> renal tubular sodium and water reabsorption
plasma aldosterone                      --[+]--> renal tubular sodium and water reabsorption
renal tubular sodium/water reabsorption --[+]--> blood volume
blood volume                            --[+]--> venous return
venous return                           --[+]--> cardiac output
mean arterial pressure                  --[+]--> renal perfusion pressure
mean arterial pressure                  --[+]--> baroreceptor afferent firing
baroreceptor afferent firing            --[-]--> baroreflex sympathetic outflow
baroreflex sympathetic outflow          --[+]--> plasma renin activity
```

*Intracellular effector arm setting TPR:*
```
plasma angiotensin II              --[+]--> AT1 receptor activation
AT1 receptor activation            --[+]--> cytosolic free calcium
cytosolic free calcium             --[+]--> myosin light-chain phosphorylation
myosin light-chain phosphorylation --[+]--> vascular smooth muscle contractile tone
vascular smooth muscle tone        --[+]--> total peripheral resistance
plasma ACE                         --[-]--> plasma bradykinin
plasma bradykinin                  --[+]--> endothelial nitric oxide production
vascular smooth muscle cGMP        --[-]--> cytosolic free calcium
```

ACE is a well-chosen example precisely because inhibition lowers angiotensin II *and* raises
bradykinin — two routes to TPR pulling the same way by different mechanisms.

Figure 1 also carries the two non-causal types explicitly: a double line for the
quantitative identity `MAP = CO × TPR`, and a dash-dot line for a modulation on the
*inhibitory* baroreceptor→sympathetic edge (in the release: modulator = plasma angiotensin
II, mixed-derivative sign `+`).

**Figure 2a**, the one worked prediction — HFE haemochromatosis:
```
do(hepcidin ↓)
plasma hepcidin      --[-]--> ferroportin (SLC40A1) iron-export activity   ⇒ ferroportin ↑
ferroportin activity --[+]--> plasma iron                                  ⇒ plasma iron ↑   ✓ HPOA
plasma iron          --[+]--> transferrin saturation (TSAT)                ⇒ TSAT ↑          ✓ HPOA
```
The release also holds `TSAT --[+]--> hepcidin`, closing the loop; the figure omits it
because the intervention cuts hepcidin's incoming edges.

### 1.5 How the paper says the content was built

Four routes (§2.5):

1. **Direct expert curation.**
2. **Extraction from quantitative models** — the cardiovascular core used **17 Guyton
   BioModels modules and CellML integrators**. "Available equations supplied derivatives" —
   the sign is read off a model's partial derivative rather than judged.
3. **Curated databases** — SIGNOR and AOP-Wiki, "directional sources [that] supplied
   constraints without complete functions": a sign but no function.
4. **Checked language-model proposals from textbooks.** An LLM proposes edges from
   textbooks; the proposals are then checked.

Trait creation is a separate pipeline: each candidate gets an entity identifier, a PATO
determinable, an optional context, a stable label, and a scale; identifiers are resolved
against pinned ontology releases; **measurement kind** is classified as extensive / ratio /
rate / intensive; bearer and quality categories are checked for compatibility; duplicates
are reconciled. Measurement kind has teeth — only composable kinds admit part-to-whole
rules, which is why volume composes over parts and pressure does not. Unresolvable traits
stay "explicitly primitive".

Release checks cover schema, references, identifiers, bearers, constitution, relation
typing, and regression against a frozen behavioral baseline. The authors state these "assess
formal consistency, not the scientific correctness of every axiom."

### 1.6 The evidence model is an admission gate, not content

§2.6, and the design decision is stated twice in the paper: evidence governs whether a
relation is **admitted**, and is then used by nothing downstream. Neither the reasoner nor
the solver reads evidence class or provenance. A relation's semantics comes from its type,
arguments, and context; its sign constrains a derivative.

Six admissible classes for causal influence, in two groups:

- **Interventional** (a manipulation or valid instrument): perturbation, pharmacological
  intervention, genetic loss/gain of function, Mendelian randomization
- **Mechanistic**: mechanistic-model evidence (sign derived from a curated model),
  curated-mechanistic evidence (a curated functional or mechanistic account)

Explicitly insufficient alone: association, coexpression, binding. Support not yet mapped to
a controlled class stays "unclassified" rather than being backfilled. Each stable relation
id links to its support and a projection trace.

### 1.7 How they evaluate

**(a) Expert content review.** A co-author (P.N.S.) reviewed a fixed-seed **stratified
sample of 83 relations** across all five types, marking TRUE (accepted) / FALSE? (flagged) /
FALSE (rejected). Unequal sampling rates preclude a map-wide accuracy estimate.

**(b) Forward prediction against HPO.** The reference construction is the interesting part:

- Per gene, specify one or more **primary lesion variables** from gene-product identity plus
  disease mechanism.
- HPO classes follow the same EQ pattern, so a class is *directional* when its quality states
  an increase or decrease. `PATO:0002300` → `+`, `PATO:0002301` → `−`. Hypoglycemia = blood
  glucose + decreased concentration.
- HPOA annotations propagate **upward only** through the subclass hierarchy — a specific
  annotation contributes an ancestor's mapping, never a descendant's.
- A gene–variable direction is retained **only when the resulting set is a singleton**.
- The intervened variable is not scored.
- Two deoxycortisol terms were hand-blocked because their asserted HPO ancestry would
  otherwise map them onto cortisol.

Metrics: `precision = C/(C+W)`, `coverage = (C+W)/(C+W+A)`; a missing prediction and a `?`
both count as abstention. Two baselines run on the *same* axioms and interventions, so the
comparison isolates the inference rule: **shortest signed path** (pick one shortest directed
path, multiply edge signs) and **signed diffusion** (`r = (1−α)(I−αS)⁻¹e`, α = 0.85, S the
column-normalized signed adjacency, sign(rᵢ) the prediction, |rᵢ| the confidence, swept for
a precision–coverage curve).

**(c) Abduction.** A closed pool of 175 single-lesion hypotheses, always containing the true
lesion. Agreement +1, contradiction −1, **abstention 0**; rank by net agreement, then fewer
contradictions, then more agreements. Note the scoring *rewards* abstaining — withholding
beats guessing wrong.

**(d) Relation-type ablation.** Both tasks re-run while cumulatively adding production,
quantitative identity, and constitution to causal influence.

### 1.8 Reported results

v1.1.1: 1,699 traits; 2,270 causal-influence, 85 production, 4 constitution, 9
quantitative-identity, 19 modulation axioms → 1,699 nodes and 2,387 relation instances.
Largest SCC 213 traits.

- **Expert review:** 69 accepted, 12 flagged, 2 rejected (both causal) of 83.
- **Forward prediction:** before exclusions, 175 determinate, 171 agreeing (97.7%).
  Discrepancy review found 3 of the 4 disagreements conflicted with the cited primary
  literature and 1 varied across studies; all 4 dropped *uniformly for every method*,
  leaving 866 adjudicated pairs. On that set: **171 determinate, 171 correct, 0 wrong, 695
  abstentions — 100% precision at 19.7% coverage.** Excluding the 15 highest-overlap genes
  left 151 determinate, all concordant.
- **Baselines:** shortest signed path 375 directions, 292 correct, 83 wrong (77.9%). Signed
  diffusion retained errors at matched prediction counts.
- **The abstention result.** On the 171 pairs where the solver committed, the path rule gave
  the same answer (0% error). On 204 pairs where the solver abstained, the path rule was
  right 121 times (40.7% error). An exact within-gene conditional permutation test — holding
  each gene's counts of path errors and abstentions fixed, permuting abstention labels within
  gene — rejected independence at **P = 2.05 × 10⁻⁷**. The claim is that abstentions
  *concentrated the hard cases*, not that the solver wins when both commit.
- **Abduction:** solver 40 unique top-1, 127 best-tied top-3, 161 top-10, MRR 0.707; shortest
  path 30/94/105/0.535; diffusion 30/99/110/0.558; chance 1/3/9/0.033.
- **Ablation:** the full first-order relation set changed **4 of 866** forward calls (no sign
  flip) and 12 of 163 inverse ranks, with no aggregate improvement.

### 1.9 Limits the authors themselves state

Unusually forthright, and not to be softened in retelling:

- **100% precision is at 19.7% coverage, on an adjudicated reference.** Four reference
  directions were removed post hoc after literature review. The exclusion was applied
  uniformly and reported as post hoc — the right procedure — but the headline is not
  "PhysioMap is never wrong."
- **The reference is not independent.** PhysioMap curation and HPOA may draw on the same
  literature; the 15-gene exclusion mitigates but does not remove this.
- **Abduction used a closed pool** always containing the true lesion, and top-*k*/MRR use the
  best position within a tie — optimistic for every rule compared.
- **Relation typing barely mattered on these tasks** (the ablation above). The richer typing
  is justified by semantics and by what it *will* enable, not by measured benchmark gain.
- Proof of concept, **not clinical readiness**.

---

# Part II — What their repository shows

## 2. Working artifacts

The repo contains substantially more than the paper describes, and the curation discipline
on display is the part most directly transferable to dismech.

### 2.1 Where the content actually lives

Not in the OWL. The source of truth is hand- and agent-curated YAML under `benchmarks/`:
**56 files in `human/systems/`** (one per physiological system — `thyroid.yaml`,
`iron_hepcidin.yaml`, `calcium_pth.yaml`, `respiratory_acidbase.yaml`,
`purine_urate_metabolism.yaml`, …), **6 in `human/curated/`** (the bulk imports), plus
`guyton/` and `multiscale/`. 2,358 causal edges across the YAML, projecting to the 2,268 in
the released graph.

`benchmarks/human/curated/README.md`, in full:

> "Merged curator contributions land here (see `scripts/curation_merge.py`). Each is a
> DRAFT FOR DOMAIN REVIEW that passed the full pre-deploy gate suite before being committed."

Every import file carries a `*** DRAFT FOR REVIEW ***` banner in its header.

### 2.2 IEM enzyme edges are Rhea-grounded, with a documented sign convention

`e1a_iem_reactions.yaml` — the largest content block — states its rule in the header:

```
# SIGN CONVENTION (comparative statics, d[metabolite]/d[enzyme_activity]):
#   enzyme_activity -(-)-> SUBSTRATE  (LoF => substrate ACCUMULATES)
#   enzyme_activity -(+)-> PRODUCT    (LoF => product FALLS)
# Physiological flux direction was curated per enzyme (can reverse the canonical Rhea
# equation, e.g. CPT2 vs CPT1A on plasma_palmitoylcarnitine -> opposite signs).
```

That last line is the non-mechanical part: the same Rhea equation yields opposite signs for
CPT1A and CPT2 depending on which way flux actually runs in vivo. A record:

```yaml
- source: cyp21a2_activity
  target: plasma_17ohp
  sign: '-'
  causal_evidence: curated_mechanistic
  mechanism: 'RHEA:50308 (EC 1.14.15.15): 17alpha-hydroxyprogesterone + reduced
    [NADPH--hemoprotein reductase] + O2 = 11-deoxycortisol + ...;
    17alpha-hydroxyprogesterone is the substrate'
  evidence: '21-hydroxylase deficiency (congenital adrenal hyperplasia), OMIM:201910
    — LoF causes massive 17-hydroxyprogesterone accumulation in plasma'
```

### 2.3 Textbook extraction is an LLM fan-out with verbatim quotes

`williams_extracted.yaml` describes its own method:

> "DRAFT within-scale signed causal edges + variables extracted from Williams Textbook of
> Endocrinology, 14th ed. via per-chapter multi-agent fan-out. Signs adversarially verified;
> every edge carries a verbatim quote + chapter/page anchor. New nodes de-duplicated against
> the existing map (`physiomap_core.reconcile`)."

```yaml
- source: type_3_deiodinase_activity
  target: free_t3
  sign: -
  causal_evidence: genetic_lof_gof
  mechanism: Type 3 iodothyronine deiodinase (DIO3) removes an inner-ring iodine from T3,
    inactivating it; overexpression (GoF) in infantile hepatic hemangiomas consumes T3
    faster than the thyroid can produce it, causing consumptive hypothyroidism
  evidence: "Large infantile hepatic hemangiomas express high D3 levels, causing
    'consumptive hypothyroidism,' because thyroid hormone is inactivated at a more rapid
    rate than it can be produced"
    — Williams Textbook of Endocrinology, 14th ed., ch 1, p 11
```

Verbatim quote plus page anchor — structurally the same discipline as dismech's snippet
rule, applied to a book rather than an abstract. Same companion files exist for Guyton &
Hall (`hall_extracted.yaml`) and West (`west_extracted.yaml`).

Some `mechanism` fields spell out an explicit quality→disposition→process→quality chain,
e.g. for phosphorylase kinase: *"quality: PHK activity → disposition: phosphotransfer
competence → process: phosphorylation of Ser-14 on glycogen phosphorylase → quality:
glycogen phosphorylase catalytic activity"*.

### 2.4 AOP-Wiki edges cite Key Event Relationships by UUID

```yaml
- source: hepatic_t4_clearance_rate
  target: plasma_t4
  sign: -
  causal_evidence: curated_mechanistic
  evidence: AOP-Wiki KER 035747ab-b591-4283-acfd-90ba868d5fc4; AOPs: 'Upregulation of
    Thyroid Hormone Catabolism via Activation of Hepatic Nuclear Receptors...' — KER:
    increased T4 clearance from serum (liver/organ) -> decreased serum T4 (organ_system);
    do(hepatic T4 clearance rate up) -> serum T4 down (sign -) | No PMID in batch |
    *** DRAFT FOR REVIEW (imported) ***
```

Note `| No PMID in batch |` — a recorded gap rather than a silent one.

### 2.5 The SIGNOR import uses `precursor of`, not signalling

SIGNOR is a signalling resource (protein→protein activation/inhibition), so it is reasonable
to wonder what it is doing supplying metabolite→metabolite edges. The answer is that **the
signalling content was not used at all.** The file is `signor_metabolism_import.yaml` and
describes itself as "steroidogenesis / amino-acid / pyrimidine / sterol metabolism". All 22
edges come from SIGNOR's **`precursor of`** relation — a chemical-conversion mechanism
SIGNOR carries alongside its protein interactions. Every edge is CHEBI→CHEBI except one
(PR:P23109 AMPD1 → CHEBI:16027 AMP).

```yaml
- source: plasma_17_hydroxypregnenolone
  target: plasma_17ohp
  sign: +
  causal_evidence: curated_mechanistic
  mechanism: 'precursor of: 3beta-HSD/HSD3B isomerase converts 17alpha-hydroxypregnenolone
    (delta-5) to 17alpha-hydroxyprogesterone (delta-4)'
  evidence: 'SIGNOR-268639: ... PMID 2139411 (Lorence et al. 1990 Endocrinology 126:2493):
    resolves OK; abstract explicitly confirms ''catalyzed the conversion of
    17 alpha-hydroxypregnenolone to 17 alpha-hydroxyprogesterone'' — concordant.
    Both nodes organ_system scale. INDRA: unreachable. *** DRAFT FOR REVIEW (imported) ***'
```

Three practices worth copying, all visible in that one record: the SIGNOR id is kept, the
PMID is independently checked to **resolve** *and* to be **concordant with the claim**, and a
failed cross-check (`INDRA: unreachable`) is recorded rather than omitted.

The header also records what was discarded — "Cross-scale/duplicate/pituitary-mediation-
conflicting candidates were dropped" — and the import was "validated by fan-out agents
(ontology IDs vs OBO, PMID existence+concordance vs PubMed, sign, scale)."

One honest failure is preserved in place: two of the 22 edges cite `NBK536726`, an NCBI
Bookshelf ID rather than a PMID. The file says `pmid_ok=false` and keeps the edge, justified
as "well-established biochemistry (PAH, phenylalanine hydroxylase)". Recorded, not hidden —
but it is a retained failure, and it covers the Phe→Tyr edge.

### 2.6 Evidence classes, as actually used

Counting `causal_evidence` across all 2,358 source edges:

| Class | Group | Edges | Share |
|---|---|---:|---:|
| `genetic_lof_gof` | interventional | 915 | 38.8% |
| `curated_mechanistic` | mechanistic | 552 | 23.4% |
| `pharmacological` | interventional | 319 | 13.5% |
| *(none — legacy unclassified)* | — | 206 | 8.7% |
| `mechanistic_model` | mechanistic | 206 | 8.7% |
| `perturbation` | interventional | 160 | 6.8% |
| **`mendelian_randomization`** | interventional | **0** | **0%** |

Mendelian randomization is defined in the paper and in `physiomap_core/causal_evidence.py`
and used **zero times**. Interventional evidence covers 59% of edges.

`causal_evidence.py` also enumerates the refused classes with reasons — `binding_only`
("ChIP-seq / motif occupancy: physical binding is not a demonstrated functional effect"),
`coexpression`, `observational_association`, `unknown` — and adds a rule not in the paper:
a **modulation edge always requires a class**, with no equivalent of the hand-curated
"no class" pass an ordinary edge may take. The stated reason is that a modulation asserts a
two-factor interaction, and "a correlation of slopes is not" one.

### 2.7 The expert review is archived in full

`benchmarks/results/expert_gold_review.tsv` holds all 83 rows with verdicts and comments.
The summary records reviewer (Paul N. Schofield), sample sent 2026-07-28, returned
2026-07-30, sampling seed 20260728, sha256 of both the sent template and the returned
workbook, the reviewer's email Message-ID, and an integrity check confirming
`identity_columns_unchanged: true`, 83/83 verdicts, 39 comments.

The sampling rates make the "no map-wide accuracy estimate" caveat concrete:

| Type | Reviewed | In map | Rate |
|---|---:|---:|---:|
| constitution | 4 | 4 | **100%** |
| quantitative | 9 | 9 | **100%** |
| modulation | 10 | 19 | 53% |
| production | 10 | 85 | 12% |
| causal | 50 | 2,268 | **2.2%** |

(Raw verdict strings are slightly inconsistent — `TRUE` 68, `True` 1, `FALSE?` 11, `False?`
1, `FALSE` 2 — normalized to the published 69/12/2.)

**Both rejections:**

> **DHCR7 activity --[-]--> plasma cholestane-triol.** "The edge is indirect (mediated by
> 7-DHC accumulation and non-enzymatic oxidation), and it's not the dominant determinant of
> plasma C-triol. Canonical DHCR7 readouts remain 7-DHC, 8-DHC and the 7-DHC/cholesterol
> ratio… Considerable disagreement and inter lab variability. Err on side of caution."

> **mesangial cell contraction --[-]--> renin secretion.** "The source is actually the
> calcium signal not the contraction although they correlate. Contractile activation is kind
> of OK but drop the mesangial contraction."

**Selected flags** — these show the class of error only a physiologist catches:

> **melatonin --[-]--> cortisol.** "Not causative. Melatonin and cortisol are in near-perfect
> antiphase… strongly inversely correlated. But both are driven by the same upstream
> pacemaker — the suprachiasmatic nucleus." *A textbook confounder that had passed with an
> evidence class of `perturbation`.*

> **GLUD1 activity --[+]--> plasma glutamate.** "Sign is the wrong way round for normal
> conditions. GDH catalyses a reversible reaction… In vivo the flux runs predominantly in the
> oxidative deamination direction."

> **thyrotroph TSH secretion --[+]--> TSH secretion.** "Tautology. No evidence."

> **DPYD --[-]--> plasma 5-hydroxymethyluracil.** "Correct target is dihydrouracil/uracil."

> **CoQ10 --[+]--> complex III.** "if target is electron flux then this is true but if target
> is enzymic activity of Complex III then its not true."

> **TPO/NIS organification --[+]--> T4 secretion.** "Source fuses two sequential and separable
> steps — NIS-mediated trapping and TPO-mediated organification… the perchlorate discharge
> test exists precisely to distinguish a trapping defect from an organification defect."

Two flags land on the Bohr-effect modulations: the reviewer's point is that pH→SaO₂ is
correct as a *level* effect, but under the strict cross-partial definition the sign flips
depending on where you sit on the dissociation curve — "A left shift at PaO₂ ≈ 100 mmHg
pushes you further onto the plateau."

The hematocrit flag is treated in §3.4, because it contradicts released content.

---

# Part III — My own analysis of the release

## 3. Analyses not in the paper

Everything in this part is computed by me from the published artifact — the repo cloned from
`bio-ontology-research-group/physiomap`, with figures derived from
`web/physiomap-1.1.1.json` and `benchmarks/results/`. The release holds 1,699 nodes, 2,268
causal, 85 production, 4 constitution, 9 quantitative-identity and 19 modulation relations,
largest SCC 213, 1,448 SCCs.

Those reconcile with the paper on every count **except causal influence, where the release
has two fewer than the paper reports**: §1.8 gives 2,270 causal-influence axioms and 2,387
projected relation instances (2,270 + 85 + 4 + 9 + 19 = 2,387, so the paper is internally
consistent), while the release sums to 2,385. A two-edge drift between a preprint and its
release is small and unremarkable in itself — text and artifact are cut at different moments —
but it is worth stating precisely rather than rounding to "identical", particularly in a
document whose subject is provenance discipline. Every other figure below matches.

### 3.1 A node is an (entity, quality, context, scale, system) tuple

```json
{ "id": "renin", "label": "plasma renin activity",
  "entity_iri": "CHEBI:50266", "quality_iri": "PATO:0001414",
  "scale": "organ_system", "system": "Cardiovascular–renal",
  "scc": 0, "in_big_scc": true, "source": "Guyton core (curated)" }
```

The EQ decomposition is machine-readable on every node — the thing dismech pathophysiology
nodes lack, where `name` is free text and ontology terms live in descriptor lists describing
the node's *participants* rather than its identity.

**Entity ontologies:** CHEBI 671, PR 510, GO 216, UBERON 139, CL 35, none 128. Predominantly
chemicals and proteins — a metabolite-and-enzyme map far more than an anatomy map.

**Quality reuse is concentrated.** Three PATO terms cover 86% of traits: `PATO:0000033`
concentration (854), `PATO:0001414` activity (389), `PATO:0000161` rate (221). The tail
(mass, volume, pressure, functionality…) is 235.

**Scale is a 7-value enum** — molecular, subcellular, cellular, tissue, organ, organ_system,
organism — against dismech's 4-value `biological_scale`. Distribution: organ_system 933,
cellular 463, organ 180, subcellular 46, molecular 43, tissue 29, organism 5. PhysioMap's
molecular tier is *thinner* than dismech's; it is more physiological, not more molecular.

### 3.2 The content is dominated by metabolism, not the cardiovascular showpiece

| System | Traits | | Edge provenance | Edges |
|---|---:|---|---|---:|
| Metabolic / hepatic | **935** | | IEM-enzyme connections | **639** |
| Cardiovascular–renal | 197 | | Curated system fragment | 273 |
| Endocrine | 175 | | Williams (endocrinology) | 247 |
| Neuro / thermal | 114 | | Curated bridges | 184 |
| Hematologic | 83 | | HPO gap-fill (lab analytes) | 151 |
| Respiratory / acid–base | 80 | | Textbook extraction (A&P/…) | 136 |
| Immune / inflammation | 68 | | Connect-isolated (curated) | 111 |
| Mineral / bone | 31 | | West (respiratory) | 106 |
| Fluid / electrolyte | 11 | | Guyton & Hall extraction | 101 |
| Unassigned | 5 | | Molecular/cellular module | 84 |
| | | | Guyton-Hall textbook | 71 |
| | | | Other | 45 |
| | | | Phenotype-connection fan-out | 43 |
| | | | *Guyton core (curated)* | *26* |
| | | | AOP-Wiki import | 26 |
| | | | SIGNOR import | 22 |
| | | | Curated (G. Gkoutos) | 3 |

The systems column is the complete 10-value enum; the provenance column is all 17 lines.
Note that Guyton-derived textbook content is split across two labels — `Guyton & Hall
extraction` (101) and `Guyton-Hall textbook` (71), so 172 edges in total — distinct from the
26-edge hand-curated `Guyton core`.

55% of traits are metabolic/hepatic and the largest single edge source is IEM enzyme
connections, against 26 edges for the Guyton core the paper's figure showcases.

Two provenance lines deserve a curator's eye given the evaluation is against HPOA: **"HPO
gap-fill (lab analytes)" (151 edges)** and **"Phenotype-connection fan-out" (43)**. Edges
added to cover HPO analytes, then scored against an HPO-derived reference, are the concrete
form of the circularity the authors flag in prose. Their 15-gene leakage control is the right
mitigation; it is worth knowing it is mitigating *this*.

### 3.3 Signs are nearly always committed; `?` is rare and well-chosen

**`+` 1,265, `−` 982, `?` 21** — 99.1% of edges carry a definite sign. All 21 `?` edges are
genuine non-monotonicities:

- `left-ventricular end-diastolic volume (preload)` → `ejection fraction`
- `lung volume` → `pulmonary vascular resistance` *(the classic U-shaped curve)*
- `plasma epinephrine` → `total peripheral resistance` *(α1 vasoconstriction vs β2 vasodilation)*
- `arterial PaCO2` → `total peripheral resistance`
- `free T4` → `plasma triglyceride`; `plasma testosterone` → `HDL-cholesterol`

Direct empirical support for R1's design note: an authored `?` is a positive claim, used 21
times out of 2,268, and must not be collapsed with "not yet curated".

### 3.4 The complete non-causal relation sets — and a flagged inconsistency

**All 4 constitutive edges** (`micro` → `macro`, all `+`): adipose tissue mass and lean body
mass constitute body weight; red cell mass and plasma volume constitute blood volume.

**All 9 quantitative identities**, each argument carrying its own derivative sign, with
`role` distinguishing factor / summand / numerator / denominator / argument:

| Result | Kind | Arguments (with derivative sign) |
|---|---|---|
| mean arterial pressure | product | cardiac output (+) × total peripheral resistance (+) |
| cardiac output | product | heart rate (+) × stroke volume (+) |
| blood volume | aggregation | red cell mass (+) + plasma volume (+) |
| body weight | aggregation | adipose tissue mass (+) + lean body mass (+) |
| **hematocrit** | ratio | red cell mass (+) / blood volume (−) — **see below** |
| arterial O₂ content | structural-function | Hb O₂ saturation (+), hematocrit (+), arterial PO₂ (+) |
| oxygen delivery | product | cardiac output (+) × arterial O₂ content (+) |
| arterial pH | structural-function | arterial PCO₂ (−), plasma bicarbonate (+) |
| alveolar PO₂ | structural-function | inspired PO₂ (+), alveolar PCO₂ (−) |

The last two are the Henderson–Hasselbalch and alveolar gas equations reduced to derivative
signs — a good illustration of signs as an abstraction *of* a quantitative constraint.

**The hematocrit row is not sound, and their own reviewer said so.** From the archived
review (§2.7):

> "Identity rather than a causal relationship. Note Blood volume = red cell volume + plasma
> volume, so red cell mass is itself a component of the denominator. Taking the partial
> derivative with respect to red cell mass 'holding blood volume constant' isn't physically
> coherent, since increasing red cell mass necessarily increases blood volume. The correct
> formulation is Hct = RCV / (RCV + PV)."

The release makes this sharper than the comment alone suggests: it holds **both**
`blood_volume = red_cell_mass + plasma_volume` (aggregation) **and** `hematocrit =
red_cell_mass / blood_volume` with independent partial signs. The two identities contradict
each other within the same file. This row was flagged 2026-07-30 and is still in v1.1.1,
which is consistent with the paper's position that the review "isolated a minority for
correction or further investigation" rather than that corrections had landed.

**All 19 modulation edges** are (modulator, edge) pairs with a mixed-derivative sign. Four
reconstruct the oxyhaemoglobin dissociation curve's shift factors as modulations of the
single `arterial PO₂ → arterial Hb O₂ saturation` edge:

```
[-] arterial PaCO2                    on  arterial PO2 -> Hb O2 saturation
[+] arterial blood pH                 on  arterial PO2 -> Hb O2 saturation
[-] body core temperature             on  arterial PO2 -> Hb O2 saturation
[-] erythrocyte 2,3-BPG               on  arterial PO2 -> Hb O2 saturation
```

Four more are cortisol's permissive effects (on glucagon→hepatic glucose production,
epinephrine→glycogenolysis, epinephrine→lipolysis, norepinephrine→TPR) — permissive hormone
action really is a mixed partial and really is awkward as an ordinary edge. This is the
clearest argument in the release for modulation as a distinct type, even though the
first-order solver does not read it. Note the reviewer flagged two of the four Bohr
modulations on cross-partial grounds (§2.7).

### 3.5 Worked edges, by provenance

Quoted verbatim from `web/physiomap-1.1.1.json`, labels truncated.

**Guyton & Hall extraction (101)** — renal haemodynamics and acid–base:
```
renal afferent arteriolar resistance (RA) --[-]--> glomerular capillary hydrostatic pressure
renal afferent arteriolar resistance (RA) --[-]--> renal blood flow
plasma angiotensin II                     --[+]--> renal efferent arteriolar resistance (RE)
arterial PaCO2                            --[+]--> renal tubular H+ secretion / bicarb reabs.
arterial blood pH                         --[-]--> renal proximal tubule ammonia (NH3) secretion
arterial blood pH                         --[+]--> total peripheral resistance
blood colloidal osmotic pressure          --[+]--> glomerular capillary colloid osmotic pressure
```

**West (106)** — ventilation mechanics, essentially a textbook derivation chain:
```
tidal volume                     --[+]--> total (minute) ventilation
respiratory rate                 --[+]--> total (minute) ventilation
total (minute) ventilation       --[+]--> alveolar ventilation
dead space ventilation           --[-]--> alveolar ventilation
tidal volume                     --[-]--> dead space fraction
alveolar ventilation             --[-]--> alveolar PCO2
whole-body CO2 production rate   --[+]--> alveolar PCO2
alveolar surface tension         --[-]--> alveolar stability against collapse
alveolar surfactant concentration--[+]--> alveolar stability against collapse
blood-gas barrier thickness      --[-]--> rate of respiratory gas diffusion
```

**Williams (247)** — axis control, including the KNDy pulse generator:
```
KNDy neuron neurokinin B secretion    --[+]--> hypothalamic kisspeptin secretion
KNDy neuron dynorphin secretion       --[-]--> hypothalamic kisspeptin secretion
hypothalamic kisspeptin secretion     --[+]--> hypothalamic GnRH secretion
tuberoinfundibular dopaminergic (TIDA)--[-]--> anterior-pituitary prolactin secretion
tissue type-III deiodinase (DIO3)     --[-]--> free plasma triiodothyronine (free T3)
plasma myostatin (GDF8)               --[-]--> lean body mass
plasma melatonin                      --[-]--> suprachiasmatic nucleus (SCN) output
```

**IEM-enzyme connections (639)** — the stereotyped substrate/product shape:
```
fumarate hydratase (fumarase) activity          --[-]--> plasma fumarate concentration
fumarate hydratase (fumarase) activity          --[+]--> urinary malic acid level
succinate dehydrogenase complex (SDH) activity  --[-]--> plasma succinate concentration
mitochondrial aconitase 2 (ACO2) activity       --[-]--> urinary citrate level
```

**AOP-Wiki (26)** — the most molecular content in the map:
```
thyroid NIS (SLC5A5) sodium/iodide symporter --[+]--> follicular cell intracellular iodide
follicular cell intracellular iodide         --[+]--> follicular cell thyroxine (T4) secretion
follicular-cell DUOX2 H2O2 generation        --[+]--> thyroid peroxidase iodide organification
endothelial AKT1/eNOS-Ser1177 phosphorylation--[+]--> endothelial nitric oxide production
renal proximal-tubule OAT1 activity          --[-]--> plasma urate concentration
```

**Cross-scale.** The transition matrix is dominated by *cellular → organ_system* (709) and
*organ_system → organ_system* (654). Overall 986 edges run finer→coarser, 975 within a scale,
and **307 coarser→finer** — genuine top-down control, not only bottom-up composition:
```
plasma (ionised) calcium concentration --[-]--> parathyroid chief-cell PTH secretion rate
CSF glucose concentration              --[+]--> intracellular ATP concentration
thrombin (FIIa) activity               --[+]--> activated platelet procoagulant surface
```

### 3.6 The topology: a coupled core bolted to a shallow fan

Classifying all 1,699 nodes by in/out degree over the causal edges:

| Role | Nodes | Share |
|---|---:|---:|
| **Pure source** (in-degree 0) — candidate lesion variables | 461 | 27.1% |
| **Pure sink** (out-degree 0) — terminal observables | 710 | 41.8% |
| **Internal** (both in and out) — can be a waypoint in a chain | **452** | 26.6% |
| **Isolated** (no causal edges at all) | 76 | 4.5% |

And **593 causal edges (26.1%) run directly from a pure source to a pure sink** — one-hop
terminal fans that can never participate in a longer chain:

```
CYP11B2 (aldosterone synthase) activity        --[+]--> adrenal zona glomerulosa aldosterone secretion
lysosomal acid beta-galactosidase (GLB1)       --[-]--> plasma tissue-non-specific alkaline phosphatase
hepatocyte apolipoprotein E secretion rate     --[-]--> plasma triglyceride concentration
```

The archetype is MCAD/ACADM activity: **out-degree 25, in-degree 0** — an enzyme fanning out
to two dozen analytes, caused by nothing. The next top sources are mostly the same shape
(VLCAD 11, BCKDH 10, DPYD 10, transaldolase 9, CPT2 8, LCAT 8) — with one exception worth
noting: `Bruton's tyrosine kinase (BTK) catalytic activity` also sits at out-degree 11, and
is an immunodeficiency gene rather than a metabolic enzyme, so the fan pattern is not
exclusively IEM.

So PhysioMap is **two graphs sharing a namespace**:

1. **A genuinely coupled physiological core** — the 213-trait SCC: 53 cardiovascular–renal,
   43 endocrine, 32 respiratory/acid–base, 32 metabolic, 21 haematologic, 15 mineral/bone.
   Renin, angiotensin II, aldosterone, ADH, ANP, baroreflex outflow, GFR, ECF volume, cardiac
   output, heart rate. Feedback is real here and the Cramer's-rule machinery earns its place.
2. **A broad one-hop enzyme→analyte fan** — the IEM content, topologically trivial, where a
   "prediction" is a single edge lookup.

That split explains §3.7, and it also explains why the relation-type ablation changed almost
nothing (§1.8): constitution, quantitative identity, and modulation live almost entirely in
graph 1, while the benchmark mostly exercises graph 2. The authors say as much in a
drug-panel benchmark comment: *"Organ targets embedded in the whole-body feedback SCC return
'?' (reported separately, never wrong)."* PhysioMap's sophisticated inference and its broad
coverage are largely in **different parts of the map**.

The 76 isolated nodes are traits with no causal edges at all — mostly secretion rates
(`intestinal L-cell GLP-1 secretion rate`, `kidney interstitial fibroblast erythropoietin
secretion rate`, `gastric G-cell gastrin secretion rate`). The "Connect-isolated (curated)"
provenance line (111 edges) shows this is a known worklist already being chipped at.

### 3.7 The benchmark result is shallower than the headline suggests

Taking the 866 adjudicated pairs in `benchmarks/results/e1b_forward_pairs.tsv` and running
BFS from each lesion variable over causal + production edges:

| | Pairs | Share |
|---|---:|---:|
| **Unreachable** from the lesion at any depth | **492** | 56.8% |
| Reachable | 374 | 43.2% |
| Lesion id not resolvable | 0 | — |

Among the 374 reachable, **161 (43.0%) are a single hop**, 53.5% within two, 70.1% within
four.

**Parsing note.** 27 of the 866 rows carry *two* semicolon-separated lesion variables in
`primary_intervention` — e.g. ARSA → `arsa_activity -; arylsulfatase_a_activity -`, and
likewise CTNS, KYNU, PKLR. These are exactly the four genes the paper excludes from the
*inverse* benchmark for having two primary lesion variables (§1.8). Every constituent id
resolves in the graph. The figures above split on `;` and take a pair as reachable at the
**minimum** distance over its lesion variables, which matches the paper's "one or more
primary lesion variables" specification. Counting only the first lesion instead gives 369
reachable / 497 unreachable / 157 one-hop — the conclusions are identical either way.
Two of these multi-lesion rows exist *because* of duplication: ARSA is one of the five
duplicate-trait groups in §3.8, where `arsa_activity` and `arylsulfatase_a_activity` are the
same trait under two ids.

1. **Most abstentions are absence of a path, not feedback-induced indeterminacy.** The solver
   abstained on 695 pairs; 492 have no directed route at all.
2. **The determinate set is plausibly concentrated at depth 1.** The solver committed on 171
   pairs; there are 161 one-hop reachable pairs — consistent with determinacy being mostly
   the near-definitional enzyme→analyte edges of §3.2.

The reachability count corroborates itself against the paper: the shortest-path rule returns
a direction exactly when a path exists, and the paper reports **375** such directions against
the **374** reachable pairs found here — a one-pair gap, which is about as close as an
independent reconstruction from the web payload can be expected to land.

**Consistent-with, not proven.** The release does not publish per-pair determinacy labels, so
I cannot confirm the 171 determinate pairs *are* the 161 one-hop pairs plus 10; the counts
permit it but do not establish it. My BFS also reconstructs reachability from the projected
web payload rather than from the solver's own graph, and does not traverse
quantitative-identity edges.

This does **not** undercut the abstention result (§1.8): that permutation test was restricted
to pairs where the shortest-path rule returned a direction — i.e. reachable pairs — so
unreachable pairs never entered it. What the depth analysis changes is the interpretation of
the *coverage* figure, not the significance of the concentration result.

### 3.8 Other content defects visible in the release

Minor, and recorded because dismech would hit the same class of problem if it built a shared
trait namespace (§4.2).

- **Exact duplicate traits.** Grouping the 1,568 nodes that carry *both* an `entity_iri` and a
  `quality_iri` by that pair finds 195 groups with more than one member (grouping all 1,699
  nodes regardless gives 202; requiring only `entity_iri` gives 196 — the conclusion below is
  identical under all three). Nearly all are legitimate context distinctions the web payload does not expose —
  `plasma_phenylalanine` and `csf_phenylalanine` share `CHEBI:28044` + `PATO:0000033` and
  differ only in context, which is what the trait definition's context conjunct is for.
  Filtering to collisions that *also* share an identical label leaves **5 genuine duplicate
  groups (6 redundant nodes)**:

  | Label | Duplicate ids |
  |---|---|
  | plasma 11-deoxycorticosterone (DOC) concentration | `plasma_deoxycorticosterone`, `plasma_doc`, `plasma_11_deoxycorticosterone` |
  | erythrocyte pyruvate kinase (PKLR) catalytic activity | `pyruvate_kinase_activity`, `erythrocyte_pyruvate_kinase_activity` |
  | alpha-galactosidase A (GLA) activity | `alpha_galactosidase_a_activity`, `gla_activity` |
  | arylsulfatase A (ARSA) activity | `arylsulfatase_a_activity`, `arsa_activity` |
  | tissue glucosylceramide content | `tissue_glucosylceramide`, `tissue_glucosylceramide_content` |

  0.35% of nodes — the "reconciled duplicates" step evidently worked, with a residue. Not
  cosmetic under SCM semantics: each of the three DOC nodes independently carries a `−` edge
  into `renin`, so an intervention on "DOC" reaches a third of its edges and the feedback
  around renin is understated. Three of the five are ARSA/GLA/PKLR — genes that also appear
  in the rare-disease benchmark.

- **One contradictory edge pair.** Exactly one (source, target) pair carries two edges with
  opposing signs: `plasma insulin → hepatic VLDL secretion rate`, once `+` and once `−`.
  Biologically a real tension (acute insulin suppresses VLDL secretion; chronic
  hyperinsulinaemia with insulin resistance raises it), so the honest encoding is a context
  distinction or a `?`, not two unqualified edges. One conflict in 2,268 edges is a good
  consistency record.

---

# Part IV — Comparison with dismech

## 4. Structural comparison

Counts measured from this repo at **`c0250519` (2026-08-28)**, the branch's merge base.

An earlier revision of this report measured at `4b2f90c` and mislabelled that column
`2026-08-23`; `4b2f90c` is in fact dated **2026-08-11**, and the KB grew substantially in the
intervening fortnight (11,923 → 15,296 nodes, 22,564 → 27,532 edges). Every figure below has
been recomputed at the current base so the document carries one vintage. No conclusion
changed: the cyclic-file share moved 1.4% → 1.5%, the description-regex share 18.3% → 18.5%,
and both self-loops are still present. The one materially different row is the
gain/loss-of-function modifier census in §4.1, which was 5/4 at the older commit and is now
37/106 — no longer a rounding error, and worth knowing before citing it.

| | PhysioMap v1.1.1 | dismech (`c0250519`, 2026-08-28) |
|---|---|---|
| Organizing axis | one shared physiology, disease-agnostic | per-disease entries + reusable modules |
| Nodes | 1,699 traits | **15,296** pathophysiology nodes |
| Causal edges | 2,385 projected relations | **27,532** `downstream` edges |
| Node identity | global EQ-pattern OWL class | free-text `name`, **scoped to its file** |
| Edge polarity | signed (`+`/`-`/`0`/`?`), semantically load-bearing | **absent** |
| Edge typing | 5 SCM-distinct types | `causal_link_type` = *directness* only |
| Feedback | first-class; SCC + Cramer's rule; largest SCC 213 | not represented as feedback |
| Inference | intervention prediction + abduction, abstains | rendering, compliance, export; no sign propagation |
| Evidence model | 6 classes, admission-gating, **not** used by solver | per-edge `EvidenceItem`, snippet-verified against cached sources |
| Cross-scale composition | `constitution` in a separate acyclic graph | `conforms_to` module anchors (manual, per-node) |

### 4.1 dismech signs *treatment* and *environmental* edges but not mechanism→mechanism edges

dismech already commits to edge polarity in two places:

- `TreatmentMechanismTarget.treatment_effect` → `INHIBITS`, `ACTIVATES`, `MODULATES`,
  `BYPASSES`, `RESTORES`
- `EnvironmentalMechanismTarget.environmental_effect` → `TRIGGERS`, `EXACERBATES`,
  `PREDISPOSES`, `PROTECTS_AGAINST`, `MODULATES`

But `CausalEdge` — the 27,532-edge backbone — carries only `target`, `description`,
`evidence`, `hypothesis_groups`, `causal_link_type`, `intermediate_mechanisms`. There is no
slot for whether A *raises* or *lowers* B.

So a drug edge into a node is signed, an exposure edge into the same node is signed, and the
mechanism edge out of it is not. Any signed traversal of a dismech pathograph dies at the
first `downstream` hop.

Polarity is not absent from the KB, just not in a queryable slot. Node-level descriptors
carry `modifier` heavily — **DECREASED 4,795, INCREASED 4,186, ABNORMAL 2,916, DYSREGULATED
856** (plus LOSS_OF_FUNCTION 106, GAIN_OF_FUNCTION 37, ABSENT 30) — counting `modifier:` on
the three ontology-bound descriptor lists that hang off a pathophysiology node
(`biological_processes`, `molecular_functions`, `cell_types`) and nowhere else. That scope
matters: descriptor lists elsewhere in an entry also carry `modifier:`, so a whole-file count
is a larger number measuring a different thing, and the claim here is specifically about
polarity attached to *pathograph nodes*. Regenerate with `uv run python
scripts/physiomap_release_analysis.py --dismech .`. `INCREASED`/`DECREASED`
are already bound to `PATO:0002300`/`PATO:0002301`, *the exact two terms PhysioMap uses for
`+`/`−`*. A crude regex over edge `description` text
(inhibit|suppress|decreas|reduc|block|impair|loss of|deplet|antagoni) matches 5,085 of 27,532
edges (18.5%). Treat that only as evidence that polarity language is pervasive in the prose —
the regex cannot distinguish "A inhibits B" from "A causes impaired B", and the two imply
*opposite* edge signs. A reason to look, not a measurement.

Note the modifier counts describe *node states*, not edge signs, and the two are not
interchangeable: a node marked `DECREASED` says nothing about whether its outgoing edge
raises or lowers its target. This is why the information cannot simply be derived.

### 4.2 The deeper gap is the namespace, not the sign

`CausalEdge.target` is `range: string`, resolved by convention within the same file.
"Hepatic Stellate Cell Activation" in `Liver_Cirrhosis.yaml` and the corresponding node in
`fibrotic_response.yaml` are related only through a hand-authored `conforms_to` anchor, and
CLAUDE.md is explicit that conformance is *not* inheritance — disorder entries fully
duplicate module content.

PhysioMap's traits are globally identified classes in one namespace, which is what lets 1,699
nodes form a single coupled system with a 213-trait feedback component.

Consequence: **dismech's 27,532 edges do not compose into one graph.** They are ~2,500
disjoint per-disease graphs joined by manual anchors. Signing the edges would make each
*entry* traversable; it would not by itself produce a whole-body physiology. That is a much
larger undertaking and should not be smuggled in as a side effect of adding a sign slot.

§3.8's duplicate-trait residue is a preview of what that undertaking costs: PhysioMap
reconciles duplicates as an explicit pipeline step and still ships six.

### 4.3 dismech pathographs are almost entirely acyclic — which makes signing them *easier*

PhysioMap's solver is elaborate because feedback is unavoidable in whole-body physiology: a
213-trait SCC forces the Cramer's-rule test and the 16-trait expansion cap. Would dismech
inherit that complexity? Measured over the 2,517 KB files with a `pathophysiology` block,
resolving `downstream` targets within each file:

| | Count | Share |
|---|---:|---:|
| Files with a genuine multi-node feedback cycle | **37** | 1.5% |
| Self-loop edges (a node listing itself as `downstream`) | **2** | — |
| Files whose pathograph is acyclic | 2,480 | 98.5% |

The 37 cyclic files are where you would expect real feedback — `Alzheimer_Disease`,
`Chronic_Kidney_Disease`, `Idiopathic_Pulmonary_Fibrosis`, `Abdominal_Aortic_Aneurysm`,
`Aortic_Valve_Stenosis`, `Epilepsy`, `Alopecia_Areata` — self-amplifying vicious circles, not
modeling accidents.

This substantially strengthens R1. For 98.5% of entries, signed propagation is plain
topological sign algebra over `{+, -, 0, ?}` — no Jacobian, no SCC decomposition, no
determinant test. PhysioMap's hard machinery would be needed for a couple of dozen entries,
and its conservative fallback (abstain when unresolved) is acceptable for those in a first
implementation.

The two self-loops are almost certainly curation errors and worth fixing independently:

- `Periventricular_Nodular_Heterotopia.yaml` — "Progressive Lung Disease" → itself
- `Autoimmune_Polyendocrine_Syndrome_Type_1.yaml` — "Chronic Mucocutaneous Candidiasis" → itself

Nothing currently rejects a node listing itself as its own `downstream` target; a one-line
assertion in `tests/test_data.py` would close that. Flagged as an observation, not fixed here.

---

# Part V — Recommendations

## 5. What to do about it

Ordered by value-to-cost. Only the first is proposed as near-term work.

### R1 — Add an optional polarity slot to `CausalEdge` (recommended)

The smallest change that unlocks the most. Sketch, deliberately mirroring the existing effect
enums rather than inventing a new vocabulary:

```yaml
CausalEdge:
  slots:
    - target
    - causal_effect        # NEW: INCREASES | DECREASES | MODULATES | UNKNOWN
    - causal_link_type     # unchanged: directness
    ...
```

Design notes, now grounded in the release rather than just the paper:

- **Keep it optional and default to absent, not to `UNKNOWN`.** PhysioMap's `?` means
  "non-constant dependence with no sign constraint" — a *positive claim*. §3.3 shows they
  used it 21 times in 2,268 edges, on genuine non-monotonicities like preload→EF and lung
  volume→PVR. That is not "nobody has curated this yet", and conflating the two turns a
  coverage gap into a false knowledge claim.
- **Do not derive it from the target node's `modifier`.** Node state and edge sign are
  different quantities (§4.1).
- **Sign is a separate claim, so it takes separate evidence** — the discipline dismech already
  applies to phenotype `frequency:` and to model-link vs. readout evidence. PhysioMap goes
  further and makes evidence class an *admission gate* (§1.6/§2.6): associational evidence
  cannot license a causal edge at all. That is worth considering for a signed dismech edge.
- Retrofitting 27,532 edges is not proposed. Curate forward and backfill opportunistically; a
  mechanically-inferred backfill from description text would be exactly the plausible-looking
  fabrication the repo's evidence SOP exists to prevent.

Before implementing, confirm no existing issue covers this. My GitHub semantic search
returned zero results on two phrasings, which I read as *inconclusive* (the queries also
failed to surface anything adjacent) rather than as confirmation none exists.

### R2 — Adopt principled abstention wherever dismech infers a direction

The most valuable *result* in the paper is not the 100% precision, it is that abstentions were
provably concentrated on cases a naive path rule got wrong 40.7% of the time. Any future
dismech feature that propagates direction along the pathograph — a signed-traversal query, a
treatment-response predictor, a compliance heuristic — should be able to return "undetermined"
and be evaluated on precision *and* coverage, never precision alone.

### R3 — Reuse the HPO-EQ directional reference construction (methodology, no schema change)

Their recipe: decompose directional HPO classes into (variable, direction) via the EQ pattern
and PATO:0002300/0002301, propagate annotations *only upward* through the subclass hierarchy,
retain a gene–variable direction only when the resulting set is a singleton. dismech already
binds those two PATO terms and relates model variables to HP terms with `threshold_direction`.
Directly reusable if dismech ever wants to validate a signed pathograph against HPOA —
including both guardrails. Note they had to hand-block two deoxycortisol terms whose asserted
HPO ancestry would have mis-mapped them to cortisol: the recipe needs spot-checking, not blind
trust.

### R4 — Steal the curation-provenance practices, not the relation types

The relation types are semantically well-motivated but changed almost nothing on the evaluated
tasks (§1.8), and dismech has no solver that would read them. Adding four more relation types
now would add curation burden with no consumer. Revisit if R1 lands and a signed-traversal
consumer exists.

What *is* worth taking now is §2's provenance discipline, most of which dismech either already
does or could adopt cheaply:

- **Record failed checks in place.** `INDRA: unreachable`, `pmid_ok=false`, `No PMID in batch`
  — recorded on the edge rather than causing a silent drop.
- **Record what was discarded and why** ("cross-scale/duplicate/pituitary-mediation-conflicting
  candidates were dropped").
- **Check the citation resolves *and* is concordant with the claim**, as two separate checks.
- **Archive human review as a first-class artifact** — sha256 of the sent and returned
  workbooks, the sampling seed, an integrity check that identity columns were not edited.
  dismech's `history/` records are the natural home for this shape.
- **A `*** DRAFT FOR REVIEW ***` banner** that survives into the committed file, marking
  content that passed automated gates but not yet domain review.

The one exception on relation types: **quantitative identity** (MAP = CO × TPR) has an obvious
dismech analogue already in the tree — `ComputationalModel` / `ModelVariable` /
`ModelVariableDescriptor`, where variables carry units, LOINC/CHEBI mappings, and thresholds.
If dismech ever links a pathograph node to a model variable, that link is closer to a
quantitative identity than to a causal edge and should not be recorded as one. §3.4's
hematocrit case is the cautionary example: an identity whose arguments are not independent is
incoherent under partial-derivative semantics, and it shipped anyway.

### R5 — Not recommended: mirroring PhysioMap content into dismech

PhysioMap is CC BY 4.0 and technically ingestible, but its content is *normal* physiology,
disease-agnostic. dismech entries are disease-scoped pathographs with per-edge,
snippet-verified evidence against cached references. There is no clean way to import a
PhysioMap trait into a dismech disorder file without either inventing disease-specific evidence
for a disease-agnostic claim, or creating nodes no entry owns. If a bridge is ever wanted, the
right shape is a **mapping** (dismech node ↔ PhysioMap trait IRI), not a copy — and that
presupposes R1 and the §4.2 namespace work.

---

## 6. Open questions

1. Is edge polarity already tracked in a dismech issue? (search inconclusive — needs a human
   check)
2. Would `causal_effect` be better on `CausalEdge`, or as a fourth mechanism-link class
   alongside `TreatmentMechanismTarget` / `EnvironmentalMechanismTarget` / `ModelMechanismLink`?
   The existing three all sign their edges; `CausalEdge` is the odd one out, which weakly argues
   for putting it on `CausalEdge` itself.
3. ~~Does the dismech pathograph have feedback cycles today?~~ **Answered in §4.3:** 37 of 2,517
   files (1.5%), plus 2 self-loops that look like curation errors.
4. Should a self-loop `downstream` edge be a test failure? (§4.3 — two exist today.)
5. `conforms_to` anchors are the only existing cross-file node identity. Are they dense enough
   to seed a shared trait namespace, or is §4.2 genuinely a from-scratch effort?
6. **Worth asking the PhysioMap authors for the per-pair determinacy labels** (which of the 866
   pairs the solver committed on). That single file would settle §3.7 — whether the 171
   determinate predictions are essentially the one-hop enzyme→analyte edges, or whether the
   solver is genuinely resolving multi-hop and feedback cases. The question is friendly, not
   adversarial: the release is unusually complete and this is the one artifact missing to
   reproduce the coverage claim end to end.

## 7. Provenance

**Part I** is the preprint, read in full (16 pp., text extracted locally with pypdf). No
supplementary material was retrieved; statements attributed to Suppl. sections are as described
in the main text. Figures quoted from the paper — the expert-review counts, the baselines, the
abduction table, the permutation test — are as printed and were not recomputed. The one place
Part I departs from the paper is the Figure 1 edge signs, which were verified against the
release because PDF extraction garbles figure layout.

**Part II** is the repo at `github.com/bio-ontology-research-group/physiomap`, cloned
2026-08-23: `benchmarks/human/curated/*.yaml` (the import files and their headers),
`benchmarks/human/systems/*.yaml`, `physiomap_core/causal_evidence.py` (the class definitions
and admission rules), and `benchmarks/results/expert_gold_review.tsv` +
`expert_gold_review_summary.json` (the 83 verdicts, comments, and review metadata). Evidence-
class counts are computed over all 2,358 `causal_edges` in the benchmark YAML. Reviewer
comments are quoted verbatim, lightly truncated where marked.

**Part III** is reproducible: `scripts/physiomap_release_analysis.py` regenerates every
figure in it from a PhysioMap clone (`uv run python scripts/physiomap_release_analysis.py
<clone>`). That script exists because the first revision of this report got §3.7 wrong — it
read `primary_intervention` as a single identifier when 27 of the 866 rows carry two
semicolon-separated lesion variables — and a committed script makes that class of error
checkable rather than trusted. It follows the precedent in
[`experiments/README.md`](../../experiments/README.md): scripts that compute metrics are
committed alongside so numbers can be regenerated rather than trusted.

Part III computes from `web/physiomap-1.1.1.json` (node/edge inventories,
sign and provenance distributions, scale/system/PATO/entity breakdowns, the complete
constitutive/quantitative/modulation sets, duplicate-trait and sign-conflict checks, and the
degree/topology analysis) and `benchmarks/results/e1b_forward_pairs.tsv` +
`e1b_forward.json`. The §3.7 depth analysis is my own BFS over causal + production edges; its
limits are stated inline. The release's headline counts reproduce the paper's exactly, which is
a good integrity signal.

**Part IV** figures are measured from this repo at commit `c0250519` (2026-08-28), the
branch's merge base, and regenerate with `scripts/physiomap_release_analysis.py --dismech .`
(the same script as Part III), which carries the directory list, the modifier-census scope,
and the negative-language regex as named constants. Computed by walking
`kb/{disorders,modules,comorbidities}/*.yaml`; the §4.3 cycle analysis resolves each
`downstream` target against `pathophysiology[].name` within the same file, so it measures
intra-entry structure only. Schema claims verified against `src/dismech/schema/dismech.yaml`
(`CausalEdge`, `TreatmentEffectEnum`, `EnvironmentalEffectEnum`, `CausalLinkTypeEnum`,
`ModifierEnum`, `ModelVariableDescriptor`).
