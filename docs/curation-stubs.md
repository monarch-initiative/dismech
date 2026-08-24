# Curation stubs: the queue as repository content

The outstanding curation queue lives in [`stubs/`](https://github.com/monarch-initiative/dismech/tree/main/stubs)
as one YAML file per disease. A curation pull request deletes the stub and adds
the `kb/` entry. The queue is therefore a directory anyone can change by PR, and
the number of files in it is the remaining work.

This replaces reading a ranked score out of `dashboard/priority.json`.

## Why the ranked dashboard was replaced

The MONDO priority dashboard scored ~24,000 candidate MONDO terms with a
deterministic weighting over child counts, aggregator tags, synonym counts, and
xref counts, then presented the top of that ordering as the thing to curate
next. Issue [#8969](https://github.com/monarch-initiative/dismech/issues/8969)
records what went wrong. In short:

- **The head of the queue was all groupings.** The top 175 candidates were
  *every one* of them `CURATE_ROOT_WITH_SUBTYPES`; the first plain leaf disease
  was at rank 176. A single config line (`broad_parent_bonus: 8`) outweighed the
  spread across every other feature, so a curator following the dashboard could
  not reach a leaf disease at all.
- **The features point the wrong way.** More MONDO children is *stronger*
  evidence that a term is a grouping, not weaker — but it scored as a bonus.
  `soft tissue sarcoma` (about 800 NCIT subclasses) ranked above discrete
  diseases.
- **Already-finished work stayed in the queue.** The coverage filter never read
  `kb/groupings/`, so concepts correctly modelled as groupings were recommended
  as Disease entries forever.
- **The output read as an instruction.** `CURATE_ROOT_WITH_SUBTYPES` is an
  action code, and agents treated it as a ruling that overrode the repository's
  own lump/split policy — then wrote elaborate justifications for entries they
  could tell were wrong ([#8908](https://github.com/monarch-initiative/dismech/issues/8908)).

The deeper problem is not tuning. Every cheap feature available from an ontology
(child count, synonym count, aggregator tags) correlates with *being a grouping*
rather than with *being worth curating*, so no weighting over those features
produces a good queue. A score has to commit to an ordering it has no basis for.

A stub file does not have to. It records a nomination, and leaves the decision
where it belongs.

## The shape of a stub

```yaml
mondo_id: MONDO:0009770
label: 3MC syndrome 1
proposed_name: 3MC_Syndrome_1
status: OPEN
entry_type: UNDECIDED
priority: NORMAL
rationale: Diagnostic delay impact; Insufficient ICD coding/underdiagnosis
synonyms:
- Michels syndrome
- MASP1 3MC syndrome
sources:
- source_name: rare-disease-identification
  source_url: https://github.com/monarch-initiative/rare-disease-identification
  source_identifier: MONDO:0009770
  source_tags:
  - prioritization_category=expanded
  - prevalence_category=L
added_date: "2026-08-19"
```

Only `mondo_id` and `label` are required. The schema is
`src/dismech/schema/curation_stub.yaml`; the filename is the label slugged into
the `Title_Case_With_Underscores` style `kb/disorders/` uses.

### MONDO context in the file

`just enrich-stubs` adds three blocks from MONDO, so the lump/split call can be
made by reading the stub rather than by querying an ontology mid-task:

```yaml
mondo_parents:
- id: MONDO:0003321
  label: hereditary Wilms tumor
genes:
- id: hgnc:12796
  label: WT1
```

- **`mondo_parents`** answers the question that comes up most: *is this a subtype
  of something we have already curated?* `Wilms tumor 1` sitting under a curated
  `Wilms_Tumor` is a `has_subtypes` question, not a new-entry question, and the
  parent term says so directly.
- **`mondo_descendants`** (with `mondo_descendant_count`) is the strongest cheap
  signal that a term is a grouping — `autoimmune disease` carries 258. The list
  is capped at 25 and the count is always the true total, so truncation is never
  silent. It is **reported, never scored**: the old dashboard scored child count
  and got the sign backwards, which is what #8969 is about.
- **`genes`** is what MONDO records as causal (`RO:0004003`), in lowercase
  `hgnc:` form. It tells sibling numbered subtypes apart — `arterial
  calcification of infancy 1` is the ENPP1 one.

Across the current queue: 1,866 stubs have a parent, 1,331 have a causal gene,
and only 181 have any descendants at all — so the queue is mostly leaf diseases,
and the 181 are where the grouping question actually lives.

Enrichment is a separate pass from seeding because it needs the MONDO database
(`just fetch-ontology-dbs mondo`) while seeding stays offline. It is idempotent,
replaces only its own three blocks, and never touches anything a person wrote.

It records which MONDO release it read in `data/mondo/MANIFEST.yaml`, the same
way `data/orphadata/` and `data/icees-kg/` pin their bulk sources. Without that,
a re-run on a machine holding a different `mondo.db` produces
`mondo_descendant_count` churn across 1,846 files that nobody can attribute.

## `entry_type` is the lump/split decision, and it is not pre-filled

Every seeded stub is `entry_type: UNDECIDED`. Deciding whether a MONDO concept
should be a `kb/disorders/` Disease, a `kb/groupings/` Grouping, a `has_subtypes`
entry inside another disease, or nothing at all is a curator's first job. The
seeder deliberately does not guess, because guessing is what produced the
grouping-as-Disease precedent the dashboard created.

Three of the five values retire a stub *without* a disorder entry:

| Decision | What happens |
|---|---|
| `DISEASE` | Curate it. Delete the stub, add `kb/disorders/<Name>.yaml`. |
| `GROUPING` | Delete the stub, add `kb/groupings/<Name>.yaml` (see the Disease Groupings section of `CLAUDE.md`). |
| `SUBTYPE` | Delete the stub; the concept becomes a `has_subtypes` entry on the parent disease. Name the parent in `notes`. |
| `OUT_OF_SCOPE` | Delete the stub. A phenotype, a susceptibility term, an obsolete concept, or a category too abstract to carry a mechanism. |
| `UNDECIDED` | Still in the queue. |

Recording `GROUPING` or `OUT_OF_SCOPE` and deleting the stub is a completed
piece of curation. Say why in `notes` so the reasoning survives in git history
and the concept does not get re-nominated.

## Priority is asserted, not computed

`priority` is `HIGH` / `NORMAL` / `LOW`, set by a person in a pull request. There
is no score and no ranking within a band. `just next-stubs` spreads a band by a
stable hash of the MONDO ID rather than alphabetically — arbitrary, because the
order genuinely is, but reproducible, and it stops the head of the list looking
like a recommendation for whatever family of diseases sorts first. Pick the
disease you know something about rather than the first row. `--alpha` gives
alphabetical order if you want it.

If you want a disease curated sooner, open a PR raising its `priority` and say
why in `notes`. That is a reviewable claim other people can disagree with, which
a weight in a YAML config file was not.

## Claiming: GitHub is the live lock, the stub is not

The stub queue says what is left to do. It deliberately does **not** say who is
doing it. Those are different kinds of fact and they want different instruments:

|  | Stub queue (`stubs/`) | Claim (`claim`-labelled issue) |
|---|---|---|
| Fact | what is left to curate | who is curating what, right now |
| Changes | rarely, by considered PR | many times a day |
| Visible | when the PR merges — days | the instant the issue is created |
| Arbiter | review | GitHub |

A claim recorded in a stub file would only become visible on merge, which is far
too late to stop two agents picking the same disease. So the schema has no
`claimed_by` and no `CLAIMED` status: one fact, one source of truth.

**A claim is an open GitHub issue labelled `claim`**, titled:

```
Curate <label> (MONDO:NNNNNNN)
```

assigned to the person driving the work. Two parts are load-bearing:

- **The `claim` label.** `gh issue list --label claim` hits GitHub's *list*
  endpoint, which is immediately consistent — an issue filed thirty seconds ago
  is already visible. The `--search` form the old preflight used hits the search
  API, whose index lags creation by seconds to minutes, which is exactly the
  width of the race it was supposed to close. The label is also why the check is
  cheap: one call fetches every claim and matching happens locally, so the cost
  does not scale with the size of the candidate pool.
- **The MONDO ID in the title.** It is the key everything matches on. An issue
  titled `curate peripartum cardiomyopathy` locks nothing; `just check-claims`
  reports those separately so they can be retitled.

The label is deliberately broader than diseases — *"claim a disease (or other
entry) for curation"* — so a module or grouping claim has no MONDO ID to carry.
`check-claims` lists those separately and asks nothing of them; only a title
beginning `Curate` is expected to be MONDO-keyed.

The label already exists in the repository. Do not run `gh label create --force`
on it: `--force` updates an existing label, so it would overwrite the colour and
description.

```bash
just fetch-claims          # one API call -> tmp/claims.json
just next-unclaimed 5      # phase 1 claims, phase 2 stubs
just check-claims          # double-claims, unkeyed titles, stale claims
```

### Long-running PRs, and when a claim goes stale

A curation PR can sit in review for weeks. That is normal, and the claim must
hold that whole time — so **a claim with an open PR is never stale, however old
it is**. Only *old with no PR to show for it* is questionable:

```
stale — over 30d old with no linked PR (2):
  #1675  116d dragon-ai-agent      Curate autosomal dominant cerebellar ataxia type I (MONDO:0019792)
  #2029  107d unassigned           curate peripartum cardiomyopathy
```

`check-claims` **reports** these; it never releases them. Reassigning somebody
else's work is a conversation, not a timeout. Ask the assignee or the user
before taking one.

### Releasing a claim

The curation PR carries `Closes #<issue>`, so merging deletes the stub and
releases the claim in one step. If the answer turned out to be `GROUPING`,
`SUBTYPE`, or `OUT_OF_SCOPE`, the PR still deletes the stub — record the
decision in `notes` and close the issue explaining it. That is a completed
curation.

## Staleness is drift, not failure

Stubs are **informative, not curated content**. Nothing here is evidence, and
nothing here blocks anything.

A curation PR *should* delete the stub it curates:

```
- stubs/Yao_Syndrome.yaml
+ kb/disorders/Yao_Syndrome.yaml
+ history/disorders/Yao_Syndrome/2026-08-19-...yaml
```

but forgetting is not an error. `main` moves fast — 27 commits and 37 changed KB
files landed during the few hours this PR was open — so a stub whose disease
somebody else curated is a routine, expected event. **Gating on it would turn
every open stub PR red the moment an unrelated curation PR merged**, and curators
would spend their time servicing a bookkeeping message about work that was
already done correctly. A bit of overlap and a bit of lag are fine.

So `check-stubs` splits its findings, and only one kind gates:

| Severity | Means | Gates? |
|---|---|---|
| **error** | the *file* is broken — unparseable YAML, a malformed MONDO ID, a duplicate of another stub, a bad enum value | **yes** — only the stub's own author sees it, and it is cheap to fix |
| **advisory** | the *queue* has drifted — `already_curated`, `obsolete_term`, `possible_kb_duplicate` | never |

### Tidying up

The stale ones are cleared on a sweep, not by whoever happens to trip over them:

```bash
just tidy-stubs            # list what has gone stale
just tidy-stubs --apply    # delete it
```

`tidy` removes stubs whose MONDO ID a committed `kb/disorders/` or
`kb/groupings/` entry now covers, and stubs naming a MONDO term that has since
been retired. It does **not** touch `possible_kb_duplicate` advisories — those
are a judgement call about two different MONDO IDs, and a script should not be
making it.

Coverage means the entry's `disease_term`, any `has_subtypes[].subtype_term`, and
any exact/narrow `mondo_mappings`.

It also means **any** mapping on a `kb/groupings/` entry, whatever the predicate
— a directory the old prioritizer never read at all
([#8768](https://github.com/monarch-initiative/dismech/issues/8768)). The
predicate rule differs there on purpose. On a disease entry, a broad or close
mapping is a cross-reference to some *other* concept and must not retire it. On
a grouping it records how the grouping sits against the MONDO term it was built
around, and every such mapping in the KB today names a grouping-level concept —
`ciliopathy`, `RASopathy`, `inborn errors of metabolism`, `microcephaly` — which
is exactly what should not be sitting in a disorder queue.

### Did anything already curated get a stub?

Not at seed time — the seeder skips any nomination whose MONDO ID a KB entry
already covers (1,200 of the 3,079 nominations), and it skips obsolete terms.
Both go stale later as `main` moves, which is what `tidy` is for.

The MONDO-ID check cannot see one thing: a disease curated under a **different**
MONDO ID. That is the `possible_kb_duplicate` advisory, and there are 40. They
need a person, because the answer genuinely varies:

- `stubs/Friedreich_Ataxia_1.yaml` (`MONDO:0100340`) against a curated
  `Friedreich_Ataxia`. Probably redundant, or the entry should gain the mapping.
- `stubs/Long_QT_Syndrome.yaml` (`MONDO:0002442`) against
  `kb/disorders/Long_QT_Syndrome.yaml`, which curates the narrower *familial*
  long QT syndrome (`MONDO:0019171`). Arguably both should exist.
- `stubs/Leber_Congenital_Amaurosis_1.yaml` against a gene-first
  `GUCY2D-Related_Retinopathy`. Arguably a distinct entry that wants keeping.

Matching normalizes case, accents, and punctuation (`Wilms' tumor` ≡
`Wilms tumor`; `DeSanto-Shinawi` ≡ `Desanto shinawi`) and ignores anything under
eight characters or one word, so acronyms — `AIP`, `Bss`, `CRD` — do not collide
by coincidence.

## Where the initial queue came from

1,867 stubs, seeded from the Monarch
[rare-disease-identification](https://github.com/monarch-initiative/rare-disease-identification)
prioritised rare disease list (3,079 diseases, human-curated for phenotypic
characterization research), minus the 1,200 already covered by the KB.

Re-running the seeder only adds what is missing — it never rewrites or deletes an
existing stub, because a stub becomes hand-edited content the moment it lands.

```bash
curl -sSL -o /tmp/prd.yml \
  https://raw.githubusercontent.com/monarch-initiative/rare-disease-identification/main/prioritised-rare-disease-list.yml
just seed-stubs /tmp/prd.yml
```

Other nomination lists can be added by writing a parser in
`src/dismech/stubs/seed.py` and registering it in `_PARSERS`.

## Commands

```bash
just fetch-claims          # open claim issues -> tmp/claims.json (one API call)
just next-unclaimed 5      # the two-phase pick: claims, then stubs
just check-claims          # double-claims, unkeyed titles, stale claims
just next-stubs 5          # stubs only, no claim filter
just next-stubs 5 --json   # same, machine-readable
just stub-stats            # queue summary by status / entry type / priority
just check-stubs           # file well-formedness; runs as part of `just qc`
just tidy-stubs --apply    # sweep out stale stubs
just validate-stubs        # schema validation
just seed-stubs <file>     # import nominations; never overwrites
uv run dismech-stubs coverage   # how many MONDO IDs the KB already covers
```

## What happened to #1079

Issue #1079 was the other half of the old arrangement: a 67KB EPIC holding a
checkbox per disease for four keyword-matched themes (neurodevelopmental,
neurodegenerative, neuroimmune, cardiac — about 620 of the 3,079), rewritten by
`sync-epic-checkboxes.yml` on every push to `main`.

It is superseded. The stub queue is drawn from the same source list, covers all
of it rather than four themes, sees `kb/groupings/`, and can express "this is a
grouping, retire it" rather than only tick or not-tick. Two bugs in the EPIC's
sync go away with it: the script only ever ticks boxes and never unticks, and it
never read `kb/groupings/`. New claim issues no longer carry
`Tracker: part of #1079` — that line was decorative anyway, since most claims
(`rickets`, `glioblastoma`) fall outside its four themes.

Progress is now `just stub-stats` and the file count of `stubs/`.

## What happened to the dashboard

`dashboard/priority.html` and the `dismech-mondo-prioritize` scoring code are
still present and still generated. They are useful as a *browsable pool* — a way
to ask "what MONDO concepts exist under this parent that we have not touched" —
and as the source of new nominations to add to `stubs/`.

They are no longer the answer to "what should I curate next". That question is
answered by `stubs/`.
