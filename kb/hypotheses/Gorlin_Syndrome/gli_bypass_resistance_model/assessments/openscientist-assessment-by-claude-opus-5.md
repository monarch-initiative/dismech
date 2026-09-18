# OpenScientist review: `gli_bypass_resistance_model` (Gorlin syndrome)

Assessor: claude-opus-5. Verdict: **PARTIALLY_SUPPORTED**.

## What the report got right

This is one of the cleaner OpenScientist runs. I fetched 14 of its 26 distinct
PMIDs into `references_cache/` and compared each quotation against the cached
source. Every identifier resolved to a real paper, every paper was on topic, and
no quotation was contradicted by its source. Two PMIDs cited in the causal-chain
diagram (`PMID:8981943`, `PMID:41129277`) are missing from the run's own
citations sidecar but are real and appropriate.

The report's genuine contribution is not support for the seed hypothesis — that
was already curated from `PMID:31036756` — but a **bound** on it. It separates
three levels of applicability:

| Stratum | Applicability | Basis |
|---|---|---|
| SUFU-driven disease (BCNS2 / MHIBCC) | Strongest — primary resistance predicted from pathway topology | PMID:26677003, PMID:24651015, PMID:32796174 |
| Sporadic advanced BCC | Moderate — ~50% of resistant tumors carry acquired SMO mutations | PMID:25759020, PMID:23446420 |
| PTCH1-related Gorlin syndrome | Weakest — tumors uniformly suppressed, resistance rare and, in the one studied case, GLI-independent | PMID:38157930, PMID:40492880, PMID:30707899 |

Since the target disease is dominated by the third stratum, the honest reading
is that the hypothesis is strongest exactly where Gorlin syndrome is least
involved. The report says this plainly, which is to its credit.

## What needed correction

**The 9.1% versus 77% comparison is not like-for-like.** `PMID:38867459` states
that "Treatment interruption predominantly occurred due to side effects (69.1%)
and secondary resistance (9.1%)" — so 9.1% is the share of *interruptions*
attributable to resistance, not the share of the 351 Gorlin patients who became
resistant. `PMID:40492880`'s 77% is 10 of 13 locally advanced and metastatic BCC
patients, a group distinct from that paper's own 13 Gorlin patients. The
conclusion the report draws is right; the arithmetic offered for it is not. The
curated entry had inherited the phrasing and has been corrected.

**Two evidence-type gradings are wrong, both in the direction of weakening
competing evidence.** `PMID:30707899` is typed "Model organism" although its
ciliome mutation load and cilia immunostaining come from human naive, Gorlin,
and resistant tumors. `PMID:30297801` is typed "Model organism + human" although
its abstract reports only a Ptch1-Trp53 mouse model.

**`PMID:22391311` is read as established where it is explicitly tentative.** The
source says the arsenic binding mechanism "is proposed" and the zinc-finger
cysteines are "potential binding sites"; the evidence matrix states it as fact.
Nothing was curated from it.

**`PMID:26765315` is understated by its own reviewer.** The report reports
P<0.05 where the paper reports P < .001, and calls the tumor responses
"insufficient" where the paper states best overall response was stable disease
and that none had tumor shrinkage.

**`CL:0002559` is mislabeled.** The report calls it "hair follicle infundibulum
basal cell"; the repository term cache records it as **hair follicle cell**, a
much broader concept. No term from the report's ontology leads was bound;
`GO:0043408` is likewise absent from the caches.

**The recommended status change is not implementable.**
`MechanisticHypothesisStatusEnum` permits `CANONICAL`, `ALTERNATIVE`,
`EMERGING`, `DEPRECATED` — there is no `PARTIALLY SUPPORTED`, and the enum
grades curation maturity rather than evidence strength. Status left `EMERGING`.

## Provenance

The frontmatter declares 26 artifacts under `openscientist_artifacts/`. That
directory does not exist in the repository; the hypothesis folder holds only the
report and its citations sidecar. Every figure, evidence matrix, and provenance
JSON the report references is unavailable for inspection, so the evidence-matrix
compilation is recorded as `REPORTED_ONLY` / `UNVERIFIABLE`. The three search
claims the report makes (trial registries for BET/HDAC agents, trials in
SUFU-mutant disease, GenCC/ClinGen annotations for SUFU-BCNS2) name no resource
version and commit no search log, so they are `UNVERIFIABLE` rather than
`SEARCHED_NO_RESULT`.

