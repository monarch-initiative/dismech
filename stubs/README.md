# Curation stubs — the outstanding work queue

One YAML file per disease we intend to curate but have not curated yet.

**This directory is the curation queue.** Its size is the remaining work, and it
shrinks by one file per curated disease.

## The contract

A curation pull request **deletes the stub and adds the KB entry**, in the same PR:

```
- stubs/Yao_Syndrome.yaml
+ kb/disorders/Yao_Syndrome.yaml
+ history/disorders/Yao_Syndrome/...
```

`just check-stubs` (part of `just qc`, and run in CI) fails if a stub names a
MONDO ID that a committed `kb/disorders/` or `kb/groupings/` entry already
covers. So you cannot curate a disease and forget its stub.

## Anyone can change the queue by pull request

This is the point of the design. The queue is repository content, not a
generated score, so changing it is a normal reviewable diff:

- **Add a disease** — write a new stub file. Only `mondo_id` and `label` are
  required.
- **Raise or lower a disease** — change `priority` to `HIGH` / `NORMAL` / `LOW`,
  and say why in `notes`.
- **Claim one** — set `status: CLAIMED` and `claimed_by: <your-handle>`.
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
| `status` | `OPEN` (default), `CLAIMED`, `BLOCKED`, `DEFERRED`. |
| `entry_type` | `UNDECIDED` (default), `DISEASE`, `GROUPING`, `SUBTYPE`, `OUT_OF_SCOPE`. |
| `priority` | `HIGH`, `NORMAL` (default), `LOW`. Hand-set. |
| `rationale` | Why this is worth curating. |
| `synonyms` | MONDO synonyms, to help duplicate checks. |
| `sources` | Who nominated it. |
| `claimed_by`, `issue` | Who has it, and the tracking issue. |
| `notes` | Everything else — lump/split reasoning, scope objections. |

## Seeded from

The initial 1,879 stubs come from the Monarch
[rare-disease-identification](https://github.com/monarch-initiative/rare-disease-identification)
prioritised rare disease list, minus every concept the KB already covers. Those
stubs are `entry_type: UNDECIDED` and `priority: NORMAL` across the board on
purpose — an importer cannot tell a disease from a grouping, and pretending
otherwise is what the old ranked dashboard got wrong (dismech#8969).

## Commands

```bash
just next-stubs 5          # what to curate next
just stub-stats            # queue summary
just check-stubs           # invariants (also runs in `just qc`)
just validate-stubs        # schema validation
just seed-stubs <file>     # import more nominations; never overwrites
```

See [`docs/curation-stubs.md`](../docs/curation-stubs.md).
