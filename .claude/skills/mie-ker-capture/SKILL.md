---
name: mie-ker-capture
description: >
  Turn a set of AOP-Wiki Key Events into a verified set of dismech causal edges.
  Use when an issue, pilot mapping, or project page names Key Events (especially
  Molecular Initiating Events) with no dismech counterpart and you need to find
  what each one leads to, judge whether the AOP-Wiki record supports the claim,
  and take the surviving edges through evidence verification. Covers the KER
  lookup, relevance filtering, chain assembly, and the evidence triage that
  decides how much literature work each edge needs.
---

# MIE -> KER capture

An AOP Key Event with no dismech counterpart is a curation lead, not a curation
task. This is the procedure that turns one into the other: find the edges the
Key Event sits on, discard the ones that are not about your disease, and find out
how much of the causal claim AOP-Wiki can actually back before you commit to
curating it.

Reaching the AOP-Wiki data is the `aop-wiki` skill's job — read it first for the
CLI, the date footgun, and the entity shapes. This skill is what you do with the
output.

**The finding that motivates the whole procedure: a KER can be completely
uncited.** In the 08-06-2026 snapshot, only 738 of 2,369 KERs carry any
references at all. A KER with an empty evidence block still renders as a clean
arrow between two named events, and nothing in the console output distinguishes
it from a well-supported one. Step 5 is where you find out, and it belongs
*before* any curation decision, not after.

## Step 1 — Fix the Key Event set, in writing

List the KE IDs you are working from and where they came from (issue, project
page table, an earlier sweep). Numeric IDs only; a KE title is not a key. Keep
the list — every later step is scoped to it, and a KE that enters the set
halfway through will silently skew the chain assembly.

## Step 2 — Run the lookup once, for the whole set

```bash
export AOP_WIKI_CLI_DATA_DIR=~/aop-wiki-data            # wherever you keep snapshots
ls "$AOP_WIKI_CLI_DATA_DIR"/outputs/cache/              # confirm the date exists first
aop-wiki-cli find-kers-for-events \
    --ke-ids 1529,593,1562,2288,2290 --date 08-06-2026
```

Pin the data directory before the first call. With none set, `aop-wiki-cli`
falls back to the current working directory — which, run from a dismech
checkout, writes `outputs/`, `xml_inputs/` and `logs/` into this repo.

One call for every KE in the set, not one per KE. The KER collection is the
expensive part and it is cached per date, so batching costs nothing extra and
keeps every result on one snapshot. Mixing snapshot dates across a set is how
you get an inconsistent chain.

## Step 3 — Read the JSON, never the console summary

The console clips each KER at 70 characters, which usually truncates the
downstream event title — the one thing the lookup exists to tell you.

```
<data-dir>/outputs/ker_lookups/<MM-DD-YYYY>/ker_lookup_<MM-DD-YYYY>.json
  {summary, matched_events, matched_kers}
```

`--limit` caps only what prints. A short console list is never a short result.

## Step 4 — Split by role, then filter by relevance

Each match carries `roles: {ke_id: "upstream"|"downstream"}`.

- **`upstream`** — the KE is the cause. These answer "what does this lead to".
- **`downstream`** — the KE is the effect. These answer "what produces it", which
  is what you want when the missing piece is an entry point rather than an outcome.

Then throw out the irrelevant ones. **A Key Event is stressor- and
organ-agnostic by design**, so its KERs run into every organ that shares the
molecular event.

`KE1562` (decreased Na/K ATPase activity) matches **six** KERs — four with
KE1562 upstream, two with it downstream. Of the four it leads to, exactly **one**
belongs to a cardiac chain:

| KER | Downstream event | Parent AOP | Keep, for cardiac work? |
|---|---|---|---|
| KER3444 | Increased, intracellular sodium | 556 — Decreased Na/K ATPase activity leading to heart failure | **yes** |
| KER2787 | Increase, cell membrane depolarization | 266 — Uncoupling of oxidative phosphorylation leading to growth inhibition | no |
| KER1811 | Decreased proximal tubular vectorial transport | 276 — Complex I inhibition leading to Fanconi syndrome | no |
| KER3287 | Decreased, sodium uptake in gills | 539 — Decreased Sodium/Potassium ATPase activity leads to Heart failure | no |

All four are correct AOP-Wiki content, and the ratio is the lesson: one edge in
six survived, because most of what a lookup returns is another organ's use of the
same molecular event.

**KER3287 is why no single title settles this.** Its parent AOP is titled "leads
to Heart failure" while the KER itself ends at sodium uptake in fish gills.
Filtering on the AOP title alone would have kept it. Resolve `aop_ids` against
`all_aops_*.json` *and* read the downstream event — where the two disagree, the
endpoint is what the edge actually asserts.

**A KER can carry both roles at once.** When Step 2 batches the whole KE set, a
KER whose two endpoints are both in that set records `upstream` and `downstream`
together. That is not ambiguity — it means the edge is internal to the chain you
are assembling, and it is a useful signal in Step 6 rather than something to
resolve here.

