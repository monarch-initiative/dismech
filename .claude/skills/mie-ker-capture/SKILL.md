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
uncited** — most are. A KER with an empty evidence block still renders as a clean
arrow between two named events, and nothing in the console output distinguishes
it from a well-supported one; `ker-evidence-triage` carries the measurement.
Step 5 is where you find out, and it belongs *before* any curation decision, not
after.

## Scope — this is the MIE case

The procedure was written for **Molecular Initiating Events**: a Key Event with
no dismech counterpart sitting at the *start* of a chain. Its worked examples are
all that shape. The same quality checks would be wanted for a pathway-terminating
Adverse Outcome, or for an intermediate Key Event, and most of this transfers
unchanged — the lookup is direction-agnostic (`find-kers-for-events` returns both
roles, and Step 4 says how to read each), and the relevance filter, evidence
triage, connected components and literature verification do not care which end
you started from.

Two things do bake in the MIE direction, and are what a future AO or
intermediate-KE version would have to revisit:

- **Step 6 checks the downstream end** against the Step 1 entity. An AO-driven
  sweep asks the mirror question — is the mechanism *leading to* this outcome
  already represented? — so that check would run on the upstream end instead.
- **Step 6's curation outcome assumes an entry point**: a new node plus a
  `downstream` edge into existing mechanism. For an Adverse Outcome the new node
  is terminal, and the edge runs from existing mechanism into it.

Do not generalize either of those speculatively. Wait for a real Adverse Outcome
or intermediate-Key-Event use case, and let it say what is actually needed.

## Step 1 — Fix the Key Event set and the disease or module entity, in writing

Record two things before anything else.

**The disease or module entity** — the dismech entry this sweep is for, by
slug. Every filtering decision from Step 4 on is relative to it, and leaving it
unrecorded means "irrelevant" cannot be justified or reviewed later.

**The KE set** — the KE IDs you are working from and where they came from
(issue, project page table, an earlier sweep). Numeric IDs only; a KE title is
not a key. Keep the list — every later step is scoped to it, and a KE that
enters the set halfway through will silently skew the chain assembly.

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

Then throw out the irrelevant ones.

`KE1562` (decreased Na/K ATPase activity) matches **six** KERs — four with
KE1562 upstream, two with it downstream. Of the four it leads to, exactly **one**
belongs to a cardiac chain:

| KER | Downstream event | Parent AOP | Keep, for the disease or module entity? |
|---|---|---|---|
| KER3444 | Increased, intracellular sodium | 556 — Decreased Na/K ATPase activity leading to heart failure | **yes** |
| KER2787 | Increase, cell membrane depolarization | 266 — Uncoupling of oxidative phosphorylation leading to growth inhibition | no |
| KER1811 | Decreased proximal tubular vectorial transport | 276 — Complex I inhibition leading to Fanconi syndrome | no |
| KER3287 | Decreased, sodium uptake in gills | 539 — Decreased Sodium/Potassium ATPase activity leads to Heart failure | no |

All four are correct AOP-Wiki content, but only one edge out of six aligns with
the disease or module entity.

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

**Do this before Step 6, and before committing any deep-research effort.** It is
a prioritization gate, not a post-hoc note: it decides what the rest of the work
costs, and an edge triaged after curation has already been paid for.

Run the `ker-evidence-triage` skill over the KERs that survived Step 4. It covers
the 29.41% stub rule, the four evidence fields to read on the KER and its parent
AOP, the three traps in reading them, and how to map an AOP's citation blob onto
its own steps.

Two of its results feed the steps below. A KER's triage outcome sets the priority
you give its edge, and it is recorded per edge for Step 8. A stub KER is not
disqualified — it means every citation will have to be found from scratch in
Step 7, and knowing that up front is the point.

## Step 6 — Assemble chains and find where they land

