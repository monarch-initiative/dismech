"""
Render disorder YAML files to HTML pages using Jinja2 templates.
"""

import json
import re
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
from typing import Callable, Optional

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

from dismech.export.browser_export import HPO_TOP_LEVEL_CATEGORIES
from dismech.graph import build_causal_graph, generate_mermaid

_HPO_CATEGORY_CACHE_PATH = Path('app/hpo_category_cache.json')

# Canonical display order for phenotype categories (matches HPO_TOP_LEVEL_CATEGORIES)
_CATEGORY_ORDER = list(HPO_TOP_LEVEL_CATEGORIES.values())


@lru_cache(maxsize=1)
def _load_hpo_category_cache() -> dict[str, list[str]]:
    """Load the HP-term-to-category cache written by browser_export."""
    if _HPO_CATEGORY_CACHE_PATH.exists():
        return json.loads(_HPO_CATEGORY_CACHE_PATH.read_text())
    return {}


def _group_phenotypes_by_category(phenotypes: list[dict]) -> list[tuple[str, list[dict]]]:
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
    'ICD10CM': {
        'adapter': 'sqlite:obo:icd10cm',
        'root': 'ICD10CM:ICD-10-CM',
        'label': 'ICD-10-CM',
    },
}


@lru_cache(maxsize=1)
def _load_prefix_map() -> dict:
    schema_path = Path(__file__).parent / 'schema' / 'dismech.yaml'
    try:
        prefixes = yaml.safe_load(schema_path.read_text()).get('prefixes', {})
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
        return '#'

    if curie.startswith(('http://', 'https://')):
        return curie

    if ':' not in curie:
        return '#'

    prefix, local_id = curie.split(':', 1)
    prefix_map = _load_prefix_map()
    base = prefix_map.get(prefix)
    if base:
        if '{id}' in base:
            return base.format(id=local_id)
        return f'{base}{local_id}'

    return f'https://bioregistry.io/{curie}'


def slugify(name: str) -> str:
    """Convert a disorder name to a filename-safe slug."""
    return name.replace(' ', '_').replace('/', '_').replace('(', '').replace(')', '')


def _normalize_disorder_lookup(value: str | None) -> str:
    """Normalize disease names/slugs for tolerant internal-link lookup."""
    if not value:
        return ''
    normalized = re.sub(r'[^a-z0-9]+', ' ', str(value).casefold())
    return ' '.join(normalized.split())


def _extract_disorder_term_id(disorder: dict) -> str | None:
    """Extract MONDO/ontology term id from a disorder model if present."""
    disease_term = disorder.get('disease_term')
    if not isinstance(disease_term, dict):
        return None
    term = disease_term.get('term')
    if not isinstance(term, dict):
        return None
    term_id = term.get('id')
    if not term_id:
        return None
    return str(term_id)


def _resolve_local_disorder_href(
    curie: str | None,
    by_term: dict[str, str],
    *,
    local_prefix: str = '',
    excluded_term_ids: set[str] | None = None,
) -> str | None:
    """Resolve MONDO CURIEs to local disorder-page hrefs when available."""
    if not isinstance(curie, str) or not curie:
        return None
    term_id = curie.upper()
    if not term_id.startswith('MONDO:'):
        return None
    if excluded_term_ids and term_id in excluded_term_ids:
        return None
    page_filename = by_term.get(term_id)
    if not page_filename:
        return None
    return f'{local_prefix}{page_filename}'


def _build_dismech_page_url_filter(
    disorders_dir: Path,
    *,
    local_prefix: str = '',
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
    local_prefix: str = '',
) -> str | None:
    """Resolve a disorder slug/name token to a local disorder-page href."""
    if not isinstance(slug, str) or not slug:
        return None
    page_filename = by_name.get(_normalize_disorder_lookup(slug))
    if not page_filename:
        return None
    return f'{local_prefix}{page_filename}'