## Step 5 — Triage the evidence, and let it set priority

This is the step that changes what the rest of the work costs. Run it **before**
committing deep-research effort, not after — it is a prioritization gate, not a
post-hoc note.

### 5a — The 29.41% rule

`completion_score.percent == 29.41` on a KER means the record is an empty stub:
endpoints and identifiers, nothing else. This is exact, not a heuristic. In the
08-06-2026 snapshot 1,536 of 2,369 KERs (65%) sit at that value and **zero of
them carry a single reference**. It is also the corpus median, so most of
AOP-Wiki's causal edges are assertions with nothing behind them.

One number, read before anything else, tells you whether the KER has content.
A stub KER is not disqualified — but it means AOP-Wiki is contributing a
hypothesis and no evidence, and every citation will have to be found from
scratch. Rank the work accordingly, and say so when you report the plan.

### 5b — The evidence fields

For each surviving KER, read three fields on `ker_info` and one on its parent AOP:

| Field | On | What it tells you |
|---|---|---|
| `references` | KER | whether any literature is attached to *this edge* |
| `weight_of_evidence.free_text` | KER | whether anyone assessed the edge |
| `empirical_support.free_text` | KER | whether experimental support is described |
| `oecd_status` | AOP | whether the pathway was ever externally reviewed |

Three traps live here.

**`completion_score` is not a quality score.** It counts populated fields on the
wiki record. AOPs 552, 555, 556, 558 and 560 score 94–100% complete, have never
been OECD reviewed (`oecd_status: ""`), and every one of their KERs used in the
cardiac chains carries zero references. High completeness on an unreviewed
pathway is the most misleading state in the data.

**An empty `oecd_status` is not a rejection.** 450 of 596 AOPs are empty. It means
no review has happened. Endorsement raises confidence in a pathway; its absence
is not evidence against one, and neither state substitutes for literature.

**AOP-level references do not discharge a KER.** The AOP record carries a
`references` HTML blob — real citations, often substantial. They attest to the
pathway as a whole and cannot be attributed to any specific causal step. Treat
them as a starting bibliography for step 7, never as the citation for an edge.

### 5c — Map the AOP's citations onto its own steps

An AOP carries a `references` blob even when its KERs carry nothing. Do not stop
at counting it. Split it into individual citations and assign each one to the step
it actually serves — upstream, this edge, downstream, or none.

Two things fall out that a count cannot show.

**Whether the author evidenced this step at all.** AOP 558 carries ten citations
and not one measures cAMP after PDE inhibition — the edge the AOP is named for.
Four are enzyme-background or therapy reviews, four belong to the downstream
RyR2/calcium half, one is tangential, one has no evident connection to the
pathway. The bibliography is real and the step is still unevidenced.

**Whether the bibliography contradicts the pathway.** In the same list, Zhou 2017
attributes RyR2 hyperphosphorylation to oxidative-stress-driven calpain
activation — a competing mechanism to the cAMP/PKA route asserted by the very
next KER. An AOP citing evidence against its own edge is a strong signal to
verify that edge before curating it, and you only see it by reading the
citations rather than counting them.

Record the triage result per edge. An uncited KER is not disqualified — it is a
claim you will have to source entirely yourself, and knowing that up front is the
point.

## Step 6 — Assemble chains and find where they land

Group the surviving KERs by `aop_ids`. A single AOP usually supplies a connected
run, and the run is more informative than its edges: it shows where the new
entry point rejoins mechanism dismech already represents.

Check each downstream KE against `kb/modules/` before treating it as missing:

```bash
just list-modules                              # descriptions + conformance targets
rg -il "<mechanism term>" kb/modules           # is this already covered?
```

When a chain's downstream end already maps to a module node, the curation is an
entry-point node plus one edge — not a new module. Establish that before
proposing one.

## Step 7 — Verify every edge against primary literature

**AOP-Wiki is never a dismech reference.** There is no `AOP:` prefix in
`references_cache/`, no fetcher, and no cacheable body for a snippet to match, so
an AOP, KE or KER cannot appear in `reference:` under any circumstances.

Each surviving causal edge is its own claim and needs its own primary literature,
found independently — one deep-research pass per edge, not one per pathway. The
AOP's own bibliography is a lead list to start from and nothing more. From there
the normal rules apply without exception: `just fetch-reference PMID:...`, an
exact-substring `snippet`, `evidence_source` classifying the cited study, and
`just count-verified-snippets` in the loop. See `dismech-references`.

An AOP author's causal assertion is a hypothesis about a chain. It tells you
where to look. It never tells you what you found.

## Step 8 — Record what did not survive

An edge dropped for irrelevance, and an edge that no literature supports, are
both results worth writing down — in the issue, or in `notes:` on the node that
prompted the search. Otherwise the same KE gets re-nominated from the same AOP on
the next sweep, and the work is repeated rather than continued.
