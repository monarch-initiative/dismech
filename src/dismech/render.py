"""
Render disorder YAML files to HTML pages using Jinja2 templates.
"""

import datetime
import hashlib
import html
import json
import os
import re
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
from typing import Callable, Optional, TypedDict

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


def _strip_line_end_whitespace(text: str) -> str:
    """Remove renderer-introduced spaces at line ends without changing content."""
    return re.sub(r"[ \t]+(?=\r?\n|$)", "", text)


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


def _build_semantic_ref_index(disorder: dict) -> dict[str, str]:
    """Resolve YAML semantic refs to in-page HTML fragment links."""
    ref_index: dict[str, str] = {}

    pathophysiology_items = disorder.get("pathophysiology") or []
    if isinstance(pathophysiology_items, list):
        for item in pathophysiology_items:
            if not isinstance(item, dict):
                continue
            name = item.get("name")
            if not name:
                continue
            anchor_id = item.get("_anchor_id") or _make_anchor_id(
                "pathophysiology", str(name)
            )
            item.setdefault("_anchor_id", anchor_id)
            ref_index[f"pathophysiology#{name}"] = f"#{anchor_id}"

    return ref_index


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


def _coerce_string_list(value: object) -> list[str]:
    """Normalize schema values that may be absent, scalar, or multivalued."""
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value if item is not None and str(item).strip()]
    if isinstance(value, str):
        return [value] if value.strip() else []
    return [str(value)]


def _annotate_hypothesis_group_links(disorder: dict) -> None:
    """Attach anchors and visible cross-links for mechanistic hypothesis groups."""
    hypotheses = disorder.get("mechanistic_hypotheses") or []
    pathophysiology_items = disorder.get("pathophysiology") or []
    if not isinstance(hypotheses, list):
        hypotheses = []
    if not isinstance(pathophysiology_items, list):
        pathophysiology_items = []

    hypotheses_by_id: dict[str, dict] = {}
    for hypothesis in hypotheses:
        if not isinstance(hypothesis, dict):
            continue
        hypothesis_id = str(hypothesis.get("hypothesis_group_id") or "").strip()
        if not hypothesis_id:
            continue
        hypothesis["_anchor_id"] = _make_anchor_id("hypothesis", hypothesis_id)
        hypothesis["_pathograph_links"] = []
        hypothesis["_research_reports"] = []
        hypotheses_by_id.setdefault(hypothesis_id, hypothesis)

    pathophysiology_by_name: dict[str, dict] = {}
    for item in pathophysiology_items:
        if not isinstance(item, dict):
            continue
        name = item.get("name")
        if not name:
            continue
        item.setdefault("_anchor_id", _make_anchor_id("pathophysiology", str(name)))
        item["_hypothesis_links"] = []
        pathophysiology_by_name[str(name)] = item

    seen_hypothesis_edges: dict[str, set[tuple[str, str]]] = defaultdict(set)

    def link_payload(hypothesis_id: str) -> dict:
        hypothesis = hypotheses_by_id.get(hypothesis_id)
        return {
            "hypothesis_id": hypothesis_id,
            "hypothesis_label": (
                hypothesis.get("hypothesis_label")
                if hypothesis
                else hypothesis_id.replace("_", " ")
            ),
            "status": hypothesis.get("status") if hypothesis else None,
            "anchor_id": hypothesis.get("_anchor_id") if hypothesis else None,
        }

    for item in pathophysiology_items:
        if not isinstance(item, dict):
            continue
        source = item.get("name")
        if not source:
            continue
        item_links: dict[str, dict] = {}

        downstream = item.get("downstream") or []
        if not isinstance(downstream, list):
            continue
        for edge in downstream:
            if not isinstance(edge, dict):
                continue
            target = edge.get("target")
            hypothesis_ids = _coerce_string_list(edge.get("hypothesis_groups"))
            if not target or not hypothesis_ids:
                continue

            edge_links = []
            for hypothesis_id in hypothesis_ids:
                payload = link_payload(hypothesis_id)
                edge_links.append(payload)
                item_links.setdefault(hypothesis_id, payload)

                hypothesis = hypotheses_by_id.get(hypothesis_id)
                if hypothesis is None:
                    continue
                edge_key = (str(source), str(target))
                if edge_key in seen_hypothesis_edges[hypothesis_id]:
                    continue
                seen_hypothesis_edges[hypothesis_id].add(edge_key)
                target_item = pathophysiology_by_name.get(str(target))
                hypothesis["_pathograph_links"].append(
                    {
                        "source": source,
                        "target": target,
                        "source_anchor": item.get("_anchor_id"),
                        "target_anchor": (
                            target_item.get("_anchor_id") if target_item else None
                        ),
                        "description": edge.get("description"),
                        "causal_link_type": edge.get("causal_link_type"),
                        "intermediate_mechanisms": _coerce_string_list(
                            edge.get("intermediate_mechanisms")
                        ),
                    }
                )

            edge["_hypothesis_links"] = edge_links

        item["_hypothesis_links"] = sorted(
            item_links.values(),
            key=lambda link: (
                str(link.get("hypothesis_label") or "").casefold(),
                str(link.get("hypothesis_id") or "").casefold(),
            ),
        )


def _annotate_hypothesis_research_links(
    disorder: dict, hypothesis_research_links: list[dict]
) -> None:
    """Attach collected report links to their disease-level hypothesis entries."""
    hypotheses = disorder.get("mechanistic_hypotheses") or []
    if not isinstance(hypotheses, list):
        return

    reports_by_hypothesis_id = {
        str(section.get("hypothesis_id")): section.get("reports") or []
        for section in hypothesis_research_links
        if isinstance(section, dict) and section.get("hypothesis_id")
    }
    for hypothesis in hypotheses:
        if not isinstance(hypothesis, dict):
            continue
        hypothesis_id = str(hypothesis.get("hypothesis_group_id") or "").strip()
        hypothesis["_research_reports"] = reports_by_hypothesis_id.get(
            hypothesis_id, []
        )


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


def _build_comorbidity_summary(
    yaml_path: Path,
    disorder_pages_by_name: dict[str, str],
) -> dict:
    """Build a compact card payload for the comorbidity index page."""
    data = load_comorbidity(yaml_path) or {}
    disease_a = data.get("disease_a") or {}
    disease_b = data.get("disease_b") or {}
    disease_a_slug = disease_a.get("slug")
    disease_b_slug = disease_b.get("slug")

    return {
        "name": data.get("name") or yaml_path.stem,
        "href": f"{yaml_path.stem}.html",
        "disease_a": {
            "label": _format_condition_label(disease_a),
            "href": _resolve_local_disorder_slug_href(
                disease_a_slug,
                disorder_pages_by_name,
                local_prefix="../disorders/",
            ),
        },
        "disease_b": {
            "label": _format_condition_label(disease_b),
            "href": _resolve_local_disorder_slug_href(
                disease_b_slug,
                disorder_pages_by_name,
                local_prefix="../disorders/",
            ),
        },
        "directionality": data.get("directionality") or "UNKNOWN",
        "curation_status": data.get("curation_status") or "UNKNOWN",
    }


def render_comorbidity_index(
    comorbidities: list[dict],
    output_path: Path = Path("pages/comorbidities/index.html"),
) -> Path:
    """Render the comorbidity landing page."""
    template_dir = Path(__file__).parent / "templates"
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(["html", "j2"]),
    )
    template = env.get_template("comorbidity_index.html.j2")

    html = template.render(
        comorbidities=sorted(
            comorbidities,
            key=lambda comorbidity: (
                str(comorbidity.get("disease_a", {}).get("label") or "").casefold(),
                str(comorbidity.get("disease_b", {}).get("label") or "").casefold(),
            ),
        )
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html)
    return output_path


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


# ---------------------------------------------------------------------------
# Deep-research provider registry — single source of truth (dismech#4765)
# ---------------------------------------------------------------------------
# One ordered entry per known deep-research provider. Every consumer derives
# from this list, so adding or renaming a provider means editing exactly one
# place:
#   * ``_humanize_provider``       — per-report label on disorder pages
#   * ``_display_name_from_provider`` — canonical browse category for the index
#   * ``provider_options``         — filter-chip key/name pairs (index page)
#   * ``research_index.html.j2``   — pill colors + legend entries
#
# Per-entry fields:
#   key          normalized category key (CSS class suffix + filter key)
#   name         canonical category display name
#   match_keys   dash-normalized report-filename slugs that collapse into this
#                category (drives ``_display_name_from_provider`` grouping)
#   humanize     per-slug overrides for ``_humanize_provider`` keyed by the raw
#                lower-cased slug; slugs not listed fall back to title-casing,
#                so only labels that title-casing cannot reproduce (e.g.
#                "OpenAI") or legacy slugs that keep their own name (e.g.
#                "falcon" -> "Falcon") need an entry here
#   url          legend link target, or None for catch-all/non-product entries
#   prefix       legend/pill prefix (e.g. the fallback warning glyph)
#   description  legend descriptive text
#   pill         pill colors {"border", "background", "color"}
class _ProviderPill(TypedDict):
    """Pill colors for a provider category."""

    border: str
    background: str
    color: str


class _ProviderEntry(TypedDict):
    """One deep-research provider category in the registry."""

    key: str
    name: str
    match_keys: tuple[str, ...]
    humanize: dict[str, str]
    url: str | None
    prefix: str
    description: str
    pill: _ProviderPill