def _build_dismech_slug_page_url_filter(
    disorders_dir: Path,
    *,
    local_prefix: str = '',
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


@lru_cache(maxsize=8)
def _build_disorder_page_index(disorders_dir: str) -> tuple[dict[str, str], dict[str, str]]:
    """Build indexes for resolving disorder pages by term ID or name."""
    root = Path(disorders_dir)
    by_term_candidates: dict[str, set[str]] = defaultdict(set)
    by_name_candidates: dict[str, set[str]] = defaultdict(set)

    for disorder_path in sorted(root.glob('*.yaml')):
        if disorder_path.name.endswith('.history.yaml'):
            continue
        try:
            disorder = load_disorder(disorder_path) or {}
        except Exception:
            continue
        disorder_name = disorder.get('name') or disorder_path.stem
        page_filename = f"{slugify(str(disorder_name))}.html"

        term_id = _extract_disorder_term_id(disorder)
        if term_id:
            by_term_candidates[term_id.upper()].add(page_filename)

        for candidate in (disorder_name, disorder_path.stem):
            lookup_key = _normalize_disorder_lookup(
                str(candidate) if candidate else None)
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
    differential_items = disorder.get('differential_diagnoses') or []
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
        diff.pop('dismech_page_href', None)

        href = None
        disease_term = diff.get('disease_term')
        if isinstance(disease_term, dict):
            term = disease_term.get('term')
            if isinstance(term, dict):
                term_id = term.get('id')
                if term_id:
                    href = by_term.get(str(term_id).upper())

        if not href:
            href = by_name.get(_normalize_disorder_lookup(diff.get('name')))

        if href and href not in {current_page_filename, default_current_page}:
            diff['dismech_page_href'] = href


def load_disorder(yaml_path: Path) -> dict:
    """Load a disorder YAML file."""
    with open(yaml_path) as f:
        return yaml.safe_load(f)


def load_comorbidity(yaml_path: Path) -> dict:
    """Load a comorbidity YAML file."""
    with open(yaml_path) as f:
        return yaml.safe_load(f)


def _format_condition_label(condition: dict) -> str:
    slug = condition.get('slug')
    if slug:
        return slug.replace('_', ' ')
    composition = condition.get('composition')
    components = condition.get('components', []) or []
    component_slugs = [c.get('slug') for c in components if c.get('slug')]
    if composition and component_slugs:
        readable = ', '.join(s.replace('_', ' ') for s in component_slugs)
        return f'{composition.title()} of {readable}'
    if component_slugs:
        return ', '.join(s.replace('_', ' ') for s in component_slugs)
    return 'Unknown'


def _extract_condition_slugs(condition: dict) -> list[str]:
    slugs: list[str] = []
    slug = condition.get('slug')
    if slug:
        slugs.append(slug)
    components = condition.get('components', []) or []
    for component in components:
        comp_slug = component.get('slug')
        if comp_slug:
            slugs.append(comp_slug)
    return slugs


def _collect_comorbidity_links(
    disorder_slug: str,
    comorbidity_dir: Path = Path('kb/comorbidities'),
    comorbidity_pages_dir: Path = Path('pages/comorbidities'),
) -> list[dict]:
    if not comorbidity_dir.exists():
        return []
    links: list[dict] = []
    for yaml_path in sorted(comorbidity_dir.glob('*.yaml')):
        try:
            data = load_comorbidity(yaml_path)
        except Exception:
            continue
        disease_a = data.get('disease_a', {}) or {}
        disease_b = data.get('disease_b', {}) or {}
        a_slugs = _extract_condition_slugs(disease_a)
        b_slugs = _extract_condition_slugs(disease_b)
        if disorder_slug not in a_slugs and disorder_slug not in b_slugs:
            continue
        page_path = comorbidity_pages_dir / f'{yaml_path.stem}.html'
        if not page_path.exists():
            continue
        role_label = None
        if disorder_slug in a_slugs:
            role_label = 'Disease A'
            if disease_a.get('slug') != disorder_slug:
                role_label = 'Component of Disease A'
        elif disorder_slug in b_slugs:
            role_label = 'Disease B'
            if disease_b.get('slug') != disorder_slug:
                role_label = 'Component of Disease B'
        title = f'{_format_condition_label(disease_a)} <-> {_format_condition_label(disease_b)}'
        links.append({
            'href': f'../comorbidities/{yaml_path.stem}.html',
            'title': title,
            'role_label': role_label,
            'directionality': data.get('directionality'),
            'curation_status': data.get('curation_status'),
        })
    return links


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

    # Read raw YAML for display
    yaml_content = yaml_path.read_text()

    # Determine output path early so we can resolve local page links relative to it.
    if output_path is None:
        disorder_name = disorder.get("name") or yaml_path.stem
        output_path = Path('pages/disorders') / \
            f'{slugify(disorder_name)}.html'
    else:
        output_path = Path(output_path)

    _annotate_internal_differential_links(
        disorder=disorder,
        current_page_filename=output_path.name,
        disorders_dir=yaml_path.parent,
    )

    # Set up Jinja2 environment
    if template_path is None:
        template_dir = Path(__file__).parent / 'templates'
        template_name = 'disorder.html.j2'
    else:
        template_dir = template_path.parent
        template_name = template_path.name

    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(['html', 'j2'])
    )

    # Register custom filters
    current_term_id = _extract_disorder_term_id(disorder)
    env.filters['curie_to_url'] = curie_to_url
    env.filters['dismech_page_url'] = _build_dismech_page_url_filter(
        yaml_path.parent,
        excluded_term_ids={current_term_id} if current_term_id else None,
    )
    env.filters['has_local_disorder_page'] = _build_has_local_disorder_filter(
        yaml_path.parent,
    )

    # Load and render template
    template = env.get_template(template_name)

    # Build GitHub source URL
    source_file = f'https://github.com/monarch-initiative/dismech/blob/main/kb/disorders/{yaml_path.name}'

    # Build causal graph and generate Mermaid code
    graph = build_causal_graph(disorder)
    mermaid_code = generate_mermaid(graph)
    comorbidity_links = _collect_comorbidity_links(yaml_path.stem)

    # Group phenotypes by HPO broad category
    phenotype_groups = _group_phenotypes_by_category(
        disorder.get("phenotypes") or [])

    html = template.render(
        disorder=disorder,
        yaml_content=yaml_content,
        source_file=source_file,
        mermaid_code=mermaid_code,
        graph_issues=graph.integrity_issues,
        comorbidity_links=comorbidity_links,
        phenotype_groups=phenotype_groups,
    )

    # Write output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html)

    return output_path


