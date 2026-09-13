---
name: aop-wiki
description: >
  Query the AOP-Wiki XML export — Adverse Outcome Pathways, Key Events, and Key
  Event Relationships — through the installable aop-wiki-cli module. Use when asked
  to find the AOP/KE/KER for a mechanism, stressor, or adverse outcome; to run
  or write an AOP-Wiki term search config; to pull KER weight-of-evidence,
  empirical support, or evidence tables; to get event completion/integration
  rankings; or to refresh the AOP-Wiki XML snapshot.
---

# AOP-Wiki access via `aop-wiki-cli`

`aop-wiki-cli` is an installable module —
[gingin77/aop_wiki_cli](https://github.com/gingin77/aop_wiki_cli). It owns the
XML download, the parsers, and the entity model; **do not add downloading or
parsing code to dismech**, and do not have dismech code read its XML or cache
files. If a query needs something the CLI cannot do, add a command there.

```bash
uvx --from git+https://github.com/gingin77/aop_wiki_cli aop-wiki-cli --help
```

That form tracks the repository's default branch, so the tool can change under
you between runs. Append `@<tag-or-commit>` to pin when a result has to be
reproducible — and record the pin next to the snapshot date, since the two
together are what make a lookup repeatable.

Installed into an environment it is just `aop-wiki-cli <command>`; from a clone,
`uv run aop-wiki-cli <command>`. All three reach the same console script, so
every example below is written as the bare `aop-wiki-cli` form.

## The data directory is the thing to get right

The tool no longer carries its own location, so **you choose where its data
lives** — inputs, outputs, dated caches and logs all resolve under one data
directory, decided at call time in this order:

1. `--data-dir <path>` — a **global option, and it must come before the
   subcommand**: `aop-wiki-cli --data-dir ~/aop-data find-kers-for-events …`
2. `$AOP_WIKI_CLI_DATA_DIR`
3. the current working directory

It derives `outputs/`, `outputs/cache/`, `xml_inputs/`, `logs/`, `inputs/` and
`curated/` beneath whichever of those wins.

**Two consequences worth internalizing before the first run.**

The cwd fallback is silent and it is the dangerous one. Run a command from the
dismech checkout with no `--data-dir` and no environment variable, and the tool
will create `outputs/`, `xml_inputs/` and `logs/` **inside dismech** — none of
which belong in this repo. Always pin the data directory, and never pin it at a
dismech checkout or worktree.

A fresh data directory has no cache, so the first command run against one
downloads the ~50 MB XML export and parses it. Point at a directory that already
holds a snapshot unless refreshing is the actual goal.

Set it once for a working session rather than repeating the flag:

```bash
export AOP_WIKI_CLI_DATA_DIR=~/aop-wiki-data   # any directory you keep snapshots in
```

If you are working from a clone, note that `outputs/` there is gitignored and
`outputs_for_vc/` is the curated subset that repo version-controls. Nothing from
either belongs in a dismech commit.

## Pick the right command

| You want | Command |
|---|---|
| What a key event leads to, and what leads to it | `find-kers-for-events --ke-ids <ids>` |
| A screening run: many terms, co-occurrence, exclusions | `search-with-config <config>` |
| KE completion + integration rankings | `collect-event-integration-rankings` |
| KER counts, table coverage, completion | `collect-ker-analytics` |
| Normalized KER evidence tables → Excel | `harmonize-ker-evidence` |
| Concordance language in KER evidence | `search-kers-for-concordance-text` |

Those six plus the two interactive commands below are the whole surface. All of
them print a summary, and all but `collect-ker-analytics` also write into
`<data-dir>/outputs/`. **`collect-ker-analytics` writes nothing** — its printed statistics
block is the entire result, so capture it from the console rather than looking
for a file. It does still populate `<data-dir>/outputs/cache/<date>/all_kers_*.json`, which
is the cache every KER command shares, not a report.

**There is no single-entity lookup command** — no `find-entities`, no
`show-entity`, no `show-aop-graph`. To find records by term, use
`search-with-config`. To read one record, open the cache JSON in the data
directory (`<data-dir>/outputs/cache/<MM-DD-YYYY>/all_events_*.json`, keyed by
AOP-Wiki ID as a string) as a one-off — an ad-hoc read while working there, which
does not license dismech code to reach into those files.

Its matcher is word-boundary, case-insensitive, HTML-stripped, with
sentence-bounded snippets. Because word-boundary matching allows flexible
internal whitespace but not punctuation changes, `"organ on a chip"` will not
match `organ-on-a-chip` — search both spellings.

### Walking outward from a key event

`find-kers-for-events` is the command for "what happens next" — it returns every
KER with a given KE as an endpoint, and reports which side the KE sits on, so
what a KE leads to is separated from what leads to it.

```bash
aop-wiki-cli find-kers-for-events --ke-ids 1529,593,1562,2288,2290 --date 08-06-2026
aop-wiki-cli find-kers-for-events --ke-terms "oxidative stress,cell death" --date 08-06-2026
```

- `--ke-ids` and `--ke-terms` are **mutually exclusive and one is required**;
  passing both, or neither, exits 1. `--ke-terms` matches against KE titles only.
- Every match is written to
  `<data-dir>/outputs/ker_lookups/<MM-DD-YYYY>/ker_lookup_<MM-DD-YYYY>.json` as
  `{summary, matched_events, matched_kers}`. `--limit` (default 25) caps only
  what prints, so a truncated console list is not a truncated result set.
- The console line prints each KER as `upstream title -> downstream title`,
  **clipped at 70 characters**. Read the JSON when the downstream title matters,
  which for this command is most of the time.
- The first KER command for a date parses the full XML and is slow; later runs
  for that date read `all_kers_*.json` from the cache.

**A KE's partner KE in a KER can add specificity to the KER with respect to the
cellular or organ location, taxa, sex, or life stage.** KERs should be filtered
for curation based on their relevance to a particular disease or module entity
that is being curated. `KE1562` (Decreased Na/K ATPase activity) matches six
KERs — four leading out of it, two into it — and of the four, only KER3444 (to
increased intracellular sodium, AOP 556) belongs to a cardiac chain. The rest
run to cell membrane depolarization, renal proximal tubular transport, and
sodium uptake in fish gills. Note that the gill KER sits inside an AOP titled
"leads to Heart failure", so check the downstream event and not just the AOP
title.

### Date handling — the main footgun

Three date formats coexist:

| Thing | Format | Example |
|---|---|---|
| `--date` on every command | **MM-DD-YYYY** | `--date 08-06-2026` |
| cache dir `<data-dir>/outputs/cache/<date>/` | MM-DD-YYYY | `08-06-2026` |
| XML snapshot filename | ISO YYYY-MM-DD | `aop-wiki-xml-2026-08-06` |

`collect-event-integration-rankings --help` claims `YYYY-MM-DD`. **It is wrong**
— every command parses `%m-%d-%Y`, and an ISO string raises `ValueError`.

**Omitting `--date` means today**, which is a cache miss on any day you have not
already pulled a snapshot — and a miss downloads the ~50 MB XML export and
parses it. Always pass an existing snapshot date unless the point is to refresh.
Check what exists before running anything:

```bash
ls "${AOP_WIKI_CLI_DATA_DIR:-.}"/outputs/cache/
```

A date directory holds `all_events_*.json` and `all_aops_*.json` once any events
or AOPs command has run for it; `all_kers_*.json` appears only after a KER
command (`collect-ker-analytics`, `harmonize-ker-evidence`, or
`find-kers-for-events`). Anything KER-shaped is slow the first time for
that date because it parses the full XML.

`--force-refresh`/`-f` re-collects from XML. Two commands spell the same flag
`--force`: `collect-ker-analytics` and `find-kers-for-events`.

## Entity shapes

Collected entities are `{id: record}` dicts keyed by AOP-Wiki ID as a **string**.

**Events** (1,598 in the 08-06-2026 snapshot) — `ke_id`, `title`, `short_name`,
`description`, `measurement_method`, `doa_free_text`, `references`,
`level_of_biological_organization` (Cellular 540 / Molecular 449 / Tissue 221 /
Organ 195 / Individual 157 / Population 36), `is_ao`, `regulatory_relevance`,
`aop_ids`, `aop_count`, `cell_term`/`organ_term` (`{source, term}`), `ecs`
(event components: `biological_process` / `biological_object` /
`biological_action`, each `{source, source_id, term}`), `sex_terms`,
`life_stage_terms`, `taxonomy_terms`, `summary_oecd_statuses`,
`summary_licenses`, `completion_score`, plus the ranking fields
`integration_score`, `percent_i_score_sans_aop_count`,
`max_i_score_sans_aop_count`, and `has_method`.

**AOPs** (596 in that snapshot) — `id`, `title`, `short_name`, `abstract`, `event_ids`, `kers`
(`{ker_id: {type: adjacent|non-adjacent}}`), `stressors`, `oecd_status`,
`wiki_license`, `authors`, `background`, `overall_assessment_description`,
`ke_essentiality`, `woe_evidence`, `quantitative_considerations`,
`potential_applications`, `references`, `taxonomy_applicability`,
`num_events`/`num_kers`/`num_stressors`, `completion_score`.

**KERs** — `upstream_ke`/`downstream_ke` (each `{id, title}`), `aop_ids`,
`adjacency_types`, `description`, `modulating_factors`, `uncertainties`,
`response_relationship`, `time_scale`, `known_loops`,
`evidence_collection_strategy`, `references`, `has_any_tables`,
`completion_score`, plus four **evidence blocks** — `weight_of_evidence`,
`empirical_support`, `biological_plausibility`, `quantitative_understanding` —
each `{free_text, tables, headers}`.

Free-text fields hold raw AOP-Wiki HTML. The CLI strips it for its own output;
if you read a field straight out of a cache JSON file, strip it yourself.

`completion_score` is `{percent, raw_score, max_score, empty_free_text,
empty_structured}` — a **data-completeness** metric on the wiki record, not a
statement about the strength of the science.

## Writing a search config

**Running a shipped config works from an install; writing a new one does not.**
`search-with-config` resolves its argument with
`importlib.import_module('aop_wiki_cli.configs.<name>')`, so it only ever sees
modules **inside the installed package**. There is no search path into the data
directory and no `--config-file`. A config you write on your own machine is
therefore invisible to a `uvx`- or pip-installed copy. To add one, work from a
clone with the package installed editable, and open a PR to the CLI repo so the
config ships for everyone. Passing an unknown name prints the configs actually
shipped, which is the quickest way to see what is available.

`search-with-config` imports `aop_wiki_cli/configs/<name>.py` and requires **both**
`SEARCH_PARAMS` and `OUTPUT_CONFIG` at module level. Three search modes:

```python
# 1. Single entity, named fields
SEARCH_PARAMS = {
    "entity": ["events"],                       # events | kers | aops
    "fields_to_search": ["measurement_method"],
    "terms": ["organoid", "organ-on-a-chip"],
}

# 2. Multiple entities with per-entity fields, co-occurrence, exclusions
SEARCH_PARAMS = {
    "entities_and_fields": {
        "events": ["title"],
        "aops": ["title", "abstract", "overall_assessment_description"],
    },
    "priority_field": "title",                  # matches here sort first
    "terms": ["lung", "immune", "fibrosis"],
    "co_occurrence_pairs": [["fibrosis", "lung"]],
    "title_exclusion_terms": ["zebrafish", "Daphnia"],
}

# 3. Iterative: KE titles -> the AOPs containing them -> all their events
SEARCH_PARAMS = {
    "search_mode": "event_to_aop",
    "ke_title_terms": ["parkinson"],
    "aop_title_exclusion_terms": [...],
    "oecd_status_filter": [...],                # optional
}

OUTPUT_CONFIG = {"directory": "outputs/<name>", "filename": f"<name>_{today}.json"}
```

Acronym terms (`HCI`, `ALI`, `TG`, `NGS`) generate false positives — check
snippets before trusting counts. `--co-occurrence-only` drops entities that
matched only single terms.

Configs to copy: `lung_and_immune_aops` (mode 2, with a long organ/disease
exclusion list), `methods_nams` (mode 1, NAM assay methods),
`regulatory_relevance` (mode 1, regulatory bodies and guidelines).
`harmonize_ker_evidence` holds constants, not a search config.

**Two shipped configs are not usable by `search-with-config`.**
`event_first_collections.py` defines `DEPRESSION_CONFIG`/`PARKINSON_CONFIG`
dicts and `reference_search.py` defines neither required name, so neither
exposes `SEARCH_PARAMS`. `_available_search_configs()` appends a module only when
it has **both** `SEARCH_PARAMS` and `OUTPUT_CONFIG`, so neither ever appears in
the `Available configs:` listing — `configs/` is the only place you meet them,
which is why this warning is here.
`configs/Configs_README.md` documents a `collect-entities-for-events` command
for them; that command **does not exist** in `cli.py`. Use `search_mode:
event_to_aop`, or read those event ID lists directly.

## Interactive commands

`collect-harmonized-seizure-aops` and `manually-review-matches` **block on
stdin** — they prompt accept `y` / reject `n` / quit `q` per fuzzy match. Never
launch them unattended or from a subagent. Run them in a terminal the user is
sitting at, or not at all.

## Bringing AOP-Wiki content into dismech

Two limits are worth stating before anyone curates from this data.

**AOP-Wiki is not a citable reference in dismech's validation stack.** There is
no `AOP:` prefix in `references_cache/` and no fetcher for one, so an AOP or KE
page cannot be an evidence `reference:`. Cite the primary literature instead —
the `references` field on the AOP, KE, and KER records is where those citations
live, and each still needs `just fetch-reference PMID:...` and a verified exact
snippet like any other. See the `dismech-references` skill.

**AOP ontology terms are not dismech bindings.** KE `cell_term`/`organ_term` use
UBERON but also plain strings; `ecs` components come from MESH, GO, CHEBI, and
others via `{source, source_id, term}`. Treat every one as a lead to re-resolve
under the `dismech-terms` rules, not as a term to copy across.

And an AOP is a hypothesis about a causal chain, weighted by the wiki's own
`weight_of_evidence` and OECD endorsement status. `oecd_status: ""` — 450 of 596
AOPs in the 08-06-2026 snapshot — means no OECD review has happened, not that
the pathway was reviewed and rejected. Carry that uncertainty into whatever you
write.