DEEP_RESEARCH_PROVIDERS: list[_ProviderEntry] = [
    {
        "key": "edison",
        "name": "Edison",
        "match_keys": ("edison", "falcon"),
        "humanize": {"falcon": "Falcon"},
        "url": "https://platform.edisonscientific.com/",
        "prefix": "",
        "description": (
            "Formerly Falcon in report filenames; deep research generated via "
            "Edison Scientific."
        ),
        "pill": {"border": "#c7d2fe", "background": "#eef2ff", "color": "#4338ca"},
    },
    {
        "key": "asta",
        "name": "Asta",
        "match_keys": ("asta",),
        "humanize": {"asta": "Asta"},
        "url": "https://asta.allen.ai/",
        "prefix": "",
        "description": "Literature citations and snippets provided by Ai2 Asta.",
        "pill": {"border": "#d9f99d", "background": "#f7fee7", "color": "#3f6212"},
    },
    {
        "key": "openai",
        "name": "OpenAI",
        "match_keys": ("openai", "codex"),
        "humanize": {"openai": "OpenAI"},
        "url": "https://openai.com/",
        "prefix": "",
        "description": "Deep research generated using OpenAI models.",
        "pill": {"border": "#bfdbfe", "background": "#eff6ff", "color": "#1d4ed8"},
    },
    {
        "key": "cyberian",
        "name": "Cyberian",
        "match_keys": ("cyberian", "cyberian-codex"),
        "humanize": {"cyberian-codex": "Cyberian Codex"},
        "url": "https://github.com/monarch-initiative/deep-research-client",
        "prefix": "",
        "description": "Includes both Cyberian and Cyberian Codex reports.",
        "pill": {"border": "#fed7aa", "background": "#fff7ed", "color": "#9a3412"},
    },
    {
        "key": "perplexity",
        "name": "Perplexity",
        "match_keys": ("perplexity",),
        "humanize": {"perplexity": "Perplexity"},
        "url": "https://www.perplexity.ai/",
        "prefix": "",
        "description": (
            "Deep research generated using Perplexity search/reasoning workflows."
        ),
        "pill": {"border": "#ddd6fe", "background": "#f5f3ff", "color": "#6d28d9"},
    },
    {
        "key": "claude-code",
        "name": "Claude Code",
        "match_keys": ("claude-code", "claudecode"),
        "humanize": {"claude_code": "Claude Code"},
        "url": "https://claude.com/claude-code",
        "prefix": "",
        "description": (
            "Web-grounded agentic deep research run via the local Claude Code CLI "
            "(WebSearch/WebFetch only); no separate API key required."
        ),
        "pill": {"border": "#f3c2b3", "background": "#fdf2ee", "color": "#b8451f"},
    },
    {
        "key": "fallback",
        "name": "Fallback",
        "match_keys": ("fallback",),
        "humanize": {},
        "url": None,
        "prefix": "⚠️ ",
        "description": (
            "Not a true deep research run; produced by fallback extraction logic."
        ),
        "pill": {"border": "#fca5a5", "background": "#fef2f2", "color": "#b91c1c"},
    },
    {
        "key": "openscientist",
        "name": "OpenScientist",
        "match_keys": ("openscientist", "openscientist-review"),
        "humanize": {"openscientist": "OpenScientist"},
        "url": "https://www.openscientist.io/",
        "prefix": "",
        "description": "Includes OpenScientist and OpenScientist Review reports.",
        "pill": {"border": "#c4b5fd", "background": "#f5f3ff", "color": "#5b21b6"},
    },
    {
        "key": "other",
        "name": "Other",
        "match_keys": (),
        "humanize": {},
        "url": None,
        "prefix": "",
        "description": "All providers outside the standard categories listed here.",
        "pill": {"border": "#d1d5db", "background": "#f3f4f6", "color": "#374151"},
    },
]

# Catch-all category key/name for slugs not matched by any registry entry.
_PROVIDER_FALLBACK_CATEGORY = "Other"

# Derived lookups (built once from the registry above).
_PROVIDER_HUMANIZE_OVERRIDES: dict[str, str] = {
    slug: label
    for entry in DEEP_RESEARCH_PROVIDERS
    for slug, label in entry["humanize"].items()
}
_PROVIDER_CATEGORY_BY_MATCH_KEY: dict[str, str] = {
    match_key: entry["name"]
    for entry in DEEP_RESEARCH_PROVIDERS
    for match_key in entry["match_keys"]
}
_PROVIDER_PREFIX_BY_KEY: dict[str, str] = {
    entry["key"]: entry["prefix"] for entry in DEEP_RESEARCH_PROVIDERS
}


def _normalize_provider_key(value: str | None) -> str:
    """Dash-normalize a provider token (lowercase, non-alphanumeric -> '-')."""
    return re.sub(r"[^a-z0-9]+", "-", (value or "").strip().casefold()).strip("-")


def _humanize_provider(value: str | None) -> str | None:
    """Convert a provider slug into a readable per-report label."""
    if not value:
        return None
    normalized = str(value).strip().lower()
    if normalized in _PROVIDER_HUMANIZE_OVERRIDES:
        return _PROVIDER_HUMANIZE_OVERRIDES[normalized]
    return " ".join(
        part.capitalize() for part in re.split(r"[-_]+", normalized) if part
    )


# Marker comments bounding the registry-generated providers table inside the
# hand-maintained docs page at ``details/index.html``. The text between these
# markers is fully regenerated from ``DEEP_RESEARCH_PROVIDERS``; everything else
# on the page stays hand-edited.
DETAILS_PROVIDER_BLOCK_BEGIN = (
    "<!-- BEGIN GENERATED: deep-research-providers "
    "(regenerate with `just gen-provider-docs`) -->"
)
DETAILS_PROVIDER_BLOCK_END = "<!-- END GENERATED: deep-research-providers -->"


def render_provider_docs_table(indent: str = " " * 12) -> str:
    """Render the deep-research provider registry as an HTML docs table.

    The table mirrors the provider categories (name, description, and product
    link) shown in the deep-research index legend, so the docs page stays in
    sync with the registry that drives the index. Generated for embedding in
    ``details/index.html`` between the provider block markers.
    """
    inner = indent + "    "
    row_indent = inner + "    "
    cell_indent = row_indent + "    "

    lines = [f"{indent}<table>"]
    lines.append(f"{inner}<thead>")
    lines.append(f"{row_indent}<tr>")
    lines.append(f"{cell_indent}<th>Provider</th>")
    lines.append(f"{cell_indent}<th>What it contributes</th>")
    lines.append(f"{cell_indent}<th>More information</th>")
    lines.append(f"{row_indent}</tr>")
    lines.append(f"{inner}</thead>")
    lines.append(f"{inner}<tbody>")

    for entry in DEEP_RESEARCH_PROVIDERS:
        name = html.escape(entry["name"])
        prefix = html.escape(entry["prefix"])
        description = html.escape(entry["description"])
        if entry["url"]:
            url = html.escape(entry["url"], quote=True)
            link_cell = (
                f'<a href="{url}" target="_blank" '
                f'rel="noopener noreferrer">{name} site</a>'
            )
        else:
            link_cell = "&mdash;"
        lines.append(f"{row_indent}<tr>")
        lines.append(f"{cell_indent}<td>{prefix}{name}</td>")
        lines.append(f"{cell_indent}<td>{description}</td>")
        lines.append(f"{cell_indent}<td>{link_cell}</td>")
        lines.append(f"{row_indent}</tr>")

    lines.append(f"{inner}</tbody>")
    lines.append(f"{indent}</table>")
    return "\n".join(lines)


def update_details_provider_docs(
    details_path: Path = Path("details/index.html"),
) -> Path:
    """Regenerate the provider table in ``details/index.html`` from the registry.

    Replaces the text between the provider block markers with a freshly
    rendered table. Raises if the markers are missing so a malformed docs page
    fails loudly rather than silently skipping the update.
    """
    text = details_path.read_text()

    begin_idx = text.find(DETAILS_PROVIDER_BLOCK_BEGIN)
    end_idx = text.find(DETAILS_PROVIDER_BLOCK_END)
    if begin_idx == -1 or end_idx == -1 or end_idx < begin_idx:
        raise SystemExit(
            f"Provider block markers not found in {details_path}; expected "
            f"{DETAILS_PROVIDER_BLOCK_BEGIN!r} ... {DETAILS_PROVIDER_BLOCK_END!r}"
        )

    # Preserve the indentation that precedes the begin marker for the table body.
    line_start = text.rfind("\n", 0, begin_idx) + 1
    indent = text[line_start:begin_idx]

    table = render_provider_docs_table(indent=indent)
    block = (
        f"{DETAILS_PROVIDER_BLOCK_BEGIN}\n"
        f"{table}\n"
        f"{indent}{DETAILS_PROVIDER_BLOCK_END}"
    )

    new_text = (
        text[:begin_idx]
        + block
        + text[end_idx + len(DETAILS_PROVIDER_BLOCK_END):]
    )
    details_path.write_text(new_text)
    return details_path