def _build_condition_graphs(
    condition: dict,
    disorders_dir: Path = Path('kb/disorders'),
) -> list[dict]:
    """Build causal graphs for a comorbidity condition (handles composites)."""
    graphs: list[dict] = []
    slugs: list[tuple[str, str]] = []
    slug = condition.get('slug')
    if slug:
        slugs.append((slug, slug.replace('_', ' ')))
    for comp in condition.get('components', []) or []:
        if comp.get('slug'):
            slugs.append((comp['slug'], comp['slug'].replace('_', ' ')))
    for s, label in slugs:
        path = disorders_dir / f'{s}.yaml'
        if path.exists():
            disorder = load_disorder(path)
            graph = build_causal_graph(disorder)
            mermaid = generate_mermaid(graph)
            if mermaid:
                graphs.append({'label': label, 'mermaid_code': mermaid})
    return graphs


def _resolve_comorbidity_disorders_dir(yaml_path: Path) -> Path:
    """Resolve disorders directory for a comorbidity file, preferring nearby kb layout."""
    candidate = yaml_path.parent.parent / 'disorders'
    if candidate.exists():
        return candidate
    return Path('kb/disorders')


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
        template_dir = Path(__file__).parent / 'templates'
        template_name = 'comorbidity.html.j2'
    else:
        template_dir = template_path.parent
        template_name = template_path.name

    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(['html', 'j2'])
    )
    env.filters['curie_to_url'] = curie_to_url
    env.filters['dismech_page_url'] = _build_dismech_page_url_filter(
        disorders_dir,
        local_prefix='../disorders/',
    )
    env.filters['has_local_disorder_page'] = _build_has_local_disorder_filter(
        disorders_dir,
    )
    env.filters['dismech_slug_page_url'] = _build_dismech_slug_page_url_filter(
        disorders_dir,
        local_prefix='../disorders/',
    )
    env.filters['has_local_disorder_slug_page'] = _build_has_local_disorder_slug_filter(
        disorders_dir,
    )

    template = env.get_template(template_name)

    source_file = f'https://github.com/monarch-initiative/dismech/blob/main/kb/comorbidities/{yaml_path.name}'

    disease_a = comorbidity.get('disease_a', {}) or {}
    disease_b = comorbidity.get('disease_b', {}) or {}

    disease_a_graphs = _build_condition_graphs(
        disease_a, disorders_dir=disorders_dir)
    disease_b_graphs = _build_condition_graphs(
        disease_b, disorders_dir=disorders_dir)

    html = template.render(
        comorbidity=comorbidity,
        yaml_content=yaml_content,
        source_file=source_file,
        disease_a_label=_format_condition_label(disease_a),
        disease_b_label=_format_condition_label(disease_b),
        disease_a_slug=disease_a.get('slug') or '',
        disease_b_slug=disease_b.get('slug') or '',
        disease_a_graphs=disease_a_graphs,
        disease_b_graphs=disease_b_graphs,
    )

    if output_path is None:
        output_dir = Path('pages/comorbidities')
        output_dir.mkdir(parents=True, exist_ok=True)
        comorbidity_name = comorbidity.get("name") or yaml_path.stem
        output_path = output_dir / f'{slugify(comorbidity_name)}.html'

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html)
    return output_path


