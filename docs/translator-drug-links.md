# Translator Disease-Drug Link Explorer

`just translator-drug-links` queries the **NCATS Biomedical Translator** for the
drugs that may treat a disease, and reports them as ranked curation *leads*.

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
