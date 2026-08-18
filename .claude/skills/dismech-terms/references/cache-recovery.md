# Term-Cache Recovery

Read this reference when a term or enum cache has malformed rows, duplicate
CURIEs, incorrect labels, suspicious timestamps, or non-canonical ordering.

## Cache roles

- `cache/<prefix>/terms.csv` caches CURIE existence and canonical labels.
- `cache/enums/*.csv` caches membership in dynamic enums.

Both are derived artifacts that stand in for ontology authorities. Corrupting a
cache can make later validation confirm the corruption that produced it.

## Never synthesize rows

Do not type, concatenate, append, or hand-position cache rows. Labels commonly
contain commas. A line such as:

```text
MONDO:0012013,Weill-Marchesani syndrome 2, dominant,2026-08-01T04:30:00.000000
```

parses as four CSV fields and truncates the label. Rewriting that malformed row
as a clean-looking three-field row can cement the truncated label as cached
truth.

## Diagnose first

```bash
just check-term-cache-integrity
just check-cache-order
```

The integrity check covers headers, CSV field counts, CURIE syntax and prefix,
non-empty labels, ISO-8601 timestamps, duplicates, and the shape of enum cache
files. It is structural; it does not re-derive labels or memberships from OAK.

Use the online membership audit only when the enum cache itself is in question:

```bash
just check-enum-cache
```

Rows sharing one synthetic timestamp, especially midnight timestamps, are a
signal of ad-hoc seeding. Verify those labels against the configured ontology
rather than trusting the cache.

## Recover a term-label row

1. Identify the exact corrupt row and the KB file that references its CURIE.
2. Remove only that derived row. Do not type a replacement label or timestamp.
3. Re-derive it through the validator:

   ```bash
   just validate-terms kb/disorders/YourFile.yaml
   ```

4. Normalize and recheck:

   ```bash
   just normalize-cache
   just check-term-cache-integrity
   just check-cache-order
   ```

5. Inspect the resulting cache diff. If normalization exposes unrelated churn,
   surface it instead of reverting canonical order or hand-placing rows.

For an enum-membership failure, inspect the schema's dynamic enum and
`reachable_from` root. Do not insert a CURIE into `cache/enums/*.csv` to force a
pass; re-derive or repair membership through the maintained enum-cache tooling.