def render_all_comorbidities(
    input_dir: Path = Path('kb/comorbidities'),
    output_dir: Path = Path('pages/comorbidities'),
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

    yaml_files = sorted(input_dir.glob('*.yaml'))
    output_files = []
    for yaml_path in yaml_files:
        output_path = output_dir / f'{yaml_path.stem}.html'
        render_comorbidity(yaml_path, output_path, template_path)
        output_files.append(output_path)
        print(f'Rendered comorbidity: {yaml_path.stem} -> {output_path}')
    return output_files


def _load_schema() -> dict:
    schema_path = Path(__file__).parent / 'schema' / 'dismech.yaml'
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


def _compact_hierarchy_path(path: list[str | None], max_nodes: int = 6) -> list[str | None]:
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
    mappings = disorder.get('mappings') or {}
    for mapping_list in mappings.values():
        if not isinstance(mapping_list, list):
            continue
        for mapping in mapping_list:
            if not isinstance(mapping, dict):
                continue
            term = mapping.get('term') or {}
            term_id = term.get('id')
            if not term_id or ':' not in term_id:
                continue
            prefix = term_id.split(':', 1)[0]
            hierarchy = STRICT_HIERARCHIES.get(prefix)
            if not hierarchy:
                continue
            adapter = _get_oak_adapter(hierarchy['adapter'])
            if adapter is None:
                continue
            path = _build_hierarchy_path(adapter, term_id, hierarchy['root'])
            if not path:
                continue
            compacted = _compact_hierarchy_path(path)
            labeled_path = []
            for curie in compacted:
                if curie is None:
                    labeled_path.append({'label': '...', 'is_ellipsis': True})
                    continue
                label = adapter.label(curie) or curie
                labeled_path.append({'id': curie, 'label': label})
            mapping['hierarchy_path'] = labeled_path


def _load_classification_enums() -> dict:
    classification_dir = Path(__file__).parent / 'schema' / 'classifications'
    enums: dict = {}
    if not classification_dir.exists():
        return enums
    for path in sorted(classification_dir.glob('*.yaml')):
        data = yaml.safe_load(path.read_text()) or {}
        source_meta = {
            'source_id': data.get('id'),
            'source_name': data.get('name'),
            'title': data.get('title'),
            'description': data.get('description'),
        }
        for enum_name, enum_def in (data.get('enums') or {}).items():
            enums[enum_name] = {
                'definition': enum_def or {},
                **source_meta,
            }
    return enums


def _assignment_class_to_enum(schema: dict) -> dict[str, str]:
    mapping: dict[str, str] = {}
    classes = schema.get('classes') or {}
    for class_name, class_def in classes.items():
        slot_usage = class_def.get('slot_usage') or {}
        classification_usage = slot_usage.get('classification_value') or {}
        enum_name = classification_usage.get('range')
        if enum_name:
            mapping[class_name] = enum_name
    return mapping


def _classification_slot_to_enum(schema: dict, assignment_to_enum: dict[str, str]) -> dict[str, str]:
    mapping: dict[str, str] = {}
    slots = schema.get('slots') or {}
    for slot_name, slot_def in slots.items():
        range_name = slot_def.get('range')
        if range_name in assignment_to_enum:
            mapping[slot_name] = assignment_to_enum[range_name]
    return mapping


def _find_enum_for_value(value: str, enums: dict) -> Optional[str]:
    for enum_name, enum_info in enums.items():
        enum_def = enum_info.get('definition') or {}
        if value in (enum_def.get('permissible_values') or {}):
            return enum_name
    return None


def _build_enum_tree(enum_def: dict) -> tuple[list[dict], dict[str, dict]]:
    values = enum_def.get('permissible_values') or {}
    nodes: dict[str, dict] = {}
    for value, meta in values.items():
        nodes[value] = {
            'name': value,
            'title': meta.get('title'),
            'description': meta.get('description'),
            'meaning': meta.get('meaning'),
            'children': [],
            'disorders': [],
            'parent_ids': [],
        }
    for value, meta in values.items():
        parents = meta.get('is_a')
        if isinstance(parents, str):
            parents = [parents]
        elif not parents:
            parents = []
        for parent in parents:
            if parent in nodes:
                nodes[parent]['children'].append(nodes[value])
                nodes[value]['parent_ids'].append(parent)
    roots = [node for node in nodes.values() if not node['parent_ids']]
    return roots, nodes


def render_classification_pages(
    input_dir: Path = Path('kb/disorders'),
    output_dir: Path = Path('pages/classifications'),
    template_path: Optional[Path] = None,
) -> list[Path]:
    enums = _load_classification_enums()
    if not enums:
        return []

    schema = _load_schema()
    assignment_to_enum = _assignment_class_to_enum(schema)
    slot_to_enum = _classification_slot_to_enum(schema, assignment_to_enum)

    disorders: list[dict] = []
    for yaml_path in sorted(input_dir.glob('*.yaml')):
        if yaml_path.name.endswith('.history.yaml'):
            continue
        disorder = load_disorder(yaml_path) or {}
        name = disorder.get('name') or yaml_path.stem
        disorders.append({
            'name': name,
            'slug': slugify(name),
            'classifications': disorder.get('classifications') or {},
        })

    disorders_by_enum_value: dict[str, dict[str, list[dict]]] = {
        name: {} for name in enums}
    for disorder in disorders:
        classifications = disorder.get('classifications') or {}
        for slot_name, entry in classifications.items():
            if entry is None:
                continue
            entries = entry if isinstance(entry, list) else [entry]
            for item in entries:
                if isinstance(item, dict):
                    value = item.get('classification_value')
                else:
                    value = item
                if not value:
                    continue
                enum_name = slot_to_enum.get(
                    slot_name) or _find_enum_for_value(value, enums)
                if not enum_name:
                    continue
                disorders_by_enum_value.setdefault(enum_name, {}).setdefault(value, []).append({
                    'name': disorder['name'],
                    'slug': disorder['slug'],
                })

    if template_path is None:
        template_dir = Path(__file__).parent / 'templates'
        template_name = 'classification.html.j2'
    else:
        template_dir = template_path.parent
        template_name = template_path.name

    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(['html', 'j2'])
    )
    env.filters['curie_to_url'] = curie_to_url
    env.filters['dismech_page_url'] = _build_dismech_page_url_filter(
        input_dir,
        local_prefix='../disorders/',
    )
    env.filters['has_local_disorder_page'] = _build_has_local_disorder_filter(
        input_dir,
    )
    template = env.get_template(template_name)

    output_dir.mkdir(parents=True, exist_ok=True)

    output_paths: list[Path] = []
    for enum_name, enum_info in enums.items():
        enum_def = enum_info.get('definition') or {}
        roots, nodes = _build_enum_tree(enum_def)
        for value, disorder_list in (disorders_by_enum_value.get(enum_name) or {}).items():
            if value in nodes:
                nodes[value]['disorders'] = sorted(
                    disorder_list, key=lambda d: d['name'])
        for node in nodes.values():
            node['is_leaf'] = len(node['children']) == 0

        html = template.render(
            enum_name=enum_name,
            enum_description=enum_def.get('description'),
            classification_title=enum_info.get('title'),
            classification_description=enum_info.get('description'),
            classification_id=enum_info.get('source_id'),
            roots=roots,
        )
        output_path = output_dir / f'{slugify(enum_name)}.html'
        output_path.write_text(html)
        output_paths.append(output_path)

    return output_paths


