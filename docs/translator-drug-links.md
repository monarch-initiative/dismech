# Translator Disease-Drug Link Explorer

`scripts/translator_drug_links.py` queries the **NCATS Biomedical Translator**
from the repo. It has two modes:

| Mode | Question | Target |
| ---- | -------- | ------ |
| **Links** (`just translator-drug-links`) | *"What drugs may treat this disease?"* | one disease |
| **Paths** (`just translator-drug-paths`) | *"By what mechanism might this drug act on this disease?"* | a disease-**drug pair** |
| **Regulation** (`just translator-regulators`) | *"What chemicals up/down-regulate this gene?"* (and the inverse) | a gene or a chemical |

These mirror the templated questions the Translator UI offers. Coverage against
the UI's own menu:

| UI feature | Here |
| ---------- | ---- |
| "What drugs may treat this disease?" | `just translator-drug-links` |
| "What chemicals up/downregulate this gene?" | `just translator-regulators GENE --direction …` |
| "What genes does this chemical up/downregulate?" | `--regulated-by CHEMICAL` |
| Pathfinder ("how are these two related?") | `just translator-drug-paths … --pathfinder` |
| Filter by approval / sort by evidence | `--asserted-only`, approval + phase columns |
| Per-result evidence (publications, sources) | per-hop `sources` and PMIDs |
| Saved workspaces, sharing, login | not replicated — the ARS pk in every report is the shareable handle |

