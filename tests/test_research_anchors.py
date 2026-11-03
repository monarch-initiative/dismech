"""The disease research prompt names the disease's causal gene (issue #14907).

A serial-number disease name does not say which gene the disease is about.
Two OpenScientist runs researched the wrong one: MONDO:0030934 (ZNF292) came
back about WDFY3, and spermatogenic failure 26 (TSGA10) about TDRD9. These
tests pin that the recipe hands the provider MONDO's causal gene, OMIM xref and
synonyms, and that a run with none of them gets the old prompt. None of them
opens a MONDO build or the network: OLS, which the anchors ask when the
local build is absent (#15436), is made unreachable for every test below.
"""

import re
from pathlib import Path

import pytest

from dismech import research_anchors
from dismech.research_anchors import (
    NOT_RECORDED,
    IdentityAnchors,
    collect_anchors,
    main,
)

ROOT = Path(__file__).parent.parent
TEMPLATE = ROOT / "templates" / "disease_pathophysiology_research.md"
RECIPES = ("research-disorder", "research-disorder-cyberian-codex")

MRD64 = "MONDO:0030934"


@pytest.fixture(autouse=True)
def _ols_offline(monkeypatch):
    """Without the local build the anchors ask OLS (#15436); keep that offline.

    OLS is unreachable here unless a test says otherwise, which is also the
    case these tests were written for: no MONDO at all. The OLS path itself is
    tested against recorded responses in ``tests/test_mondo_ols.py``.
    """
    from dismech import mondo_ols

    def _ols_down(url, timeout):
        raise mondo_ols.OlsLookupError(f"could not reach OLS ({url}): offline")

    monkeypatch.setattr(mondo_ols, "_get_json", _ols_down)


class StubMondoAdapter:
    """Answers the calls preflight_dr's lookup and the synonym lookup make."""

    def __init__(self, labels, relationships=(), mappings=(), aliases=()):
        self._labels = labels
        self._relationships = relationships
        self._mappings = mappings
        self._aliases = aliases

    def label(self, curie):
        return self._labels.get(curie)

    def relationships(self, subjects=None, predicates=None, objects=None):
        return [
            (s, p, o)
            for s, p, o in self._relationships
            if (subjects is None or s in subjects)
            and (predicates is None or p in predicates)
            and (objects is None or o in objects)
        ]

    def simple_mappings_by_curie(self, curie):
        return list(self._mappings)

    def alias_relationships(self, curie, exclude_labels=False):
        return list(self._aliases)


def _mrd64_adapter(gene_label="ZNF292"):
    return StubMondoAdapter(
        labels={
            MRD64: "intellectual developmental disorder, autosomal dominant 64",
            "HGNC:18410": gene_label,
        },
        relationships=[(MRD64, "RO:0004003", "HGNC:18410")],
        mappings=[
            ("skos:exactMatch", "OMIM:619188"),
            ("skos:exactMatch", "Orphanet:1"),
        ],
        aliases=[
            ("oio:hasExactSynonym", "ZNF292-related neurodevelopmental disorder"),
            ("oio:hasExactSynonym", "MRD64"),
            ("oio:hasRelatedSynonym", "a related synonym is not an identity anchor"),
        ],
    )


ENTRY = {"name": "Intellectual Developmental Disorder, Autosomal Dominant 64"}


def test_numbered_disease_gets_its_causal_gene_omim_and_synonyms(tmp_path):
    anchors = collect_anchors(
        ENTRY, MRD64, adapter=_mrd64_adapter(), stubs_dir=tmp_path
    )
    assert anchors.template_vars() == {
        "causal_genes": "ZNF292",
        "omim_id": "OMIM:619188",
        "synonyms": "ZNF292-related neurodevelopmental disorder; MRD64",
    }
    assert anchors.gene_source == "MONDO"


def test_no_build_no_stub_no_gene_leaves_the_prompt_as_it_was(tmp_path, monkeypatch):
    """The non-Mendelian / no-build case: every anchor reads "not recorded"."""
    monkeypatch.setattr(research_anchors, "_open_local_mondo", lambda: None)
    anchors = collect_anchors({"name": "Asthma"}, "MONDO:0004979", stubs_dir=tmp_path)
    assert anchors.template_vars() == {
        "causal_genes": NOT_RECORDED,
        "omim_id": NOT_RECORDED,
        "synonyms": NOT_RECORDED,
    }


def test_absent_mondo_build_is_never_downloaded(tmp_path, monkeypatch):
    """Opening ``sqlite:obo:mondo`` downloads a missing build, so it must not be opened."""
    import oaklib

    monkeypatch.setattr("dismech.oak_db.local_build_present", lambda spec: False)

    def _refuse(*args, **kwargs):
        raise AssertionError("get_adapter was called for an absent MONDO build")

    monkeypatch.setattr(oaklib, "get_adapter", _refuse)
    anchors = collect_anchors(ENTRY, MRD64, stubs_dir=tmp_path)
    assert anchors.causal_genes == ()


def test_stub_genes_stand_in_for_the_mondo_build(tmp_path, monkeypatch):
    monkeypatch.setattr(research_anchors, "_open_local_mondo", lambda: None)
    (tmp_path / "Spermatogenic_Failure_26.yaml").write_text(
        "mondo_id: MONDO:0054730\nlabel: spermatogenic failure 26\n"
        "genes:\n- id: hgnc:14927\n  label: TSGA10\n"
    )
    (tmp_path / "Other.yaml").write_text(
        "mondo_id: MONDO:0054731\nlabel: other\ngenes:\n- id: hgnc:1\n  label: TDRD9\n"
    )
    anchors = collect_anchors(
        {"name": "Spermatogenic Failure 26"}, "MONDO:0054730", stubs_dir=tmp_path
    )
    assert anchors.causal_genes == ("TSGA10",)
    assert anchors.gene_source == "stub"


