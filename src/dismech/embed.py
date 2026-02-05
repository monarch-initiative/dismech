"""
Embedding-based disorder similarity analysis using linkml-store.

Generates embeddings for disorder YAML files enabling:
- Similarity analysis in pathophysiology space
- Similarity analysis in phenotype space
- Correlation between the two spaces
- 2D visualization with UMAP

Requires OPENAI_API_KEY environment variable.
Install with: uv sync --group embeddings
"""

import json
from pathlib import Path

import yaml
from linkml_store import Client
from linkml_store.index.implementations.llm_indexer import LLMIndexer

# Template paths relative to this module
TEMPLATES_DIR = Path(__file__).parent / "templates"
PATHO_TEMPLATE = TEMPLATES_DIR / "embed_patho.j2"
PHENO_TEMPLATE = TEMPLATES_DIR / "embed_pheno.j2"
TREAT_TEMPLATE = TEMPLATES_DIR / "embed_treat.j2"
CELLS_TEMPLATE = TEMPLATES_DIR / "embed_cells.j2"
MECHANISM_TEMPLATE = TEMPLATES_DIR / "embed_mechanism.j2"

def compute_group_field(
    disorder: dict,
    group_by: str,
    groups: list[str],
    other_label: str = "Other",
) -> str:
    """
    Compute a grouping field value for a disorder based on specified groups.

    Args:
        disorder: The disorder dict
        group_by: Field name to group by (e.g., "parents", "category")
        groups: List of values to highlight (case-insensitive matching)
        other_label: Label for items not matching any group

    Returns:
        The matching group name or other_label
    """
    value = disorder.get(group_by)
    if value is None:
        return other_label

    # Normalize groups for case-insensitive matching
    groups_lower = {g.lower(): g for g in groups}

    # Handle list fields (like parents)
    if isinstance(value, list):
        for item in value:
            item_lower = item.lower() if isinstance(item, str) else str(item).lower()
            if item_lower in groups_lower:
                return groups_lower[item_lower]
        return other_label

    # Handle string fields (like category)
    value_lower = value.lower() if isinstance(value, str) else str(value).lower()
    if value_lower in groups_lower:
        return groups_lower[value_lower]

    return other_label


