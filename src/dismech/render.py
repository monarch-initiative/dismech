"""
Render disorder YAML files to HTML pages using Jinja2 templates.
"""

import hashlib
import json
import os
import re
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
from typing import Callable, Optional

import markdown as markdown_lib
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

from dismech.export.browser_export import HPO_TOP_LEVEL_CATEGORIES
from dismech.graph import build_causal_graph, generate_mermaid, graph_to_json

_HPO_CATEGORY_CACHE_PATH = Path("app/hpo_category_cache.json")
_FDA_SURROGATE_ENDPOINTS_RELATIVE_PATH = Path(
    "surrogate_endpoints/fda_surrogate_endpoints.yaml"
)
_LITERATURE_START_PATTERNS = (
    re.compile(r"(?m)^# .+\bReport\s*$"),
    re.compile(r"(?m)^Disease (?:Pathophysiology|Characteristics) Research Report\s*$"),
    re.compile(r"(?m)^## Executive Summary\s*$"),
    re.compile(r"(?m)^## Key Findings\s*$"),
    re.compile(r"(?m)^## Pathophysiology [Dd]escription\b.*$"),
    re.compile(r"(?m)^Pathophysiology [Dd]escription\b.*$"),
    re.compile(r"(?m)^## \d+\. Core Pathophysiology\b.*$"),
    re.compile(r"(?m)^## \d+\. Disease Information\b.*$"),
    re.compile(r"(?m)^## Disease Information\b.*$"),
    re.compile(r"(?m)^### Disorder\s*$"),
)
_RELATIVE_URL_ATTR_PATTERN = re.compile(
    r'(?P<attr>\b(?:src|href))=(?P<quote>["\'])(?P<url>[^"\']+)(?P=quote)',
    re.IGNORECASE,
)

# Canonical display order for phenotype categories (matches HPO_TOP_LEVEL_CATEGORIES)
_CATEGORY_ORDER = list(HPO_TOP_LEVEL_CATEGORIES.values())


@lru_cache(maxsize=1)
def _load_hpo_category_cache() -> dict[str, list[str]]:
    """Load the HP-term-to-category cache written by browser_export."""
    if _HPO_CATEGORY_CACHE_PATH.exists():
        return json.loads(_HPO_CATEGORY_CACHE_PATH.read_text())
    return {}


def _group_phenotypes_by_category(
    phenotypes: list[dict],
) -> list[tuple[str, list[dict]]]:
    """Group phenotypes by their HPO broad category, returning (category, phenotypes) pairs.

    Phenotypes without an HP term go into an "Other" group at the end.
    """
    cache = _load_hpo_category_cache()
    groups: dict[str, list[dict]] = defaultdict(list)
    seen: set[int] = set()

    for i, pheno in enumerate(phenotypes):
        hp_id = None
        pt = pheno.get("phenotype_term")
        if pt:
            term = pt.get("term")
            if term:
                hp_id = term.get("id")

        if hp_id and hp_id in cache:
            categories = cache[hp_id]
            if categories:
                # Assign to the first (most specific) category
                groups[categories[0]].append(pheno)
                seen.add(i)

    # Anything not resolved goes to "Other"
    for i, pheno in enumerate(phenotypes):
        if i not in seen:
            groups["Other"].append(pheno)

    # Sort by canonical order
    result = []
    for cat in _CATEGORY_ORDER:
        if cat in groups:
            result.append((cat, groups[cat]))
    if "Other" in groups:
        result.append(("Other", groups["Other"]))
    return result


STRICT_HIERARCHIES = {
    "ICD10CM": {
        "adapter": "sqlite:obo:icd10cm",
        "root": "ICD10CM:ICD-10-CM",
        "label": "ICD-10-CM",
    },
    "NCIT": {
        "adapter": "sqlite:obo:ncit",
        "root": "NCIT:C7057",
        "label": "NCIT",
    },
}


@lru_cache(maxsize=1)
def _load_prefix_map() -> dict:
    schema_path = Path(__file__).parent / "schema" / "dismech.yaml"
    try:
        prefixes = yaml.safe_load(schema_path.read_text()).get("prefixes", {})
    except FileNotFoundError:
        return {}
    return {
        prefix: base
        for prefix, base in prefixes.items()
        if isinstance(prefix, str) and isinstance(base, str)
    }


def curie_to_url(curie: str) -> str:
    """Convert a CURIE to a resolvable URL."""
    if not curie:
        return "#"

    if curie.startswith(("http://", "https://")):
        return curie

    if ":" not in curie:
        return "#"

    prefix, local_id = curie.split(":", 1)
    prefix_map = _load_prefix_map()
    base = prefix_map.get(prefix)
    if base:
        if "{id}" in base:
            return base.format(id=local_id)
        return f"{base}{local_id}"

    return f"https://bioregistry.io/{curie}"


def slugify(name: str) -> str:
    """Convert a disorder name to a filename-safe slug."""
    return name.replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "")


def _normalize_disorder_lookup(value: str | None) -> str:
    """Normalize disease names/slugs for tolerant internal-link lookup."""
    if not value:
        return ""
    normalized = re.sub(r"[^a-z0-9]+", " ", str(value).casefold())
    return " ".join(normalized.split())


def _extract_disorder_term_id(disorder: dict) -> str | None:
    """Extract MONDO/ontology term id from a disorder model if present."""
    disease_term = disorder.get("disease_term")
    if not isinstance(disease_term, dict):
        return None
    term = disease_term.get("term")
    if not isinstance(term, dict):
        return None
    term_id = term.get("id")
    if not term_id:
        return None
    return str(term_id)


def _resolve_local_disorder_href(
    curie: str | None,
    by_term: dict[str, str],
    *,
    local_prefix: str = "",
    excluded_term_ids: set[str] | None = None,
) -> str | None:
    """Resolve MONDO CURIEs to local disorder-page hrefs when available."""
    if not isinstance(curie, str) or not curie:
        return None
    term_id = curie.upper()
    if not term_id.startswith("MONDO:"):
        return None
    if excluded_term_ids and term_id in excluded_term_ids:
        return None
    page_filename = by_term.get(term_id)
    if not page_filename:
        return None
    return f"{local_prefix}{page_filename}"


def _build_dismech_page_url_filter(
    disorders_dir: Path,
    *,
    local_prefix: str = "",
    excluded_term_ids: set[str] | None = None,
) -> Callable[[str], str | None]:
    """Build a filter that resolves MONDO CURIEs to local DisMech page hrefs."""
    by_term, _ = _build_disorder_page_index(str(disorders_dir.resolve()))
    excluded = {
        term_id.upper()
        for term_id in (excluded_term_ids or set())
        if isinstance(term_id, str) and term_id
    }

    def _curie_to_dismech_url(curie: str) -> str | None:
        return _resolve_local_disorder_href(
            curie,
            by_term,
            local_prefix=local_prefix,
            excluded_term_ids=excluded,
        )

    return _curie_to_dismech_url


def _build_has_local_disorder_filter(
    disorders_dir: Path,
) -> Callable[[str], bool]:
    """Build a filter that reports whether a MONDO CURIE resolves to a local page."""
    by_term, _ = _build_disorder_page_index(str(disorders_dir.resolve()))

    def _has_local_disorder_page(curie: str) -> bool:
        return _resolve_local_disorder_href(curie, by_term) is not None

    return _has_local_disorder_page


def _resolve_local_disorder_slug_href(
    slug: str | None,
    by_name: dict[str, str],
    *,
    local_prefix: str = "",
) -> str | None:
    """Resolve a disorder slug/name token to a local disorder-page href."""
    if not isinstance(slug, str) or not slug:
        return None
    page_filename = by_name.get(_normalize_disorder_lookup(slug))
    if not page_filename:
        return None
    return f"{local_prefix}{page_filename}"