def _rebase_relative_html_urls(html_doc: str, base_prefix: str) -> str:
    """Prefix relative src/href URLs so embedded report assets resolve from the page."""
    if not html_doc or base_prefix in {"", "."}:
        return html_doc

    def _replace(match: re.Match[str]) -> str:
        url = match.group("url")
        if re.match(r"^(?:[a-z][a-z0-9+.-]*:|/|#|\?)", url, re.IGNORECASE):
            return match.group(0)
        rebased = f"{base_prefix.rstrip('/')}/{url.lstrip('./')}"
        return (
            f"{match.group('attr')}={match.group('quote')}"
            f"{rebased}{match.group('quote')}"
        )

    return _RELATIVE_URL_ATTR_PATTERN.sub(_replace, html_doc)


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
    _annotate_hypothesis_group_links(disorder)
    semantic_ref_index = _build_semantic_ref_index(disorder)

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
    env.filters["semantic_ref_href"] = (
        lambda ref: semantic_ref_index.get(str(ref), "") if ref is not None else ""
    )
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
    _annotate_hypothesis_research_links(disorder, hypothesis_research_links)

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

    html = _strip_line_end_whitespace(
        template.render(
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


def _display_name_from_slug(slug: str) -> str:
    """Convert a disorder slug-like token to a human-readable label."""
    return re.sub(r"\s+", " ", slug.replace("_", " ")).strip()


def _display_name_from_provider(provider: str) -> str:
    """Normalize provider token to canonical deep-research browser categories."""
    provider_key = _normalize_provider_key(provider)
    return _PROVIDER_CATEGORY_BY_MATCH_KEY.get(
        provider_key, _PROVIDER_FALLBACK_CATEGORY
    )


_RESEARCH_REPORT_PATTERN = re.compile(
    r"^(?P<slug>.+)-deep-research-(?P<provider>[^.]+)\.md$",
    re.IGNORECASE,
)


def _research_report_output_name(report_path: Path) -> str:
    """Per-report HTML filename, e.g. ``Asthma-deep-research-falcon.md`` -> ``Asthma-falcon.html``."""
    return f"{report_path.stem.replace('-deep-research-', '-', 1)}.html"


def _format_report_date(value: object) -> str | None:
    """Reduce a report timestamp to a bare ``YYYY-MM-DD`` date, dropping the time."""
    if value is None:
        return None
    if isinstance(value, datetime.datetime):
        return value.date().isoformat()
    if isinstance(value, datetime.date):
        return value.isoformat()
    text = str(value).strip()
    if not text:
        return None
    # Split off any time component (ISO "T" separator or a plain space).
    date_part = re.split(r"[T ]", text, maxsplit=1)[0]
    return date_part or None


def _scan_research_reports(
    research_dir: Path,
    disorders_dir: Path,
) -> list[dict]:
    """Scan the research directory and return one metadata dict per deep-research report.

    Shared by both the index (aggregated per disorder) and the per-report pages,
    so the two views stay in lock-step. The report body is *not* rendered here —
    that is done lazily at report-page render time to avoid parsing every markdown
    file when only the index is needed.
    """
    if not research_dir.exists():
        return []

    _, disorder_pages_by_name = _build_disorder_page_index(str(disorders_dir.resolve()))

    disorder_meta_by_filename: dict[str, dict] = {}
    for yaml_path in sorted(disorders_dir.glob("*.yaml")):
        if yaml_path.name.endswith(".history.yaml"):
            continue
        disorder = load_disorder(yaml_path) or {}
        disorder_name = disorder.get("name") or yaml_path.stem
        disorder_meta_by_filename[f"{slugify(str(disorder_name))}.html"] = {
            "name": str(disorder_name),
            "mondo_id": _extract_disorder_term_id(disorder),
        }

    reports: list[dict] = []
    for report_path in sorted(research_dir.glob("*.md")):
        match = _RESEARCH_REPORT_PATTERN.match(report_path.name)
        if not match:
            continue

        slug = match.group("slug")
        provider_raw = match.group("provider")
        category = _display_name_from_provider(provider_raw)
        key = _normalize_provider_key(category)
        lookup = _normalize_disorder_lookup(_display_name_from_slug(slug))
        page_filename = disorder_pages_by_name.get(lookup)
        meta = disorder_meta_by_filename.get(page_filename) if page_filename else None

        reports.append(
            {
                "path": report_path,
                "slug": slug,
                "provider_raw": provider_raw,
                "provider_category": category,
                "provider_key": key,
                "provider_label": _humanize_provider(provider_raw) or category,
                "prefix": _PROVIDER_PREFIX_BY_KEY.get(key, ""),
                "disorder_name": (
                    meta["name"] if meta else _display_name_from_slug(slug)
                ),
                "disorder_page_filename": page_filename,
                "disorder_page_href": (
                    f"../disorders/{page_filename}#literature-summaries"
                    if page_filename
                    else None
                ),
                "mondo_id": meta["mondo_id"] if meta else None,
                "output_name": _research_report_output_name(report_path),
                "row_key": page_filename or slug,
            }
        )

    reports.sort(
        key=lambda report: (
            str(report["disorder_name"]).casefold(),
            str(report["provider_label"]).casefold(),
            report["path"].name.casefold(),
        )
    )
    return reports


def _index_rows_from_reports(reports: list[dict]) -> list[dict]:
    """Aggregate scanned reports into one index row per disorder."""
    rows: dict[str, dict] = {}
    for report in reports:
        row_key = report["row_key"]
        if row_key not in rows:
            rows[row_key] = {
                "name": report["disorder_name"],
                "mondo_id": report["mondo_id"],
                "href": report["disorder_page_href"],
                "report_count": 0,
                "provider_counts": defaultdict(int),
                "reports": [],
            }
        row = rows[row_key]
        row["report_count"] += 1
        row["provider_counts"][report["provider_category"]] += 1
        row["reports"].append(
            {
                "label": report["provider_label"],
                "key": report["provider_key"],
                "prefix": report["prefix"],
                "href": report["output_name"],
                "category": report["provider_category"],
            }
        )

    normalized_rows: list[dict] = []
    for row in rows.values():
        providers = []
        for provider_name, count in sorted(
            row["provider_counts"].items(),
            key=lambda item: item[0].casefold(),
        ):
            key = _normalize_provider_key(provider_name)
            providers.append(
                {
                    "name": provider_name,
                    "key": key,
                    "count": count,
                    "prefix": _PROVIDER_PREFIX_BY_KEY.get(key, ""),
                }
            )
        report_links = sorted(
            row["reports"],
            key=lambda item: str(item.get("label") or "").casefold(),
        )
        normalized_rows.append(
            {
                "name": row["name"],
                "mondo_id": row["mondo_id"],
                "href": row["href"],
                "report_count": row["report_count"],
                "provider_count": len(providers),
                "providers": providers,
                "reports": report_links,
            }
        )

    normalized_rows.sort(key=lambda row: str(row.get("name") or "").casefold())
    return normalized_rows


def _collect_research_index_rows(
    research_dir: Path,
    disorders_dir: Path,
) -> list[dict]:
    """Collect report-count and provider metadata per disorder for index rendering."""
    return _index_rows_from_reports(_scan_research_reports(research_dir, disorders_dir))


def render_research_index(
    rows: list[dict],
    output_path: Path = Path("pages/research/index.html"),
) -> Path:
    """Render the deep-research disorder index page."""
    template_dir = Path(__file__).parent / "templates"
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(["html", "j2"]),
    )
    template = env.get_template("research_index.html.j2")

    provider_options = [
        {"key": entry["key"], "name": entry["name"]}
        for entry in DEEP_RESEARCH_PROVIDERS
    ]

    total_reports = sum(int(row.get("report_count") or 0) for row in rows)
    html = template.render(
        disorders=rows,
        disorder_count=len(rows),
        total_reports=total_reports,
        provider_options=provider_options,
        provider_registry=DEEP_RESEARCH_PROVIDERS,
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html)
    return output_path


def render_research_report(
    report: dict,
    siblings: list[dict],
    prev_report: dict | None,
    next_report: dict | None,
    output_dir: Path = Path("pages/research"),
) -> Path:
    """Render a single deep-research markdown report to a standalone HTML page."""
    template_dir = Path(__file__).parent / "templates"
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(["html", "j2"]),
    )
    template = env.get_template("research_report.html.j2")

    report_path: Path = report["path"]
    metadata, body = _extract_literature_body(report_path.read_text())

    md = markdown_lib.Markdown(extensions=["tables", "fenced_code"])
    body_html = md.convert(body) if body else ""
    base_prefix = os.path.relpath(
        report_path.parent.resolve(), output_dir.resolve()
    )
    body_html = _rebase_relative_html_urls(body_html, base_prefix)

    subtitle = _extract_display_title(body, "")
    if subtitle.casefold() in {"", "disorder", str(report["disorder_name"]).casefold()}:
        subtitle = None

    context = dict(report)
    context.update(
        {
            "subtitle": subtitle,
            "body_html": body_html,
            "model": metadata.get("model"),
            "citation_count": metadata.get("citation_count"),
            "date": _format_report_date(
                metadata.get("end_time") or metadata.get("start_time")
            ),
            "source_url": _github_blob_url(Path("research") / report_path.name),
        }
    )

    html = template.render(
        report=context,
        siblings=siblings,
        prev_report=prev_report,
        next_report=next_report,
        provider_registry=DEEP_RESEARCH_PROVIDERS,
    )

    output_path = output_dir / report["output_name"]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html)
    return output_path