**Compute connected components over the surviving KERs, and treat each component
as one chain.** Two edges belong to the same chain when they share a Key Event —
including an event you never named, since a chain routinely runs through events
outside your Step 1 set. A component is more informative than its edges: it shows
where the new entry point rejoins mechanism dismech already represents.

**Do not group by `aop_ids`.** An AOP is a curatorial packaging unit, not a
mechanism boundary, so grouping by it goes wrong twice: it splits one connected
mechanism across many buckets, and it double-counts, because a KER commonly
belongs to several AOPs at once. A five-KE trial over the androgen-receptor axis
returned 28 KERs forming exactly two components — the androgen chain and an
unrelated cholinergic one, a split that matches the biology. Grouping the same
edges by `aop_ids` scattered the 24-edge androgen component across **19** AOPs and
listed one edge, KER2124, in **ten** of them.

AOP identity is **provenance**: carry it on each edge so you can say which pathway
asserted the claim, and cite it when you report. It is not the organizing key.

### Is the downstream end already represented?

Check each downstream KE before treating it as missing, and check the **entity
from Step 1 first**. Its own pathophysiology nodes are what decide the question;
`kb/modules/` answers a different one.

```bash
# The entity you recorded in Step 1. Cystic fibrosis is the example used
# throughout this section; substitute your own. A module target lives under
# kb/modules/<name>.yaml and works the same way.
ENTITY=kb/disorders/Cystic_Fibrosis.yaml

# 1. the entity's own nodes — this is what "already represented" means
python3 -c "import yaml,sys; print('\n'.join(p['name'] for p in \
  yaml.safe_load(open(sys.argv[1]))['pathophysiology']))" "$ENTITY"

# 2. modules — asked separately, and for conformance rather than coverage
just list-modules                              # descriptions + conformance targets
rg -il "<mechanism term>" kb/modules
```

**Do not use `conforms_to` as the test.** A node represents its mechanism whether
or not it declares one: 60% of disorder entries carry no `conforms_to` at all and
only 17% of pathophysiology nodes have one, so routing the check through modules
misses the majority case. Cystic fibrosis is typical — 27 nodes, none conforming,
and its mucus and airway-obstruction nodes plainly cover the downstream half of
AOP 148's EGFR chain.

Three outcomes, and they differ in what work remains:

| The downstream KE matches | What to curate | Step 7? |
|---|---|---|
| a node in the Step 1 entity | an entry-point node plus a `downstream` edge to the existing node | **no** — that edge is already carried, with its own evidence |
| a node in `kb/modules/` but not in the entity | a node in the entity for it, declaring `conforms_to` the module node | yes |
| nothing | the node and the edge, from scratch | yes |

Row 1 is the only place this procedure narrows Step 7's input, and it is worth
the check: re-verifying an edge dismech already holds is wasted deep-research
effort. Record it in Step 8 so the next sweep does not re-nominate it.

**The edge you add takes a bare name, not an entity reference.** A `downstream`
target is matched verbatim against another item's `name` — writing
`pathophysiology#Mucus Plugging` there is not an error anyone will catch for you.
It draws a phantom node and silently detaches the real one (see `CLAUDE.md`,
"Pathograph Targets Are Bare Names"). Run `just check-causal-targets <file>` after
adding it.

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

## Step 8 — Record what you did not curate, and why

Three outcomes end without a new curated edge. Write all three down — in the
issue, or in `notes:` on the node that prompted the search — so the next sweep
continues the work rather than repeating it:

| Outcome | Decided at | What a later sweep would otherwise do |
|---|---|---|
| Dropped as irrelevant to the disease or module entity | Step 4 | re-nominate the same KE from the same AOP |
| Already represented in dismech | Step 6 | re-nominate an edge dismech already carries, with its own evidence |
| No primary literature supports it | Step 7 | repeat a search that has already been paid for |

The second is the one most easily lost, because it is not a failure — the edge
exists, and the sweep's result is the confirmation that it does.