def _build_dismech_slug_page_url_filter(
    disorders_dir: Path,
    *,
    local_prefix: str = "",
) -> Callable[[str], str | None]:
    """Build a filter that resolves disorder slug/name tokens to local page hrefs."""
    _, by_name = _build_disorder_page_index(str(disorders_dir.resolve()))

    def _slug_to_dismech_url(slug: str) -> str | None:
        return _resolve_local_disorder_slug_href(
            slug,
            by_name,
            local_prefix=local_prefix,
        )

    return _slug_to_dismech_url


def _build_has_local_disorder_slug_filter(
    disorders_dir: Path,
) -> Callable[[str], bool]:
    """Build a filter that reports whether a disorder slug/name token resolves locally."""
    _, by_name = _build_disorder_page_index(str(disorders_dir.resolve()))

    def _has_local_disorder_slug_page(slug: str) -> bool:
        return _resolve_local_disorder_slug_href(slug, by_name) is not None

    return _has_local_disorder_slug_page


def _make_anchor_id(prefix: str, value: str) -> str:
    """Build a stable HTML anchor ID for an in-page object."""
    slug = re.sub(r"[^a-z0-9]+", "-", str(value).casefold()).strip("-")
    return f"{prefix}-{slug or 'item'}"


@lru_cache(maxsize=8)
def _build_disorder_page_index(
    disorders_dir: str,
) -> tuple[dict[str, str], dict[str, str]]:
    """Build indexes for resolving disorder pages by term ID or name."""
    root = Path(disorders_dir)
    by_term_candidates: dict[str, set[str]] = defaultdict(set)
    by_name_candidates: dict[str, set[str]] = defaultdict(set)

    for disorder_path in sorted(root.glob("*.yaml")):
        if disorder_path.name.endswith(".history.yaml"):
            continue
        try:
            disorder = load_disorder(disorder_path) or {}
        except Exception:
            continue
        disorder_name = disorder.get("name") or disorder_path.stem
        page_filename = f"{slugify(str(disorder_name))}.html"

        term_id = _extract_disorder_term_id(disorder)
        if term_id:
            by_term_candidates[term_id.upper()].add(page_filename)

        for candidate in (disorder_name, disorder_path.stem):
            lookup_key = _normalize_disorder_lookup(
                str(candidate) if candidate else None
            )
            if lookup_key:
                by_name_candidates[lookup_key].add(page_filename)

    by_term = {
        term_id: next(iter(page_names))
        for term_id, page_names in by_term_candidates.items()
        if len(page_names) == 1
    }
    by_name = {
        lookup_key: next(iter(page_names))
        for lookup_key, page_names in by_name_candidates.items()
        if len(page_names) == 1
    }
    return by_term, by_name


def _annotate_internal_differential_links(
    disorder: dict,
    current_page_filename: str,
    disorders_dir: Path,
) -> None:
    """Attach local DisMech page hrefs to differential entries when resolvable."""
    differential_items = disorder.get("differential_diagnoses") or []
    if isinstance(differential_items, dict):
        entries = differential_items.values()
    elif isinstance(differential_items, list):
        entries = differential_items
    else:
        return

    by_term, by_name = _build_disorder_page_index(str(disorders_dir.resolve()))
    default_current_page = f"{slugify(str(disorder.get('name') or ''))}.html"
    for diff in entries:
        if not isinstance(diff, dict):
            continue
        diff.pop("dismech_page_href", None)

        href = None
        disease_term = diff.get("disease_term")
        if isinstance(disease_term, dict):
            term = disease_term.get("term")
            if isinstance(term, dict):
                term_id = term.get("id")
                if term_id:
                    href = by_term.get(str(term_id).upper())

        if not href:
            href = by_name.get(_normalize_disorder_lookup(diff.get("name")))

        if href and href not in {current_page_filename, default_current_page}:
            diff["dismech_page_href"] = href


def _annotate_model_links(disorder: dict) -> None:
    """Attach in-page anchors and bidirectional model-to-pathophysiology links."""
    pathophysiology_items = disorder.get("pathophysiology") or []
    if not isinstance(pathophysiology_items, list):
        return

    patho_by_name: dict[str, dict] = {}
    for item in pathophysiology_items:
        if not isinstance(item, dict):
            continue
        name = item.get("name")
        if not name:
            continue
        item["_anchor_id"] = _make_anchor_id("pathophysiology", name)
        item["_experimental_model_links"] = []
        item["_computational_model_links"] = []
        patho_by_name[str(name)] = item

    experimental_models = disorder.get("experimental_models") or []
    if isinstance(experimental_models, list):
        for model in experimental_models:
            if not isinstance(model, dict):
                continue
            model_name = model.get("name")
            if not model_name:
                continue

            model["_anchor_id"] = _make_anchor_id("experimental-model", model_name)
            resolved_links: list[dict] = []

            for link in model.get("modeled_mechanisms") or []:
                if not isinstance(link, dict):
                    continue
                target = link.get("target")
                if not target:
                    continue

                resolved_link = dict(link)
                target_item = patho_by_name.get(str(target))
                if target_item is None:
                    continue

                resolved_link["_target_anchor"] = target_item["_anchor_id"]
                resolved_links.append(resolved_link)
                target_item["_experimental_model_links"].append(
                    {
                        "model_name": model_name,
                        "model_anchor": model["_anchor_id"],
                        "description": link.get("description"),
                        "experimental_model_type": model.get("experimental_model_type"),
                        "namo_type": model.get("namo_type"),
                    }
                )

            model["_modeled_mechanisms_resolved"] = resolved_links

    computational_models = disorder.get("computational_models") or []
    if isinstance(computational_models, list):
        for model in computational_models:
            if not isinstance(model, dict):
                continue
            model_name = model.get("name")
            if not model_name:
                continue

            model["_anchor_id"] = _make_anchor_id("computational-model", model_name)
            resolved_links: list[dict] = []

            for link in model.get("modeled_mechanisms") or []:
                if not isinstance(link, dict):
                    continue
                target = link.get("target")
                if not target:
                    continue

                resolved_link = dict(link)
                target_item = patho_by_name.get(str(target))
                if target_item is None:
                    continue

                resolved_link["_target_anchor"] = target_item["_anchor_id"]
                resolved_links.append(resolved_link)
                target_item["_computational_model_links"].append(
                    {
                        "model_name": model_name,
                        "model_anchor": model["_anchor_id"],
                        "description": link.get("description"),
                        "model_type": model.get("model_type"),
                        "model_software": model.get("model_software"),
                        "model_format": model.get("model_format"),
                    }
                )

            model["_modeled_mechanisms_resolved"] = resolved_links


def _resolve_fda_surrogate_endpoints_path(yaml_path: Path) -> Path:
    """Resolve the FDA surrogate endpoint source table relative to a disease file."""
    nearby_kb_path = yaml_path.parent.parent / _FDA_SURROGATE_ENDPOINTS_RELATIVE_PATH
    if nearby_kb_path.exists():
        return nearby_kb_path
    return Path("kb") / _FDA_SURROGATE_ENDPOINTS_RELATIVE_PATH


@lru_cache(maxsize=8)
def _load_fda_surrogate_endpoint_index(source_path: str) -> dict[str, dict]:
    """Load source-level FDA surrogate endpoint rows by stable row_id."""
    path = Path(source_path)
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text()) or {}
    rows = data.get("surrogate_endpoints") or []
    return {
        str(row["row_id"]): row
        for row in rows
        if isinstance(row, dict) and row.get("row_id")
    }