def render_all_research_reports(
    reports: list[dict],
    output_dir: Path = Path("pages/research"),
) -> list[Path]:
    """Render standalone HTML pages for every scanned deep-research report."""
    siblings_by_row: dict[str, list[dict]] = defaultdict(list)
    for report in reports:
        siblings_by_row[report["row_key"]].append(report)

    output_paths: list[Path] = []
    for index, report in enumerate(reports):
        prev_report = reports[index - 1] if index > 0 else None
        next_report = reports[index + 1] if index + 1 < len(reports) else None
        output_paths.append(
            render_research_report(
                report,
                siblings=siblings_by_row[report["row_key"]],
                prev_report=prev_report,
                next_report=next_report,
                output_dir=output_dir,
            )
        )
    return output_paths


def render_research_index_page(
    research_dir: Path = Path("research"),
    disorders_dir: Path = Path("kb/disorders"),
    output_path: Path = Path("pages/research/index.html"),
) -> Path:
    """Collect and render the browsable index plus every per-report page."""
    reports = _scan_research_reports(research_dir, disorders_dir)
    rows = _index_rows_from_reports(reports)
    rendered_path = render_research_index(rows, output_path)
    report_pages = render_all_research_reports(reports, output_dir=output_path.parent)
    print(
        f"Rendered research index -> {rendered_path} "
        f"({len(report_pages)} per-report pages)"
    )
    return rendered_path


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
    disorders_dir = input_dir.parent / "disorders"
    _, disorder_pages_by_name = _build_disorder_page_index(str(disorders_dir.resolve()))

    yaml_files = sorted(input_dir.glob("*.yaml"))
    output_files = []
    comorbidity_summaries: list[dict] = []
    for yaml_path in yaml_files:
        output_path = output_dir / f"{yaml_path.stem}.html"
        render_comorbidity(yaml_path, output_path, template_path)
        output_files.append(output_path)
        comorbidity_summaries.append(
            _build_comorbidity_summary(yaml_path, disorder_pages_by_name)
        )
        print(f"Rendered comorbidity: {yaml_path.stem} -> {output_path}")

    index_path = render_comorbidity_index(
        comorbidity_summaries, output_dir / "index.html"
    )
    output_files.append(index_path)
    print(f"Rendered comorbidity index -> {index_path}")
    return output_files


# --------------------------------------------------------------------------- #
# Disease groupings
# --------------------------------------------------------------------------- #

EXACT_MATCH = "skos:exactMatch"


def load_grouping(yaml_path: Path) -> dict:
    """Load a grouping YAML file."""
    return yaml.safe_load(yaml_path.read_text()) or {}


def _term_chip(descriptor: dict | None) -> dict | None:
    """Build a {label, id, url} chip from a descriptor's ontology term."""
    if not isinstance(descriptor, dict):
        return None
    term = descriptor.get("term")
    if not isinstance(term, dict) or not term.get("id"):
        return None
    label = descriptor.get("preferred_term") or term.get("label") or term.get("id")
    return {"label": label, "id": term.get("id"), "url": curie_to_url(term.get("id"))}


def _module_href(module_ref: str | None) -> dict | None:
    """Build a {stem, node, href} link for a module reference (with #anchor)."""
    if not module_ref:
        return None
    stem, _, node = module_ref.partition("#")
    stem = stem.strip()
    node = node.strip()
    if not stem:
        return None
    return {"stem": stem, "node": node, "href": f"../modules/{stem}.html"}


def _logic_view(node: dict | None) -> dict | None:
    """Build a template-friendly recursive view of a LogicalCriterion node."""
    if not isinstance(node, dict):
        return None
    from .groupings import NodeKind, classify_node

    kind = classify_node(node)
    view: dict = {
        "kind": kind.value,
        "description": node.get("description"),
        "negated": bool(node.get("negated")),
    }
    if kind is NodeKind.BRANCH:
        view["operator"] = node.get("operator")
        view["operands"] = [
            v for v in (_logic_view(child) for child in node.get("operands") or []) if v
        ]
    else:
        view["predicate"] = node.get("criterion_predicate")
        view["min_frequency"] = node.get("min_frequency")
        view["module"] = _module_href(node.get("module"))
        chips: list[dict] = []
        for slot in ("phenotype_term", "gene"):
            chip = _term_chip(node.get(slot))
            if chip:
                chips.append(chip)
        for bp in node.get("biological_processes") or []:
            chip = _term_chip(bp)
            if chip:
                chips.append(chip)
        view["terms"] = chips
    return view


def _resolve_member_href(member: dict, by_name: dict[str, str]) -> str | None:
    """Resolve a grouping member to its page href."""
    mtype = member.get("member_type", "DISEASE")
    ref = member.get("member")
    if not ref:
        return None
    if mtype in ("DISEASE", "SUBTYPE"):
        page = by_name.get(_normalize_disorder_lookup(ref))
        return f"../disorders/{page}" if page else None
    if mtype == "MODULE":
        return f"../modules/{ref.split('#', 1)[0].strip()}.html"
    if mtype == "GROUPING":
        return f"{slugify(ref)}.html"
    return None


def _grouping_mondo_mappings(grouping: dict) -> list[dict]:
    """Return template-friendly MONDO mappings declared by a grouping."""
    out: list[dict] = []
    mappings = (grouping.get("mappings") or {}).get("mondo_mappings") or []
    for mapping in mappings:
        if not isinstance(mapping, dict):
            continue
        term = mapping.get("term") or {}
        if not isinstance(term, dict):
            continue
        term_id = term.get("id")
        if not isinstance(term_id, str) or not term_id.startswith("MONDO:"):
            continue
        predicate = mapping.get("mapping_predicate") or ""
        out.append(
            {
                "id": term_id,
                "label": term.get("label") or term_id,
                "predicate": predicate,
                "source": mapping.get("mapping_source"),
                "url": curie_to_url(term_id),
                "is_exact": predicate == EXACT_MATCH,
            }
        )
    return out


def _leaf_term_ids(node: dict) -> list[str]:
    """Collect compact term ids for a criterion leaf."""
    ids: list[str] = []
    for slot in ("phenotype_term", "gene"):
        chip = _term_chip(node.get(slot))
        if chip:
            ids.append(chip["id"])
    for bp in node.get("biological_processes") or []:
        chip = _term_chip(bp)
        if chip:
            ids.append(chip["id"])
    return ids


def _grouping_criteria_columns(grouping: dict) -> list[dict]:
    """Flatten criteria leaves into table columns."""
    try:
        from .groupings import NodeKind, classify_node, iter_nodes
    except Exception:
        return []

    columns: list[dict] = []
    for ci, criteria in enumerate(grouping.get("membership_criteria") or []):
        logic = criteria.get("logic")
        if logic is None:
            continue
        leaf_index = 0
        for node in iter_nodes(logic):
            if classify_node(node) is not NodeKind.LEAF:
                continue
            description = node.get("description") or node.get(
                "criterion_predicate", "criterion"
            )
            term_ids = _leaf_term_ids(node)
            columns.append(
                {
                    "key": f"{ci}:{leaf_index}",
                    "short_label": f"C{ci + 1}.{leaf_index + 1}",
                    "label": description,
                    "predicate": node.get("criterion_predicate"),
                    "semantics": criteria.get("criteria_semantics"),
                    "term_ids": term_ids,
                    "title": " | ".join(
                        part
                        for part in (
                            criteria.get("criteria_semantics"),
                            node.get("criterion_predicate"),
                            description,
                            ", ".join(term_ids),
                        )
                        if part
                    ),
                }
            )
            leaf_index += 1
    return columns


def _primary_mondo_term(disorder: dict) -> dict | None:
    disease_term = disorder.get("disease_term")
    if not isinstance(disease_term, dict):
        return None
    term = disease_term.get("term")
    if not isinstance(term, dict):
        return None
    term_id = term.get("id")
    if not isinstance(term_id, str) or not term_id.startswith("MONDO:"):
        return None
    return {
        "id": term_id,
        "label": disease_term.get("preferred_term") or term.get("label") or term_id,
        "url": curie_to_url(term_id),
    }


def _top_level_mondo_mapping_terms(disorder: dict) -> list[dict]:
    terms: list[dict] = []
    mappings = (disorder.get("mappings") or {}).get("mondo_mappings") or []
    for mapping in mappings:
        if not isinstance(mapping, dict):
            continue
        term = mapping.get("term") or {}
        if not isinstance(term, dict):
            continue
        term_id = term.get("id")
        if not isinstance(term_id, str) or not term_id.startswith("MONDO:"):
            continue
        terms.append(
            {
                "id": term_id,
                "label": term.get("label") or term_id,
                "url": curie_to_url(term_id),
            }
        )
    return terms


