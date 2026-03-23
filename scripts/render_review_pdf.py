#!/usr/bin/env python3
"""Render a disorder YAML file to a clean PDF for expert review."""

import argparse
import subprocess
import tempfile
from datetime import datetime
from pathlib import Path

import yaml
from jinja2 import Environment

TEMPLATE = r"""
# {{ d.name }}

*This report was generated from the curated disease record of {{ d.name }} in
the Disorder Mechanisms Knowledge Base (https://github.com/monarch-initiative/dismech,
commit {{ commit_hash }}). The contents are highly experimental (pre-alpha). This
report is intended for review by medical experts to verify the correctness of the
presented information.*

{% if d.synonyms %}*Also known as: {{ d.synonyms | join(', ') }}*{% endif %}

**Category:** {{ d.category or 'Not specified' }}
{% if d.disease_term %} | **MONDO:** {{ d.disease_term.term.id }} ({{ d.disease_term.term.label }}){% endif %}

{% if d.parents %}**Parents:** {{ d.parents | join(' . ') }}{% endif %}

{% if d.creation_date %}*Created: {{ d.creation_date }}* | {% endif %}{% if d.updated_date %}*Updated: {{ d.updated_date }}*{% endif %}

---

{{ d.description | wordwrap(90) }}

{% if d.has_subtypes %}
## Subtypes

{% for s in d.has_subtypes %}
### {{ s.name }}{% if s.classification %} ({{ s.classification }}){% endif %}

{{ s.description | wordwrap(90) }}
{{ evidence_block(s.evidence, claim=s.name + " is a subtype of " + d.name) }}
{% endfor %}
{% endif %}

{% if d.pathophysiology %}
## Pathophysiology

{% for p in d.pathophysiology %}
### {{ p.name }}
{% if p.conforms_to %}
*Conforms to module:* `{{ p.conforms_to }}`
{% endif %}

{{ p.description | wordwrap(90) }}

{% if p.cell_types %}
**Cell types:**
{% for ct in p.cell_types %}
- {{ ct.preferred_term }} -- `{{ ct.term.id }}` ({{ ct.term.label }}){% if ct.modifier %} [{{ el(ct.modifier) }}]{% endif %}

{% endfor %}
{% endif %}
{% if p.biological_processes %}
**Biological processes:**
{% for bp in p.biological_processes %}
- {{ bp.preferred_term }} -- `{{ bp.term.id }}` ({{ bp.term.label }}){% if bp.modifier %} [{{ el(bp.modifier) }}]{% endif %}

{% endfor %}
{% endif %}
{% if p.molecular_functions %}
**Molecular functions:**
{% for mf in p.molecular_functions %}
- {{ mf.preferred_term }} -- `{{ mf.term.id }}` ({{ mf.term.label }}){% if mf.modifier %} [{{ el(mf.modifier) }}]{% endif %}

{% endfor %}
{% endif %}
{% if p.locations %}
**Anatomical locations:**
{% for loc in p.locations %}
- {{ loc.preferred_term }} -- `{{ loc.term.id }}` ({{ loc.term.label }})
{% endfor %}
{% endif %}
{% if p.cellular_components %}
**Cellular components:**
{% for cc in p.cellular_components %}
- {{ cc.preferred_term }} -- `{{ cc.term.id }}` ({{ cc.term.label }})
{% endfor %}
{% endif %}
{% if p.chemical_entities %}
**Chemical entities:**
{% for ce in p.chemical_entities %}
- {{ ce.preferred_term }} -- `{{ ce.term.id }}` ({{ ce.term.label }}){% if ce.modifier %} [{{ el(ce.modifier) }}]{% endif %}

{% endfor %}
{% endif %}
{% if p.gene_products %}
**Gene products:**
{% for gp in p.gene_products %}
- {{ gp.preferred_term }} -- `{{ gp.term.id }}` ({{ gp.term.label }})
{% endfor %}
{% endif %}
{% if p.triggers %}
**Triggers:**
{% for t in p.triggers %}
- {{ t.preferred_term }}{% if t.term %} -- `{{ t.term.id }}` ({{ t.term.label }}){% endif %}

{% endfor %}
{% endif %}
{% if p.downstream %}
**Downstream effects:**
{% for de in p.downstream %}
- **{{ de.target }}**: {{ de.description }}
{% endfor %}
{% endif %}
{% if p.notes %}
*Notes:* {{ p.notes }}
{% endif %}
{{ evidence_block(p.evidence, claim=p.name + " is a pathophysiological mechanism in " + d.name) }}
{% endfor %}
{% endif %}

{% if d.phenotypes %}
## Phenotypes

{% for ph in d.phenotypes %}
### {{ ph.name }}{% if ph.category %} [{{ ph.category }}]{% endif %}

{% if ph.frequency %}**Frequency:** {{ freq(ph.frequency) }}{% endif %}{% if ph.severity %} | **Severity:** {{ ph.severity }}{% endif %}{% if ph.diagnostic %} | **Diagnostic**{% endif %}

{% if ph.subtype %}**Subtype:** {{ ph.subtype }}{% endif %}

{{ ph.description | wordwrap(90) }}

{% if ph.phenotype_term %}
**HPO term:** {{ ph.phenotype_term.preferred_term }} -- `{{ ph.phenotype_term.term.id }}` ({{ ph.phenotype_term.term.label }}){% if ph.phenotype_term.modifier %} [{{ el(ph.phenotype_term.modifier) }}]{% endif %}

{% endif %}
{% if ph.notes %}
*Notes:* {{ ph.notes }}
{% endif %}
{{ evidence_block(ph.evidence, claim=ph.name + " is " + (article(freq_lower(ph.frequency)) + " " if ph.frequency else "a ") + "phenotype of " + d.name) }}
{% endfor %}
{% endif %}

{% if d.histopathology %}
## Histopathology

{% for h in d.histopathology %}
### {{ h.name }}
{% if h.frequency %}**Frequency:** {{ freq(h.frequency) }}{% endif %}{% if h.diagnostic %} | **Diagnostic**{% endif %}

{{ h.description | default('', true) | wordwrap(90) }}
{% if h.finding_term %}
**Finding term:** {{ h.finding_term.preferred_term }} -- `{{ h.finding_term.term.id }}` ({{ h.finding_term.term.label }})
{% endif %}
{{ evidence_block(h.evidence, claim=h.name + " is a histopathological finding in " + d.name) }}
{% endfor %}
{% endif %}

{% if d.biochemical %}
## Biochemical Markers

{% for b in d.biochemical %}
### {{ b.name }}
{% if b.presence %}**Presence:** {{ b.presence }}{% endif %}{% if b.frequency %} | **Frequency:** {{ freq(b.frequency) }}{% endif %}

{{ b.description | default('', true) | wordwrap(90) }}
{% if b.biomarker_term %}
**Biomarker term:** {{ b.biomarker_term.preferred_term }} -- `{{ b.biomarker_term.term.id }}` ({{ b.biomarker_term.term.label }})
{% endif %}
{{ evidence_block(b.evidence, claim=b.name + " is a biochemical marker of " + d.name) }}
{% endfor %}
{% endif %}

{% if d.genetic %}
## Genetics

{% for g in d.genetic %}
### {{ g.name }}
{% if g.association %}**Association:** {{ g.association }}{% endif %}

{% if g.gene_term %}
**Gene:** {{ g.gene_term.preferred_term }} -- `{{ g.gene_term.term.id }}` ({{ g.gene_term.term.label }})
{% endif %}

{% if g.features %}{{ g.features | wordwrap(90) }}{% endif %}

{% if g.inheritance %}
**Inheritance:**
{% for inh in g.inheritance %}
- {{ inh.name }}{% if inh.inheritance_term %} -- `{{ inh.inheritance_term.term.id }}`{% endif %}{% if inh.penetrance %} | Penetrance: {{ el(inh.penetrance) }}{% endif %}{% if inh.expressivity %} | Expressivity: {{ el(inh.expressivity) }}{% endif %}{% if inh.de_novo_rate %} | De novo rate: {{ inh.de_novo_rate }}{% endif %}

{{ evidence_block(inh.evidence, claim=d.name + " follows " + inh.name, indent=2) }}
{% endfor %}
{% endif %}

{% if g.variants %}
**Variants:**
{% for v in g.variants %}
#### {{ v.name }}
{% if v.clinical_significance %}**Clinical significance:** {{ el(v.clinical_significance) }}{% endif %}

{{ v.description | default('', true) | wordwrap(90) }}
{{ evidence_block(v.evidence, claim=v.name + " is a variant associated with " + d.name) }}
{% endfor %}
{% endif %}
{{ evidence_block(g.evidence, claim=g.name + " is a genetic basis of " + d.name) }}
{% endfor %}
{% endif %}

{% if d.environmental %}
## Environmental Factors

{% for e in d.environmental %}
### {{ e.name }}
{% if e.presence %}**Presence:** {{ e.presence }}{% endif %}

{{ e.description | default('', true) | wordwrap(90) }}
{{ evidence_block(e.evidence, claim=e.name + " is an environmental factor in " + d.name) }}
{% endfor %}
{% endif %}

{% if d.treatments %}
## Treatments

{% for t in d.treatments %}
### {{ t.name }}
{% if t.treatment_term %}
**Treatment term:** {{ t.treatment_term.preferred_term }} -- `{{ t.treatment_term.term.id }}` ({{ t.treatment_term.term.label }})
{% endif %}
{% if t.role %}**Role:** {{ t.role }}{% endif %}

{% if t.mechanism %}**Mechanism:** {{ t.mechanism }}{% endif %}

{{ t.description | default('', true) | wordwrap(90) }}

{% if t.target_phenotypes %}
**Target phenotypes:**
{% for tp in t.target_phenotypes %}
- {{ tp.preferred_term }}{% if tp.term %} -- `{{ tp.term.id }}`{% endif %}

{% endfor %}
{% endif %}
{% if t.target_mechanisms %}
**Target mechanisms:**
{% for tm in t.target_mechanisms %}
- **{{ tm.target }}** ({{ tm.treatment_effect }}): {{ tm.description | default('') }}
{% endfor %}
{% endif %}
{% if t.notes %}
*Notes:* {{ t.notes }}
{% endif %}
{{ evidence_block(t.evidence, claim=t.name + " is a treatment for " + d.name) }}
{% endfor %}
{% endif %}

{% if d.clinical_trials %}
## Clinical Trials

{% for ct in d.clinical_trials %}
### {{ ct.name }}
{% if ct.phase %}**Phase:** {{ ct.phase }}{% endif %}{% if ct.status %} | **Status:** {{ ct.status }}{% endif %}

{{ ct.description | default('', true) | wordwrap(90) }}
{{ evidence_block(ct.evidence, claim=ct.name + " is a clinical trial for " + d.name) }}
{% endfor %}
{% endif %}

{% if d.animal_models %}
## Animal Models

{% for am in d.animal_models %}
### {{ am.species }}{% if am.genotype %} -- {{ am.genotype }}{% endif %}

{% if am.category %}**Category:** {{ am.category }}{% endif %}

{{ am.description | default('', true) | wordwrap(90) }}
{{ evidence_block(am.evidence, claim=am.species + " is an animal model for " + d.name) }}
{% endfor %}
{% endif %}

{% if d.datasets %}
## Datasets

{% for ds in d.datasets %}
{% if ds.accession or ds.title %}
### {{ ds.title | default(ds.accession) }}
{% if ds.accession %}**Accession:** `{{ ds.accession }}`{% endif %}{% if ds.data_type %} | **Type:** {{ ds.data_type }}{% endif %}

{{ ds.description | default('', true) | wordwrap(90) }}
{% if ds.publication %}**Publication:** {{ ds.publication }}{% endif %}

{% endif %}
{% endfor %}
{% endif %}

{% if d.computational_models %}
## Computational Models

{% for cm in d.computational_models %}
### {{ cm.name }}
{% if cm.model_type %}**Type:** {{ cm.model_type }}{% endif %}

{{ cm.description | default('', true) | wordwrap(90) }}
{{ evidence_block(cm.evidence, claim=cm.name + " is a computational model of " + d.name) }}
{% endfor %}
{% endif %}

{% if d.diagnosis %}
## Diagnosis

{% for dx in d.diagnosis %}
### {{ dx.name }}
{{ dx.description | default('', true) | wordwrap(90) }}
{{ evidence_block(dx.evidence, claim=dx.name + " is a diagnostic criterion for " + d.name) }}
{% endfor %}
{% endif %}

{% if d.differential_diagnoses %}
## Differential Diagnoses

{% for dd in d.differential_diagnoses %}
### {{ dd.name }}
{{ dd.description | default('', true) | wordwrap(90) }}
{% if dd.distinguishing_features %}
**Distinguishing features:**
{% for f in dd.distinguishing_features %}
- {{ f }}
{% endfor %}
{% endif %}
{{ evidence_block(dd.evidence, claim=dd.name + " is a differential diagnosis for " + d.name) }}
{% endfor %}
{% endif %}

{% if d.prevalence %}
## Prevalence

{% for p in d.prevalence %}
- {% if p.population %}{{ p.population }}: {% endif %}{{ p.percentage }}{% if p.subtype %} ({{ p.subtype }}){% endif %}{% if p.notes %} -- {{ p.notes }}{% endif %}

{% endfor %}
{% endif %}

{% if d.progression %}
## Progression

{% for p in d.progression %}
- {% if p.phase %}{{ p.phase }}: {% endif %}{% if p.duration %}Duration: {{ p.duration }}{% endif %}{% if p.notes %} -- {{ p.notes }}{% endif %}

{% endfor %}
{% endif %}

{% if d.stages %}
## Disease Stages

{% for s in d.stages %}
### {{ s.name }}
{{ s.description | default('', true) | wordwrap(90) }}
{{ evidence_block(s.evidence, claim=s.name + " is a stage of " + d.name) }}
{% endfor %}
{% endif %}

{% if d.infectious_agent %}
## Infectious Agent

{% for ia in d.infectious_agent %}
### {{ ia.name }}
{{ ia.description | default('', true) | wordwrap(90) }}
{{ evidence_block(ia.evidence, claim=ia.name + " is an infectious agent causing " + d.name) }}
{% endfor %}
{% endif %}

{% if d.notes %}
## Notes

{{ d.notes | wordwrap(90) }}
{% endif %}

---
*Generated {{ now }} from dismech knowledge base for expert review.*

{{ glossary() }}
"""