def _summarize_regulatory_endpoint(row: dict) -> dict:
    """Return the row fields needed for compact disease-page display."""
    fields = (
        "row_id",
        "source_table",
        "disease_or_use",
        "patient_population",
        "surrogate_endpoint",
        "approval_type",
        "drug_mechanism_of_action",
        "age_range",
        "endpoint_validation_level",
        "clinical_benefit_linkage",
        "context_of_use",
        "source_url",
    )
    return {field: row[field] for field in fields if row.get(field) is not None}


def _annotate_regulatory_endpoint_refs(disorder: dict, yaml_path: Path) -> None:
    """Resolve biomarker readout FDA row refs for rendering without duplicating curation."""
    source_path = _resolve_fda_surrogate_endpoints_path(yaml_path)
    endpoint_index = _load_fda_surrogate_endpoint_index(str(source_path.resolve()))
    if not endpoint_index:
        return

    for biomarker in disorder.get("biochemical") or []:
        if not isinstance(biomarker, dict):
            continue
        for readout in biomarker.get("readouts") or []:
            if not isinstance(readout, dict):
                continue
            refs = readout.get("regulatory_endpoint_refs") or []
            if isinstance(refs, str):
                refs = [refs]
                readout["regulatory_endpoint_refs"] = refs
            if not isinstance(refs, list):
                continue

            resolved = []
            missing = []
            for ref in refs:
                row = endpoint_index.get(str(ref))
                if row is None:
                    missing.append(str(ref))
                else:
                    resolved.append(_summarize_regulatory_endpoint(row))
            if resolved:
                readout["_regulatory_endpoints"] = resolved
            if missing:
                readout["_missing_regulatory_endpoint_refs"] = missing


def load_disorder(yaml_path: Path) -> dict:
    """Load a disorder YAML file."""
    with open(yaml_path) as f:
        return yaml.safe_load(f)


def load_comorbidity(yaml_path: Path) -> dict:
    """Load a comorbidity YAML file."""
    with open(yaml_path) as f:
        return yaml.safe_load(f)


def _parse_module_reference(value: str | None) -> tuple[str, str] | None:
    """Split a conforms_to reference into (module_id, module_node_name)."""
    if not isinstance(value, str) or "#" not in value:
        return None
    module_id, module_node_name = value.split("#", 1)
    module_id = module_id.strip()
    module_node_name = module_node_name.strip()
    if not module_id or not module_node_name:
        return None
    return module_id, module_node_name


def _descriptor_display_label(descriptor: dict) -> str:
    """Build a display label for ontology-backed descriptors."""
    if not isinstance(descriptor, dict):
        return ""
    term = descriptor.get("term")
    if not isinstance(term, dict):
        term = {}
    return str(
        descriptor.get("preferred_term")
        or term.get("label")
        or term.get("id")
        or descriptor.get("name")
        or ""
    ).strip()


def _collect_unique_descriptors(
    pathophysiology_items: list[dict],
    slot_name: str,
) -> list[dict]:
    """Collect unique descriptors across a module's pathophysiology nodes."""
    unique_descriptors: list[dict] = []
    seen: set[tuple[str, str]] = set()

    for node in pathophysiology_items:
        if not isinstance(node, dict):
            continue
        for descriptor in node.get(slot_name) or []:
            if not isinstance(descriptor, dict):
                continue
            term = descriptor.get("term")
            if not isinstance(term, dict):
                term = {}

            label = _descriptor_display_label(descriptor)
            term_id = str(term.get("id") or "").strip()
            modifier = str(descriptor.get("modifier") or "").strip()
            laterality = str(descriptor.get("laterality") or "").strip()
            spatial_extent = str(descriptor.get("spatial_extent") or "").strip()
            temporality = str(descriptor.get("temporality") or "").strip()
            clinical_course = str(descriptor.get("clinical_course") or "").strip()
            severity = str(descriptor.get("severity") or "").strip()
            onset = descriptor.get("onset")
            onset_key = ""
            if isinstance(onset, dict):
                onset_key = json.dumps(onset, sort_keys=True)

            key = (
                term_id or label,
                modifier,
                laterality,
                spatial_extent,
                temporality,
                clinical_course,
                severity,
                onset_key,
            )
            if not key[0] or key in seen:
                continue

            seen.add(key)
            unique_descriptors.append(
                {
                    "label": label or term_id,
                    "id": term_id or None,
                    "modifier": modifier or None,
                    "laterality": laterality or None,
                    "spatial_extent": spatial_extent or None,
                    "temporality": temporality or None,
                    "clinical_course": clinical_course or None,
                    "severity": severity or None,
                    "onset": onset if isinstance(onset, dict) else None,
                }
            )

    return unique_descriptors


def _collect_module_usage(
    disorders_dir: Path = Path("kb/disorders"),
) -> dict[str, list[dict]]:
    """Index which disorder entries reference each shared module."""
    usage_by_module: dict[str, list[dict]] = defaultdict(list)

    for yaml_path in sorted(disorders_dir.glob("*.yaml")):
        if yaml_path.name.endswith(".history.yaml"):
            continue

        try:
            disorder = load_disorder(yaml_path) or {}
        except Exception:
            continue

        pathophysiology_items = disorder.get("pathophysiology") or []
        if not isinstance(pathophysiology_items, list):
            continue

        disorder_name = str(disorder.get("name") or yaml_path.stem)
        disorder_slug = slugify(disorder_name)
        matches_by_module: dict[str, list[dict]] = defaultdict(list)
        seen_matches: dict[str, set[tuple[str, str]]] = defaultdict(set)

        for patho in pathophysiology_items:
            if not isinstance(patho, dict):
                continue

            parsed_reference = _parse_module_reference(patho.get("conforms_to"))
            if parsed_reference is None:
                continue

            module_id, module_node_name = parsed_reference
            disorder_node_name = str(patho.get("name") or module_node_name)
            match_key = (module_node_name, disorder_node_name)
            if match_key in seen_matches[module_id]:
                continue

            seen_matches[module_id].add(match_key)
            matches_by_module[module_id].append(
                {
                    "module_node_name": module_node_name,
                    "disorder_node_name": disorder_node_name,
                }
            )

        for module_id, matches in matches_by_module.items():
            usage_by_module[module_id].append(
                {
                    "name": disorder_name,
                    "slug": disorder_slug,
                    "href": f"../disorders/{disorder_slug}.html",
                    "matches": matches,
                }
            )

    return {
        module_id: sorted(
            usages,
            key=lambda usage: (
                str(usage.get("name") or "").casefold(),
                str(usage.get("slug") or "").casefold(),
            ),
        )
        for module_id, usages in usage_by_module.items()
    }


def _annotate_module_usage(module: dict, disorder_usage: list[dict]) -> None:
    """Attach per-node disorder cross-references to a module payload."""
    pathophysiology_items = module.get("pathophysiology") or []
    if not isinstance(pathophysiology_items, list):
        return

    nodes_by_name: dict[str, dict] = {}
    for node in pathophysiology_items:
        if not isinstance(node, dict):
            continue
        node_name = str(node.get("name") or "").strip()
        if not node_name:
            continue
        node["_anchor_id"] = _make_anchor_id("module-pathophysiology", node_name)
        node["_disorder_links"] = []
        nodes_by_name[node_name] = node

    for usage in disorder_usage:
        for match in usage.get("matches") or []:
            if not isinstance(match, dict):
                continue
            node = nodes_by_name.get(str(match.get("module_node_name") or "").strip())
            if node is None:
                continue
            node["_disorder_links"].append(
                {
                    "name": usage.get("name"),
                    "href": usage.get("href"),
                    "disorder_node_name": match.get("disorder_node_name"),
                }
            )

    for node in nodes_by_name.values():
        node["_disorder_links"] = sorted(
            node["_disorder_links"],
            key=lambda item: (
                str(item.get("name") or "").casefold(),
                str(item.get("disorder_node_name") or "").casefold(),
            ),
        )