Paths mode can additionally be run as a **hypothesis-investigation provider**
(`just translator-hypothesis`), writing its report into `kb/hypotheses/` beside
the OpenScientist/Falcon reports — see [Translator as a hypothesis provider](#translator-as-a-hypothesis-provider).

## Links mode

`just translator-drug-links` asks for the drugs that may treat a disease, and
reports them as ranked curation *leads*.

It is the programmatic equivalent of typing a disease into
[ui.transltr.io](https://ui.transltr.io/) (or the CI instance,
[ui.ci.transltr.io](https://ui.ci.transltr.io/)) and asking *"what drugs may
treat this?"* — with three things the web UI cannot do:

1. it reads the MONDO id straight out of a `kb/disorders/*.yaml` entry,
2. it flags which answers the entry **already curates**, turning a result list
   into a treatment-gap list,
3. it extracts the per-answer **PMIDs and NCT ids** so they can go straight into
   the normal `just fetch-reference` verification path.

## Leads, not evidence

Translator answers are aggregated across dozens of knowledge providers and are
partly **model-inferred** (the "creative mode" query this tool submits is the
drug-repurposing inference mode). They come with no quotable snippet, so a
Translator row can never be an evidence `reference:` on its own.

Treat the output exactly like a deep-research report — see the DR verification
workflow in [CLAUDE.md](https://github.com/monarch-initiative/dismech/blob/main/CLAUDE.md):

* every PMID must be fetched with `just fetch-reference PMID:XXXX` and the
  snippet you quote must survive `just validate-references`;
* every NCT id must be fetched the same way before a `clinical_trials:` block
  cites it;
* the drug identity (CHEBI/NCIT) must be checked with `just validate-terms`.

The script never writes KB YAML. This is deliberate, and it is what
distinguishes it from `just cohd-signal`: COHD returns a *citable statistic* for
a named cohort, so that tool emits a ready-made `association_signals` block.
Translator returns a *ranked belief*, so this tool emits a report.

## Usage

```bash
# Leads for an existing entry (MONDO id read from disease_term)
just translator-drug-links kb/disorders/Asthma.yaml

# Treatment gaps only: accepted/asserted links the entry does not yet curate
just translator-drug-gaps kb/disorders/Asthma.yaml

# No entry yet — query by CURIE or by name
just translator-drug-links --mondo MONDO:0004979 --top 40
just translator-drug-links --name "Marfan syndrome"

# Machine-readable output
just translator-drug-links kb/disorders/Asthma.yaml --format tsv
just translator-drug-links kb/disorders/Asthma.yaml --format json --output /tmp/leads.json

# Re-render an earlier run without re-querying (the pk is printed on every run)
just translator-drug-links kb/disorders/Asthma.yaml --pk 0d49364a-4340-4916-a4f1-6cb05c8c85a9
```

A run submits the query to the ARS and polls until the ARAs settle — typically
**2-6 minutes**. Progress is written to stderr, one line per poll, showing each
agent's status. Some agents error or hang on any given run; that is normal, and
the merged answer is assembled from whoever responds. A single straggler can
otherwise hold the run open for a long time, so polling also stops once no agent
status has changed for `--stall-seconds` (default 180). Whenever the run is cut
short — by a stall or by `--timeout` — the partial answer is still rendered and
the report is marked `**Partial**`; re-run with `--pk <pk>` later to pick up the
complete set.

Useful flags:

| Flag | Effect |
| ---- | ------ |
| `--top N` | Candidates to report (default 25; a run typically returns several hundred) |
| `--asserted-only` | Drop answers supported only by `prediction`-level edges |
| `--new-only` | Drop answers already curated in the entry |
| `--no-inferred` | Lookup-only query — asserted links, no repurposing inference |
| `--timeout` / `--stall-seconds` | Hard cap on the run, and how long to wait on a stalled agent (default 900 / 180) |
| `--predicate` | Query a different Biolink predicate |
| `--ci` | Use the CI deployment (`ars.ci.transltr.io`) instead of prod |
| `--save-raw PATH` | Keep the merged TRAPI message for offline inspection |

## Reading the report

```
| # | Status | Drug         | CURIE         | Score | Level    | Evidence                                | Sources |
| 2 | NEW    | Montelukast  | `CHEBI:50730` | 1.00  | asserted | 17 pub, 25 trial, approved_for_condition, phase 4 | ctd, drugcentral, ... |
```

* **Status** — `CURATED` if the drug is already in the entry (matched on a
  normalized CURIE against `treatments[].treatment_term.therapeutic_agent`, or
  on an exact treatment/agent name), otherwise `NEW`. Entries that curate drug
  *classes* without a `therapeutic_agent` (e.g. "Short-acting Beta Agonist")
  will show their member drugs as `NEW` — that is a signal to add the agent
  binding, not necessarily a missing treatment.
* **Score** — the ARA's ranking score. It orders candidates; it is not a
  probability and carries no evidential weight.
* **Level** — `asserted` when at least one chemical→disease edge carries a
  non-prediction `biolink:knowledge_level` (i.e. some source *asserts* the
  indication); `predicted` when the answer rests only on inference.
* **Evidence** — counts of publications and trials found on the direct
  chemical→disease edges, plus `biolink:clinical_approval_status` and
  `biolink:max_research_phase` when present. Mechanism-path edges reached
  through a support graph are deliberately excluded: they explain *how* a
  prediction was made, not whether the drug treats the disease.
* **Sources** — the `primary_knowledge_source` infores ids behind those edges
  (`drugcentral`, `ctd`, `semmeddb`, `multiomics-clinicaltrials`, …). Prefer
  candidates backed by curated sources over text-mined ones (`semmeddb` is
  co-occurrence text mining and is frequently wrong about directionality).

Answers that normalize to the same chemical (salt vs base, `UNII:` vs `CHEBI:`)
are collapsed into one row via the
[SRI node normalizer](https://nodenormalization-sri.renci.org/docs), which also
supplies the equivalent identifiers used for the `CURATED` match.

## Worked example

`just translator-drug-links kb/disorders/Chronic_Myeloid_Leukemia.yaml --top 15`
(709 candidates, top 15 shown):

```
| # | Status  | Drug               | CURIE          | Score | Level     | Evidence                                          |
| 1 | CURATED | Imatinib           | `CHEBI:45783`  | 1.00  | asserted  | 24 pub, 5 trial, approved_for_condition, phase 4  |
| 3 | CURATED | Dasatinib          | `CHEBI:49375`  | 1.00  | asserted  | 4 trial, approved_for_condition, phase 4          |
| 4 | NEW     | Hydroxyurea        | `CHEBI:44423`  | 1.00  | asserted  | 17 pub, approved_for_condition                    |
| 5 | NEW     | Bosutinib          | `CHEBI:39112`  | 0.99  | asserted  | approved_for_condition                            |
| 6 | NEW     | Indirubin          | `UNII:1LXW6D3W2Z` | 0.99 | predicted |                                                 |
| 13| NEW     | omacetaxine        | `CHEBI:71019`  | 0.96  | asserted  |                                                   |
```

The four curated TKIs come back as `CURATED`, which is the check that the query
resolved the right disease. The useful rows are the asserted `NEW` ones —
bosutinib, omacetaxine and hydroxyurea are accepted CML therapies the entry does
not yet carry. The `predicted` rows (indirubin here) are repurposing hypotheses:
interesting, and exactly the class of claim that needs primary literature before
it can appear in an entry at all.

## Paths mode: a disease-drug pair in, mechanism paths out

```bash
just translator-drug-paths kb/disorders/Chronic_Myeloid_Leukemia.yaml imatinib
just translator-drug-paths kb/disorders/Asthma.yaml CHEBI:50730 --via process
just translator-drug-paths kb/disorders/Asthma.yaml montelukast --new-only --top 40
```

Both ends of the query are pinned, so every answer is a **route** rather than a
ranked drug: `drug -> intermediate -> disease`, with each hop carrying its own
predicate, primary knowledge sources and PMIDs.

```
| # | Intermediate         | In entry?      | Score | Path                                                                        |
| 1 | ABL1 (`NCBIGene:25`) | genetic: ABL1  | 0.78  | imatinib --affects--> ABL1 | ABL1 --target_for--> chronic myelogenous leukemia |
| 3 | PDGFRA (`NCBIGene:5156`) | —          | 0.67  | imatinib --directly_physically_interacts_with--> PDGFRA | PDGFRA --gene_associated_with_condition--> ... |
| 4 | ABCB1 (`NCBIGene:5243`) | —          | 0.66  | imatinib --directly_physically_interacts_with--> ABCB1 | ABCB1 --gene_associated_with_condition--> ... |
```

`--via` picks the intermediate node type: `gene` (default), `protein`,
`gene-or-protein`, `pathway`, `process`, `phenotype`, `chemical`, `any`. In
practice **only `gene` has broad KP support** — an everolimus→TSC run with
`--via process` came back with no merged result set at all, because no ARA
answers a `BiologicalProcessOrActivity` intermediate. The other values are
wired up and worth retrying as coverage improves, but do not expect answers
today.
Predicates are deliberately left open — `physically_interacts_with`, `affects`
and `interacts_with` are all used for the same drug-target relation by different
providers, so constraining the predicate silently drops real routes.

**"In entry?"** resolves the intermediate against what the disorder entry
already models: `genetic[].gene_term`, and the `genes`, `biological_processes`,
`molecular_functions`, `chemical_entities` and `gene_products` bound on any
pathophysiology node. Matching is CURIE-first through the SRI normalizer
(Translator answers in `NCBIGene:`, dismech curates `hgnc:`), falling back to an
exact name. So the report reads as *mechanism you already model* vs *mechanism
you don't* — and a top-ranked route showing `—` is often a binding gap rather
than a new mechanism (the CML entry names its fusion gene "BCR-ABL1" with no
gene CURIE, so ABL1 shows as new).

When the drug is already a curated treatment, the header also prints its
declared `target_mechanisms`, which is the claim the paths should be read
against:

```
- Entry already curates this drug as: **imatinib**
  - declared `target_mechanisms`: Constitutive Tyrosine Kinase Activation (INHIBITS)
```

### What paths mode is not

Ranking mixes provenance of very different quality — text-mined co-occurrence
(`semmeddb`) is scored alongside curated pharmacology (`drugcentral`, `dgidb`,
`chembl`). A high-scoring route is a **hypothesis about mechanism**, and the
per-hop `sources` column is the first thing to read. Reversed hops appear too
(`ABCG2 --interacts_with--> imatinib`): direction is a property of the asserting
source, not a claim about causality.

Two other things worth knowing: the ARS's own creative-mode "support graphs" are
evidence *bundles* (all the direct drug-disease edges, look-alike diseases, a bag
of disease genes), not chains — which is why paths mode issues an explicit
two-hop query instead of mining them. And the TRAPI Pathfinder query shape is
rejected by every ARA on the prod ARS today (400/422), so it is not used.

### Pathfinder

`--pathfinder` swaps the hand-built two-hop lookup for the ARS's own Pathfinder
query — the UI's "how are these two related?" mode. It returns arbitrary-length
routes and lets the ARS combine lookup and inferred reasoning:

```bash
just translator-drug-paths kb/disorders/Chronic_Myeloid_Leukemia.yaml imatinib --pathfinder
```

Three things to know before relying on it:

* **CI only.** Every prod ARA rejects the query shape (400/422); only
  `ars.ci.transltr.io` answers it, so the flag implies `--ci`. That is why the
  CI UI is worth keeping open alongside the prod one.
* **Routes come back unordered.** A Pathfinder answer is a *bag* of edges in an
  auxiliary graph, not a chain, so the tool walks it back into an ordered route
  from drug to disease. A hop traversed against its asserted direction is
  rendered pointing backwards (`SIN3A <--interacts_with-- BCR`) rather than
  silently flipped — the arrow always shows what the source actually claims.
* **Co-target routes are dropped by default.** `intermediate_categories` only
  requires that a gene appear *somewhere* on the route, so an unfiltered
  imatinib→CML Pathfinder run returns `imatinib → PDGFRB → ABL1 → ponatinib →
  CML` and nine more of the same shape: every top route detours through a rival
  TKI. Those are co-prescription and shared-target artifacts, so routes through
  another drug are excluded unless you pass `--include-chemical-intermediates`.

Given the CI-only status and the noise, the two-hop default remains the one to
reach for; Pathfinder is worth it when you want multi-hop routes the two-hop
query structurally cannot see.

## Regulation mode: the up/down-regulation templates

```bash
just translator-regulators ABL1                       # chemicals that decrease ABL1
just translator-regulators TP53 --direction increased
just translator-drug-links --regulated-by imatinib --direction decreased
```

The direction rides on the Biolink **qualifier set**
(`object_direction_qualifier: decreased`, `object_aspect_qualifier:
activity_or_abundance`), not on the predicate, which stays `biolink:affects`.
Pin the gene to ask which chemicals regulate it; pin the chemical
(`--regulated-by`) to ask which genes it regulates.

This is the mode that lines up most directly with the dismech data model: a
pathophysiology node's `biological_processes` and `genes` carry
`modifier: INCREASED`/`DECREASED`, and a treatment's `target_mechanisms` carries
`treatment_effect: INHIBITS`/`ACTIVATES`. Asking "what decreases ABL1 activity"
returns imatinib, ponatinib, dasatinib and nilotinib in rank order — the
`INHIBITS` set for the CML kinase node.

Answers are cross-referenced like the other modes: chemical answers against the
entry's curated treatments, gene answers against its curated mechanism.

!!! warning "Gene lookups are pinned to human"

    An unrestricted name-resolver lookup for `ABL1` returns the **dog**
    orthologue (`NCBIGene:491292`) ahead of the human gene, which would answer a
    different question without complaining. Symbol lookups therefore force
    `only_taxa=NCBITaxon:9606`. Pass an explicit CURIE if you want another
    species.

## Translator as a hypothesis provider

dismech already has a provider pipeline for mechanistic-hypothesis
investigation: a report lands at
`kb/hypotheses/<Disorder>/<hypothesis_group_id>/<provider>.md`, gets reviewed
with the `review-hypothesis-exploration` skill into an
`assessments/<provider>-assessment-by-<assessor>.yaml` sidecar, and only then
does anything reach the disorder YAML (see
[Hypothesis Report Assessments](hypothesis-report-assessments.md)).

Translator plugs into that pipeline as the provider slug **`translator`** — the
non-LLM member of the set. Where OpenScientist reasons over literature, this
returns knowledge-graph routes:

```bash
just translator-hypothesis kb/disorders/Siderius_Type_X-Linked_Intellectual_Disability.yaml \
    sirolimus mtor_targeting
```

writes:

```text
kb/hypotheses/Siderius_Type_X-Linked_Intellectual_Disability/mtor_targeting/
  translator.md               # frontmatter (provider, timings, ARS pk, query graph) + the path report
  translator.md.citations.md  # the numbered PMIDs the paths rest on
```

The `hypothesis_group_id` must exist in the entry's `mechanistic_hypotheses`
(the script lists the available ids on a miss). Because the report is named for
its provider, `just research-hypotheses --missing-provider translator` picks up
the coverage gap for free, and the report renders on the disorder page like any
other hypothesis report.

Review it exactly like an LLM provider report — with one extra caveat specific
to this provider: a `report_quote` in the assessment sidecar will be quoting a
*graph assertion*, not a sentence from a paper.

### Side by side with OpenScientist

Three hypotheses now carry a `translator.md` next to a provider report, and the
contrast is the point — they answer different questions and fail in different
directions:

| | OpenScientist | Translator |
| --- | --- | --- |
| TSC / `canonical_tsc1_tsc2_mtorc1_hyperactivation_model` | 564 lines, 48 citations, ~46 min. Verdict "STRONGLY SUPPORTED with seven critical qualifications" — RCT evidence that everolimus does *not* improve IQ or autism, mTORC1-independent pathways, the developmental critical window | 3 paths, 4 citations, ~4 min. TSC1 and TSC2 matched to the entry's own pathophysiology node; one unmatched IFNG route |
| Gorlin / `gli_bypass_resistance_model` | narrative assessment of SMO-inhibitor resistance | 3 paths, all three intermediates (SUFU, PTCH2, PTCH1) matched to curated genes |
| Siderius XLID / `mtor_targeting` | — | 2 weak routes, neither through PHF8/RSK1/mTOR |

Read that as a division of labour, not a ranking. OpenScientist weighs a
hypothesis against the literature and argues; Translator says what a dozen
curated knowledge graphs *already assert*, in minutes, with the answers already
diffed against the entry. The Gorlin run is the cleanest illustration: every
returned intermediate was one the entry curates, so the honest conclusion is
"the graph adds nothing here" — quick, and worth knowing before commissioning a
deep-research run.

**Know what the query shape can and cannot express.** In the TSC run, `MTOR` —
everolimus's actual target and the whole subject of the hypothesis — never
appears. A gene-intermediate two-hop asks for genes that are *associated with
the disease* and that the drug touches, and MTOR is correctly not a TSC disease
gene. The mode therefore finds disease genes the drug contacts, not a mechanism
of action.

Neither alternative rescued it for this pair, and it is worth knowing before you
go looking:

| Query | Result for everolimus → TSC |
| ----- | --------------------------- |
| two-hop `--via gene` (default) | TSC1, TSC2 — correct disease genes, both matched to the entry's own pathophysiology node; plus one unmatched IFNG route |
| `--via process` | **no merged result set at all** — no ARA answers a `BiologicalProcessOrActivity` intermediate |
| `--pathfinder` | 12 routes, every one through generic intermediates (Apoptosis, IL4, interferon-γ, phosphorylation) at score ≈0.17; no MTOR, TSC1 or TSC2 |

So for a drug whose mechanism is textbook, the Translator graph does not carry
the drug → target → pathway chain in any mode currently queryable, and the plain
two-hop gives the most on-target answer. Treat "what does the graph assert" and
"what is the mechanism" as different questions — which is the whole reason this
output is filed as leads.

**Absence is a result.** The Siderius worked example is a negative one,
and deliberately so. The `mtor_targeting` hypothesis (status `EMERGING`) rests
on a single Phf8-knockout mouse study in which rapamycin reversed the
phenotype. Translator returns just two weak routes from sirolimus to the
disease, through **FGD1** and **UBE2B**, both from a drug-response correlation
KP — neither through PHF8, RSK1, or mTOR itself. That "no independent
knowledge-graph route supports this mechanism" is exactly the kind of finding
worth recording in an assessment sidecar, and it is one an LLM provider is
much less likely to state plainly.

## Where it fits

| Source | What it gives | Emits YAML? |
| ------ | ------------- | ----------- |
| `NCIT:P302` (`just ncit-p302-audit`) | Curated NCI *accepted therapeutic use*, citable as a structured-source snippet | evidence-ready |
| `just cohd-signal` / `ICEES:` | EHR co-occurrence statistics for disease pairs | yes (`association_signals`) |
| **`just translator-drug-links`** | Ranked drug candidates across ~15 knowledge providers, incl. repurposing inference | no — leads only |

Translator is the widest net of the three and the only one that surfaces
*candidate* (not yet accepted) therapies; it is correspondingly the one whose
output needs the most verification.

## Implementation

`scripts/translator_drug_links.py`. The network layer is a thin ARS client
(submit → poll `?trace=y` → fetch the merged message); everything that shapes
the report is pure and covered by `tests/test_translator_drug_links.py`.