SCHEMA_PATH = Path(__file__).parent.parent / "src" / "dismech" / "schema" / "dismech.yaml"


def _load_enum_metadata(schema_path, enum_name):
    """Load title and description from a LinkML enum's permissible_values."""
    with open(schema_path) as f:
        schema = yaml.safe_load(f)
    pv = schema.get("enums", {}).get(enum_name, {}).get("permissible_values", {})
    return {
        k: {"title": v.get("title", k), "description": v.get("description", "")}
        for k, v in pv.items()
    }


ENUM_NAMES = [
    "EvidenceSourceEnum",
    "EvidenceItemSupportEnum",
    "FrequencyEnum",
    "ModifierEnum",
    "PenetranceEnum",
    "ExpressivityEnum",
    "ClinicalSignificanceEnum",
    "RegulatoryVariantCategoryEnum",
    "RegulatoryElementTypeEnum",
    "LateralityEnum",
]

ALL_ENUM_META = {name: _load_enum_metadata(SCHEMA_PATH, name) for name in ENUM_NAMES}

# Convenience aliases
SOURCE_META = ALL_ENUM_META["EvidenceSourceEnum"]
SUPPORT_META = ALL_ENUM_META["EvidenceItemSupportEnum"]
FREQUENCY_META = ALL_ENUM_META["FrequencyEnum"]

