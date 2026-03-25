# Disorder Embeddings System

The dismech knowledge base includes a semantic embedding system for analyzing disorder similarity across multiple dimensions. This enables:

- Finding disorders with similar pathophysiology, phenotypes, treatments, or cell types
- Visualizing disease relationships in 2D space
- Semantic search ("find disorders involving inflammation")

## Architecture Overview

### Embedding Spaces

Disorders are embedded in four separate semantic spaces, each capturing a different aspect:

| Space | Template | Content Embedded |
|-------|----------|------------------|
| `pathophysiology` | `embed_patho.j2` | Disease mechanisms, cell types, biological processes, downstream effects |
| `phenotypes` | `embed_pheno.j2` | Clinical symptoms, HPO terms, frequency, diagnostic markers |
| `treatments` | `embed_treat.j2` | Therapies, MAXO terms, mechanisms, effectiveness |
| `celltypes` | `embed_cells.j2` | Cell types (CL), tissues (UBERON), histopathology |

### Data Flow

```
kb/disorders/*.yaml
        │
        ▼
┌─────────────────────────────┐
│   load_disorders()          │  Load YAML, serialize datetimes,
│                             │  add _group field for visualization
└─────────────────────────────┘
        │
        ▼
┌─────────────────────────────┐
│   Jinja2 Templates          │  Extract relevant text for each space
│   (embed_*.j2)              │  e.g., "Disease: Asthma\nCell Types: Mast Cell..."
└─────────────────────────────┘
        │
        ▼
┌─────────────────────────────┐
│   OpenAI Embeddings API     │  Via linkml-store LLMIndexer
│   (text-embedding-ada-002)  │  1536-dimensional vectors
└─────────────────────────────┘
        │
        ▼
┌─────────────────────────────┐
│   DuckDB Cache              │  Embeddings cached by text hash
│   (cache/embeddings/*.db)   │  Avoids re-calling API for unchanged content
└─────────────────────────────┘
        │
        ▼
┌─────────────────────────────┐
│   Dimensionality Reduction  │  UMAP or t-SNE
│                             │  1536D → 2D coordinates
└─────────────────────────────┘
        │
        ▼
┌─────────────────────────────┐
│   app/embeddings/data.js    │  Pre-computed coordinates + metadata
│                             │  for interactive browser visualization
└─────────────────────────────┘
        │
        ▼
┌─────────────────────────────┐
│   app/embeddings/index.html │  Interactive Plotly scatter plot
│                             │  Hover, filter, color by group
└─────────────────────────────┘
```

### Key Files

| File | Purpose |
|------|---------|
| `src/dismech/embed.py` | Main module with `DisorderEmbedder` class and CLI |
| `src/dismech/templates/embed_*.j2` | Jinja2 templates for text extraction |
| `cache/embeddings/disorders.duckdb` | Main DuckDB with disorder collections |
| `cache/embeddings/*_cache.db` | Embedding cache per space |
| `app/embeddings/index.html` | Interactive browser UI |
| `app/embeddings/data.js` | Pre-computed visualization data |

## Commands Reference

### Indexing (requires OPENAI_API_KEY)

```bash
# Index all disorders with default settings
just embed-index

# Index with recreate (clears cache, re-embeds everything)
just embed-index recreate=1

# Index with parent-based grouping (recommended for visualization)
just embed-index-grouped

# Index with custom grouping
just embed-index-custom category "Cancer,Genetic,Infectious"
```

### Search and Similarity

```bash
# Semantic search across disorders
just embed-search "inflammatory airway disease"
just embed-search "autoimmune" phenotypes
just embed-search "steroids" treatments
just embed-search "epithelial" celltypes

# Find disorders similar to a specific one
just embed-similar "Asthma"
just embed-similar "Type 2 Diabetes" phenotypes
just embed-similar "Asthma" celltypes
```

### Visualization

```bash
# Generate browser data and open explorer
just embed-app-data
just embed-app

# Generate interactive Plotly HTML
just embed-plotly
just embed-plotly-pheno

# Full rebuild (reindex + generate app data)
just embed-all
```

### Export

```bash
# Export similarity matrices
just embed-export           # pathophysiology
just embed-export-pheno     # phenotypes

# Compare spaces (correlation analysis)
just embed-compare
```

## Jinja2 Templates

Each template extracts specific content from disorder YAML files. The template output becomes the text that gets embedded.

### Pathophysiology Template (`embed_patho.j2`)

```jinja
Disease: {{ name }}
Category: {{ category | default('Unknown') }}

Pathophysiology:
{% for p in pathophysiology %}
- {{ p.name }}: {{ p.description }}
  Cell types: {{ p.cell_types | map(attribute='preferred_term') | join(', ') }}
  Biological processes: {{ p.biological_processes | map(attribute='preferred_term') | join(', ') }}
{% endfor %}
```

### Cell Types Template (`embed_cells.j2`)