@lru_cache(maxsize=8)
def _build_grouping_disorder_context(disorders_dir: str) -> dict:
    """Parse disorders once for all indexes needed by grouping rendering."""
    try:
        from .groupings import extract_disease_facts
    except Exception:
        extract_disease_facts = None

    root = Path(disorders_dir)
    page_by_name_candidates: dict[str, set[str]] = defaultdict(set)
    identity_by_name: dict[str, dict] = {}
    by_mondo: dict[str, list[dict]] = defaultdict(list)
    disease_index: dict[str, object] = {}

    for disorder_path in sorted(root.glob("*.yaml")):
        if disorder_path.name.endswith(".history.yaml"):
            continue
        try:
            disorder = load_disorder(disorder_path) or {}
        except Exception:
            continue
        name = disorder.get("name") or disorder_path.stem
        name = str(name)
        display_name = disorder.get("display_name")
        page_filename = f"{slugify(name)}.html"
        href = f"../disorders/{page_filename}"

        for candidate in (name, disorder_path.stem):
            lookup_key = _normalize_disorder_lookup(
                str(candidate) if candidate else None
            )
            if lookup_key:
                page_by_name_candidates[lookup_key].add(page_filename)

        primary = _primary_mondo_term(disorder)
        identity_terms = (
            [primary] if primary else _top_level_mondo_mapping_terms(disorder)
        )
        entry = {
            "name": name,
            "display_name": display_name,
            "href": href,
            "mondo_terms": [t for t in identity_terms if t],
        }
        identity_by_name[_normalize_disorder_lookup(name)] = entry
        for term in entry["mondo_terms"]:
            by_mondo[term["id"]].append(entry)

        if extract_disease_facts is not None and disorder.get("name"):
            disease_index[name] = extract_disease_facts(name, disorder)

    page_by_name = {
        lookup_key: next(iter(page_names))
        for lookup_key, page_names in page_by_name_candidates.items()
        if len(page_names) == 1
    }
    return {
        "page_by_name": page_by_name,
        "identity_by_name": identity_by_name,
        "by_mondo": dict(by_mondo),
        "disease_index": disease_index,
    }


def _mondo_term(term_id: str, label: str | None = None) -> dict:
    return {
        "id": term_id,
        "label": label or term_id,
        "url": curie_to_url(term_id),
    }


@lru_cache(maxsize=256)
def _cached_mondo_descendants(term_id: str) -> tuple[str, ...]:
    adapter = _get_oak_adapter("sqlite:obo:mondo")
    if adapter is None:
        return ()
    try:
        from oaklib.datamodels.vocabulary import IS_A

        return tuple(
            sorted(
                d
                for d in adapter.descendants([term_id], predicates=[IS_A])
                if isinstance(d, str) and d.startswith("MONDO:") and d != term_id
            )
        )
    except Exception:
        return ()


@lru_cache(maxsize=2048)
def _cached_mondo_label(term_id: str) -> str:
    adapter = _get_oak_adapter("sqlite:obo:mondo")
    if adapter is None:
        return term_id
    try:
        return adapter.label(term_id) or term_id
    except Exception:
        return term_id


def _exact_mondo_descendant_terms(
    root_ids: list[str], by_mondo: dict[str, list[dict]]
) -> tuple[dict[str, dict], set[str], set[str], str | None]:
    """Fetch visible exact-MONDO descendant terms for coverage rows.

    Descendants under an already-covered DisMech MONDO class are suppressed as
    finer ontology splits of a curated entry, matching the standalone gap report.
    """
    if not root_ids:
        return {}, set(), set(), None

    adapter = _get_oak_adapter("sqlite:obo:mondo")
    if adapter is None:
        return {}, set(), set(), "MONDO descendant lookup unavailable."

    descendant_terms: dict[str, dict] = {}
    exact_scope_ids: set[str] = set(root_ids)
    shadowed_ids: set[str] = set()
    covered_ids = set(by_mondo)

    try:
        for root_id in root_ids:
            descendants = set(_cached_mondo_descendants(root_id))
            exact_scope_ids.update(descendants)
            covered_descendants = descendants & covered_ids
            for covered_id in covered_descendants:
                shadowed_ids.update(_cached_mondo_descendants(covered_id))
            for term_id in sorted(descendants):
                if term_id in shadowed_ids and term_id not in covered_ids:
                    continue
                descendant_terms[term_id] = _mondo_term(
                    term_id, _cached_mondo_label(term_id)
                )
    except Exception:
        return {}, set(root_ids), set(), "MONDO descendant lookup failed."

    return descendant_terms, exact_scope_ids, shadowed_ids, None


def _coverage_criteria_cells(
    names: list[str],
    criteria_columns: list[dict],
    audit: dict[str, list[dict]],
) -> list[dict]:
    """Build criteria cells for one coverage row across one or more entries."""
    order = {"NOT_SATISFIED": 0, "UNKNOWN": 1, "SATISFIED": 2}
    by_key: dict[str, list[dict]] = defaultdict(list)
    for name in names:
        for audit_entry in audit.get(name, []):
            for leaf in audit_entry.get("leaves", []):
                by_key[leaf["key"]].append(
                    {
                        "entry": name,
                        "result": leaf["result"],
                        "description": leaf["description"],
                    }
                )

    cells: list[dict] = []
    for column in criteria_columns:
        entries = by_key.get(column["key"], [])
        if not entries:
            cells.append({"result": "", "label": "", "title": column["title"]})
            continue
        worst = min(entries, key=lambda e: order.get(e["result"], 1))
        results = sorted({e["result"] for e in entries})
        title = "; ".join(
            f"{e['entry']}: {e['result'].replace('_', ' ').lower()}" for e in entries
        )
        cells.append(
            {
                "result": worst["result"],
                "label": "mixed" if len(results) > 1 else worst["result"],
                "title": title or column["title"],
            }
        )
    return cells


def _mondo_scope_state(row: dict, exact_scope_ids: set[str]) -> dict:
    """Describe whether this row falls inside the grouping's exact MONDO scope."""
    if not exact_scope_ids:
        return {
            "value": "not_assessed",
            "label": "not assessed",
            "class": "na",
            "title": "No exact MONDO grouping mapping is declared.",
        }
    if row["mondo"] is None:
        return {
            "value": "no_mondo",
            "label": "no MONDO ID",
            "class": "no",
            "title": "This DisMech row has no MONDO identity to test.",
        }
    if row["mondo"]["id"] in exact_scope_ids:
        return {
            "value": "yes",
            "label": "yes",
            "class": "yes",
            "title": "This MONDO concept is the exact grouping term or an is-a descendant.",
        }
    return {
        "value": "no",
        "label": "no",
        "class": "no",
        "title": "This MONDO concept is outside the exact grouping MONDO scope.",
    }


def _coverage_status(row: dict, exact_scope_ids: set[str]) -> tuple[str, str]:
    has_dismech = bool(row["dismech_entries"])
    has_mondo = row["mondo"] is not None
    is_listed = any(e["member_state"] == "listed" for e in row["dismech_entries"])
    is_candidate = any(e["member_state"] == "candidate" for e in row["dismech_entries"])
    is_not_listed = any(
        e["member_state"] == "not_listed" for e in row["dismech_entries"]
    )
    mondo_id = row["mondo"]["id"] if row["mondo"] else None
    has_exact_scope = bool(exact_scope_ids)

    if (
        has_exact_scope
        and has_dismech
        and has_mondo
        and mondo_id not in exact_scope_ids
    ):
        if is_listed:
            return "outside_scope", "listed outside grouping MONDO"
        if is_candidate:
            return "outside_scope", "candidate outside grouping MONDO"
        if is_not_listed:
            return "outside_scope", "DisMech outside grouping MONDO"
        return "outside_scope", "outside grouping MONDO"
    if has_dismech and has_mondo and is_listed:
        if has_exact_scope:
            return "mapped", "listed in scope"
        return "mapped", "listed with MONDO ID"
    if has_dismech and has_mondo and is_candidate:
        if has_exact_scope:
            return "candidate", "candidate in scope"
        return "candidate", "DisMech candidate"
    if has_dismech and has_mondo and is_not_listed:
        if has_exact_scope:
            return "not_listed", "DisMech not listed"
        return "not_listed", "not listed, MONDO ID"
    if has_dismech and not has_mondo:
        return "dismech_only", "DisMech only"
    if has_mondo:
        return "mondo_gap", "MONDO gap"
    return "dismech_only", "DisMech only"