# Build a flat lookup: enum_value -> (enum_name, title, description)
_FLAT_ENUM_LOOKUP = {}
for enum_name, meta in ALL_ENUM_META.items():
    for value, info in meta.items():
        if value not in _FLAT_ENUM_LOOKUP:
            _FLAT_ENUM_LOOKUP[value] = (enum_name, info["title"], info["description"])


class GlossaryCollector:
    """Tracks which enum values are used and assigns footnote numbers."""

    def __init__(self):
        self._used = {}  # (enum_name, value) -> footnote number
        self._counter = 0

    def ref(self, enum_name, value):
        """Return the footnote number for a used enum value, registering it if new."""
        key = (enum_name, value)
        if key not in self._used:
            self._counter += 1
            self._used[key] = self._counter
        return self._used[key]

    def render_glossary(self):
        """Render the glossary as an endnote-style reference list."""
        if not self._used:
            return ""
        lines = ["\n## Glossary\n"]
        for (enum_name, value), num in sorted(self._used.items(), key=lambda x: x[1]):
            meta = ALL_ENUM_META.get(enum_name, {}).get(value, {})
            title = meta.get("title", value)
            desc = meta.get("description", "")
            lines.append(f"^{num}^ **{title}**: {desc}\n")
        return "\n".join(lines)