def _load_module_context(
    yaml_path: Path,
    *,
    disorders_dir: Path = Path("kb/disorders"),
    usage_index: dict[str, list[dict]] | None = None,
) -> tuple[dict, list[dict]]:
    """Load a module and decorate it with derived summary data."""
    module = load_disorder(yaml_path) or {}
    pathophysiology_items = module.get("pathophysiology") or []
    if not isinstance(pathophysiology_items, list):
        pathophysiology_items = []

    module_id = yaml_path.stem
    disorder_usage = (usage_index or _collect_module_usage(disorders_dir)).get(
        module_id, []
    )

    _annotate_module_usage(module, disorder_usage)
    module["_module_id"] = module_id
    module["_pathophysiology_count"] = len(
        [node for node in pathophysiology_items if isinstance(node, dict)]
    )
    module["_cell_types"] = _collect_unique_descriptors(
        pathophysiology_items,
        "cell_types",
    )
    module["_biological_processes"] = _collect_unique_descriptors(
        pathophysiology_items,
        "biological_processes",
    )
    module["_used_by_disorders"] = disorder_usage

    return module, disorder_usage


def _build_module_summary(module: dict) -> dict:
    """Build a compact card payload for the module index page."""
    module_id = str(module.get("_module_id") or "")
    used_by_disorders = module.get("_used_by_disorders") or []
    return {
        "id": module_id,
        "name": module.get("name") or module_id,
        "description": module.get("description"),
        "href": f"{module_id}.html",
        "pathophysiology_count": module.get("_pathophysiology_count") or 0,
        "cell_type_count": len(module.get("_cell_types") or []),
        "biological_process_count": len(module.get("_biological_processes") or []),
        "disorder_count": len(used_by_disorders),
        "used_by_disorders": used_by_disorders,
    }


def _format_condition_label(condition: dict) -> str:
    slug = condition.get("slug")
    if slug:
        return slug.replace("_", " ")
    composition = condition.get("composition")
    components = condition.get("components", []) or []
    component_slugs = [c.get("slug") for c in components if c.get("slug")]
    if composition and component_slugs:
        readable = ", ".join(s.replace("_", " ") for s in component_slugs)
        return f"{composition.title()} of {readable}"
    if component_slugs:
        return ", ".join(s.replace("_", " ") for s in component_slugs)
    return "Unknown"


def _extract_condition_slugs(condition: dict) -> list[str]:
    slugs: list[str] = []
    slug = condition.get("slug")
    if slug:
        slugs.append(slug)
    components = condition.get("components", []) or []
    for component in components:
        comp_slug = component.get("slug")
        if comp_slug:
            slugs.append(comp_slug)
    return slugs


def _collect_comorbidity_links(
    disorder_slug: str,
    comorbidity_dir: Path = Path("kb/comorbidities"),
    comorbidity_pages_dir: Path = Path("pages/comorbidities"),
) -> list[dict]:
    if not comorbidity_dir.exists():
        return []
    links: list[dict] = []
    for yaml_path in sorted(comorbidity_dir.glob("*.yaml")):
        try:
            data = load_comorbidity(yaml_path)
        except Exception:
            continue
        disease_a = data.get("disease_a", {}) or {}
        disease_b = data.get("disease_b", {}) or {}
        a_slugs = _extract_condition_slugs(disease_a)
        b_slugs = _extract_condition_slugs(disease_b)
        if disorder_slug not in a_slugs and disorder_slug not in b_slugs:
            continue
        page_path = comorbidity_pages_dir / f"{yaml_path.stem}.html"
        if not page_path.exists():
            continue
        role_label = None
        if disorder_slug in a_slugs:
            role_label = "Disease A"
            if disease_a.get("slug") != disorder_slug:
                role_label = "Component of Disease A"
        elif disorder_slug in b_slugs:
            role_label = "Disease B"
            if disease_b.get("slug") != disorder_slug:
                role_label = "Component of Disease B"
        title = f"{_format_condition_label(disease_a)} <-> {_format_condition_label(disease_b)}"
        links.append(
            {
                "href": f"../comorbidities/{yaml_path.stem}.html",
                "title": title,
                "role_label": role_label,
                "directionality": data.get("directionality"),
                "curation_status": data.get("curation_status"),
            }
        )
    return links


def _resolve_nearby_dir(start: Path, dirname: str) -> Path:
    """Find the nearest sibling directory named dirname by walking upward."""
    for parent in (start, *start.parents):
        candidate = parent / dirname
        if candidate.exists():
            return candidate
    return Path(dirname)


def _split_front_matter(text: str) -> tuple[dict, str]:
    """Split YAML front matter from markdown content when present."""
    normalized = text.replace("\r\n", "\n")
    lines = normalized.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}, normalized
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            metadata = yaml.safe_load("\n".join(lines[1:index])) or {}
            if not isinstance(metadata, dict):
                metadata = {}
            return metadata, "\n".join(lines[index + 1 :])
    return {}, normalized


def _normalize_embedded_markdown(text: str) -> str:
    """Remove wrapper indentation commonly found in embedded agent transcripts."""
    normalized = text.strip("\n")
    indented_lines = [
        line
        for line in normalized.splitlines()
        if line.strip() and line.startswith("        ")
    ]
    if len(indented_lines) >= 3:
        normalized = re.sub(r"(?m)^ {8}", "", normalized)
    return normalized.strip()


def _extract_literature_body(text: str) -> tuple[dict, str]:
    """Extract the summary portion from a deep-research markdown artifact."""
    metadata, body = _split_front_matter(text)
    output_chunks = re.split(r"(?m)^## Output\s*$", body)
    if len(output_chunks) > 1:
        body = output_chunks[-1]
    body = _normalize_embedded_markdown(body)
    starts = [
        match.start()
        for pattern in _LITERATURE_START_PATTERNS
        for match in [pattern.search(body)]
        if match
    ]
    if starts:
        body = body[min(starts) :]
    return metadata, _normalize_embedded_markdown(body)


def _extract_display_title(text: str, fallback: str) -> str:
    """Extract a short display title from markdown content."""
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("## "):
            return stripped[3:].strip()
        if stripped.startswith("### "):
            return stripped[4:].strip()
        if (
            stripped
            and len(stripped) <= 120
            and not stripped.startswith(("-", "|", "```"))
        ):
            return stripped
    return fallback


def _humanize_provider(value: str | None) -> str | None:
    """Convert a provider slug into a readable label."""
    if not value:
        return None
    special_cases = {
        "asta": "Asta",
        "cyberian-codex": "Cyberian Codex",
        "falcon": "Falcon",
        "openai": "OpenAI",
        "openscientist": "OpenScientist",
        "perplexity": "Perplexity",
    }
    normalized = str(value).strip().lower()
    if normalized in special_cases:
        return special_cases[normalized]
    return " ".join(
        part.capitalize() for part in re.split(r"[-_]+", normalized) if part
    )


def _rebase_relative_html_urls(html: str, base_prefix: str) -> str:
    """Prefix relative src/href URLs so embedded report assets resolve from the page."""
    if not html or base_prefix in {"", "."}:
        return html

    def _replace(match: re.Match[str]) -> str:
        url = match.group("url")
        if re.match(r"^(?:[a-z][a-z0-9+.-]*:|/|#|\?)", url, re.IGNORECASE):
            return match.group(0)
        rebased = f"{base_prefix.rstrip('/')}/{url.lstrip('./')}"
        return (
            f"{match.group('attr')}={match.group('quote')}"
            f"{rebased}{match.group('quote')}"
        )

    return _RELATIVE_URL_ATTR_PATTERN.sub(_replace, html)