def _build_grouping_coverage_rows(
    grouping: dict,
    *,
    audit: dict[str, list[dict]],
    candidates: list[dict],
    criteria_columns: list[dict],
    identity_by_name: dict[str, dict],
    by_mondo: dict[str, list[dict]],
) -> tuple[list[dict], dict]:
    """Build a unified DisMech/MONDO coverage table for a grouping page."""
    mondo_mappings = _grouping_mondo_mappings(grouping)
    exact_roots = [m["id"] for m in mondo_mappings if m["is_exact"]]
    descendant_terms, exact_scope_ids, shadowed_ids, note = (
        _exact_mondo_descendant_terms(exact_roots, by_mondo)
    )

    listed_names = {
        m.get("member")
        for m in grouping.get("members") or []
        if isinstance(m, dict) and m.get("member")
    }
    candidate_names = {c["name"] for c in candidates if c.get("name")}

    member_by_name = {
        m.get("member"): m
        for m in grouping.get("members") or []
        if isinstance(m, dict) and m.get("member")
    }
    rows: dict[str, dict] = {}

    def ensure_row(key: str) -> dict:
        return rows.setdefault(
            key,
            {
                "key": key,
                "mondo": None,
                "dismech_entries": [],
                "criteria_cells": [],
                "status": "",
                "status_label": "",
                "is_leaf_gap": False,
            },
        )

    def add_mondo(term: dict) -> dict:
        row = ensure_row(f"mondo:{term['id']}")
        row["mondo"] = term
        return row

    def add_dismech(row: dict, entry: dict, member: dict | None = None) -> None:
        name = entry["name"]
        if any(existing["name"] == name for existing in row["dismech_entries"]):
            return
        if name in listed_names:
            state = "listed"
        elif name in candidate_names:
            state = "candidate"
        else:
            state = "not_listed"
        row["dismech_entries"].append(
            {
                "name": name,
                "display_name": entry.get("display_name") or name,
                "href": entry.get("href"),
                "member_state": state,
                "member_type": (member or {}).get("member_type", "DISEASE"),
                "mechanisms": (member or {}).get("differentiating_mechanisms") or [],
            }
        )

    # Add exact-root descendants first, collapsed with any DisMech entry that
    # declares the same primary identity MONDO id.
    for term_id, term in sorted(
        descendant_terms.items(), key=lambda item: item[1]["label"]
    ):
        row = add_mondo(term)
        for entry in by_mondo.get(term_id, []):
            add_dismech(row, entry, member_by_name.get(entry["name"]))

    # Add exact roots themselves when a DisMech entry maps directly to the root.
    # For inexact mappings, the mapping target is diagnostic/provenance context,
    # not a scope whose DisMech entries should be pulled into this table.
    for mapping in mondo_mappings:
        if not mapping["is_exact"]:
            continue
        term = _mondo_term(mapping["id"], mapping["label"])
        for entry in by_mondo.get(mapping["id"], []):
            row = add_mondo(term)
            add_dismech(row, entry, member_by_name.get(entry["name"]))

    # Add all listed members and advisory candidates, including DisMech-only or
    # outside-MONDO-scope rows.
    for name in sorted(listed_names | candidate_names):
        entry = identity_by_name.get(_normalize_disorder_lookup(name))
        if entry is None:
            entry = {
                "name": name,
                "display_name": name,
                "href": None,
                "mondo_terms": [],
            }
        terms = entry.get("mondo_terms") or []
        if terms:
            for term in terms:
                if term["id"] in exact_scope_ids:
                    row = add_mondo(term)
                else:
                    row = ensure_row(
                        f"dismech:{_normalize_disorder_lookup(name)}:mondo:{term['id']}"
                    )
                    row["mondo"] = term
                add_dismech(row, entry, member_by_name.get(name))
        else:
            row = ensure_row(f"dismech:{_normalize_disorder_lookup(name)}")
            add_dismech(row, entry, member_by_name.get(name))

    # Add criteria results and status labels.
    for row in rows.values():
        names = [entry["name"] for entry in row["dismech_entries"]]
        row["criteria_cells"] = _coverage_criteria_cells(names, criteria_columns, audit)
        row["mondo_scope"] = _mondo_scope_state(row, exact_scope_ids)
        status, status_label = _coverage_status(row, exact_scope_ids)
        row["status"] = status
        row["status_label"] = status_label

    status_order = {
        "mapped": 0,
        "candidate": 1,
        "not_listed": 2,
        "mondo_gap": 3,
        "outside_scope": 4,
        "dismech_only": 5,
    }
    sorted_rows = sorted(
        rows.values(),
        key=lambda row: (
            status_order.get(row["status"], 99),
            (row["mondo"] or {}).get("label")
            or ", ".join(e["display_name"] for e in row["dismech_entries"]),
        ),
    )
    scope_rows = [row for row in sorted_rows if row["mondo_scope"]["value"] == "yes"]
    scope_listed = sum(
        1
        for row in scope_rows
        if any(entry["member_state"] == "listed" for entry in row["dismech_entries"])
    )
    scope_dismech = sum(1 for row in scope_rows if row["dismech_entries"])
    scope_total = len(scope_rows)
    scope_percent = (
        round((scope_listed / scope_total) * 100, 1) if scope_total else None
    )
    coverage = {
        "note": note,
        "exact_roots": [m for m in mondo_mappings if m["is_exact"]],
        "shadowed_count": len(shadowed_ids - set(descendant_terms)),
        "completeness": {
            "available": bool(exact_roots and scope_total),
            "covered": scope_listed,
            "dismech_covered": scope_dismech,
            "total": scope_total,
            "percent": scope_percent,
            "label": (
                f"{scope_listed}/{scope_total} ({scope_percent:.1f}%)"
                if scope_percent is not None
                else None
            ),
        },
        "counts": {
            "rows": len(sorted_rows),
            "mapped": sum(1 for r in sorted_rows if r["status"] == "mapped"),
            "mondo_gap": sum(1 for r in sorted_rows if r["status"] == "mondo_gap"),
            "not_listed": sum(1 for r in sorted_rows if r["status"] == "not_listed"),
            "dismech_only": sum(
                1
                for r in sorted_rows
                if r["status"] in {"dismech_only", "outside_scope"}
            ),
        },
    }
    return sorted_rows, coverage


def _annotate_grouping(
    grouping: dict,
    *,
    disorders_dir: Path = Path("kb/disorders"),
) -> dict:
    """Decorate a grouping with member hrefs, criteria views, and an advisory
    membership audit, returning summary metadata used by the page templates."""
    disorder_context = _build_grouping_disorder_context(str(disorders_dir.resolve()))
    by_name = disorder_context["page_by_name"]
    mondo_mappings = _grouping_mondo_mappings(grouping)
    criteria_columns = _grouping_criteria_columns(grouping)

    # Criteria views (recursive logic trees).
    for criteria in grouping.get("membership_criteria") or []:
        criteria["_logic_view"] = _logic_view(criteria.get("logic"))

    # Member hrefs + differentiating-mechanism chips.
    for member in grouping.get("members") or []:
        member["_href"] = _resolve_member_href(member, by_name)
        for mech in member.get("differentiating_mechanisms") or []:
            chips = []
            for slot in ("gene", "phenotype_term"):
                chip = _term_chip(mech.get(slot))
                if chip:
                    chips.append(chip)
            for bp in mech.get("biological_processes") or []:
                chip = _term_chip(bp)
                if chip:
                    chips.append(chip)
            mech["_chips"] = chips
            mech["_module"] = _module_href(mech.get("module"))

    # Advisory membership audit (never let this break rendering).
    audit: dict[str, list[dict]] = {}
    candidates: list[dict] = []
    try:
        from .groupings import (
            evaluate_grouping,
            find_candidate_members,
        )

        index = disorder_context["disease_index"]
        for ev in evaluate_grouping(grouping, index):
            audit.setdefault(ev.member, []).append(
                {
                    "criteria_index": ev.criteria_index,
                    "semantics": ev.semantics,
                    "result": ev.result.value,
                    "leaves": [
                        {
                            "key": f"{ev.criteria_index}:{leaf_index}",
                            "description": description,
                            "result": result.value,
                        }
                        for leaf_index, (description, result) in enumerate(ev.leaves)
                    ],
                    "unmet": [d for d, r in ev.leaves if r.value != "SATISFIED"],
                }
            )
        for name in find_candidate_members(grouping, index):
            page = by_name.get(_normalize_disorder_lookup(name))
            candidates.append(
                {"name": name, "href": f"../disorders/{page}" if page else None}
            )
    except Exception:
        audit = {}
        candidates = []
    grouping["_audit"] = audit
    grouping["_candidates"] = candidates
    grouping["_mondo_mappings"] = mondo_mappings
    grouping["_criteria_columns"] = criteria_columns
    try:
        coverage_rows, coverage = _build_grouping_coverage_rows(
            grouping,
            audit=audit,
            candidates=candidates,
            criteria_columns=criteria_columns,
            identity_by_name=disorder_context["identity_by_name"],
            by_mondo=disorder_context["by_mondo"],
        )
    except Exception:
        coverage_rows = []
        coverage = {
            "note": "Coverage table could not be built.",
            "exact_roots": [m for m in mondo_mappings if m["is_exact"]],
            "shadowed_count": 0,
            "completeness": {
                "available": False,
                "covered": 0,
                "dismech_covered": 0,
                "total": 0,
                "percent": None,
                "label": None,
            },
            "counts": {
                "rows": 0,
                "mapped": 0,
                "mondo_gap": 0,
                "not_listed": 0,
                "dismech_only": 0,
            },
        }
    grouping["_coverage_rows"] = coverage_rows
    grouping["_coverage"] = coverage

    member_count = len(grouping.get("members") or [])
    child_grouping_names = [
        str(member["member"])
        for member in grouping.get("members") or []
        if member.get("member_type") == "GROUPING" and member.get("member")
    ]
    return {
        "id": slugify(str(grouping.get("name") or "")),
        "name": grouping.get("name"),
        "display_name": grouping.get("display_name"),
        "description": grouping.get("description"),
        "grouping_basis": grouping.get("grouping_basis") or [],
        "mondo_mappings": mondo_mappings,
        "coverage": coverage,
        "member_count": member_count,
        "child_grouping_names": child_grouping_names,
        "criteria_count": len(grouping.get("membership_criteria") or []),
        "candidate_count": len(candidates),
        "href": f"{slugify(str(grouping.get('name') or ''))}.html",
    }