def test_entry_causative_genes_are_the_last_resort(tmp_path, monkeypatch):
    monkeypatch.setattr(research_anchors, "_open_local_mondo", lambda: None)
    entry = {
        "name": ENTRY["name"],
        "synonyms": ["MRD64", ENTRY["name"]],
        "genetic": [
            {
                "name": "ZNF292",
                "relationship_type": "CAUSATIVE",
                "gene_term": {"term": {"id": "hgnc:18410", "label": "ZNF292"}},
            },
            {
                "name": "APOE",
                "relationship_type": "RISK_FACTOR",
                "gene_term": {"term": {"id": "hgnc:613", "label": "APOE"}},
            },
        ],
    }
    anchors = collect_anchors(entry, MRD64, stubs_dir=tmp_path)
    assert anchors.causal_genes == ("ZNF292",)
    assert anchors.gene_source == "entry"
    # The entry's own name is not repeated back as a synonym.
    assert anchors.synonyms == ("MRD64",)


def _row(symbol, hgnc, relationship_type=None):
    row = {"name": symbol, "gene_term": {"term": {"id": hgnc, "label": symbol}}}
    if relationship_type:
        row["relationship_type"] = relationship_type
    return row


def test_a_single_untyped_gene_stands_in_when_no_row_is_causative(
    tmp_path, monkeypatch
):
    """Monogenic entries often leave relationship_type unset (Cystic_Fibrosis's CFTR row)."""
    monkeypatch.setattr(research_anchors, "_open_local_mondo", lambda: None)
    entry = {
        "name": "Cystic Fibrosis",
        "genetic": [_row("CFTR", "hgnc:1884"), _row("APOE", "hgnc:613", "MODIFIER")],
    }
    anchors = collect_anchors(entry, "MONDO:0009061", stubs_dir=tmp_path)
    assert anchors.causal_genes == ("CFTR",)
    assert anchors.gene_source == "entry"


def test_several_untyped_genes_are_not_named_as_causal(tmp_path, monkeypatch):
    """Untyped genes in a multigenic entry may be somatic drivers or a differential."""
    monkeypatch.setattr(research_anchors, "_open_local_mondo", lambda: None)
    entry = {
        "name": "Some Cancer",
        "genetic": [_row("BRAF", "hgnc:1097"), _row("MLH1", "hgnc:7127")],
    }
    anchors = collect_anchors(entry, "MONDO:0000000", stubs_dir=tmp_path)
    assert anchors.causal_genes == ()


def test_a_failed_label_lookup_keeps_the_genes_already_found(tmp_path):
    adapter = _mrd64_adapter()
    real_label = adapter.label
    adapter.label = lambda curie: (
        (_ for _ in ()).throw(RuntimeError("boom"))
        if curie == MRD64
        else real_label(curie)
    )
    anchors = collect_anchors(ENTRY, MRD64, adapter=adapter, stubs_dir=tmp_path)
    assert anchors.causal_genes == ("ZNF292",)


def test_a_gene_mondo_holds_only_as_a_bare_curie_is_not_an_anchor(tmp_path):
    adapter = _mrd64_adapter(gene_label=None)
    anchors = collect_anchors(ENTRY, MRD64, adapter=adapter, stubs_dir=tmp_path)
    assert anchors.causal_genes == ()


def test_cli_prints_one_var_per_line(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(research_anchors, "_open_local_mondo", lambda: None)
    entry = tmp_path / "Foo.yaml"
    entry.write_text("name: Foo\nsynonyms:\n- Foo  syndrome\n  type 1\n")
    assert main([str(entry), "", "--stubs-dir", str(tmp_path)]) == 0
    lines = capsys.readouterr().out.splitlines()
    assert lines == [
        f"causal_genes={NOT_RECORDED}",
        f"omim_id={NOT_RECORDED}",
        "synonyms=Foo syndrome type 1",
    ]


def test_template_renders_with_exactly_the_variables_the_recipes_pass():
    """A template variable no recipe passes makes the client refuse the run."""
    from deep_research_client.templates import TemplateManager

    template = TEMPLATE.read_text()
    variables = {"disease_name": "X", "mondo_id": MRD64, "category": "Genetic"}
    variables.update(IdentityAnchors(causal_genes=("ZNF292",)).template_vars())
    assert TemplateManager().get_template_variables(template) == set(variables)
    rendered = TemplateManager().substitute_variables(template, variables)
    assert "**Causal gene(s):** ZNF292" in rendered
    assert "{" + "causal_genes}" not in rendered


@pytest.mark.parametrize("recipe", RECIPES)
def test_recipes_rendering_the_template_pass_the_anchors(recipe):
    text = (ROOT / "project.justfile").read_text()
    match = re.search(
        rf"^{re.escape(recipe)} .*?:\n(.*?)(?=^\S)", text, re.MULTILINE | re.DOTALL
    )
    assert match, recipe
    body = match.group(1)
    assert 'python -m dismech.research_anchors "$yaml_file" "$mondo_id"' in body
    assert '"${anchor_vars[@]}"' in body
