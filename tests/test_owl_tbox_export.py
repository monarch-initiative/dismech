"""Tests for the pathograph OWL TBox exporter (py-horned-owl)."""

from __future__ import annotations

from pathlib import Path

import pyhornedowl
import pytest

from dismech.export.owl_tbox_export import BASE, build, main, node_class_iri

TREE = """\
CELLULAR EFFECT
  cell death -- the cell is lost
    = biological_processes some GO:0008219 'cell death'
    [Toy_Disease] Neuronal Death
TISSUE / ORGAN EFFECT
  inflammation
    = biological_processes some GO:0006954 'inflammatory response' modifier INCREASED and locations some UBERON
"""

MODULE = """\
name: toy_module
pathophysiology:
- name: Cell Loss
"""

DISEASE = """\
name: Toy Disease
disease_term:
  term:
    id: MONDO:0000001
    label: disease
pathophysiology:
- name: Neuronal Death
  conforms_to: "toy_module#Cell Loss"
  biological_processes:
  - preferred_term: cell death
    term:
      id: GO:0008219
      label: cell death
    modifier: INCREASED
  downstream:
  - target: Seizures
  - target: Nothing By This Name
phenotypes:
- name: Seizures
  phenotype_term:
    term:
      id: HP:0001250
      label: Seizure
"""


TREATMENT = """\
treatments:
- name: Antiseizure Medication
  treatment_term:
    preferred_term: Pharmacotherapy
    term:
      id: NCIT:C15986
      label: Pharmacotherapy
  target_phenotypes:
  - preferred_term: Seizure
    term:
      id: HP:0001250
      label: Seizure
"""


@pytest.fixture
def toy_kb(tmp_path: Path) -> tuple[Path, Path]:
    disorders = tmp_path / "disorders"
    modules = tmp_path / "modules"
    disorders.mkdir()
    modules.mkdir()
    (disorders / "Toy_Disease.yaml").write_text(DISEASE)
    (modules / "toy_module.yaml").write_text(MODULE)
    tree = tmp_path / "tree.txt"
    tree.write_text(TREE)
    return tree, tmp_path


def _ofn(tree: Path, root: Path):
    builder = build(tree, [root / "disorders", root / "modules"])
    return builder, builder.onto.save_to_string("ofn")


def test_every_node_gets_its_own_iri(toy_kb):
    tree, root = toy_kb
    builder, _ = _ofn(tree, root)
    classes = {str(c) for c in builder.onto.get_classes()}
    assert f"{BASE}node/Toy_Disease/pathophysiology/Neuronal_Death" in classes
    assert f"{BASE}node/Toy_Disease/phenotype/Seizures" in classes
    assert f"{BASE}node/toy_module/pathophysiology/Cell_Loss" in classes


def test_node_axioms(toy_kb):
    tree, root = toy_kb
    builder, ofn = _ofn(tree, root)
    death = f"{BASE}node/Toy_Disease/pathophysiology/Neuronal_Death"
    # descriptor existential, narrowed by the modifier individual
    assert (
        "SubClassOf(dismech:node/Toy_Disease/pathophysiology/Neuronal_Death "
        "ObjectSomeValuesFrom(dismech:biological_processes ObjectIntersectionOf(obo:GO_0008219 "
        "ObjectHasValue(dismech:modifier dismech:ModifierEnum/INCREASED))))"
    ) in ofn
    supers = {str(s) for s in builder.onto.get_superclasses(death)}
    assert f"{BASE}node/toy_module/pathophysiology/Cell_Loss" in supers  # conforms_to
    assert node_class_iri("CELLULAR_EFFECT__CELL_DEATH") in supers  # tree example
    assert f"{BASE}PathophysiologyNode" in supers
    assert f"{BASE}PhenotypeNode" in {str(s) for s in builder.onto.get_superclasses(f"{BASE}node/Toy_Disease/phenotype/Seizures")}
    seizures = f"{BASE}node/Toy_Disease/phenotype/Seizures"
    assert "http://purl.obolibrary.org/obo/HP_0001250" in {
        str(s) for s in builder.onto.get_superclasses(seizures)
    }
    assert "ObjectSomeValuesFrom(dismech:causes dismech:node/Toy_Disease/phenotype/Seizures)" in ofn
    assert builder.stats.unresolved_targets == [("Toy_Disease", "Neuronal Death", "Nothing By This Name")]


def test_other_node_kinds_and_edges(toy_kb):
    tree, root = toy_kb
    path = root / "disorders" / "Toy_Disease.yaml"
    path.write_text(path.read_text() + TREATMENT)
    builder, ofn = _ofn(tree, root)
    drug = f"{BASE}node/Toy_Disease/treatment/Antiseizure_Medication"
    assert drug in {str(c) for c in builder.onto.get_classes()}
    supers = {str(s) for s in builder.onto.get_superclasses(drug)}
    assert f"{BASE}TreatmentNode" in supers
    assert "http://purl.obolibrary.org/obo/NCIT_C15986" in supers
    assert "ObjectSomeValuesFrom(dismech:treats dismech:node/Toy_Disease/phenotype/Seizures)" in ofn


def test_tree_definitions_become_gcis(toy_kb):
    tree, root = toy_kb
    builder, ofn = _ofn(tree, root)
    assert builder.stats.counts["tree_definitions"] == 2
    assert "ObjectSomeValuesFrom(dismech:locations dismech:AnyTerm/UBERON)" in ofn
    assert "ObjectHasValue(dismech:modifier" in ofn


def test_cli_writes_a_loadable_file(toy_kb, tmp_path):
    tree, root = toy_kb
    out = tmp_path / "out.owx"
    assert main(["-o", str(out), "--tree", str(tree),
                 "--kb-dir", str(root / "disorders"), "--kb-dir", str(root / "modules")]) == 0
    reloaded = pyhornedowl.open_ontology_from_file(str(out))
    assert f"{BASE}node/Toy_Disease/phenotype/Seizures" in {str(c) for c in reloaded.get_classes()}


def test_cli_refuses_functional_syntax(toy_kb, tmp_path):
    tree, root = toy_kb
    with pytest.raises(SystemExit):
        main(["-o", str(tmp_path / "out.ofn"), "--tree", str(tree), "--kb-dir", str(root / "disorders")])


def test_real_tree_parses_into_owl(tmp_path):
    """The committed tree (no KB walk) translates without error."""
    empty = tmp_path / "empty"
    empty.mkdir()
    builder = build(kb_dirs=[empty])
    assert builder.stats.counts["tree_classes"] > 50
    assert builder.stats.counts["tree_definitions"] > 30