def _render_grouping_document(
    grouping: dict,
    summary: dict,
    yaml_path: Path,
    output_path: Optional[Path] = None,
    template_path: Optional[Path] = None,
) -> Path:
    """Render a loaded and annotated grouping to HTML."""
    yaml_content = yaml_path.read_text()

    if template_path is None:
        template_dir = Path(__file__).parent / "templates"
        template_name = "grouping.html.j2"
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
        f"kb/groupings/{yaml_path.name}"
    )
    html = template.render(
        grouping=grouping,
        summary=summary,
        yaml_content=yaml_content,
        source_file=source_file,
    )

    if output_path is None:
        output_path = Path("pages/groupings") / f"{summary['id']}.html"
    else:
        output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html)
    return output_path


def render_grouping(
    yaml_path: Path,
    output_path: Optional[Path] = None,
    template_path: Optional[Path] = None,
    *,
    disorders_dir: Path = Path("kb/disorders"),
) -> Path:
    """Render a single disease grouping YAML file to HTML."""
    grouping = load_grouping(yaml_path)
    summary = _annotate_grouping(grouping, disorders_dir=disorders_dir)
    return _render_grouping_document(
        grouping, summary, yaml_path, output_path, template_path
    )


def _build_grouping_tree(groupings: list[dict]) -> dict:
    """Build a forest from explicit GROUPING members on grouping summaries."""
    by_name = {str(g.get("name")): g for g in groupings if g.get("name")}
    children_by_parent: dict[str, list[str]] = {}
    parents_by_child: dict[str, list[str]] = defaultdict(list)

    for grouping in groupings:
        parent = grouping.get("name")
        if not parent:
            continue
        parent_name = str(parent)
        children: list[str] = []
        for child in grouping.get("child_grouping_names") or []:
            if child in by_name:
                children.append(child)
                parents_by_child[child].append(parent_name)
        children_by_parent[parent_name] = sorted(children, key=str.casefold)

    names = sorted(by_name, key=str.casefold)
    roots = [name for name in names if not parents_by_child.get(name)]
    if not roots and names:
        roots = names

    def make_node(name: str, stack: tuple[str, ...] = ()) -> dict:
        summary = by_name[name]
        cycle = name in stack
        child_names = [] if cycle else children_by_parent.get(name, [])
        return {
            "name": summary.get("name"),
            "display_name": summary.get("display_name"),
            "href": summary.get("href"),
            "member_count": summary.get("member_count", 0),
            "children": [make_node(child, (*stack, name)) for child in child_names],
            "parent_count": len(parents_by_child.get(name, [])),
            "is_shared": len(parents_by_child.get(name, [])) > 1,
            "cycle": cycle,
        }

    edge_count = sum(len(children) for children in children_by_parent.values())
    nested_count = len(parents_by_child)
    return {
        "roots": [make_node(name) for name in roots],
        "edge_count": edge_count,
        "nested_count": nested_count,
        "root_count": len(roots),
    }


def render_grouping_index(
    groupings: list[dict],
    output_path: Path = Path("pages/groupings/index.html"),
) -> Path:
    """Render the disease-grouping index page."""
    template_dir = Path(__file__).parent / "templates"
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(["html", "j2"]),
    )
    template = env.get_template("grouping_index.html.j2")
    sorted_groupings = sorted(
        groupings, key=lambda g: str(g.get("name") or "").casefold()
    )
    html = template.render(
        groupings=sorted_groupings,
        grouping_tree=_build_grouping_tree(sorted_groupings),
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html)
    return output_path


def render_all_groupings(
    input_dir: Path = Path("kb/groupings"),
    output_dir: Path = Path("pages/groupings"),
    template_path: Optional[Path] = None,
    *,
    disorders_dir: Path = Path("kb/disorders"),
) -> list[Path]:
    """Render all disease groupings plus their index page."""
    if not input_dir.exists():
        return []
    output_dir.mkdir(parents=True, exist_ok=True)

    output_files: list[Path] = []
    summaries: list[dict] = []
    for yaml_path in sorted(input_dir.glob("*.yaml")):
        # Load once per file so the index summary matches the rendered grouping.
        grouping = load_grouping(yaml_path)
        summary = _annotate_grouping(grouping, disorders_dir=disorders_dir)
        output_path = output_dir / summary["href"]
        _render_grouping_document(
            grouping, summary, yaml_path, output_path, template_path
        )
        output_files.append(output_path)
        summaries.append(summary)
        print(f"Rendered grouping: {yaml_path.stem} -> {output_path}")

    index_path = render_grouping_index(summaries, output_dir / "index.html")
    output_files.append(index_path)
    print(f"Rendered grouping index -> {index_path}")
    return output_files


# ---------------------------------------------------------------------------
# Project pages (curation projects under projects/*.md)
# ---------------------------------------------------------------------------

# Frontmatter keys whose values are lists of entities, mapped to the kind of
# local/external page each entity links to.
_PROJECT_ENTITY_KINDS = ("diseases", "modules", "groupings", "drugs", "phenotypes")

_PROJECT_STATUS_LABELS = {
    "PLANNED": "Planned",
    "IN_PROGRESS": "In progress",
    "ACTIVE": "Active",
    "COMPLETE": "Complete",
    "EVERGREEN": "Evergreen",
    "ARCHIVED": "Archived",
}


def _coerce_entity_entry(entry: object) -> dict | None:
    """Normalize a frontmatter entity entry (string slug or mapping) to a dict.

    Returns a dict with at least a ``token`` (the form written in the markdown
    body) plus an optional ``id`` (CURIE) and ``label``.
    """
    if isinstance(entry, str):
        token = entry.strip()
        if not token:
            return None
        return {"token": token, "id": None, "label": _display_name_from_slug(token)}
    if isinstance(entry, dict):
        token = entry.get("slug") or entry.get("name") or entry.get("id")
        token = str(token).strip() if token else ""
        if not token:
            return None
        curie = entry.get("id")
        label = entry.get("label") or entry.get("name") or _display_name_from_slug(token)
        return {
            "token": token,
            "id": str(curie) if curie else None,
            "label": str(label),
            "note": entry.get("note"),
        }
    return None


def _build_groupings_page_index(groupings_dir: Path) -> dict[str, str]:
    """Build a normalized name/stem -> grouping page filename index."""
    index: dict[str, str] = {}
    if not groupings_dir.exists():
        return index
    for grouping_path in sorted(groupings_dir.glob("*.yaml")):
        try:
            grouping = load_grouping(grouping_path) or {}
        except Exception:
            continue
        name = grouping.get("name") or grouping_path.stem
        page = f"{slugify(str(name))}.html"
        for candidate in (name, grouping_path.stem):
            key = _normalize_disorder_lookup(str(candidate) if candidate else None)
            if key:
                index[key] = page
    return index


def _resolve_project_entities(
    metadata: dict,
    *,
    by_name: dict[str, str],
    modules_dir: Path,
    groupings_by_name: dict[str, str],
) -> dict[str, list[dict]]:
    """Resolve frontmatter entity lists into render-ready records with hrefs.

    Disease/module/grouping slugs resolve to local page hrefs (relative to a
    project page in ``pages/projects/``); drugs/phenotypes resolve to external
    ontology browser URLs when an ``id`` CURIE is supplied. ``by_name`` and
    ``groupings_by_name`` are prebuilt page indexes so batch rendering avoids
    re-scanning the (large) disorder corpus per project.
    """
    resolved: dict[str, list[dict]] = {kind: [] for kind in _PROJECT_ENTITY_KINDS}
    for kind in _PROJECT_ENTITY_KINDS:
        for raw in metadata.get(kind, []) or []:
            entry = _coerce_entity_entry(raw)
            if entry is None:
                continue
            href: str | None = None
            local = False
            if kind == "diseases":
                href = _resolve_local_disorder_slug_href(
                    entry["token"], by_name, local_prefix="../disorders/"
                )
                local = href is not None
            elif kind == "modules":
                if (modules_dir / f"{entry['token']}.yaml").exists():
                    href = f"../modules/{entry['token']}.html"
                    local = True
            elif kind == "groupings":
                page = groupings_by_name.get(_normalize_disorder_lookup(entry["token"]))
                if page:
                    href = f"../groupings/{page}"
                    local = True
            if href is None and entry.get("id"):
                external = curie_to_url(entry["id"])
                if external:
                    href = external
            entry["href"] = href
            entry["local"] = local
            entry["unresolved"] = href is None
            resolved[kind].append(entry)
    return resolved


def _autolink_project_body(body: str, link_map: dict[str, tuple[str, str]]) -> str:
    """Wrap declared entity slug tokens in the markdown body with links.

    Only tokens declared in the project frontmatter (and resolving to a page)
    are linked, and only outside fenced/inline code and existing links.
    """
    if not link_map:
        return body

    tokens = sorted(link_map, key=len, reverse=True)
    # Boundaries reject word chars, existing-link/code delimiters, and a
    # trailing "." so filename references (e.g. Lynch_Syndrome.yaml) and anchor
    # paths are left untouched.
    pattern = re.compile(
        r"(?<![\w/\[`#.-])(" + "|".join(re.escape(t) for t in tokens) + r")(?![\w`\]./-])"
    )

    def _sub(match: re.Match) -> str:
        href, label = link_map[match.group(1)]
        return f"[{label}]({href})"

    def _autolink_line(line: str) -> str:
        # Protect inline code spans from substitution.
        parts = re.split(r"(`[^`]*`)", line)
        for index, part in enumerate(parts):
            if part.startswith("`"):
                continue
            parts[index] = pattern.sub(_sub, part)
        return "".join(parts)

    out_lines: list[str] = []
    in_fence = False
    for line in body.split("\n"):
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            out_lines.append(line)
            continue
        out_lines.append(line if in_fence else _autolink_line(line))
    return "\n".join(out_lines)


