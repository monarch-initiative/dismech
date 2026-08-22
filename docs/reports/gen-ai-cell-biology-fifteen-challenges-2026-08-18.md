# Can dismech help? An assessment against the "Fifteen challenges for generative AI applications to cell biology"

**Source paper:** Dupire L, Khan AA, Karaletsos T, Kelley S, Lundberg E, Ma J, Paull E,
Quake SR, Rabadan R, Rowan C, Sims P, Tavazoie S, Tsang JS, Zhang M, Califano A.
*Fifteen challenges for generative AI applications to cell biology.* Cell 189, September 17,
2026. [doi:10.1016/j.cell.2026.07.004](https://doi.org/10.1016/j.cell.2026.07.004) (CC BY).

**Written:** 2026-08-18. All dismech counts are computed directly from `kb/` at the commit
this report was written; the script is in the [appendix](#appendix-reproducing-the-numbers).

---

## TL;DR

- The paper's central argument is **not** the fifteen challenges themselves — it is that
  Gen-AI for cell biology is structurally data-starved, that single-cell foundation models
  fail out-of-distribution for that reason, and that the fix is to **pre-wire curated
  biological priors** into model architectures.
- Every prior the authors actually name is **molecular**: STRING, PrePPI, ENCODE, ARACNe,
  MINDy. Their list contains **no prior at the pathophysiology scale** — no curated, causal,
  evidence-anchored representation of mechanism chains linking molecular lesion → cell state
  → tissue → organism phenotype. That is precisely what dismech is.
- dismech offers **real leverage on 3 of the 15 challenges** (6 drug mechanism of action,
  10 systems-level mechanisms, 12 drug toxicity), **partial leverage on 6** (3, 5, 8, 11, 13,
  15), and **nothing on 6** (1, 2, 4, 7, 9, 14). It should not pretend otherwise.
- The larger opportunity is **benchmarks, not priors**. The authors explicitly ask for
  CASP/DREAM-style prospective benchmarks and concede they do not exist. dismech carries four
  benchmark-shaped assets that are hard to reconstruct from public corpora — most distinctively
  a **342-item curated corpus of human/model-system divergences** (`HUMAN_MODEL_MISMATCH`),
  which speaks directly to their TGN1412 argument under challenge 12.
- The binding constraint on any dismech-derived benchmark is **training-data leakage**, since
  dismech is curated *from* the literature. This is tractable: the reference cache carries a
  publication `year` for all 29,524 cached PMIDs, of which **5,663 are 2024 or later**,
  making a temporal holdout directly constructible.

---

## 1. What the paper actually argues

The fifteen challenges are the paper's framing device (explicitly modeled on Hilbert's 23
problems), but the load-bearing argument sits in two earlier sections.

**"The challenge of current Gen-AI models."** Cell behavior cannot be represented as a linear
string of tokens, because large repertoires of N-way interactions must be modeled explicitly —
their multi-information is not recoverable from marginals. The authors' combinatorics: modeling
regulatory motifs and protein isoforms in combinations up to 47 elements (the size of the 60S
ribosomal subunit) yields ~3.48 × 10^150 possibilities. Their proposed remedy is to
"pre-wire" biological knowledge into the model — "representing transcriptional, signaling, and
cell-cell communication networks as probabilistic graphs that restrict the model's attention via
diffusion kernels, and/or by incorporating curated knowledge bases … or by including basic
physical and mechanism-based constraints into the model's architecture." They also note that
this addresses "the suboptimal representation of causality in probabilistic models based on
transformer architectures."

**"The bitter lesson."** They pre-empt the Sutton objection with three arguments: (i) fundamental
data scarcity — the largest biological datasets hold 10^10–10^11 tokens, ~1000× short of LLM
training corpora, and even the Human Immunome Project would not close the gap; (ii) biological
priors encode physical law, not human convention, so encoding them is "not hand-coding but rather
restricting hypotheses to physically plausible mechanisms"; (iii) the cost of waiting is measured
in clinical-trial failures and preventable deaths.

Two supporting observations matter for dismech's positioning. First, they cite benchmarking work
showing scGPT/Geneformer-class models fail to beat linear baselines on held-out cell types,
perturbations, and tissues, and argue those failures are **structural rather than incidental**.
Second, their conclusion calls for a public-private consortium and honest progress measurement:
"What matters is starting now, creating sustainable infrastructure, and measuring progress
honestly."

## 2. The gap dismech occupies

The authors' prior stack is complete at the molecular layer and empty above it:

| Layer | Priors they name | dismech |
|---|---|---|
| Protein structure / interaction | AlphaFold, OpenFold, STRING, PrePPI | — |
| Regulatory / epigenetic | ENCODE, ARACNe, MINDy, Enformer, ChromBPNet, DeepSEA | — |
| **Pathophysiology (lesion → cell → tissue → organism)** | **none named** | **dismech** |
| Clinical outcome | (proposed consortium; does not exist) | partial (trials, definitions) |

Three properties make dismech a candidate for that empty row rather than just another
biomedical database:

1. **The edges are asserted causal claims, not co-occurrence.** A `downstream` edge is a directed
   mechanistic assertion carrying its own citation and verified quotation. This is a different
   signal class from anything derivable from expression atlases, and it speaks directly to the
   causality limitation the authors flag in transformer-based models.
2. **The node set is explicitly multi-scale.** `biological_scale` tags nodes MOLECULAR /
   CELLULAR / TISSUE / ORGANISM — the same four levels as the paper's Figure 1 hierarchy
   (molecular interactions → molecular function → cellular/systems function → translation).
3. **The graph is cross-disease factored.** 124 mechanism modules capture conserved processes,
   and 1,623 `conforms_to` edges assert that a specific disease node instantiates a generic
   module node. This is a built-in generalization structure: it states which mechanisms are
   shared across diseases and which are disease-specific — exactly the "biology-specific
   generalization" the authors argue is possible.

## 3. Current state of the knowledge base

Counts over `kb/disorders`, `kb/modules`, `kb/comorbidities`, `kb/groupings` at the commit of
this report.

### Scale

| | Files | Pathophysiology nodes | Causal (`downstream`) edges |
|---|---|---|---|
| Disorders | 2,000 | 11,981 | 23,304 |
| Modules | 124 | 585 | 506 |
| Comorbidities | 21 | 0 | 0 |
| Groupings | 69 | n/a | n/a |

`conforms_to` links: **1,623** from disorder nodes to module nodes (plus 7 module→module).
Most-instantiated modules: `epilepsy_excitation_inhibition_imbalance` (145),
`lysosomal_substrate_accumulation` (91), `cardiac_ion_channel_repolarization` (67),
`ciliopathy_dysfunction` (67), `fibrotic_response` (63), `complex_iv_assembly_deficiency` (61).

### Evidence

**117,139 structured evidence items**, each a citation + an exact quotation verified against a
cached copy of the source + a support classification (SUPPORT / REFUTE / PARTIAL / …).
**23,965 distinct PMIDs.** (A further ~11,700 citations sit in top-level `references:` blocks,
which are a parallel bibliography rather than claim-level evidence.)

| Reference prefix | Count | | `evidence_source` | Count |
|---|---|---|---|---|
| PMID | 101,793 | | HUMAN_CLINICAL | 75,724 |
| ORPHA | 7,309 | | OTHER | 19,617 |
| DOI | 5,234 | | IN_VITRO | 6,945 |
| clinicaltrials | 1,208 | | MODEL_ORGANISM | 6,363 |
| CGGV (ClinGen) | 610 | | COMPUTATIONAL | 460 |
| other (url, NCIT, PPR, CIViC, GEO, ICEES, …) | ~975 | | *(unset)* | ~8,030 |

The `evidence_source` split is itself informative for the paper's argument: dismech's evidence
base is **65% human-clinical by construction**, with model-organism evidence explicitly typed
and separable — the authors' complaint about "model organisms that only partially recapitulate
human biology" is a first-class distinction in the schema, not a caveat in prose.

### Mechanism annotation depth

| Feature | Count |
|---|---|
| Nodes tagged `biological_scale` | 4,007 of 12,566 (32%) — MOLECULAR 1,164 / CELLULAR 1,049 / TISSUE 995 / ORGANISM 799 |
| Cell-type (CL) annotations on nodes | 8,463 |
| Biological-process (GO) annotations on nodes | 12,396 |
| Molecular-function (GO) annotations on nodes | 766 |
| Phenotype entries (HP-bound) | 23,586 |
| Genetic entries | 4,905 |
| Biochemical markers | 1,924 (44 with LOINC reference ranges) |
| Environmental exposures | 925, with 546 `influences_mechanisms` edges into the graph |
| Datasets | 1,690 |
| Computable definitions / phenotype algorithms | 287 |
| Clinical trials | 966 |

### Therapeutics

**8,499 treatment entries**, with **2,664 `target_mechanisms` links** binding a drug to the
specific pathophysiology node it acts on, each with its own evidence and an interaction type
(INHIBITS / ACTIVATES / …). Modality distribution: SMALL_MOLECULE 1,062, BEHAVIORAL 814,
SURGERY 759, OTHER 278, DEVICE 168, MONOCLONAL_ANTIBODY 129, RADIOTHERAPY 102, GENE_THERAPY 97,
CELL_THERAPY 90, PROTEIN_REPLACEMENT 69, VACCINE 43, PEPTIDE 39.

### Models and epistemic state

| Model sections | Count |
|---|---|
| Animal models | 535 |
| Experimental models (NAMs: organoids, organ-chips, iPSC) | 250 |
| Computational models | 45 |
| `modeled_mechanisms` links into the pathograph | 449 |
| Readouts on those links | 106 |

Link `relationship` distribution: RECAPITULATES 100, PARTIALLY_RECAPITULATES 44, PERTURBS 16,
MEASURES 15, **FAILS_TO_RECAPITULATE 11**, RESCUES 9, unset 254. *The 58% unset rate is a real
curation gap and is discussed in §6.*

| `discussions` kind | Count | | `mechanistic_hypotheses` status | Count |
|---|---|---|---|---|
| KNOWLEDGE_GAP | 1,025 | | EMERGING | 290 |
| **HUMAN_MODEL_MISMATCH** | **342** | | CANONICAL | 252 |
| CONTROVERSY | 126 | | ALTERNATIVE | 99 |
| OPEN_QUESTION | 92 | | DEPRECATED | 13 |
| INTERPRETATION | 66 | | *(657 blocks total)* | |
| EMERGING_HYPOTHESIS | 20 | | | |
| CURATION_TODO | 18 | | | |

### Delivery formats

Exporters already exist for Biolink/KGX, CX2 (Cytoscape), SEPIO, HPOA, a pathograph export, and
tabular dumps; `dismech-perturb` produces executable models with SED-ML/COMBINE output. A prior
in the form the paper asks for (a graph to restrict attention over) is therefore an export
target, not a new engineering programme.

## 4. Challenge-by-challenge assessment

Ratings: **Strong** = dismech supplies a substantial, distinctive asset today. **Partial** =
relevant structure exists but is thin or indirect. **None** = out of scope; dismech should not
claim it.

| # | Challenge (level) | dismech | What it supplies |
|---|---|---|---|
| 1 | Regulatory & signaling interactions *(molecular)* | None | No molecular-interaction resolution. GO molecular-function tags (766) are annotations, not interaction predictions. |
| 2 | Epigenetic interactions *(molecular)* | None | Not modeled. |
| 3 | Cell-cell interactions *(molecular)* | Partial | 8,463 CL-typed nodes and multicellular modules (`immune_checkpoint_blockade`, `granuloma_formation`, `tumor_promoting_inflammation`, `atherogenesis`) encode which cell types act on which. No ligand-receptor layer. |
| 4 | Synthetic mechanisms *(function)* | None | Out of scope. |
| 5 | Genome → biochemical function *(function)* | Partial | 4,905 genetic entries with `functional_impact_category` (LOF / partial-LOF / GOF / dominant-negative / hypermorphic / neomorphic) — a labeled variant-consequence set matching the hypomorph/hypermorph/neomorph typing the challenge describes. It is a label set, not a sequence-to-function predictor. |
| 6 | **Drug mechanism of action** *(function)* | **Strong** | 2,664 evidence-backed drug→mechanism-node links across 8,499 treatments, at the cell-context-specific granularity the challenge demands. The `target_mechanisms` pattern in modules generalizes a drug mechanism across every conforming disease — e.g. senolytics against `cellular_senescence#Senescent Cell Accumulation`, echinocandins against Fks glucan synthase, six distinct antibacterial target modules. |
| 7 | Genome → phenotype (minimal cell) *(cellular)* | None | Out of scope. |
| 8 | Cell state reprogramming *(cellular)* | Partial | Cell-state transitions appear as nodes (EMT, epithelioid transformation, T-cell exhaustion, SMC phenotypic switching), but with no perturbation-response data attached. |
| 9 | Synthetic circuit design *(cellular)* | None | Out of scope. |
| 10 | **Systems-level mechanisms** *(cellular)* | **Strong** | 23,810 causal edges spanning four biological scales and multiple cell types is the native representation. The immunosuppressive-microenvironment example in the paper (M2/TREM2+ TAMs, myCAFs, N2 TANs, HELIOS+ Tregs acting in concert) is the exact shape of a dismech module. |
| 11 | Complex biomarker identification *(translation)* | Partial | 1,924 biochemical markers attached to the mechanism node they read out, 44 with LOINC-coded reference ranges and interpretation bands; 106 model readouts. Small, and not multi-omics. |
| 12 | **Drug toxicity** *(translation)* | **Strong** | Toxicity-as-mechanism modules (`myelosuppression`, `drug_induced_liver_injury`, `drug_induced_nephrotoxicity`, `drug_hypersensitivity_scar`, plus `cardiomyopathy_maladaptive_remodeling` and `cardiac_ion_channel_repolarization` doubling as toxicity targets) model *why* two drugs against the same target diverge in toxicity — the paper's doxorubicin-vs-etoposide example. HLA-gated `drug_hypersensitivity_scar` encodes host-genetic susceptibility to an immune-mediated adverse reaction, the class of failure TGN1412 exemplifies. |
| 13 | Drug efficacy *(translation)* | Partial | Subtype-stratified mechanism means the Herceptin/15% problem is structurally represented (a treatment targets a node that only a subtype instantiates), and 966 curated trials carry registry-validated evidence. No response/non-response outcome data — which the paper says does not exist publicly anyway. |
| 14 | Organismal responses / immune setpoint *(translation)* | None | Individual-level immune state is not modeled. dismech is disease-level, not person-level. |
| 15 | Clinical trial outcomes *(translation)* | Partial | 966 trials with phase/status and 287 computable phenotype definitions give a substrate for cohort definition, not for outcome prediction. |

**Summary: strong on 3 (6, 10, 12), partial on 6 (3, 5, 8, 11, 13, 15), none on 6 (1, 2, 4, 7, 9, 14).**
The concentration is unsurprising and is the point: dismech's leverage is entirely at the paper's
Level 2–4 (molecular function, systems function, translation), and nil at Level 1 (molecular
interactions), which is where the existing prior stack is already strong.

## 5. The sharper opportunity: four benchmarks

The paper asks for prospective, CASP/DREAM-style benchmarks with tier-1 (relative) and tier-2
(absolute) scoring, and states plainly that for most challenges these do not exist. Four are
constructible from dismech today.

### B1. Mechanism-chain completion (challenges 6, 10)

**Construction.** Mask an intermediate node from a curated causal chain and require the model to
recover it, given the flanking nodes and the disease context. Scoring is ontology-aware: a
prediction is scored against the held-out node's GO/CL/HP terms with partial credit over the
ontology closure (`groupings.py` already computes closure over HP and GO for criteria
evaluation).

**Why it is not trivially gameable.** The generalization split is built in: train on the
disorders that `conforms_to` a module, test on a held-out conformer of the *same* module. This is
a direct analogue of the out-of-distribution failure mode the paper documents for single-cell
foundation models — can a model transfer a conserved mechanism to a disease it has not seen it
instantiated in?

**Available today.** 23,810 edges; 1,623 conformance links across 124 modules; the
most-instantiated modules have 30–145 conformers each, enough for held-out splits.

### B2. Human/model-system divergence (challenges 12, 14) — *the distinctive asset*

**Construction.** Given a mechanism claim and the model system it was demonstrated in, predict
whether the finding transfers to human disease biology. Positives: `RECAPITULATES` links
(100). Hard negatives: `FAILS_TO_RECAPITULATE` (11) and `PARTIALLY_RECAPITULATES` (44) links,
plus **342 curated `HUMAN_MODEL_MISMATCH` discussions**, each carrying an explicit statement of
the mismatch, a rationale for why it is mechanistically meaningful, an `attaches_to` pointer to
the affected node, and often `proposed_experiments`.

**Why this matters most.** The paper's TGN1412 case — six healthy volunteers, cytokine storm
within hours, preclinical models safe — is presented as the hallmark illustration of a
"pervasive challenge," and the authors state that computational approaches "must account for
species-specific immune differences." A curated corpus of *known, adjudicated* human/model
divergences is the natural evaluation set for that capability. The negative class is what makes
it valuable: publication bias means the literature reports successful recapitulation far more
readily than failure, so this corpus is exactly the part that cannot be scraped.

**Honest sizing.** The strictly structured negative set (11 + 44 links) is small. The 342
discussions are semi-structured (typed, node-anchored, prose body) and would need a one-pass
extraction into (claim, model system, verdict, rationale) tuples. See §6.

### B3. Competing-hypothesis discrimination (challenges 6, 10, 13)

**Construction.** dismech carries 657 `mechanistic_hypotheses` blocks with explicit status —
252 CANONICAL, 290 EMERGING, 99 ALTERNATIVE, 13 DEPRECATED — and causal edges opt into hypothesis
groups, so competing mechanistic accounts of the same phenomenon are represented as *alternative
edge sets over the same nodes* rather than as one flattened consensus. The worked case is the
`glymphatic_dysfunction` module's convective-vs-diffusive transport pair; the 126 `CONTROVERSY`
discussions are a second seam.

**What it measures.** Not recall but **epistemic calibration** — can a model identify which of two
mechanistically coherent accounts the evidence actually supports, and can it decline to commit
where the KB records genuine controversy? The 13 DEPRECATED hypotheses are a bonus adversarial
set: mechanisms that were once canonical and are now superseded, where a model trained on the
historical literature should be expected to fail.

### B4. Experiment design against knowledge gaps (challenges 8, 11, 12)

**Construction.** 1,025 `KNOWLEDGE_GAP` discussions, many carrying `proposed_experiments` with
structured readouts (name, target node, direction, interpretation). Give the model the gap and
score its proposed experiment against the curated one. This mirrors the shape of the paper's own
Table 1, which specifies for each challenge a "potential challenge design" and a "validation
benchmark design."

### Leakage control — the binding constraint for all four

dismech is curated *from* the literature, so a frontier model has plausibly seen the source
abstracts. Any benchmark built from it measures memorization unless split temporally. This is
directly tractable: **every cached reference carries a publication `year` in its frontmatter**
(29,524 cached PMID records, of which 5,663 are 2024 or later and 3,095 are 2025 or later), and
every entry carries a `creation_date` (populated on 1,998 of 2,000 disorders). A defensible split
is therefore: *test only on claims whose supporting evidence postdates the model's training
cutoff*. The truly prospective version — curate first, benchmark on the next quarter's entries —
is available because curation is ongoing.

## 6. Limitations, stated plainly

1. **Leakage, as above.** Without a temporal split, any dismech benchmark is a memorization test.
2. **Qualitative, not quantitative.** dismech edges are directed causal assertions without
   effect sizes, rate constants, or dose-response. The paper's success metrics (Table 2) are
   quantitative throughout — MSE, Pearson r, AUROC, Hill coefficients. dismech cannot score
   against most of them. The `dismech-perturb` executable-model layer is the bridge and it is
   currently tiny (4 committed model runs, 45 computational-model entries).
3. **Uneven depth.** 2,000 disorder entries range from flagship multi-module conformers to thin
   stubs. Any benchmark needs an explicit depth filter, not a uniform sample.
4. **Model links are under-typed.** 254 of 449 `modeled_mechanisms` links (58%) have no
   `relationship` value, so the structured recapitulation signal is weaker than the raw model
   count suggests. This is the single highest-value curation backfill for B2.
5. **`biological_scale` coverage is 32%.** The multi-scale claim in §2 is real but partial;
   two-thirds of nodes are untagged, which limits scale-stratified evaluation.
6. **Not person-level.** Challenges 11, 14, and 15 ultimately need individual-level multi-omics
   and outcomes. dismech is a disease-level model of mechanism and will not become a cohort.
7. **A knowledge prior, not training data at scale.** 23,810 edges is negligible as a token
   corpus. The honest framing is the graph-attention/diffusion-kernel prior the authors describe,
   or a retrieval-and-grounding layer — never "here is a corpus, train on it."

## 7. What would need to change in dismech

Ordered by value-per-effort for the positioning above:

1. **Backfill `relationship` on the 254 untyped `modeled_mechanisms` links** (§6.4). Directly
   gates B2, the most distinctive benchmark.
2. **Extract the 342 `HUMAN_MODEL_MISMATCH` discussions into a structured (claim, model system,
   verdict, rationale) table** and publish it as a standalone evaluation set. This is the most
   cite-able artifact dismech could put in front of this community.
3. **Ship a temporal-split harness** — filter entries and evidence by publication year using the
   existing reference-cache frontmatter — so any benchmark is leakage-controlled by construction.
4. **Extend `biological_scale` coverage** beyond 32%, prioritizing the modules and their
   conformers, so scale-stratified evaluation is possible.
5. **Publish the KGX/Biolink export as a named, versioned prior artifact** with a stated node/edge
   schema, so it can be consumed as a graph-attention prior without reading dismech YAML.

None of these are new subsystems; all five are backfills or packaging of structures that already
exist.

## 8. Positioning statement

> dismech is the missing pathophysiology-scale prior in an otherwise molecular list of priors, and
> its curated corpus of human/model-system divergences is a benchmark asset for the drug-toxicity
> and organismal-response challenges that does not exist elsewhere.

That claim is defensible on the numbers above. The claim that dismech addresses the fifteen
challenges *broadly* is not, and should not be made.

---

## Appendix: reproducing the numbers

Counts in §3 come from a single pass over `kb/`. Save as `/tmp/dismech_stats.py` and run with
`uv run python /tmp/dismech_stats.py` from the repository root; it parses 2,214 YAML files in ~30 s.

```python
import glob, json, collections, yaml
try:
    from yaml import CSafeLoader as Loader
except ImportError:
    from yaml import SafeLoader as Loader

S, scale, disc = collections.Counter(), collections.Counter(), collections.Counter()
hypstatus, rel, evsrc, refpre = (collections.Counter() for _ in range(4))
pmids, mods = set(), collections.Counter()

def count_evidence(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == 'evidence' and isinstance(v, list):
                for e in v:
                    if isinstance(e, dict) and e.get('reference'):
                        r = str(e['reference']); S['evidence_items'] += 1
                        refpre[r.split(':')[0]] += 1
                        if r.upper().startswith('PMID'): pmids.add(r.split(':', 1)[1])
                        if e.get('evidence_source'): evsrc[e['evidence_source']] += 1
            count_evidence(v)
    elif isinstance(obj, list):
        for v in obj:
            count_evidence(v)

for kind, pat in (('disorder', 'kb/disorders/*.yaml'), ('module', 'kb/modules/*.yaml'),
                  ('comorbidity', 'kb/comorbidities/*.yaml'), ('grouping', 'kb/groupings/*.yaml')):
    files = glob.glob(pat)
    S[f'{kind}_files'] = len(files)
    for f in files:
        d = yaml.load(open(f, encoding='utf-8'), Loader=Loader)
        if not isinstance(d, dict):
            continue
        count_evidence(d)
        if kind == 'grouping':
            continue
        for n in d.get('pathophysiology') or []:
            S[f'{kind}_nodes'] += 1
            if n.get('biological_scale'):
                scale[n['biological_scale']] += 1
            if n.get('conforms_to'):
                S[f'{kind}_conforms_to'] += 1
                mods[str(n['conforms_to']).split('#')[0]] += 1
            S[f'{kind}_edges'] += len(n.get('downstream') or [])
            for k in ('cell_types', 'biological_processes', 'molecular_functions'):
                S[f'{kind}_{k}'] += len(n.get(k) or [])
        for h in d.get('mechanistic_hypotheses') or []:
            S[f'{kind}_hypotheses'] += 1
            hypstatus[h.get('status', 'UNSET')] += 1
        for x in d.get('discussions') or []:
            disc[x.get('kind', 'UNSET')] += 1
        for t in d.get('treatments') or []:
            S[f'{kind}_treatments'] += 1
            S[f'{kind}_target_mechanism_links'] += len(t.get('target_mechanisms') or [])
        for sec in ('experimental_models', 'animal_models', 'computational_models'):
            for m in d.get(sec) or []:
                S[f'{kind}_{sec}'] += 1
                for lk in m.get('modeled_mechanisms') or []:
                    S[f'{kind}_model_links'] += 1
                    rel[lk.get('relationship', 'UNSET')] += 1
                    S[f'{kind}_model_readouts'] += len(lk.get('readouts') or [])
        for p in ('phenotypes', 'genetic', 'biochemical', 'clinical_trials',
                  'environmental', 'datasets', 'definitions'):
            S[f'{kind}_{p}'] += len(d.get(p) or [])

print(json.dumps({'S': dict(S), 'scale': dict(scale), 'discussions': dict(disc),
                  'hypothesis_status': dict(hypstatus), 'model_relationship': dict(rel),
                  'evidence_source': dict(evsrc), 'reference_prefix': dict(refpre.most_common(15)),
                  'distinct_pmids': len(pmids), 'top_modules': dict(mods.most_common(15))},
                 indent=1, sort_keys=True))
```

Reference-cache year distribution (§5, leakage control):

```bash
cd references_cache && grep -h -m1 -E "^year:" PMID_*.md | tr -d "'\"" | awk '{print $2}' \
  | awk '{if($1>=2024) r++; tot++} END {print "cached:", tot, "| >=2024:", r}'
```
