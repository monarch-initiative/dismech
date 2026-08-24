# Curation stubs — the outstanding work queue

One YAML file per disease we intend to curate but have not curated yet.

**This directory is the curation queue.** Its size is the remaining work, and it
shrinks by one file per curated disease.

## These files are informative, not curated content

Nothing here is evidence, and nothing here blocks anything. A curation pull
request *should* delete the stub it curates:

```
- stubs/Yao_Syndrome.yaml
+ kb/disorders/Yao_Syndrome.yaml
+ history/disorders/Yao_Syndrome/...
```

but if it does not, that is fine. A stub whose disease got curated elsewhere is
**stale, not wrong** — `just check-stubs` reports it as an advisory and never
fails on it. Gating would mean an unrelated curation PR merging on `main` turns
every open stub PR red, and no curator should ever have to service that.

`just tidy-stubs --apply` sweeps the stale ones out periodically. A bit of
overlap and a bit of lag in between are expected.

`just check-stubs` fails only on a **malformed file**: unparseable YAML, a bad
MONDO ID, a duplicate of another stub, a bad enum value. Only the person who
wrote that stub sees those.

## Anyone can change the queue by pull request

This is the point of the design. The queue is repository content, not a
generated score, so changing it is a normal reviewable diff:

- **Add a disease** — write a new stub file. Only `mondo_id` and `label` are
  required.
- **Raise or lower a disease** — change `priority` to `HIGH` / `NORMAL` / `LOW`,
  and say why in `notes`.
- **Claim one** — *not here.* Claims are open GitHub issues labelled `claim`,
  titled `Curate <label> (MONDO:NNNNNNN)`. A stub edit only becomes visible when
  its PR merges, which is useless as a lock. See "Claiming" below.
- **Argue it out of the queue** — set `entry_type` to `GROUPING`, `SUBTYPE`, or
  `OUT_OF_SCOPE` with the reason in `notes`. Once agreed, the stub is deleted
  without a `kb/disorders/` entry ever being written. That is a real curation
  outcome, not a failure.

A stub carries no computed score and no ranking within a priority band —
`just next-stubs` spreads a band by a stable hash, so its order is arbitrary by
design. Pick the disease you actually know something about.

## Fields

Defined by [`src/dismech/schema/curation_stub.yaml`](../src/dismech/schema/curation_stub.yaml).

| Field | Meaning |
|---|---|
| `mondo_id` | Required. `MONDO:NNNNNNN`. |
| `label` | Required. MONDO label. The filename is this label slugged. |
| `proposed_name` | Suggested `kb/disorders/` filename stem. Advisory. |
| `status` | `OPEN` (default), `BLOCKED`, `DEFERRED`. A durable judgement about availability — *not* a claim. |
| `entry_type` | `UNDECIDED` (default), `DISEASE`, `GROUPING`, `SUBTYPE`, `OUT_OF_SCOPE`. |
| `priority` | `HIGH`, `NORMAL` (default), `LOW`. Hand-set. |
| `rationale` | Why this is worth curating. |
| `synonyms` | MONDO synonyms, to help duplicate checks. |
| `mondo_parents` | Direct MONDO superclasses — is this a subtype of something already curated? |
| `mondo_descendants` | MONDO subclass descendants (capped at 25) plus `mondo_descendant_count`. A long list means grouping. |
| `genes` | MONDO's causal genes (`RO:0004003`), lowercase `hgnc:`. Tells sibling subtypes apart. |
| `sources` | Who nominated it. |
| `notes` | Everything else — lump/split reasoning, scope objections. |

## Seeded from

The initial 1,867 stubs come from the Monarch
[rare-disease-identification](https://github.com/monarch-initiative/rare-disease-identification)
prioritised rare disease list, minus every concept the KB already covers. Those
stubs are `entry_type: UNDECIDED` and `priority: NORMAL` across the board on
purpose — an importer cannot tell a disease from a grouping, and pretending
otherwise is what the old ranked dashboard got wrong (dismech#8969).

## Claiming

The lock is an **open GitHub issue labelled `claim`**, titled
`Curate <label> (MONDO:NNNNNNN)`, assigned to whoever is driving the work. The
label makes the check a fast, immediately consistent list query; the MONDO ID in
the title is the key it matches on.

```bash
just fetch-claims          # one API call -> tmp/claims.json
just next-unclaimed 5      # stubs minus everything already claimed
just check-claims          # double-claims, unkeyed titles, stale claims
```

A claim holds for as long as its PR is open — long-running curation PRs are
normal. Only *old with no PR* is questionable, and `check-claims` reports those
for a person rather than releasing them automatically.

## Commands

```bash
just next-stubs 5          # what to curate next (no claim filter)
just stub-stats            # queue summary
just check-stubs           # file well-formedness (also runs in `just qc`)
just tidy-stubs --apply    # sweep out stale stubs
just validate-stubs        # schema validation
just seed-stubs <file>     # import more nominations; never overwrites
```

See [`docs/curation-stubs.md`](../docs/curation-stubs.md).