def _project_summary(
    md_path: Path,
    metadata: dict,
    body: str,
    entities: dict[str, list[dict]],
) -> dict:
    """Build the index-card summary for a single project."""
    title = (
        metadata.get("title")
        or _extract_display_title(body, md_path.stem)
        or _display_name_from_slug(md_path.stem)
    )
    status = str(metadata.get("status") or "").upper()
    counts = {kind: len(entities.get(kind, [])) for kind in _PROJECT_ENTITY_KINDS}
    return {
        "id": md_path.stem,
        "href": f"{md_path.stem}.html",
        "title": title,
        "description": metadata.get("description"),
        "status": status,
        "status_label": _PROJECT_STATUS_LABELS.get(status, status.title() or None),
        "tags": [str(tag) for tag in (metadata.get("tags") or [])],
        "counts": counts,
        "entity_total": sum(counts.values()),
    }


def _render_project_html(
    md_path: Path,
    metadata: dict,
    body: str,
    entities: dict[str, list[dict]],
    output_path: Path,
    template_path: Optional[Path],
) -> Path:
    """Render an already-parsed/resolved project to HTML and write it out.

    Split out so batch rendering can reuse the metadata/body/entities it has
    already computed instead of re-reading and re-resolving each file.
    """
    # Auto-link only entities that resolve to a page (local or external).
    link_map = {
        entry["token"]: (entry["href"], entry["label"])
        for kind in _PROJECT_ENTITY_KINDS
        for entry in entities[kind]
        if entry.get("href")
    }
    linked_body = _autolink_project_body(body, link_map)

    md = markdown_lib.Markdown(extensions=["tables", "fenced_code", "toc", "sane_lists"])
    body_html = md.convert(linked_body)

    summary = _project_summary(md_path, metadata, body, entities)

    if template_path is None:
        template_dir = Path(__file__).parent / "templates"
        template_name = "project.html.j2"
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
        f"projects/{md_path.name}"
    )
    html = template.render(
        project=summary,
        metadata=metadata,
        entities=entities,
        body_html=body_html,
        source_file=source_file,
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html)
    return output_path


def render_project(
    md_path: Path,
    output_path: Optional[Path] = None,
    template_path: Optional[Path] = None,
    *,
    disorders_dir: Path = Path("kb/disorders"),
    modules_dir: Path = Path("kb/modules"),
    groupings_dir: Path = Path("kb/groupings"),
    by_name: dict[str, str] | None = None,
    groupings_by_name: dict[str, str] | None = None,
) -> Path:
    """Render a single curation-project markdown file to an HTML page.

    ``by_name`` (disorder page index) and ``groupings_by_name`` may be passed
    in by batch callers to avoid re-scanning the corpus for every project.
    """
    metadata, body = _split_front_matter(md_path.read_text())

    if by_name is None:
        _, by_name = _build_disorder_page_index(str(disorders_dir.resolve()))
    if groupings_by_name is None:
        groupings_by_name = _build_groupings_page_index(groupings_dir)

    entities = _resolve_project_entities(
        metadata,
        by_name=by_name,
        modules_dir=modules_dir,
        groupings_by_name=groupings_by_name,
    )

    if output_path is None:
        output_path = Path("pages/projects") / f"{md_path.stem}.html"
    else:
        output_path = Path(output_path)
    return _render_project_html(
        md_path, metadata, body, entities, output_path, template_path
    )


def render_project_index(
    projects: list[dict],
    output_path: Path = Path("pages/projects/index.html"),
) -> Path:
    """Render the curation-project index page."""
    template_dir = Path(__file__).parent / "templates"
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(["html", "j2"]),
    )
    template = env.get_template("project_index.html.j2")
    sorted_projects = sorted(
        projects, key=lambda project: str(project.get("title") or "").casefold()
    )
    all_tags = sorted({tag for project in projects for tag in project.get("tags", [])})
    html = template.render(projects=sorted_projects, all_tags=all_tags)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html)
    return output_path


def render_all_projects(
    input_dir: Path = Path("projects"),
    output_dir: Path = Path("pages/projects"),
    template_path: Optional[Path] = None,
    *,
    disorders_dir: Path = Path("kb/disorders"),
    modules_dir: Path = Path("kb/modules"),
    groupings_dir: Path = Path("kb/groupings"),
) -> list[Path]:
    """Render every top-level ``projects/*.md`` page plus the project index."""
    if not input_dir.exists():
        return []
    output_dir.mkdir(parents=True, exist_ok=True)

    # Build the (expensive) page indexes once and reuse for every project so the
    # disorder corpus is scanned a single time, and the index summaries resolve
    # groupings with the same index the per-project pages use.
    _, by_name = _build_disorder_page_index(str(disorders_dir.resolve()))
    groupings_by_name = _build_groupings_page_index(groupings_dir)

    output_files: list[Path] = []
    summaries: list[dict] = []
    for md_path in sorted(input_dir.glob("*.md")):
        # Parse and resolve once, then reuse for both the page and the index
        # summary (no second file read or entity resolution per project).
        metadata, body = _split_front_matter(md_path.read_text())
        entities = _resolve_project_entities(
            metadata,
            by_name=by_name,
            modules_dir=modules_dir,
            groupings_by_name=groupings_by_name,
        )
        output_path = _render_project_html(
            md_path,
            metadata,
            body,
            entities,
            output_dir / f"{md_path.stem}.html",
            template_path,
        )
        summaries.append(_project_summary(md_path, metadata, body, entities))
        output_files.append(output_path)
        print(f"Rendered project: {md_path.stem} -> {output_path}")

    index_path = render_project_index(summaries, output_dir / "index.html")
    output_files.append(index_path)
    print(f"Rendered project index -> {index_path}")
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


def _build_classification_summary(
    enum_name: str,
    enum_info: dict,
    disorders_by_value: dict[str, list[dict]],
) -> dict:
    """Build a compact card payload for the classification index page."""
    unique_disorders = {
        disorder.get("slug"): disorder
        for disorder_list in (disorders_by_value or {}).values()
        for disorder in disorder_list
        if isinstance(disorder, dict) and disorder.get("slug")
    }
    return {
        "enum_name": enum_name,
        "title": enum_info.get("title") or enum_name,
        "description": enum_info.get("description") or "",
        "href": f"{slugify(enum_name)}.html",
        "disorder_count": len(unique_disorders),
    }


def render_classification_index(
    classifications: list[dict],
    output_path: Path = Path("pages/classifications/index.html"),
) -> Path:
    """Render the classification landing page."""
    template_dir = Path(__file__).parent / "templates"
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(["html", "j2"]),
    )
    template = env.get_template("classification_index.html.j2")

    html = template.render(
        classifications=sorted(
            classifications,
            key=lambda classification: str(
                classification.get("title") or classification.get("enum_name") or ""
            ).casefold(),
        )
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html)
    return output_path


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
    classification_summaries: list[dict] = []
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
        classification_summaries.append(
            _build_classification_summary(
                enum_name,
                enum_info,
                disorders_by_enum_value.get(enum_name) or {},
            )
        )

    index_path = render_classification_index(
        classification_summaries,
        output_dir / "index.html",
    )
    output_paths.append(index_path)

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
    render_research_index_page(disorders_dir=input_dir)

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
    parser.add_argument(
        "--grouping", action="store_true", help="Render grouping page(s)"
    )
    parser.add_argument("--research", action="store_true", help="Render research index")
    parser.add_argument(
        "--provider-docs",
        action="store_true",
        help="Regenerate the deep-research provider table in details/index.html",
    )
    parser.add_argument(
        "--project", action="store_true", help="Render curation-project page(s)"
    )
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

    if args.grouping:
        if args.path is None:
            raise SystemExit("Error: --grouping requires a file or directory path")
        input_path = Path(args.path)
        if input_path.is_dir():
            output_dir = Path(args.output) if args.output else Path("pages/groupings")
            render_all_groupings(input_path, output_dir, template_path)
        else:
            output_path = Path(args.output) if args.output else None
            result = render_grouping(input_path, output_path, template_path)
            print(f"Generated: {result}")
        return

    if args.project:
        input_path = Path(args.path) if args.path else Path("projects")
        if input_path.is_dir():
            output_dir = Path(args.output) if args.output else Path("pages/projects")
            render_all_projects(input_path, output_dir, template_path)
        else:
            output_path = Path(args.output) if args.output else None
            result = render_project(input_path, output_path, template_path)
            print(f"Generated: {result}")
        return

    if args.provider_docs:
        details_path = (
            Path(args.path)
            if args.path
            else (Path(args.output) if args.output else Path("details/index.html"))
        )
        result = update_details_provider_docs(details_path)
        print(f"Updated provider docs: {result}")
        return

    if args.research:
        research_dir = Path(args.path) if args.path else Path("research")
        output_path = (
            Path(args.output) if args.output else Path("pages/research/index.html")
        )
        result = render_research_index_page(
            research_dir=research_dir,
            disorders_dir=Path("kb/disorders"),
            output_path=output_path,
        )
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