def render_all_disorders(
    input_dir: Path = Path('kb/disorders'),
    output_dir: Path = Path('pages/disorders'),
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

    yaml_files = [
        path
        for path in sorted(input_dir.glob('*.yaml'))
        if not path.name.endswith('.history.yaml')
    ]
    output_files = []

    # Each disorder should have a name,
    # but if not, we'll use the filename as a fallback
    for yaml_path in yaml_files:
        disorder = load_disorder(yaml_path)
        disorder_name = disorder.get("name") or yaml_path.stem
        output_path = output_dir / f'{slugify(disorder_name)}.html'

        render_disorder(yaml_path, output_path, template_path)
        output_files.append(output_path)
        print(f'Rendered: {disorder_name} -> {output_path}')

    render_classification_pages(input_dir=input_dir)

    print(f'\nGenerated {len(output_files)} HTML pages in {output_dir}')
    return output_files


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Render disorder and comorbidity pages')
    parser.add_argument('path', nargs='?',
                        help='Single YAML file or directory')
    parser.add_argument('--all', '-a', action='store_true',
                        help='Render all disorders')
    parser.add_argument('--comorbidity', action='store_true',
                        help='Render comorbidity page(s)')
    parser.add_argument(
        '--output', '-o', help='Output path (file or directory)')
    parser.add_argument('--template', '-t', help='Custom template path')

    args = parser.parse_args()

    template_path = Path(args.template) if args.template else None

    if args.comorbidity:
        if args.path is None:
            raise SystemExit(
                'Error: --comorbidity requires a file or directory path')
        input_path = Path(args.path)
        if input_path.is_dir():
            output_dir = Path(args.output) if args.output else Path(
                'pages/comorbidities')
            render_all_comorbidities(input_path, output_dir, template_path)
        else:
            output_path = Path(args.output) if args.output else None
            result = render_comorbidity(input_path, output_path, template_path)
            print(f'Generated: {result}')
        return

    if args.all or args.path is None:
        input_dir = Path(args.path) if args.path else Path('kb/disorders')
        output_dir = Path(args.output) if args.output else Path(
            'pages/disorders')
        render_all_disorders(input_dir, output_dir, template_path)
    else:
        yaml_path = Path(args.path)
        output_path = Path(args.output) if args.output else None
        result = render_disorder(yaml_path, output_path, template_path)
        print(f'Generated: {result}')


if __name__ == '__main__':
    main()