# Module-level collector instance, reset per render
_glossary = GlossaryCollector()


def freq(value):
    """Convert a frequency enum value to a human-readable label with footnote."""
    if not value:
        return ""
    return enum_label(value, "FrequencyEnum")


def freq_lower(value):
    """Like freq() but lowercased for mid-sentence use."""
    if not value:
        return ""
    result = enum_label(value, "FrequencyEnum")
    if result and result[0].isupper():
        return result[0].lower() + result[1:]
    return result


def article(text):
    """Return 'a' or 'an' + text based on the first letter."""
    if not text:
        return "a"
    first = text.lstrip().lstrip("*_")[0:1].lower()
    return f"an {text}" if first in "aeiou" else f"a {text}"


def enum_label(value, enum_name_hint=None):
    """Convert any enum value to a human-readable label with glossary footnote."""
    if not value:
        return ""
    if enum_name_hint and enum_name_hint in ALL_ENUM_META:
        meta = ALL_ENUM_META[enum_name_hint].get(value, {})
        if meta:
            title = meta["title"]
            ref = _glossary.ref(enum_name_hint, value)
            return f"{title}^{ref}^"
    # Fall back to flat lookup
    if value in _FLAT_ENUM_LOOKUP:
        enum_name, title, _ = _FLAT_ENUM_LOOKUP[value]
        ref = _glossary.ref(enum_name, value)
        return f"{title}^{ref}^"
    return value