def collect_reports(
    disorder_slug: str,
    reports_root: Path = Path("reports"),
    output_dir: Path | None = None,
) -> list[dict]:
    """Collect markdown report files for a disorder and convert to HTML.

    Args:
        disorder_slug: The slugified disorder name (matching a subdirectory under reports_root).
        reports_root: Root directory containing per-disorder report subdirectories.

    Returns:
        List of dicts with keys 'title', 'html', 'filename', sorted by filename.
    """
    report_dir = reports_root / disorder_slug
    if not report_dir.is_dir():
        return []
    md = markdown_lib.Markdown(extensions=["tables", "fenced_code"])
    results = []
    for md_path in sorted(report_dir.glob("*.md")):
        text = md_path.read_text()
        md.reset()
        html = md.convert(text)
        if output_dir is not None:
            base_prefix = os.path.relpath(
                md_path.parent.resolve(), output_dir.resolve()
            )
            html = _rebase_relative_html_urls(html, base_prefix)
        title = md_path.stem
        for line in text.splitlines():
            stripped = line.strip()
            if stripped.startswith("# ") and not stripped.startswith("##"):
                title = stripped[2:].strip()
                break
        results.append({"title": title, "html": html, "filename": md_path.name})
    return results


def collect_literature_summaries(
    disorder_slug: str,
    research_root: Path = Path("research"),
    output_dir: Path | None = None,
) -> list[dict]:
    """Collect deep-research markdown summaries for a disorder and convert to HTML."""
    if not research_root.is_dir():
        return []
    md = markdown_lib.Markdown(extensions=["tables", "fenced_code"])
    results = []
    for md_path in sorted(research_root.glob(f"{disorder_slug}-deep-research-*.md")):
        if md_path.name.endswith(".citations.md"):
            continue
        metadata, body = _extract_literature_body(md_path.read_text())
        if not body:
            continue
        md.reset()
        html = md.convert(body)
        if output_dir is not None:
            base_prefix = os.path.relpath(
                md_path.parent.resolve(), output_dir.resolve()
            )
            html = _rebase_relative_html_urls(html, base_prefix)
        title = _humanize_provider(metadata.get("provider")) or _extract_display_title(
            body, md_path.stem
        )
        subtitle = _extract_display_title(body, "")
        if subtitle.casefold() in {"", "disorder", title.casefold()}:
            subtitle = None
        results.append(
            {
                "title": title,
                "subtitle": subtitle,
                "html": html,
                "filename": md_path.name,
                "provider": metadata.get("provider"),
                "model": metadata.get("model"),
                "citation_count": metadata.get("citation_count"),
                "end_time": metadata.get("end_time") or metadata.get("start_time"),
            }
        )
    return results


def _github_blob_url(relative_path: Path) -> str:
    """Return the post-merge GitHub page for a repository-relative file."""
    return (
        "https://github.com/monarch-initiative/dismech/blob/main/"
        f"{relative_path.as_posix()}"
    )


def collect_hypothesis_research_links(
    disorder_slug: str,
    hypotheses: list[dict],
    hypotheses_root: Path = Path("kb/hypotheses"),
) -> list[dict]:
    """Collect hypothesis-level deep-research outputs as compact GitHub links."""
    disorder_dir = hypotheses_root / disorder_slug
    if not disorder_dir.is_dir():
        return []

    hypothesis_lookup = {
        str(hypothesis.get("hypothesis_group_id")): hypothesis
        for hypothesis in hypotheses
        if isinstance(hypothesis, dict) and hypothesis.get("hypothesis_group_id")
    }
    hypothesis_order = {
        str(hypothesis.get("hypothesis_group_id")): index
        for index, hypothesis in enumerate(hypotheses)
        if isinstance(hypothesis, dict) and hypothesis.get("hypothesis_group_id")
    }

    sections = []
    for hypothesis_dir in sorted(
        path for path in disorder_dir.iterdir() if path.is_dir()
    ):
        reports = []
        for md_path in sorted(hypothesis_dir.glob("*.md")):
            if md_path.name.endswith(".citations.md"):
                continue
            metadata, _ = _split_front_matter(md_path.read_text(encoding="utf-8"))
            provider = str(metadata.get("provider") or md_path.stem)
            rel_report = (
                Path("kb/hypotheses")
                / disorder_slug
                / hypothesis_dir.name
                / md_path.name
            )
            citations_path = Path(f"{md_path}.citations.md")
            rel_citations = (
                Path("kb/hypotheses")
                / disorder_slug
                / hypothesis_dir.name
                / citations_path.name
            )
            reports.append(
                {
                    "provider": provider,
                    "provider_label": _humanize_provider(provider) or provider,
                    "href": _github_blob_url(rel_report),
                    "filename": md_path.name,
                    "citations_href": _github_blob_url(rel_citations)
                    if citations_path.exists()
                    else None,
                    "citation_count": metadata.get("citation_count"),
                    "end_time": metadata.get("end_time") or metadata.get("start_time"),
                }
            )
        if not reports:
            continue

        hypothesis = hypothesis_lookup.get(hypothesis_dir.name, {})
        sections.append(
            {
                "hypothesis_id": hypothesis_dir.name,
                "hypothesis_label": hypothesis.get("hypothesis_label")
                or hypothesis_dir.name.replace("_", " "),
                "status": hypothesis.get("status"),
                "reports": reports,
                "_sort": hypothesis_order.get(
                    hypothesis_dir.name, len(hypothesis_order)
                ),
            }
        )

    return sorted(
        sections, key=lambda section: (section["_sort"], section["hypothesis_id"])
    )


