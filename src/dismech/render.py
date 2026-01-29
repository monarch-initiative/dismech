"""
Render disorder YAML files to HTML pages using Jinja2 templates.
"""

from functools import lru_cache
from pathlib import Path
from typing import Optional

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

from dismech.graph import build_causal_graph, generate_mermaid


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


def load_disorder(yaml_path: Path) -> dict:
    """Load a disorder YAML file."""
    with open(yaml_path) as f:
        return yaml.safe_load(f)


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

    # Read raw YAML for display
    yaml_content = yaml_path.read_text()

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
    env.filters['curie_to_url'] = curie_to_url

    # Load and render template
    template = env.get_template(template_name)

    # Build GitHub source URL
    source_file = f'https://github.com/monarch-initiative/dismech/blob/main/kb/disorders/{yaml_path.name}'

    # Build causal graph and generate Mermaid code
    graph = build_causal_graph(disorder)
    mermaid_code = generate_mermaid(graph)

    html = template.render(
        disorder=disorder,
        yaml_content=yaml_content,
        source_file=source_file,
        mermaid_code=mermaid_code,
        graph_issues=graph.integrity_issues,
    )

    # Determine output path
    if output_path is None:
        output_dir = Path('pages/disorders')
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / f'{slugify(disorder["name"])}.html'

    # Write output
    output_path.write_text(html)

    return output_path


def _load_schema() -> dict:
    schema_path = Path(__file__).parent / 'schema' / 'dismech.yaml'
    try:
        return yaml.safe_load(schema_path.read_text()) or {}
    except FileNotFoundError:
        return {}


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
        disorder = load_disorder(yaml_path) or {}
        name = disorder.get('name') or yaml_path.stem
        disorders.append({
            'name': name,
            'slug': slugify(name),
            'classifications': disorder.get('classifications') or {},
        })

    disorders_by_enum_value: dict[str, dict[str, list[dict]]] = {name: {} for name in enums}
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
                enum_name = slot_to_enum.get(slot_name) or _find_enum_for_value(value, enums)
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
    template = env.get_template(template_name)

    output_dir.mkdir(parents=True, exist_ok=True)

    output_paths: list[Path] = []
    for enum_name, enum_info in enums.items():
        enum_def = enum_info.get('definition') or {}
        roots, nodes = _build_enum_tree(enum_def)
        for value, disorder_list in (disorders_by_enum_value.get(enum_name) or {}).items():
            if value in nodes:
                nodes[value]['disorders'] = sorted(disorder_list, key=lambda d: d['name'])
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

    yaml_files = sorted(input_dir.glob('*.yaml'))
    output_files = []

    for yaml_path in yaml_files:
        disorder = load_disorder(yaml_path)
        output_path = output_dir / f'{slugify(disorder["name"])}.html'

        render_disorder(yaml_path, output_path, template_path)
        output_files.append(output_path)
        print(f'Rendered: {disorder["name"]} -> {output_path}')

    render_classification_pages(input_dir=input_dir)

    print(f'\nGenerated {len(output_files)} HTML pages in {output_dir}')
    return output_files


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Render disorder pages')
    parser.add_argument('path', nargs='?', help='Single YAML file or directory')
    parser.add_argument('--all', '-a', action='store_true', help='Render all disorders')
    parser.add_argument('--output', '-o', help='Output path (file or directory)')
    parser.add_argument('--template', '-t', help='Custom template path')

    args = parser.parse_args()

    template_path = Path(args.template) if args.template else None

    if args.all or args.path is None:
        input_dir = Path(args.path) if args.path else Path('kb/disorders')
        output_dir = Path(args.output) if args.output else Path('pages/disorders')
        render_all_disorders(input_dir, output_dir, template_path)
    else:
        yaml_path = Path(args.path)
        output_path = Path(args.output) if args.output else None
        result = render_disorder(yaml_path, output_path, template_path)
        print(f'Generated: {result}')


if __name__ == '__main__':
    main()