```jinja
Disease: {{ name }}
Category: {{ category | default('Unknown') }}

Cell Types and Anatomy:
{% for p in pathophysiology %}
{% if p.cell_types %}
{{ p.name }}:
{% for ct in p.cell_types %}
  - {{ ct.preferred_term }} ({{ ct.term.id }})
{% endfor %}
{% endif %}
{% endfor %}
```

## Grouping for Visualization

The `_group` field controls point coloring in the visualization. Set during indexing:

```bash
# Group by parent disease categories
just embed-index-grouped

# This runs:
# --group-by parents
# --groups "Autoimmune Disease,Cardiovascular Disease,..."
```

Disorders matching a group get that label; others become "Other".

## Troubleshooting

### Empty names in visualization

**Symptom**: Clusters of unnamed points in the explorer.

**Cause**: History files (`*.history.yaml`) or other non-disorder YAML files were indexed.

**Fix**: The `load_disorders()` function now skips `.history.yaml` files. Reindex:

```bash
just embed-index-grouped
just embed-app-data
```

### Stale cache data

**Symptom**: Old embeddings appear after modifying disorder files.

**Cause**: The embedding cache persists across runs to avoid re-calling the API.

**Fix**: Use `recreate=1` to clear caches:

```bash
just embed-index recreate=1
```

### All groups show as "Other"

**Symptom**: No color differentiation in visualization.

**Cause**: Indexed without grouping options.

**Fix**: Use `embed-index-grouped` instead of plain `embed-index`:

```bash
just embed-index-grouped
just embed-app-data
```

### Missing OPENAI_API_KEY

**Symptom**: `Error: OPENAI_API_KEY environment variable not set`

**Fix**: Set the API key:

```bash
export OPENAI_API_KEY=sk-...
just embed-index-grouped
```

### Datetime serialization error

**Symptom**: `TypeError: Object of type datetime is not JSON serializable`

**Cause**: Some disorder files have datetime objects (e.g., in `edit_history`).

**Fix**: Already handled by `_serialize_datetimes()` in `load_disorders()`.

## Adding a New Embedding Space

1. Create a new Jinja2 template in `src/dismech/templates/embed_<name>.j2`

2. Add template path constant in `embed.py`:
   ```python
   NEW_TEMPLATE = TEMPLATES_DIR / "embed_<name>.j2"
   ```

3. Add index method:
   ```python
   def index_<name>(self, disorders: list[dict], recreate: bool = False) -> None:
       if recreate:
           self._clear_cache("<name>_cache.db")
       coll = self.db.create_collection("<name>", recreate_if_exists=recreate)
       # ... (follow existing pattern)
   ```

4. Update `index_all()` to call the new method

5. Add cache mapping in `get_embeddings()`:
   ```python
   cache_files = {
       ...
       "<name>": "<name>_cache.db",
   }
   ```

6. Add to CLI choices and `export_app_data()` default spaces

7. Add dropdown option in `app/embeddings/index.html`

## Mechanism Comparison Browser

In addition to disease-level embeddings, there's a mechanism-level embedding system that embeds individual pathophysiology entries. This enables comparing the mechanistic overlap between diseases.

### Concept

- **Disease-level**: One embedding per disease (what the main explorer uses)
- **Mechanism-level**: One embedding per pathophysiology entry

For example, "Asthma" has mechanisms like "Airway Inflammation", "Bronchoconstriction", "Mucus Overproduction". Each gets its own embedding, allowing you to see where mechanisms from different diseases cluster together.

### Commands

```bash
# Index individual mechanisms
just embed-index-mechanisms

# Export browser data
just embed-mechanisms-data

# Or do both:
just embed-mechanisms-all
```

### Browser Usage

Open `app/embeddings/mechanisms.html`:

1. Search and add diseases to compare (up to 10)
2. Each disease gets a unique color
3. View mechanism clusters - overlapping regions suggest shared pathophysiology
4. Toggle "Show unselected as gray" for context
5. Hover over points to see mechanism names

### Data Structure

The mechanism embedding uses `embed_mechanism.j2` template:

```
Disease: {{ disease_name }}
Mechanism: {{ mechanism.name }}
Description: {{ mechanism.description }}
Cell types: [list]
Biological processes: [list]
```

### Files

| File | Purpose |
|------|---------|
| `src/dismech/templates/embed_mechanism.j2` | Mechanism text template |
| `cache/embeddings/mechanisms_cache.db` | Embedding cache |
| `app/embeddings/mechanisms.html` | Interactive comparison browser |
| `app/embeddings/mechanisms_data.js` | Pre-computed coordinates |

## Dependencies

Install embedding dependencies:

```bash
uv sync --group embeddings
```

Required packages:
- `linkml-store[llm]` - Embedding generation and storage
- `umap-learn` - UMAP dimensionality reduction
- `scikit-learn` - t-SNE implementation
- `plotly` - Interactive visualization
- `numpy` - Numerical operations