def render_disorder(
    yaml_path: Path,
    output_path: Optional[Path] = None,
    template_path: Optional[Path] = None,
) -> Path:
    """
    Render a single disorder YAML file to HTML.

    Args:
        yaml_path: Path to the disorder YAML file
        output_path: Optional output path. Defaults to pages/disorders/{name}.html
        template_path: Optional custom template path

    Returns:
        Path to the generated HTML file
    """
    # Load the disorder data
    disorder = load_disorder(yaml_path)
    _augment_mapping_hierarchies(disorder)
    _annotate_regulatory_endpoint_refs(disorder, yaml_path)

    # Read raw YAML for display
    yaml_content = yaml_path.read_text()

    # Determine output path early so we can resolve local page links relative to it.
    if output_path is None:
        disorder_name = disorder.get("name") or yaml_path.stem
        output_path = Path("pages/disorders") / f"{slugify(disorder_name)}.html"
    else:
        output_path = Path(output_path)

    _annotate_internal_differential_links(
        disorder=disorder,
        current_page_filename=output_path.name,
        disorders_dir=yaml_path.parent,
    )
    _annotate_model_links(disorder)

    # Set up Jinja2 environment
    if template_path is None:
        template_dir = Path(__file__).parent / "templates"
        template_name = "disorder.html.j2"
    else:
        template_dir = template_path.parent
        template_name = template_path.name

    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(["html", "j2"]),
    )

    # Register custom filters
    current_term_id = _extract_disorder_term_id(disorder)
    env.filters["curie_to_url"] = curie_to_url
    env.filters["basename"] = lambda p: Path(p).name
    env.filters["dismech_page_url"] = _build_dismech_page_url_filter(
        yaml_path.parent,
        excluded_term_ids={current_term_id} if current_term_id else None,
    )
    env.filters["has_local_disorder_page"] = _build_has_local_disorder_filter(
        yaml_path.parent,
    )

    # Load and render template
    template = env.get_template(template_name)

    # Build GitHub source URL
    source_file = f"https://github.com/monarch-initiative/dismech/blob/main/kb/disorders/{yaml_path.name}"

    # Build causal graph and generate Mermaid code + pathograph JSON
    graph = build_causal_graph(disorder)
    mermaid_code = generate_mermaid(graph)
    pathograph_data = graph_to_json(graph, disorder)
    pathograph_node_count = len(
        {node_name for edge in graph.edges for node_name in (edge.source, edge.target)}
    )
    comorbidity_links = _collect_comorbidity_links(yaml_path.stem)
    reports_root = _resolve_nearby_dir(yaml_path.parent, "reports")
    research_root = _resolve_nearby_dir(yaml_path.parent, "research")
    hypotheses_root = _resolve_nearby_dir(yaml_path.parent, "kb/hypotheses")
    disorder_slug = slugify(disorder.get("name") or yaml_path.stem)
    file_stem = yaml_path.stem
    report_sections = collect_reports(
        disorder_slug,
        reports_root=reports_root,
        output_dir=output_path.parent,
    )
    literature_sections = collect_literature_summaries(
        disorder_slug,
        research_root=research_root,
        output_dir=output_path.parent,
    )
    # Research files are named after the YAML file stem, which may differ from
    # the slugified disorder name.  Fall back to the file stem when needed.
    if not literature_sections and file_stem != disorder_slug:
        literature_sections = collect_literature_summaries(
            file_stem,
            research_root=research_root,
            output_dir=output_path.parent,
        )
    if not report_sections and file_stem != disorder_slug:
        report_sections = collect_reports(
            file_stem,
            reports_root=reports_root,
            output_dir=output_path.parent,
        )
    hypothesis_research_links = collect_hypothesis_research_links(
        file_stem,
        disorder.get("mechanistic_hypotheses") or [],
        hypotheses_root=hypotheses_root,
    )
    if not hypothesis_research_links and file_stem != disorder_slug:
        hypothesis_research_links = collect_hypothesis_research_links(
            disorder_slug,
            disorder.get("mechanistic_hypotheses") or [],
            hypotheses_root=hypotheses_root,
        )
    hypothesis_research_count = sum(
        len(section.get("reports") or []) for section in hypothesis_research_links
    )

    # Group phenotypes by HPO broad category
    phenotype_groups = _group_phenotypes_by_category(disorder.get("phenotypes") or [])

    # OpenScientist integration context
    yaml_revision = hashlib.sha256(yaml_content.encode()).hexdigest()[:12]
    disease_term = disorder.get("disease_term") or {}
    disease_term_term = disease_term.get("term") or {}
    openscientist_proxy_url = os.environ.get(
        "OPENSCIENTIST_PROXY_URL",
        "https://dismech-openscientist.bbop.workers.dev",
    )

    # Relative path from the output page directory to research root, so that
    # artifact image <img src="..."> paths resolve correctly in the HTML.
    research_root_rel = os.path.relpath(
        research_root.resolve(), output_path.parent.resolve()
    )

    html = template.render(
        disorder=disorder,
        yaml_content=yaml_content,
        source_file=source_file,
        mermaid_code=mermaid_code,
        pathograph_data=pathograph_data,
        pathograph_node_count=pathograph_node_count,
        graph_issues=graph.integrity_issues,
        comorbidity_links=comorbidity_links,
        phenotype_groups=phenotype_groups,
        report_sections=report_sections,
        literature_sections=literature_sections,
        hypothesis_research_links=hypothesis_research_links,
        hypothesis_research_count=hypothesis_research_count,
        research_root_rel=research_root_rel,
        # OpenScientist integration
        disorder_slug=disorder_slug,
        yaml_revision=yaml_revision,
        mondo_id=disease_term_term.get("id", ""),
        openscientist_proxy_url=openscientist_proxy_url,
    )

    # Write output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html)

    return output_path


def _build_condition_graphs(
    condition: dict,
    disorders_dir: Path = Path("kb/disorders"),
) -> list[dict]:
    """Build causal graphs for a comorbidity condition (handles composites)."""
    graphs: list[dict] = []
    slugs: list[tuple[str, str]] = []
    slug = condition.get("slug")
    if slug:
        slugs.append((slug, slug.replace("_", " ")))
    for comp in condition.get("components", []) or []:
        if comp.get("slug"):
            slugs.append((comp["slug"], comp["slug"].replace("_", " ")))
    for s, label in slugs:
        path = disorders_dir / f"{s}.yaml"
        if path.exists():
            disorder = load_disorder(path)
            graph = build_causal_graph(disorder)
            mermaid = generate_mermaid(graph)
            if mermaid:
                graphs.append({"label": label, "mermaid_code": mermaid})
    return graphs


def _resolve_comorbidity_disorders_dir(yaml_path: Path) -> Path:
    """Resolve disorders directory for a comorbidity file, preferring nearby kb layout."""
    candidate = yaml_path.parent.parent / "disorders"
    if candidate.exists():
        return candidate
    return Path("kb/disorders")


def render_comorbidity(
    yaml_path: Path,
    output_path: Optional[Path] = None,
    template_path: Optional[Path] = None,
) -> Path:
    """
    Render a single comorbidity YAML file to HTML.

    Args:
        yaml_path: Path to the comorbidity YAML file
        output_path: Optional output path. Defaults to pages/comorbidities/{name}.html
        template_path: Optional custom template path

    Returns:
        Path to the generated HTML file
    """
    comorbidity = load_comorbidity(yaml_path)
    yaml_content = yaml_path.read_text()
    disorders_dir = _resolve_comorbidity_disorders_dir(yaml_path)

    if template_path is None:
        template_dir = Path(__file__).parent / "templates"
        template_name = "comorbidity.html.j2"
    else:
        template_dir = template_path.parent
        template_name = template_path.name

    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(["html", "j2"]),
    )
    env.filters["curie_to_url"] = curie_to_url
    env.filters["dismech_page_url"] = _build_dismech_page_url_filter(
        disorders_dir,
        local_prefix="../disorders/",
    )
    env.filters["has_local_disorder_page"] = _build_has_local_disorder_filter(
        disorders_dir,
    )
    env.filters["dismech_slug_page_url"] = _build_dismech_slug_page_url_filter(
        disorders_dir,
        local_prefix="../disorders/",
    )
    env.filters["has_local_disorder_slug_page"] = _build_has_local_disorder_slug_filter(
        disorders_dir,
    )

    template = env.get_template(template_name)

    source_file = f"https://github.com/monarch-initiative/dismech/blob/main/kb/comorbidities/{yaml_path.name}"

    disease_a = comorbidity.get("disease_a", {}) or {}
    disease_b = comorbidity.get("disease_b", {}) or {}

    disease_a_graphs = _build_condition_graphs(disease_a, disorders_dir=disorders_dir)
    disease_b_graphs = _build_condition_graphs(disease_b, disorders_dir=disorders_dir)

    html = template.render(
        comorbidity=comorbidity,
        yaml_content=yaml_content,
        source_file=source_file,
        disease_a_label=_format_condition_label(disease_a),
        disease_b_label=_format_condition_label(disease_b),
        disease_a_slug=disease_a.get("slug") or "",
        disease_b_slug=disease_b.get("slug") or "",
        disease_a_graphs=disease_a_graphs,
        disease_b_graphs=disease_b_graphs,
    )

    if output_path is None:
        output_dir = Path("pages/comorbidities")
        output_dir.mkdir(parents=True, exist_ok=True)
        comorbidity_name = comorbidity.get("name") or yaml_path.stem
        output_path = output_dir / f"{slugify(comorbidity_name)}.html"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html)
    return output_path