def evidence_block(evidence, claim="", indent=0):
    """Render a list of evidence items as markdown."""
    if not evidence:
        return ""
    prefix = "  " * indent
    if claim:
        header = f"**Evidence** (*{claim.strip()}*)"
    else:
        header = "**Evidence**"
    lines = [f"\n{prefix}{header}:\n"]
    for i, e in enumerate(evidence, 1):
        ref = e.get("reference", "?")
        supports = e.get("supports", "?")
        source = e.get("evidence_source", "?")
        snippet = e.get("snippet", "")
        explanation = e.get("explanation", "")

        support_title = SUPPORT_META.get(supports, {}).get("title", supports)
        source_title = SOURCE_META.get(source, {}).get("title", source)
        support_ref = _glossary.ref("EvidenceItemSupportEnum", supports) if supports in SUPPORT_META else None
        source_ref = _glossary.ref("EvidenceSourceEnum", source) if source in SOURCE_META else None

        support_str = f"{support_title}^{support_ref}^" if support_ref else support_title
        source_str = f"{source_title}^{source_ref}^" if source_ref else source_title

        lines.append(f"{prefix}{i}. **{ref}** -- {support_str} [{source_str}]\n")
        if snippet:
            lines.append(f'{prefix}   Quote:\n\n{prefix}   > "{snippet.strip()}"\n')
        if explanation:
            lines.append(f"{prefix}   Interpretation: *{explanation.strip()}*\n")
    return "\n".join(lines)


class DotDict(dict):
    """Dict that returns None for missing keys and supports dot access."""

    def __getattr__(self, key):
        val = self.get(key)
        if isinstance(val, dict):
            return DotDict(val)
        if isinstance(val, list):
            return [DotDict(v) if isinstance(v, dict) else v for v in val]
        return val

    def __getitem__(self, key):
        val = super().get(key)
        if isinstance(val, dict):
            return DotDict(val)
        if isinstance(val, list):
            return [DotDict(v) if isinstance(v, dict) else v for v in val]
        return val

    def get(self, key, default=None):
        val = super().get(key, default)
        if isinstance(val, dict):
            return DotDict(val)
        if isinstance(val, list):
            return [DotDict(v) if isinstance(v, dict) else v for v in val]
        return val