## Integration into the disease YAML

All changes are in `kb/disorders/Gorlin_Syndrome.yaml`.

**Corrected** the `gli_bypass_resistance_model` `notes:` block, replacing the
"~9% vs ~77%" contrast with the Gan cohort's own Gorlin-specific observation and
an explicit statement of why the two published percentages are not comparable.

**Added seven evidence items** to the `gli_bypass_resistance_model` hypothesis
entry, each backing a clause the notes already asserted without a citation:

- `PMID:24651015` (SUPPORT, MODEL_ORGANISM) — SUFU-mutant and MYCN-amplified
  SHH-medulloblastoma xenografts are primarily resistant while PTCH1-mutant ones
  respond. This is the functional test of the pathway-topology argument that
  `PMID:26677003` makes only by inference, and it is in the tumor type Gorlin
  SUFU carriers actually develop.
- `PMID:21123452` (SUPPORT, MODEL_ORGANISM) — the primary source for the GLI2
  amplification arm, with its murine-allograft provenance stated so the arm is
  not read as equal in weight to the human SMO-mutation data.
- `PMID:29055107` (SUPPORT, IN_VITRO) — class I HDAC inhibition as a second,
  chemically independent demonstration that the convergent node is druggable.
- `PMID:40492880` twice — SUPPORT for 77% acquired resistance in advanced BCC,
  and REFUTE for the Gorlin arm of the same cohort, where all 11 patients who
  stayed on therapy kept sustained suppression.
- `PMID:30707899` twice — SUPPORT for "resistant BCCs usually maintain HH
  pathway activation", which is the premise the whole model rests on, and REFUTE
  for the cilia-loss/RAS-MAPK subset that escapes with *reduced* GLI output.
- `PMID:30297801` (REFUTE, MODEL_ORGANISM) — the WNT-dependent persister state,
  with the mouse-model caveat stated.

**Added one evidence item** to the existing `gap_gli_directed_therapy_resistance`
discussion: `PMID:26765315`, the only clinical test of GLI-directed therapy after
SMO-inhibitor failure. The gap previously cited only a review listing preclinical
agents; the trial result separates the pharmacodynamic question (GLI1 down 75%)
from the clinical one (best response stable disease, no shrinkage), which is what
the gap actually asks.

**Added one `KNOWLEDGE_GAP` discussion**,
`gap_gorlin_specific_resistance_mechanism`, with the report's multi-patient
Gorlin resistance-genomics study as its proposed experiment. This is the report's
highest-priority gap and the clearest curation need it surfaced: the entry cited
the lineage-transition finding but had nowhere recording that the Gorlin-specific
mechanism rests on a single patient and is otherwise open.

### Deliberately not changed

- **Status stays `EMERGING`.** The recommended value does not exist in the enum,
  and on the merits the report's own findings argue against promotion for a
  PTCH1-dominated disease entry.
- **No new pathophysiology nodes.** The report proposes nodes for BCC-to-SCC
  transition, WNT persistence, and cilia loss. These are acquired
  treatment-resistance states of tumors under therapy, documented almost entirely
  in sporadic BCC; modelling them as Gorlin pathophysiology nodes would assert a
  disease mechanism the sources do not support in this disease. They are captured
  as directional evidence on the hypothesis and as the new knowledge gap instead.
- **No ontology terms bound** — see `CL:0002559` above.
- **No `mechanistic_hypotheses` entry for the immune-checkpoint alternative**
  (`PMID:34000246`). Cemiplimab after Hedgehog-inhibitor failure is a therapeutic
  strategy, not a competing mechanism for how resistance arises, and the report
  itself files it as "parallel therapeutic strategy".
- **Nothing curated from `PMID:22391311`, `PMID:33608498`, `PMID:29550418`,
  `PMID:38757343`, or `PMID:37597490`** — respectively a review stating a
  proposed binding mode as fact, a colorectal-cancer result, and three
  preclinical GLI-degradation mechanisms with no BCC or Gorlin data.