def _serialize_datetimes(obj):
    """Recursively convert datetime objects to ISO format strings."""
    from datetime import date, datetime

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    elif isinstance(obj, dict):
        return {k: _serialize_datetimes(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [_serialize_datetimes(item) for item in obj]
    return obj


def load_disorders(
    kb_dir: Path = Path("kb/disorders"),
    group_by: str | None = None,
    groups: list[str] | None = None,
) -> list[dict]:
    """
    Load all disorder YAML files.

    Args:
        kb_dir: Directory containing disorder YAML files
        group_by: Optional field name to create a grouping from
        groups: Optional list of values to highlight for grouping

    Returns:
        List of disorder dicts with optional _group field added
    """
    disorders = []
    for yaml_path in sorted(kb_dir.glob("*.yaml")):
        # Skip history files
        if yaml_path.name.endswith(".history.yaml"):
            continue
        with open(yaml_path) as f:
            disorder = yaml.safe_load(f)
            disorder = _serialize_datetimes(disorder)
            disorder["_source_file"] = yaml_path.name

            # Add computed group field if specified
            if group_by and groups:
                disorder["_group"] = compute_group_field(disorder, group_by, groups)

            disorders.append(disorder)
    return disorders


def extract_mechanisms(disorders: list[dict]) -> list[dict]:
    """
    Extract individual pathophysiology mechanisms from disorders.

    Each mechanism becomes its own entry with disease context.

    Returns:
        List of mechanism dicts with disease_name, mechanism, and _group fields
    """
    mechanisms = []
    for disorder in disorders:
        disease_name = disorder.get("name", "")
        if not disease_name:
            continue
        group = disorder.get("_group", "Other")
        for mechanism in disorder.get("pathophysiology", []):
            mechanisms.append({
                "disease_name": disease_name,
                "mechanism": mechanism,
                "_group": group,
                "_mechanism_name": mechanism.get("name", "Unknown"),
            })
    return mechanisms


class DisorderEmbedder:
    """Embedding analysis for disorder knowledge base using linkml-store."""

    def __init__(self, db_path: str = "cache/embeddings/disorders.duckdb"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.client = Client()
        # Handle format: duckdb:///path/to/file.db
        handle = f"duckdb:///{self.db_path}"
        self.db = self.client.attach_database(handle, alias="disorders")
        self._cache_dir = self.db_path.parent

    def _clear_cache(self, cache_name: str) -> None:
        """Delete embedding cache file if it exists."""
        cache_path = self._cache_dir / cache_name
        if cache_path.exists():
            cache_path.unlink()
            print(f"  Cleared cache: {cache_name}")

    def index_pathophysiology(self, disorders: list[dict], recreate: bool = False) -> None:
        """Index disorders by pathophysiology content."""
        if recreate:
            self._clear_cache("patho_cache.db")

        coll = self.db.create_collection("pathophysiology", recreate_if_exists=recreate)

        # Only insert if collection is empty or recreating
        if recreate or coll.find().num_rows == 0:
            coll.insert(disorders)

        cache_db = str(self._cache_dir / "patho_cache.db")
        indexer = LLMIndexer(
            name="patho_index",
            cached_embeddings_database=cache_db,
            text_template=PATHO_TEMPLATE.read_text(),
            text_template_syntax="jinja2",
        )
        coll.attach_indexer(indexer)
        # Index all objects in the collection
        rows = coll.find(limit=10000).rows
        coll.index_objects(rows, "patho_index")
        print(f"Indexed {len(rows)} disorders in pathophysiology space")

    def index_phenotypes(self, disorders: list[dict], recreate: bool = False) -> None:
        """Index disorders by phenotype content."""
        if recreate:
            self._clear_cache("pheno_cache.db")

        coll = self.db.create_collection("phenotypes", recreate_if_exists=recreate)

        if recreate or coll.find().num_rows == 0:
            coll.insert(disorders)

        cache_db = str(self._cache_dir / "pheno_cache.db")
        indexer = LLMIndexer(
            name="pheno_index",
            cached_embeddings_database=cache_db,
            text_template=PHENO_TEMPLATE.read_text(),
            text_template_syntax="jinja2",
        )
        coll.attach_indexer(indexer)
        rows = coll.find(limit=10000).rows
        coll.index_objects(rows, "pheno_index")
        print(f"Indexed {len(rows)} disorders in phenotype space")

    def index_treatments(self, disorders: list[dict], recreate: bool = False) -> None:
        """Index disorders by treatment content."""
        if recreate:
            self._clear_cache("treat_cache.db")

        coll = self.db.create_collection("treatments", recreate_if_exists=recreate)

        if recreate or coll.find().num_rows == 0:
            coll.insert(disorders)

        cache_db = str(self._cache_dir / "treat_cache.db")
        indexer = LLMIndexer(
            name="treat_index",
            cached_embeddings_database=cache_db,
            text_template=TREAT_TEMPLATE.read_text(),
            text_template_syntax="jinja2",
        )
        coll.attach_indexer(indexer)
        rows = coll.find(limit=10000).rows
        coll.index_objects(rows, "treat_index")
        print(f"Indexed {len(rows)} disorders in treatment space")

    def index_celltypes(self, disorders: list[dict], recreate: bool = False) -> None:
        """Index disorders by cell types and anatomy content."""
        if recreate:
            self._clear_cache("cells_cache.db")

        coll = self.db.create_collection("celltypes", recreate_if_exists=recreate)

        if recreate or coll.find().num_rows == 0:
            coll.insert(disorders)

        cache_db = str(self._cache_dir / "cells_cache.db")
        indexer = LLMIndexer(
            name="cells_index",
            cached_embeddings_database=cache_db,
            text_template=CELLS_TEMPLATE.read_text(),
            text_template_syntax="jinja2",
        )
        coll.attach_indexer(indexer)
        rows = coll.find(limit=10000).rows
        coll.index_objects(rows, "cells_index")
        print(f"Indexed {len(rows)} disorders in cell types/anatomy space")

    def index_mechanisms(self, mechanisms: list[dict], recreate: bool = False) -> None:
        """Index individual pathophysiology mechanisms.

        Unlike other index methods, this takes mechanism entries (not full disorders).
        Use extract_mechanisms() to prepare the input.
        """
        if recreate:
            self._clear_cache("mechanisms_cache.db")

        coll = self.db.create_collection("mechanisms", recreate_if_exists=recreate)

        if recreate or coll.find().num_rows == 0:
            coll.insert(mechanisms)

        cache_db = str(self._cache_dir / "mechanisms_cache.db")
        indexer = LLMIndexer(
            name="mechanisms_index",
            cached_embeddings_database=cache_db,
            text_template=MECHANISM_TEMPLATE.read_text(),
            text_template_syntax="jinja2",
        )
        coll.attach_indexer(indexer)
        rows = coll.find(limit=10000).rows
        coll.index_objects(rows, "mechanisms_index")
        print(f"Indexed {len(rows)} individual mechanisms")

    def index_all(self, disorders: list[dict], recreate: bool = False) -> None:
        """Index disorders in all embedding spaces."""
        self.index_pathophysiology(disorders, recreate=recreate)
        self.index_phenotypes(disorders, recreate=recreate)
        self.index_treatments(disorders, recreate=recreate)
        self.index_celltypes(disorders, recreate=recreate)

    def search(self, query: str, space: str = "pathophysiology", limit: int = 10) -> list[dict]:
        """Semantic search for similar disorders."""
        coll = self.db.get_collection(space)
        results = coll.search(query, limit=limit)
        # ranked_rows returns (score, object) tuples
        return [
            {
                "name": obj.get("name", "Unknown"),
                "score": score,
                "category": obj.get("category", ""),
                "source_file": obj.get("_source_file", ""),
            }
            for score, obj in results.ranked_rows
        ]

    def find_similar(self, disorder_name: str, space: str = "pathophysiology", limit: int = 10) -> list[dict]:
        """Find disorders similar to a specific disorder."""
        coll = self.db.get_collection(space)

        # Find the disorder by name
        matches = coll.find({"name": disorder_name}).rows
        if not matches:
            # Try partial match
            all_disorders = coll.find(limit=10000).rows
            for d in all_disorders:
                if disorder_name.lower() in d.get("name", "").lower():
                    matches = [d]
                    break

        if not matches:
            raise ValueError(f"Disorder not found: {disorder_name}")

        disorder = matches[0]

        # Search using the disorder's text representation
        results = coll.search(disorder.get("name", ""), limit=limit + 1)

        # Filter out the query disorder itself
        similar = []
        for score, obj in results.ranked_rows:
            if obj.get("name") != disorder.get("name"):
                similar.append({
                    "name": obj.get("name", "Unknown"),
                    "score": score,
                    "category": obj.get("category", ""),
                    "source_file": obj.get("_source_file", ""),
                })

        return similar[:limit]

    def get_embeddings(self, space: str = "pathophysiology") -> tuple[list[str], list[list[float]]]:
        """Get all embeddings from a space.

        Returns:
            Tuple of (names, embeddings) where names is list of disorder names
            and embeddings is list of embedding vectors.
        """
        import duckdb

        cache_files = {
            "pathophysiology": "patho_cache.db",
            "phenotypes": "pheno_cache.db",
            "treatments": "treat_cache.db",
            "celltypes": "cells_cache.db",
        }
        cache_file = cache_files.get(space, "patho_cache.db")
        cache_path = self._cache_dir / cache_file

        if not cache_path.exists():
            raise FileNotFoundError(f"Embeddings cache not found: {cache_path}")

        # Read from DuckDB cache (linkml-store format)
        conn = duckdb.connect(str(cache_path), read_only=True)
        rows = conn.execute("SELECT text, embedding FROM all_embeddings").fetchall()
        conn.close()

        names = []
        embeddings = []
        for text, embedding in rows:
            # Extract disease name from text (first line: "Disease: <name>")
            if text.startswith("Disease: "):
                name = text.split("\n")[0].replace("Disease: ", "").strip()
            else:
                name = text[:50]
            names.append(name)
            embeddings.append(list(embedding))

        return names, embeddings

    def export_app_data(self, output_path: Path, spaces: list[str] | None = None) -> None:
        """Export embedding data for the JavaScript explorer app.

        Exports pre-computed 2D coordinates (UMAP and t-SNE) plus metadata
        for interactive visualization.

        Args:
            output_path: Path to output JSON file
            spaces: List of spaces to export (default: both)
        """
        import numpy as np

        if spaces is None:
            spaces = ["pathophysiology", "phenotypes", "treatments", "celltypes"]

        result = {}

        for space in spaces:
            print(f"Processing {space} space...")

            # Get embeddings
            names, embeddings = self.get_embeddings(space)
            X = np.array(embeddings)

            print(f"  Loaded {len(names)} embeddings")

            # Compute UMAP
            print("  Computing UMAP...")
            from umap import UMAP
            umap_reducer = UMAP(n_components=2, random_state=42, metric="cosine", n_neighbors=15)
            umap_coords = umap_reducer.fit_transform(X)

            # Compute t-SNE
            print("  Computing t-SNE...")
            from sklearn.manifold import TSNE
            tsne_reducer = TSNE(n_components=2, random_state=42, metric="cosine",
                               perplexity=min(30, len(names) - 1))
            tsne_coords = tsne_reducer.fit_transform(X)

            # Get metadata from collection
            coll = self.db.get_collection(space)
            disorders = coll.find(limit=10000).rows
            name_to_disorder = {d.get("name", ""): d for d in disorders}

            # Build metadata list aligned with coordinates
            metadata = []
            for name in names:
                d = name_to_disorder.get(name, {})
                metadata.append({
                    "name": name,
                    "category": d.get("category") or "Unknown",
                    "parents": d.get("parents") or [],
                    "_group": d.get("_group") or "Other",
                    "_source_file": d.get("_source_file", ""),
                })

            result[space] = {
                "umap": umap_coords.tolist(),
                "tsne": tsne_coords.tolist(),
                "metadata": metadata,
            }

        # Write as JavaScript module (works with file:// and GitHub Pages)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w") as f:
            f.write("// Auto-generated embedding data - do not edit\n")
            f.write("// Generated with: just embed-app-data\n")
            f.write("window.EMBEDDING_DATA = ")
            json.dump(result, f)
            f.write(";\n")

        print(f"Exported app data to {output_path}")

    def export_mechanisms_data(self, output_path: Path) -> None:
        """Export mechanism-level embedding data for the mechanisms browser.

        Creates a JS file with individual mechanism embeddings for comparing
        pathophysiology across diseases.
        """
        import numpy as np

        print("Processing mechanisms space...")

        # Get embeddings from mechanisms cache
        cache_path = self._cache_dir / "mechanisms_cache.db"
        if not cache_path.exists():
            raise FileNotFoundError(
                f"Mechanisms cache not found: {cache_path}. "
                "Run 'just embed-index-mechanisms' first."
            )

        import duckdb
        conn = duckdb.connect(str(cache_path), read_only=True)
        rows = conn.execute("SELECT text, embedding FROM all_embeddings").fetchall()
        conn.close()

        # Parse mechanism info from embedded text
        embeddings = []
        text_to_idx = {}
        for i, (text, embedding) in enumerate(rows):
            embeddings.append(list(embedding))
            text_to_idx[text] = i

        X = np.array(embeddings)
        print(f"  Loaded {len(embeddings)} mechanism embeddings")

        # Compute UMAP
        print("  Computing UMAP...")
        from umap import UMAP
        n_neighbors = min(15, len(embeddings) - 1)
        umap_reducer = UMAP(n_components=2, random_state=42, metric="cosine", n_neighbors=n_neighbors)
        umap_coords = umap_reducer.fit_transform(X)

        # Compute t-SNE
        print("  Computing t-SNE...")
        from sklearn.manifold import TSNE
        perplexity = min(30, len(embeddings) - 1)
        tsne_reducer = TSNE(n_components=2, random_state=42, metric="cosine", perplexity=perplexity)
        tsne_coords = tsne_reducer.fit_transform(X)

        # Get metadata from collection (use large limit to get all rows)
        coll = self.db.get_collection("mechanisms")
        mechanism_rows = coll.find(limit=10000).rows

        # Build points list with metadata
        from jinja2 import Template
        template = Template(MECHANISM_TEMPLATE.read_text())

        points = []
        diseases = set()
        for mech in mechanism_rows:
            # Render the same text that was embedded to find the right coordinates
            text = template.render(**mech)
            idx = text_to_idx.get(text)
            if idx is None:
                continue

            disease_name = mech.get("disease_name", "Unknown")
            mechanism_name = mech.get("_mechanism_name", "Unknown")
            diseases.add(disease_name)

            points.append({
                "disease": disease_name,
                "mechanism": mechanism_name,
                "group": mech.get("_group", "Other"),
                "umap": umap_coords[idx].tolist(),
                "tsne": tsne_coords[idx].tolist(),
            })

        result = {
            "points": points,
            "diseases": sorted(diseases),
        }

        # Write as JavaScript module
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w") as f:
            f.write("// Auto-generated mechanism embedding data - do not edit\n")
            f.write("// Generated with: just embed-mechanisms-data\n")
            f.write("window.MECHANISM_DATA = ")
            json.dump(result, f)
            f.write(";\n")

        print(f"Exported {len(points)} mechanisms from {len(diseases)} diseases to {output_path}")

    def compute_similarity_matrix(self, space: str = "pathophysiology") -> dict:
        """Compute pairwise similarity matrix for all disorders."""
        coll = self.db.get_collection(space)
        disorders = coll.find(limit=10000).rows

        matrix = {}
        for disorder in disorders:
            name = disorder.get("name", "Unknown")
            results = coll.search(name, limit=len(disorders))
            matrix[name] = {
                obj.get("name", "Unknown"): score
                for score, obj in results.ranked_rows
            }

        return matrix

    def compare_spaces(self) -> dict:
        """Compare similarity rankings between pathophysiology and phenotype spaces."""
        patho_matrix = self.compute_similarity_matrix("pathophysiology")
        pheno_matrix = self.compute_similarity_matrix("phenotypes")

        # Calculate correlation between the two spaces
        disorders = list(patho_matrix.keys())
        correlations = []

        for d1 in disorders:
            if d1 not in pheno_matrix:
                continue
            for d2 in disorders:
                if d2 not in patho_matrix.get(d1, {}) or d2 not in pheno_matrix.get(d1, {}):
                    continue
                patho_sim = patho_matrix[d1].get(d2, 0)
                pheno_sim = pheno_matrix[d1].get(d2, 0)
                correlations.append((patho_sim, pheno_sim))

        # Compute Pearson correlation
        if len(correlations) < 2:
            return {"correlation": None, "n_pairs": len(correlations)}

        patho_vals = [c[0] for c in correlations]
        pheno_vals = [c[1] for c in correlations]

        mean_p = sum(patho_vals) / len(patho_vals)
        mean_h = sum(pheno_vals) / len(pheno_vals)

        numerator = sum((p - mean_p) * (h - mean_h) for p, h in correlations)
        denom_p = sum((p - mean_p) ** 2 for p in patho_vals) ** 0.5
        denom_h = sum((h - mean_h) ** 2 for h in pheno_vals) ** 0.5

        if denom_p == 0 or denom_h == 0:
            correlation = 0.0
        else:
            correlation = numerator / (denom_p * denom_h)

        return {
            "correlation": round(correlation, 4),
            "n_pairs": len(correlations),
            "n_disorders": len(disorders),
        }

    def export_similarities(self, output_path: Path, space: str = "pathophysiology") -> None:
        """Export similarity matrix to CSV."""
        matrix = self.compute_similarity_matrix(space)
        disorders = sorted(matrix.keys())

        with open(output_path, "w") as f:
            # Header
            f.write("disorder," + ",".join(disorders) + "\n")
            # Rows
            for d in disorders:
                scores = [str(round(matrix[d].get(d2, 0), 4)) for d2 in disorders]
                f.write(f"{d}," + ",".join(scores) + "\n")

        print(f"Exported {len(disorders)}x{len(disorders)} similarity matrix to {output_path}")

    def plot_interactive(
        self,
        space: str = "pathophysiology",
        output_path: Path | None = None,
        method: str = "umap",
        color_field: str = "_group",
        show: bool = True,
    ) -> Path:
        """Create interactive Plotly plot of disorders in 2D embedding space.

        Args:
            space: Embedding space to plot ("pathophysiology" or "phenotypes")
            output_path: Path to save the HTML file
            method: Dimensionality reduction method ("umap" or "tsne")
            color_field: Field to use for coloring points (default: "_group")
            show: Whether to open the plot in browser

        Returns:
            Path to the saved HTML file
        """
        import numpy as np
        import plotly.express as px

        # Get embeddings
        names, embeddings = self.get_embeddings(space)
        X = np.array(embeddings)

        print(f"Loaded {len(names)} embeddings with {X.shape[1]} dimensions")

        # Dimensionality reduction
        if method == "umap":
            from umap import UMAP
            reducer = UMAP(n_components=2, random_state=42, metric="cosine", n_neighbors=15)
        elif method == "tsne":
            from sklearn.manifold import TSNE
            reducer = TSNE(n_components=2, random_state=42, metric="cosine", perplexity=min(30, len(names) - 1))
        else:
            raise ValueError(f"Unknown method: {method}")

        print(f"Running {method.upper()}...")
        X_2d = reducer.fit_transform(X)

        # Get metadata for coloring and hover
        coll = self.db.get_collection(space)
        disorders = coll.find(limit=10000).rows
        name_to_disorder = {d.get("name", ""): d for d in disorders}

        # Build dataframe for plotly
        data = []
        for i, name in enumerate(names):
            disorder = name_to_disorder.get(name, {})
            data.append({
                "name": name,
                "x": X_2d[i, 0],
                "y": X_2d[i, 1],
                color_field: disorder.get(color_field) or "Other",
                "category": disorder.get("category") or "Unknown",
                "parents": ", ".join(disorder.get("parents", [])) if disorder.get("parents") else "",
            })

        # Create interactive plot with plotly.express
        fig = px.scatter(
            data,
            x="x",
            y="y",
            color=color_field,
            hover_data=["name", "category", "parents", color_field],
            title=f"Disorders in {space.title()} Space ({method.upper()}) - Colored by {color_field}",
            width=1400,
            height=1000,
        )

        # Update styling
        fig.update_traces(marker=dict(size=10, opacity=0.8, line=dict(width=0.5, color="white")))
        fig.update_layout(
            hovermode="closest",
            xaxis_title=f"{method.upper()} 1",
            yaxis_title=f"{method.upper()} 2",
            legend_title=color_field,
        )

        # Save
        if output_path is None:
            output_path = self._cache_dir / f"{space}_{method}_interactive.html"

        fig.write_html(str(output_path))
        print(f"Saved interactive plot to {output_path}")

        if show:
            import webbrowser
            webbrowser.open(f"file://{output_path.absolute()}")

        return output_path

    def plot_embeddings(
        self,
        space: str = "pathophysiology",
        output_path: Path | None = None,
        method: str = "umap",
        show: bool = True,
    ) -> Path:
        """Plot disorders in 2D embedding space using dimensionality reduction.

        Args:
            space: Embedding space to plot ("pathophysiology" or "phenotypes")
            output_path: Path to save the plot (PNG/PDF/SVG)
            method: Dimensionality reduction method ("umap" or "tsne")
            show: Whether to display the plot interactively

        Returns:
            Path to the saved plot file
        """
        import numpy as np

        # Get embeddings
        names, embeddings = self.get_embeddings(space)
        X = np.array(embeddings)

        print(f"Loaded {len(names)} embeddings with {X.shape[1]} dimensions")

        # Dimensionality reduction
        if method == "umap":
            from umap import UMAP
            reducer = UMAP(n_components=2, random_state=42, metric="cosine")
        elif method == "tsne":
            from sklearn.manifold import TSNE
            reducer = TSNE(n_components=2, random_state=42, metric="cosine", perplexity=min(30, len(names)-1))
        else:
            raise ValueError(f"Unknown method: {method}")

        print(f"Running {method.upper()}...")
        X_2d = reducer.fit_transform(X)

        # Get categories for coloring
        coll = self.db.get_collection(space)
        disorders = coll.find(limit=10000).rows
        name_to_category = {d.get("name", ""): (d.get("category") or "Unknown") for d in disorders}
        categories = [name_to_category.get(name) or "Unknown" for name in names]

        # Create plot
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots(figsize=(14, 10))

        # Color by category
        unique_cats = sorted(set(categories))
        colors = plt.cm.tab20(np.linspace(0, 1, len(unique_cats)))
        cat_to_color = dict(zip(unique_cats, colors))

        for cat in unique_cats:
            mask = [c == cat for c in categories]
            xs = X_2d[mask, 0]
            ys = X_2d[mask, 1]
            ax.scatter(xs, ys, c=[cat_to_color[cat]], label=cat, alpha=0.7, s=60)

        # Add labels
        for i, name in enumerate(names):
            # Shorten long names
            short_name = name[:25] + "..." if len(name) > 25 else name
            ax.annotate(
                short_name,
                (X_2d[i, 0], X_2d[i, 1]),
                fontsize=6,
                alpha=0.8,
                ha='left',
                va='bottom',
            )

        ax.set_title(f"Disorders in {space.title()} Embedding Space ({method.upper()})")
        ax.set_xlabel(f"{method.upper()} 1")
        ax.set_ylabel(f"{method.upper()} 2")
        ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=8)

        plt.tight_layout()

        # Save
        if output_path is None:
            output_path = self._cache_dir / f"{space}_{method}_plot.png"

        fig.savefig(output_path, dpi=150, bbox_inches='tight')
        print(f"Saved plot to {output_path}")

        if show:
            plt.show()

        plt.close(fig)
        return output_path


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Embedding-based disorder similarity analysis",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Index all disorders (requires OPENAI_API_KEY)
  python -m dismech.embed index

  # Search for similar disorders
  python -m dismech.embed search "inflammatory airway disease"

  # Find disorders similar to a specific one
  python -m dismech.embed similar "Asthma"

  # Compare pathophysiology vs phenotype spaces
  python -m dismech.embed compare

  # Export similarity matrix
  python -m dismech.embed export --output similarities.csv

  # Plot disorders in 2D embedding space
  python -m dismech.embed plot --space pathophysiology
        """,
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Index command
    index_parser = subparsers.add_parser("index", help="Generate embeddings for all disorders")
    index_parser.add_argument("--output", "-o", default="cache/embeddings", help="Output directory")
    index_parser.add_argument("--kb-dir", default="kb/disorders", help="Knowledge base directory")
    index_parser.add_argument("--recreate", action="store_true", help="Recreate collections from scratch")
    index_parser.add_argument("--group-by", help="Field to use for grouping (e.g., 'parents', 'category')")
    index_parser.add_argument("--groups", help="Comma-separated list of values to highlight (rest become 'Other')")

    # Search command
    search_parser = subparsers.add_parser("search", help="Semantic search for disorders")
    search_parser.add_argument("query", help="Search query")
    search_parser.add_argument("--space", "-s", default="pathophysiology",
                              choices=["pathophysiology", "phenotypes", "treatments", "celltypes"],
                              help="Embedding space to search")
    search_parser.add_argument("--limit", "-n", type=int, default=10, help="Max results")
    search_parser.add_argument("--db", default="cache/embeddings/disorders.duckdb", help="Database path")

    # Similar command
    similar_parser = subparsers.add_parser("similar", help="Find disorders similar to a specific one")
    similar_parser.add_argument("disorder", help="Disorder name")
    similar_parser.add_argument("--space", "-s", default="pathophysiology",
                               choices=["pathophysiology", "phenotypes", "treatments", "celltypes"],
                               help="Embedding space")
    similar_parser.add_argument("--limit", "-n", type=int, default=10, help="Max results")
    similar_parser.add_argument("--db", default="cache/embeddings/disorders.duckdb", help="Database path")

    # Compare command
    compare_parser = subparsers.add_parser("compare", help="Compare pathophysiology vs phenotype spaces")
    compare_parser.add_argument("--output", "-o", help="Output JSON file")
    compare_parser.add_argument("--db", default="cache/embeddings/disorders.duckdb", help="Database path")

    # Export command
    export_parser = subparsers.add_parser("export", help="Export similarity matrix")
    export_parser.add_argument("--output", "-o", default="cache/embeddings/similarities.csv",
                              help="Output CSV file")
    export_parser.add_argument("--space", "-s", default="pathophysiology",
                              choices=["pathophysiology", "phenotypes", "treatments", "celltypes"],
                              help="Embedding space")
    export_parser.add_argument("--db", default="cache/embeddings/disorders.duckdb", help="Database path")

    # Plot command (matplotlib - static)
    plot_parser = subparsers.add_parser("plot", help="Plot disorders in 2D embedding space (static)")
    plot_parser.add_argument("--space", "-s", default="pathophysiology",
                            choices=["pathophysiology", "phenotypes", "treatments", "celltypes"],
                            help="Embedding space to plot")
    plot_parser.add_argument("--method", "-m", default="umap",
                            choices=["umap", "tsne"],
                            help="Dimensionality reduction method")
    plot_parser.add_argument("--output", "-o", help="Output file path (PNG/PDF/SVG)")
    plot_parser.add_argument("--no-show", action="store_true", help="Don't display the plot interactively")
    plot_parser.add_argument("--db", default="cache/embeddings/disorders.duckdb", help="Database path")

    # Plotly command (interactive HTML)
    plotly_parser = subparsers.add_parser("plotly", help="Interactive Plotly plot in 2D embedding space")
    plotly_parser.add_argument("--space", "-s", default="pathophysiology",
                              choices=["pathophysiology", "phenotypes", "treatments", "celltypes"],
                              help="Embedding space to plot")
    plotly_parser.add_argument("--method", "-m", default="umap",
                              choices=["umap", "tsne"],
                              help="Dimensionality reduction method")
    plotly_parser.add_argument("--color-field", "-c", default="_group",
                              help="Field to use for coloring (default: _group)")
    plotly_parser.add_argument("--output", "-o", help="Output HTML file path")
    plotly_parser.add_argument("--no-show", action="store_true", help="Don't open in browser")
    plotly_parser.add_argument("--db", default="cache/embeddings/disorders.duckdb", help="Database path")

    # App data export command (for JS explorer)
    appdata_parser = subparsers.add_parser("app-data", help="Export data for JS embedding explorer")
    appdata_parser.add_argument("--output", "-o", default="app/embeddings/data.js",
                               help="Output JS file")
    appdata_parser.add_argument("--db", default="cache/embeddings/disorders.duckdb", help="Database path")

    # Index mechanisms command
    mech_index_parser = subparsers.add_parser("index-mechanisms",
                                               help="Index individual pathophysiology mechanisms")
    mech_index_parser.add_argument("--output", "-o", default="cache/embeddings", help="Output directory")
    mech_index_parser.add_argument("--kb-dir", default="kb/disorders", help="Knowledge base directory")
    mech_index_parser.add_argument("--recreate", action="store_true", help="Recreate from scratch")
    mech_index_parser.add_argument("--group-by", help="Field to use for grouping")
    mech_index_parser.add_argument("--groups", help="Comma-separated list of values to highlight")

    # Export mechanisms data command
    mech_data_parser = subparsers.add_parser("mechanisms-data",
                                              help="Export data for mechanisms browser")
    mech_data_parser.add_argument("--output", "-o", default="app/embeddings/mechanisms_data.js",
                                  help="Output JS file")
    mech_data_parser.add_argument("--db", default="cache/embeddings/disorders.duckdb", help="Database path")

    args = parser.parse_args()

    if args.command == "index":
        output_dir = Path(args.output)
        output_dir.mkdir(parents=True, exist_ok=True)
        db_path = output_dir / "disorders.duckdb"

        # Parse grouping options
        group_by = args.group_by
        groups = [g.strip() for g in args.groups.split(",")] if args.groups else None

        disorders = load_disorders(Path(args.kb_dir), group_by=group_by, groups=groups)
        print(f"Loaded {len(disorders)} disorders from {args.kb_dir}")

        if group_by and groups:
            from collections import Counter
            group_counts = Counter(d.get("_group", "Other") for d in disorders)
            print(f"Grouping by '{group_by}' with {len(groups)} highlighted groups:")
            for g, c in sorted(group_counts.items(), key=lambda x: -x[1]):
                print(f"  {g}: {c}")

        embedder = DisorderEmbedder(str(db_path))
        embedder.index_all(disorders, recreate=args.recreate)
        print(f"Embeddings stored in {output_dir}")

    elif args.command == "search":
        embedder = DisorderEmbedder(args.db)
        results = embedder.search(args.query, space=args.space, limit=args.limit)

        print(f"\nSearch results for '{args.query}' in {args.space} space:\n")
        for i, r in enumerate(results, 1):
            print(f"  {i}. {r['name']} (score: {r['score']:.3f})")
            if r['category']:
                print(f"     Category: {r['category']}")

    elif args.command == "similar":
        embedder = DisorderEmbedder(args.db)
        results = embedder.find_similar(args.disorder, space=args.space, limit=args.limit)

        print(f"\nDisorders similar to '{args.disorder}' in {args.space} space:\n")
        for i, r in enumerate(results, 1):
            print(f"  {i}. {r['name']} (score: {r['score']:.3f})")
            if r['category']:
                print(f"     Category: {r['category']}")

    elif args.command == "compare":
        embedder = DisorderEmbedder(args.db)
        result = embedder.compare_spaces()

        print(f"\nSpace Comparison Results:")
        print(f"  Correlation: {result['correlation']}")
        print(f"  Disorder pairs: {result['n_pairs']}")
        print(f"  Total disorders: {result['n_disorders']}")

        if args.output:
            with open(args.output, "w") as f:
                json.dump(result, f, indent=2)
            print(f"\nSaved to {args.output}")

    elif args.command == "export":
        embedder = DisorderEmbedder(args.db)
        embedder.export_similarities(Path(args.output), space=args.space)

    elif args.command == "plot":
        embedder = DisorderEmbedder(args.db)
        output_path = Path(args.output) if args.output else None
        embedder.plot_embeddings(
            space=args.space,
            output_path=output_path,
            method=args.method,
            show=not args.no_show,
        )

    elif args.command == "plotly":
        embedder = DisorderEmbedder(args.db)
        output_path = Path(args.output) if args.output else None
        embedder.plot_interactive(
            space=args.space,
            output_path=output_path,
            method=args.method,
            color_field=args.color_field,
            show=not args.no_show,
        )

    elif args.command == "app-data":
        embedder = DisorderEmbedder(args.db)
        embedder.export_app_data(Path(args.output))

    elif args.command == "index-mechanisms":
        output_dir = Path(args.output)
        output_dir.mkdir(parents=True, exist_ok=True)
        db_path = output_dir / "disorders.duckdb"

        # Parse grouping options
        group_by = args.group_by
        groups = [g.strip() for g in args.groups.split(",")] if args.groups else None

        disorders = load_disorders(Path(args.kb_dir), group_by=group_by, groups=groups)
        mechanisms = extract_mechanisms(disorders)
        print(f"Extracted {len(mechanisms)} mechanisms from {len(disorders)} disorders")

        embedder = DisorderEmbedder(str(db_path))
        embedder.index_mechanisms(mechanisms, recreate=args.recreate)

    elif args.command == "mechanisms-data":
        embedder = DisorderEmbedder(args.db)
        embedder.export_mechanisms_data(Path(args.output))


if __name__ == "__main__":
    main()