def main():
    parser = argparse.ArgumentParser(description="Render disorder YAML to PDF for expert review")
    parser.add_argument("yaml_file", help="Path to disorder YAML file")
    parser.add_argument("-o", "--output", help="Output PDF path (default: same name as YAML)")
    parser.add_argument("--md-only", action="store_true", help="Output markdown only, no PDF")
    args = parser.parse_args()

    yaml_path = Path(args.yaml_file)
    with open(yaml_path) as f:
        data = DotDict(yaml.safe_load(f))

    # Reset the glossary collector for each render
    global _glossary
    _glossary = GlossaryCollector()

    env = Environment(autoescape=False)
    env.globals["evidence_block"] = evidence_block
    env.globals["freq"] = freq
    env.globals["freq_lower"] = freq_lower
    env.globals["article"] = article
    env.globals["el"] = enum_label
    env.globals["glossary"] = lambda: _glossary.render_glossary()
    template = env.from_string(TEMPLATE)

    # Get current git commit hash
    try:
        commit_hash = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, cwd=yaml_path.parent
        ).stdout.strip() or "unknown"
    except Exception:
        commit_hash = "unknown"

    md = template.render(
        d=data,
        now=datetime.now().strftime("%Y-%m-%d %H:%M"),
        commit_hash=commit_hash,
    )
    # Clean up excessive blank lines
    while "\n\n\n" in md:
        md = md.replace("\n\n\n", "\n\n")

    if args.md_only:
        out = Path(args.output) if args.output else yaml_path.with_suffix(".md")
        out.write_text(md)
        print(f"Markdown written to {out}")
        return

    # Convert markdown to PDF via pandoc
    pdf_path = Path(args.output) if args.output else yaml_path.with_suffix(".pdf")

    with tempfile.NamedTemporaryFile(suffix=".html", delete=False, mode="w") as tmp:
        result = subprocess.run(
            ["pandoc", "-f", "markdown", "-t", "html5", "--standalone",
             "--metadata", f"title={data.name}",
             "--css", "/dev/null"],
            input=md, capture_output=True, text=True
        )
        if result.returncode != 0:
            print(f"Pandoc error: {result.stderr}")
            return

        html = result.stdout.replace("</head>", REVIEW_CSS + "</head>")
        tmp.write(html)
        tmp_path = tmp.name

    chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    subprocess.run(
        [chrome, "--headless", "--disable-gpu",
         f"--print-to-pdf={pdf_path}",
         "--print-to-pdf-no-header",
         f"file://{tmp_path}"],
        capture_output=True
    )
    Path(tmp_path).unlink()
    print(f"PDF written to {pdf_path}")


REVIEW_CSS = """
<style>
  @page { margin: 2cm; }
  body {
    font-family: 'Georgia', 'Times New Roman', serif;
    font-size: 11pt;
    line-height: 1.5;
    color: #1a1a1a;
    max-width: 48em;
    margin: 0 auto;
    padding: 2em;
  }
  h1 {
    font-size: 22pt;
    border-bottom: 3px solid #0f766e;
    padding-bottom: 0.3em;
    margin-bottom: 0.5em;
    color: #0f766e;
  }
  h2 {
    font-size: 16pt;
    color: #0f766e;
    border-bottom: 1px solid #ccc;
    margin-top: 1.5em;
    padding-bottom: 0.2em;
    page-break-after: avoid;
  }
  h3 {
    font-size: 13pt;
    color: #333;
    margin-top: 1em;
    page-break-after: avoid;
  }
  h4 {
    font-size: 11pt;
    color: #555;
    margin-top: 0.8em;
  }
  p { margin: 0.4em 0; }
  blockquote {
    border-left: 3px solid #0f766e;
    margin: 0.5em 0;
    padding: 0.3em 0.8em;
    background: #f0fdfa;
    font-style: italic;
    font-size: 10pt;
    color: #333;
  }
  code {
    font-family: 'SF Mono', 'Menlo', monospace;
    font-size: 9pt;
    background: #f3f4f6;
    padding: 0.1em 0.3em;
    border-radius: 3px;
  }
  strong { color: #111; }
  em { color: #444; }
  ul, ol { margin: 0.3em 0; padding-left: 1.5em; }
  li { margin: 0.2em 0; }
  hr {
    border: none;
    border-top: 2px solid #e5e7eb;
    margin: 1.5em 0;
  }
  li + li { page-break-before: avoid; }
</style>
"""


if __name__ == "__main__":
    main()
