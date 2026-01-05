"""
Render disorder YAML files to HTML pages using Jinja2 templates.
"""

from pathlib import Path
from typing import Optional

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

from dismech.graph import build_causal_graph, generate_mermaid


def curie_to_url(curie: str) -> str:
    """Convert a CURIE to a resolvable URL."""
    if not curie or ':' not in curie:
        return '#'

    prefix, local_id = curie.split(':', 1)

    url_patterns = {
        # Ontology terms
        'HP': f'https://hpo.jax.org/browse/term/HP:{local_id}',
        'MONDO': f'https://monarchinitiative.org/disease/MONDO:{local_id}',
        'CL': f'https://www.ebi.ac.uk/ols4/ontologies/cl/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCL_{local_id}',
        'GO': f'https://amigo.geneontology.org/amigo/term/GO:{local_id}',
        'UBERON': f'https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_{local_id}',
        'CHEBI': f'https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:{local_id}',
        'PMID': f'https://pubmed.ncbi.nlm.nih.gov/{local_id}',
        'GENO': f'http://purl.obolibrary.org/obo/GENO_{local_id}',
        'MAXO': f'https://www.ebi.ac.uk/ols4/ontologies/maxo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FMAXO_{local_id}',
        'ECTO': f'https://www.ebi.ac.uk/ols4/ontologies/ecto/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FECTO_{local_id}',
        'NCBITaxon': f'https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id={local_id}',
        # Model repositories
        'biomodels': f'https://www.ebi.ac.uk/biomodels/{local_id}',
        # Dataset repositories
        'geo': f'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc={local_id}',
        'arrayexpress': f'https://www.ebi.ac.uk/biostudies/arrayexpress/studies/{local_id}',
        'sra': f'https://www.ncbi.nlm.nih.gov/sra/{local_id}',
        'dbgap': f'https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id={local_id}',
        'pride': f'https://www.ebi.ac.uk/pride/archive/projects/{local_id}',
        'metabolights': f'https://www.ebi.ac.uk/metabolights/{local_id}',
        'hca': f'https://data.humancellatlas.org/explore/projects/{local_id}',
        'gtex': f'https://gtexportal.org/home/datasets',
        'encode': f'https://www.encodeproject.org/experiments/{local_id}',
        'phenopacket-store': f'https://github.com/monarch-initiative/phenopacket-store/tree/main/notebooks/{local_id}',
        'clinvar': f'https://www.ncbi.nlm.nih.gov/clinvar/variation/{local_id}',
        # Gene identifiers
        'HGNC': f'https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:{local_id}',
    }

    if prefix in url_patterns:
        return url_patterns[prefix]

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