def render_module(
    yaml_path: Path,
    output_path: Optional[Path] = None,
    template_path: Optional[Path] = None,
    *,
    disorders_dir: Path = Path("kb/disorders"),
    usage_index: dict[str, list[dict]] | None = None,
) -> Path:
    """Render a single shared module YAML file to HTML."""
    module, disorder_usage = _load_module_context(
        yaml_path,
        disorders_dir=disorders_dir,
        usage_index=usage_index,
    )
    yaml_content = yaml_path.read_text()

    if template_path is None:
        template_dir = Path(__file__).parent / "templates"
        template_name = "module.html.j2"
    else:
        template_dir = template_path.parent
        template_name = template_path.name

    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(["html", "j2"]),
    )
    env.filters["curie_to_url"] = curie_to_url
    template = env.get_template(template_name)

    source_file = (
        "https://github.com/monarch-initiative/dismech/blob/main/"
        f"kb/modules/{yaml_path.name}"
    )
    graph = build_causal_graph(module)
    pathograph_data = graph_to_json(graph, module)
    pathograph_node_count = len(
        {node_name for edge in graph.edges for node_name in (edge.source, edge.target)}
    )

    html = template.render(
        module=module,
        module_id=yaml_path.stem,
        disorder_usage=disorder_usage,
        pathograph_data=pathograph_data,
        pathograph_node_count=pathograph_node_count,
        graph_issues=graph.integrity_issues,
        yaml_content=yaml_content,
        source_file=source_file,
    )

    if output_path is None:
        output_path = Path("pages/modules") / f"{yaml_path.stem}.html"
    else:
        output_path = Path(output_path)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html)
    return output_path


def render_module_index(
    modules: list[dict],
    output_path: Path = Path("pages/modules/index.html"),
) -> Path:
    """Render the shared-module index page."""
    template_dir = Path(__file__).parent / "templates"
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(["html", "j2"]),
    )
    template = env.get_template("module_index.html.j2")

    html = template.render(
        modules=sorted(
            modules,
            key=lambda module: str(module.get("name") or "").casefold(),
        )
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html)
    return output_path


def render_all_modules(
    input_dir: Path = Path("kb/modules"),
    output_dir: Path = Path("pages/modules"),
    template_path: Optional[Path] = None,
    *,
    disorders_dir: Path = Path("kb/disorders"),
) -> list[Path]:
    """Render all shared mechanism modules plus their index page."""
    if not input_dir.exists():
        return []

    output_dir.mkdir(parents=True, exist_ok=True)
    usage_index = _collect_module_usage(disorders_dir)

    output_files: list[Path] = []
    module_summaries: list[dict] = []

    for yaml_path in sorted(input_dir.glob("*.yaml")):
        module, _ = _load_module_context(
            yaml_path,
            disorders_dir=disorders_dir,
            usage_index=usage_index,
        )
        output_path = output_dir / f"{yaml_path.stem}.html"
        render_module(
            yaml_path,
            output_path,
            template_path,
            disorders_dir=disorders_dir,
            usage_index=usage_index,
        )
        output_files.append(output_path)
        module_summaries.append(_build_module_summary(module))
        print(f"Rendered module: {yaml_path.stem} -> {output_path}")

    index_path = render_module_index(module_summaries, output_dir / "index.html")
    output_files.append(index_path)
    print(f"Rendered module index -> {index_path}")
    return output_files


def render_all_comorbidities(
    input_dir: Path = Path("kb/comorbidities"),
    output_dir: Path = Path("pages/comorbidities"),
    template_path: Optional[Path] = None,
) -> list[Path]:
    """
    Render all comorbidity YAML files to HTML pages.

    Args:
        input_dir: Directory containing comorbidity YAML files
        output_dir: Directory for output HTML files
        template_path: Optional custom template path

    Returns:
        List of generated HTML file paths
    """
    if not input_dir.exists():
        return []
    output_dir.mkdir(parents=True, exist_ok=True)

    yaml_files = sorted(input_dir.glob("*.yaml"))
    output_files = []
    for yaml_path in yaml_files:
        output_path = output_dir / f"{yaml_path.stem}.html"
        render_comorbidity(yaml_path, output_path, template_path)
        output_files.append(output_path)
        print(f"Rendered comorbidity: {yaml_path.stem} -> {output_path}")
    return output_files


def _load_schema() -> dict:
    schema_path = Path(__file__).parent / "schema" / "dismech.yaml"
    try:
        return yaml.safe_load(schema_path.read_text()) or {}
    except FileNotFoundError:
        return {}


@lru_cache(maxsize=None)
def _get_oak_adapter(adapter_str: str):
    try:
        from oaklib import get_adapter
    except Exception:
        return None
    try:
        return get_adapter(adapter_str)
    except Exception:
        return None


def _compact_hierarchy_path(
    path: list[str | None], max_nodes: int = 6
) -> list[str | None]:
    if len(path) <= max_nodes:
        return path
    head = path[:2]
    tail = path[-3:]
    return head + [None] + tail


def _build_hierarchy_path(adapter, term_id: str, root_id: str) -> list[Optional[str]]:
    path: list[str] = []
    current = term_id
    visited = set()
    while current and current not in visited:
        visited.add(current)
        path.append(current)
        if current == root_id:
            break
        parents = list(adapter.hierarchical_parents(current))
        if not parents:
            break
        current = sorted(parents)[0]
    return list(reversed(path))


def _augment_mapping_hierarchies(disorder: dict) -> None:
    mappings = disorder.get("mappings") or {}
    for mapping_list in mappings.values():
        if not isinstance(mapping_list, list):
            continue
        for mapping in mapping_list:
            if not isinstance(mapping, dict):
                continue
            term = mapping.get("term") or {}
            term_id = term.get("id")
            if not term_id or ":" not in term_id:
                continue
            prefix = term_id.split(":", 1)[0]
            hierarchy = STRICT_HIERARCHIES.get(prefix)
            if not hierarchy:
                continue
            adapter = _get_oak_adapter(hierarchy["adapter"])
            if adapter is None:
                continue
            path = _build_hierarchy_path(adapter, term_id, hierarchy["root"])
            if not path:
                continue
            compacted = _compact_hierarchy_path(path)
            labeled_path = []
            for curie in compacted:
                if curie is None:
                    labeled_path.append({"label": "...", "is_ellipsis": True})
                    continue
                label = adapter.label(curie) or curie
                labeled_path.append({"id": curie, "label": label})
            mapping["hierarchy_path"] = labeled_path


def _load_classification_enums() -> dict:
    classification_dir = Path(__file__).parent / "schema" / "classifications"
    enums: dict = {}
    if not classification_dir.exists():
        return enums
    for path in sorted(classification_dir.glob("*.yaml")):
        data = yaml.safe_load(path.read_text()) or {}
        source_meta = {
            "source_id": data.get("id"),
            "source_name": data.get("name"),
            "title": data.get("title"),
            "description": data.get("description"),
        }
        for enum_name, enum_def in (data.get("enums") or {}).items():
            enums[enum_name] = {
                "definition": enum_def or {},
                **source_meta,
            }
    return enums


def _assignment_class_to_enum(schema: dict) -> dict[str, str]:
    mapping: dict[str, str] = {}
    classes = schema.get("classes") or {}
    for class_name, class_def in classes.items():
        slot_usage = class_def.get("slot_usage") or {}
        classification_usage = slot_usage.get("classification_value") or {}
        enum_name = classification_usage.get("range")
        if enum_name:
            mapping[class_name] = enum_name
    return mapping


def _classification_slot_to_enum(
    schema: dict, assignment_to_enum: dict[str, str]
) -> dict[str, str]:
    mapping: dict[str, str] = {}
    slots = schema.get("slots") or {}
    for slot_name, slot_def in slots.items():
        range_name = slot_def.get("range")
        if range_name in assignment_to_enum:
            mapping[slot_name] = assignment_to_enum[range_name]
    return mapping


