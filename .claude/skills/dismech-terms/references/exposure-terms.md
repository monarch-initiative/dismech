# Exposure-Term Decisions

Read this reference when selecting, reviewing, or changing ECTO or XCO
bindings.

## Use the pinned local ontology

`conf/oak_config.yaml` configures ECTO and XCO with pinned local SQLite builds.
Search the same build the validator reads:

```bash
uv run runoak -i sqlite:obo:ecto search 'l~exposure to dust'
uv run runoak -i sqlite:obo:ecto info ECTO:0000006 -O obo
uv run runoak -i sqlite:obo:ecto descendants ECTO:3000000 -p i
```

Do not select an ECTO term solely because OLS resolves it. OLS may expose a
newer branch that the pinned validator build cannot see. A term that exists in a
different ontology snapshot is not a valid binding for the current repository.

Use `just environmental-term-audit` to measure exposure-binding coverage.

## Inspect both ancestry and semantic anchors

For a candidate exposure term, inspect ancestry and the full OBO record:

```bash
uv run runoak -i sqlite:obo:ecto ancestors ECTO:9000027 -p i
uv run runoak -i sqlite:obo:ecto info ECTO:9000027 -O obo
```

Ancestry shows the branch; the record shows relationships such as
`RO:0002309` (`involving`). Do not infer a specificity ladder merely from
similar labels.

## Smoking and alcohol bindings

The smoking and alcohol pairs below occupy distinct or disconnected branches.
Bind the term stated by the entry's own `name`:

| Entry name states | Bind |
|---|---|
| Smoking, tobacco smoking, or tobacco use as a habit | `ECTO:6000029` exposure to tobacco smoking |
| Cigarette smoking specifically | `ECTO:0100003` exposure to cigarette smoking |
| Alcohol consumption or drinking as a habit | `ECTO:0001082` exposure to alcohol consumption |
| Ethanol as a chemical exposure | `ECTO:9000027` exposure to ethanol |

The alcohol pair separates behavior from chemical substance.
`ECTO:0100003`, however, is not the chemical counterpart of tobacco smoking: it
describes product-specific cigarette-smoking behavior in a disconnected branch.
It is not a narrower child of `ECTO:6000029`.

Use the curated name as the binding signal. Descriptions and evidence often
mention a product or substance incidentally while making a behavioral claim.

If the name and mechanism disagree, fix the name before changing the CURIE. For
example, an entry centered on acetaldehyde, ALDH2, or ethanol-derived DNA adducts
should be named as ethanol exposure before binding `ECTO:9000027`. An entry that
only describes drinking-associated risk remains a behavioral exposure.

Record the reason for an ambiguous binding in `notes`, not `description`. Do not
migrate between a pair without checking that the entry name and mechanistic
claim both support the destination.
