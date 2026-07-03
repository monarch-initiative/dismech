# Curation Projects

Curation projects are thematic, human-authored markdown files under `projects/`
(e.g. `projects/CANCER.md`). They track scope, priorities, and progress for a
body of related curation work. This page documents the **standardized YAML
frontmatter** that turns a project markdown file into a browsable HTML page with
auto-linked entities, and the auto-generated project index.

This is modeled on the project pages in
[`ai4curation/ai-gene-review`](https://github.com/ai4curation/ai-gene-review),
adapted to dismech's entity types (diseases, modules, groupings, drugs,
phenotypes) rather than genes.

## Frontmatter

A project file may begin with a YAML frontmatter block delimited by `---`:

```markdown
---
title: Cancer Curation Project
status: EVERGREEN
description: >-
  Curation of cancers with precise genetic etiology and well-characterized
  pathophysiological progression.
tags: [DISEASE_DOMAIN, ONCOLOGY, FLAGSHIP]
diseases:
  - Lynch_Syndrome
  - Non-Small_Cell_Lung_Cancer
modules:
  - dna_repair_synthetic_lethality
groupings:
  - Mucopolysaccharidoses
drugs:
  - id: CHEBI:45783
    label: imatinib
phenotypes:
  - id: HP:0002664
    label: Neoplasm
---

# Cancer Curation Project
...
```

All keys are optional; a file with no frontmatter still renders (its title is
taken from the first `# H1`).

### Scalar keys

| Key | Meaning |
|-----|---------|
| `title` | Display title (falls back to the first `# H1`, then the filename). |
| `status` | One of `PLANNED`, `IN_PROGRESS`, `ACTIVE`, `COMPLETE`, `EVERGREEN`, `ARCHIVED`. Rendered as a colored badge. |
| `description` | One-line summary shown on the project index card. |
| `tags` | Free-text labels shown as chips and aggregated on the index. |

### Entity keys

Each entity key is a list. List items may be either:

- a **bare string** (the entity *token* — see the slug convention below), or
- a **mapping** with `slug`/`name`/`id`, an optional `label`, and an optional
  `note`.

| Key | Resolves to | Notes |
|-----|-------------|-------|
| `diseases` | `pages/disorders/<slug>.html` | Token is a disorder slug (the `kb/disorders/*.yaml` stem / disease name). |
| `modules` | `pages/modules/<stem>.html` | Token is a `kb/modules/` file stem. |
| `groupings` | `pages/groupings/<slug>.html` | Token is a `Grouping.name` or `kb/groupings/` stem. |
| `drugs` | external ontology browser | Supply `id:` as a CHEBI/NCIT CURIE for a link. |
| `phenotypes` | external ontology browser | Supply `id:` as an HP CURIE for a link. |

## Slug convention and auto-linking

The convention is: **refer to diseases (and modules/groupings) by their slug in
the markdown body**, e.g. write `Lynch_Syndrome`, not "Lynch Syndrome".

When a project page is rendered, every entity token declared in the frontmatter
that resolves to a dismech page is automatically turned into a link wherever it
appears in the body — in prose, tables, or lists. Only declared tokens are
linked, so there are no spurious links.

Auto-linking deliberately leaves the following untouched:

- text inside fenced code blocks and inline `` `code` `` spans,
- existing markdown links,
- filename references such as `Lynch_Syndrome.yaml` or `Lynch_Syndrome.html`
  (a token immediately followed by `.` is not linked).

The frontmatter also drives the page sidebar, which lists each entity as a chip
linking to its page (local entities) or ontology browser (drugs/phenotypes with
a CURIE). Tokens that do not resolve render as a muted "unresolved" chip — a
quick signal that a slug is mistyped or the entry has not been curated yet.

## Rendering

```bash
# Render all projects/*.md plus the auto-generated index
just gen-project-pages

# Render a single project page
just gen-project-page projects/CANCER.md
```

Output goes to `pages/projects/` (derived — not committed, like other
`pages/**` HTML). The index at `pages/projects/index.html` lists every project
with its status, tags, and entity counts, and serves as the main project index.
`just gen-all` includes project pages.