def _find_enum_for_value(value: str, enums: dict) -> Optional[str]:
    for enum_name, enum_info in enums.items():
        enum_def = enum_info.get("definition") or {}
        if value in (enum_def.get("permissible_values") or {}):
            return enum_name
    return None


def _build_enum_tree(enum_def: dict) -> tuple[list[dict], dict[str, dict]]:
    values = enum_def.get("permissible_values") or {}
    nodes: dict[str, dict] = {}
    for value, meta in values.items():
        nodes[value] = {
            "name": value,
            "title": meta.get("title"),
            "description": meta.get("description"),
            "meaning": meta.get("meaning"),
            "children": [],
            "disorders": [],
            "parent_ids": [],
        }
    for value, meta in values.items():
        parents = meta.get("is_a")
        if isinstance(parents, str):
            parents = [parents]
        elif not parents:
            parents = []
        for parent in parents:
            if parent in nodes:
                nodes[parent]["children"].append(nodes[value])
                nodes[value]["parent_ids"].append(parent)
    roots = [node for node in nodes.values() if not node["parent_ids"]]
    return roots, nodes


def render_classification_pages(
    input_dir: Path = Path("kb/disorders"),
    output_dir: Path = Path("pages/classifications"),
    template_path: Optional[Path] = None,
) -> list[Path]:
    enums = _load_classification_enums()
    if not enums:
        return []

    schema = _load_schema()
    assignment_to_enum = _assignment_class_to_enum(schema)
    slot_to_enum = _classification_slot_to_enum(schema, assignment_to_enum)

    disorders: list[dict] = []
    for yaml_path in sorted(input_dir.glob("*.yaml")):
        if yaml_path.name.endswith(".history.yaml"):
            continue
        disorder = load_disorder(yaml_path) or {}
        name = disorder.get("name") or yaml_path.stem
        disorders.append(
            {
                "name": name,
                "slug": slugify(name),
                "classifications": disorder.get("classifications") or {},
            }
        )

    disorders_by_enum_value: dict[str, dict[str, list[dict]]] = {
        name: {} for name in enums
    }
    for disorder in disorders:
        classifications = disorder.get("classifications") or {}
        for slot_name, entry in classifications.items():
            if entry is None:
                continue
            entries = entry if isinstance(entry, list) else [entry]
            for item in entries:
                if isinstance(item, dict):
                    value = item.get("classification_value")
                else:
                    value = item
                if not value:
                    continue
                enum_name = slot_to_enum.get(slot_name) or _find_enum_for_value(
                    value, enums
                )
                if not enum_name:
                    continue
                disorders_by_enum_value.setdefault(enum_name, {}).setdefault(
                    value, []
                ).append(
                    {
                        "name": disorder["name"],
                        "slug": disorder["slug"],
                    }
                )

    if template_path is None:
        template_dir = Path(__file__).parent / "templates"
        template_name = "classification.html.j2"
    else:
        template_dir = template_path.parent
        template_name = template_path.name

    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(["html", "j2"]),
    )
    env.filters["curie_to_url"] = curie_to_url
    env.filters["dismech_page_url"] = _build_dismech_page_url_filter(
        input_dir,
        local_prefix="../disorders/",
    )
    env.filters["has_local_disorder_page"] = _build_has_local_disorder_filter(
        input_dir,
    )
    template = env.get_template(template_name)

    output_dir.mkdir(parents=True, exist_ok=True)

    output_paths: list[Path] = []
    for enum_name, enum_info in enums.items():
        enum_def = enum_info.get("definition") or {}
        roots, nodes = _build_enum_tree(enum_def)
        for value, disorder_list in (
            disorders_by_enum_value.get(enum_name) or {}
        ).items():
            if value in nodes:
                nodes[value]["disorders"] = sorted(
                    disorder_list, key=lambda d: d["name"]
                )
        for node in nodes.values():
            node["is_leaf"] = len(node["children"]) == 0

        html = template.render(
            enum_name=enum_name,
            enum_description=enum_def.get("description"),
            classification_title=enum_info.get("title"),
            classification_description=enum_info.get("description"),
            classification_id=enum_info.get("source_id"),
            roots=roots,
        )
        output_path = output_dir / f"{slugify(enum_name)}.html"
        output_path.write_text(html)
        output_paths.append(output_path)

    return output_paths


def render_all_disorders(
    input_dir: Path = Path("kb/disorders"),
    output_dir: Path = Path("pages/disorders"),
    template_path: Optional[Path] = None,
) -> list[Path]:
    """
    Render all disorder YAML files to HTML pages.

    Args:
        input_dir: Directory containing disorder YAML files
        output_dir: Directory for output HTML files
        template_path: Optional custom template path

    Returns:
        List of generated HTML file paths
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    render_all_comorbidities()
    render_all_modules(disorders_dir=input_dir)

    yaml_files = [
        path
        for path in sorted(input_dir.glob("*.yaml"))
        if not path.name.endswith(".history.yaml")
    ]
    output_files = []

    # Each disorder should have a name,
    # but if not, we'll use the filename as a fallback
    for yaml_path in yaml_files:
        disorder = load_disorder(yaml_path)
        disorder_name = disorder.get("name") or yaml_path.stem
        output_path = output_dir / f"{slugify(disorder_name)}.html"

        render_disorder(yaml_path, output_path, template_path)
        output_files.append(output_path)
        print(f"Rendered: {disorder_name} -> {output_path}")

    render_classification_pages(input_dir=input_dir)

    print(f"\nGenerated {len(output_files)} HTML pages in {output_dir}")
    return output_files


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Render disorder, comorbidity, and module pages"
    )
    parser.add_argument("path", nargs="?", help="Single YAML file or directory")
    parser.add_argument("--all", "-a", action="store_true", help="Render all disorders")
    parser.add_argument(
        "--comorbidity", action="store_true", help="Render comorbidity page(s)"
    )
    parser.add_argument("--module", action="store_true", help="Render module page(s)")
    parser.add_argument("--output", "-o", help="Output path (file or directory)")
    parser.add_argument("--template", "-t", help="Custom template path")

    args = parser.parse_args()

    template_path = Path(args.template) if args.template else None

    if args.comorbidity:
        if args.path is None:
            raise SystemExit("Error: --comorbidity requires a file or directory path")
        input_path = Path(args.path)
        if input_path.is_dir():
            output_dir = (
                Path(args.output) if args.output else Path("pages/comorbidities")
            )
            render_all_comorbidities(input_path, output_dir, template_path)
        else:
            output_path = Path(args.output) if args.output else None
            result = render_comorbidity(input_path, output_path, template_path)
            print(f"Generated: {result}")
        return

    if args.module:
        if args.path is None:
            raise SystemExit("Error: --module requires a file or directory path")
        input_path = Path(args.path)
        if input_path.is_dir():
            output_dir = Path(args.output) if args.output else Path("pages/modules")
            render_all_modules(input_path, output_dir, template_path)
        else:
            output_path = Path(args.output) if args.output else None
            result = render_module(input_path, output_path, template_path)
            print(f"Generated: {result}")
        return

    if args.all or args.path is None:
        input_dir = Path(args.path) if args.path else Path("kb/disorders")
        output_dir = Path(args.output) if args.output else Path("pages/disorders")
        render_all_disorders(input_dir, output_dir, template_path)
    else:
        yaml_path = Path(args.path)
        output_path = Path(args.output) if args.output else None
        result = render_disorder(yaml_path, output_path, template_path)
        print(f"Generated: {result}")


if __name__ == "__main__":
    main()
