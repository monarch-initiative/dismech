"""The two ways a drug-or-exposure search returns a confidently wrong answer.

Both of these shipped in review and both were silent: the scripts ran, exited 0
and printed a plausible report.

``entity_path_locator.py`` answers "is this mention a curated identity or just
prose", and it did so by looking one level under a term-bearing slot for a
string. The CURIE on a treatment or an exposure sits two levels down, at
``<slot>.term.id``, so every treatment and every exposure came back as having no
bound term, while a free-text ``preferred_term`` was counted as a binding.

``drug_exposure_query.py`` resolves a name to CURIEs, and matched the bound
label and the holder name. CHEBI labels a substance systematically where
curators prefer the clinical name -- ``CHEBI:15765`` is ``L-dopa``, preferred as
``levodopa`` -- so the headline query missed the substance its own documentation
warns about. Reading ``preferred_term`` fixes that, but only where it names the
descriptor's own term: on a ``TreatmentDescriptor`` it names the treatment as a
whole ("levodopa pharmacotherapy") while the term is the action
(``NCIT:C15986``), and trusting it there resolves the action as if it were the
drug.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from drug_exposure_query import PROBES, Query, collect, walk_terms
from entity_path_locator import bound_terms

# A treatment shaped like the real schema: the action on the descriptor, the
# substances in therapeutic_agent, the clinical name only in preferred_term.
TREATMENT = {
    "name": "Levodopa/Carbidopa",
    "treatment_term": {
        "preferred_term": "Pharmacotherapy",
        "term": {"id": "NCIT:C15986", "label": "Pharmacotherapy"},
        "therapeutic_agent": [
            {"preferred_term": "levodopa", "term": {"id": "CHEBI:15765", "label": "L-dopa"}},
            {"preferred_term": "carbidopa", "term": {"id": "CHEBI:3395", "label": "carbidopa"}},
        ],
    },
}

BOUND_EXPOSURE = {
    "name": "Pesticide Exposure",
    "exposure_term": {
        "preferred_term": "exposure to pesticide",
        "term": {"id": "ECTO:0000530", "label": "exposure to pesticide"},
    },
}

# A real pattern: an exposure curated by name with nothing bound to it.
UNBOUND_EXPOSURE = {"name": "Rural Living", "description": "Residence in a rural area."}


class TestBoundTerms:
    def test_finds_the_curie_two_levels_down(self):
        """The action term is at treatment_term.term.id, not directly under the holder."""
        assert "treatment_term.term.id=NCIT:C15986" in bound_terms(TREATMENT)

    def test_finds_the_agent_curies_below_the_descriptor(self):
        found = bound_terms(TREATMENT)
        agents = [b for b in found if "therapeutic_agent" in b]
        assert "treatment_term.therapeutic_agent[].term.id=CHEBI:15765" in agents
        assert "treatment_term.therapeutic_agent[].term.id=CHEBI:3395" in agents

    def test_finds_an_exposure_curie(self):
        assert bound_terms(BOUND_EXPOSURE) == ["exposure_term.term.id=ECTO:0000530"]

    def test_free_text_is_not_a_binding(self):
        """An exposure with a name and a description binds nothing."""
        assert bound_terms(UNBOUND_EXPOSURE) == []

    def test_preferred_term_alone_is_not_a_binding(self):
        """preferred_term is the label a curator chose, not an identifier."""
        holder = {"name": "Some therapy", "treatment_term": {"preferred_term": "levodopa"}}
        assert bound_terms(holder) == []

    def test_preferred_term_in_a_list_item_is_not_a_binding(self):
        """A latent case, pinned rather than observed.

        The old code read ``preferred_term`` from list items, so a term slot
        holding a list of free text counted as bound. No holder in the KB puts a
        list at one of those slots, so this never fired -- which is exactly why
        it is worth a test rather than a note.
        """
        assert bound_terms({"name": "x", "term": [{"preferred_term": "levodopa"}]}) == []


class TestPreferredTermResolution:
    def test_walk_terms_hands_back_the_descriptors_preferred_term(self):
        pairs = list(walk_terms(TREATMENT, "treatment_term.therapeutic_agent[].term"))
        assert [(t["id"], p) for t, p in pairs] == [
            ("CHEBI:15765", "levodopa"),
            ("CHEBI:3395", "carbidopa"),
        ]

    def test_a_systematic_label_is_reached_through_preferred_term(self):
        q = Query(terms=["levodopa"], curies=[])
        # "levodopa" is in neither the label nor this descriptor's own name.
        assert q.matches_term("CHEBI:15765", "L-dopa", "", "levodopa") == "preferred_term"

    def test_the_label_still_wins_when_it_matches(self):
        q = Query(terms=["l-dopa"], curies=[])
        assert q.matches_term("CHEBI:15765", "L-dopa", "", "levodopa") == "label"

    def test_the_treatment_action_slot_does_not_trust_preferred_term(self):
        """Otherwise 'levodopa pharmacotherapy' resolves NCIT:C15986 as the drug."""
        therapy = next(p for p in PROBES if p["role"] == "therapy")
        assert "treatment_term.term" in therapy["action_paths"]
        assert "treatment_term.therapeutic_agent[].term" not in therapy["action_paths"]


class TestEndToEnd:
    def _kb(self, tmp_path: Path, name: str, body: str) -> Path:
        (tmp_path / "kb" / "disorders").mkdir(parents=True, exist_ok=True)
        (tmp_path / "kb" / "disorders" / name).write_text(body, encoding="utf-8")
        return tmp_path

    def test_a_clinical_name_resolves_the_substance(self, tmp_path):
        repo = self._kb(tmp_path, "Parkinsonism.yaml", """
name: Parkinsonism
disease_term:
  term: {id: "MONDO:0005180", label: "Parkinson disease"}
treatments:
- name: Levodopa/Carbidopa
  treatment_term:
    preferred_term: Pharmacotherapy
    term: {id: "NCIT:C15986", label: Pharmacotherapy}
    therapeutic_agent:
    - preferred_term: levodopa
      term: {id: "CHEBI:15765", label: L-dopa}
""")
        q = Query(terms=["levodopa"], curies=[])
        res = collect(repo, ["kb/disorders/*.yaml"], q)
        assert "CHEBI:15765" in res["resolved"]

    def test_a_drug_named_in_a_treatment_descriptor_does_not_resolve_the_action(self, tmp_path):
        repo = self._kb(tmp_path, "Neuronopathy.yaml", """
name: Neuronopathy
disease_term:
  term: {id: "MONDO:0011142", label: Neuronopathy}
treatments:
- name: Dopaminergic trial
  treatment_term:
    preferred_term: levodopa pharmacotherapy
    term: {id: "NCIT:C15986", label: Pharmacotherapy}
""")
        q = Query(terms=["levodopa"], curies=[])
        res = collect(repo, ["kb/disorders/*.yaml"], q)
        assert "NCIT:C15986" not in res["resolved"]


class TestRoleVocabulary:
    """The two scripts are documented as a pair, so one role name per block.

    ``docs/searching_drugs_and_exposures_in_dismech.md`` runs the query script
    and then the inventory, and invites reading the two outputs together. They
    each carry a ``role`` column, and five blocks named the same thing twice:
    ``pathophysiology`` was ``mechanism_node`` in one and ``mechanism`` in the
    other, and ``biochemical``, ``datasets``, ``computational_models`` and
    ``discussions`` were a hand-chosen name against the bare slot name. A join
    or a filter on role silently returned nothing for those blocks.
    """

    def _query_roles(self) -> dict[str, str]:
        from drug_exposure_query import PROBES, PROPOSED_PROBE

        roles = {p["block"]: p["role"] for p in PROBES}
        roles[PROPOSED_PROBE["block"]] = PROPOSED_PROBE["role"]
        return roles

    def test_every_shared_block_has_one_role_name(self):
        from chemical_binding_inventory import ROLE_BY_ROOT

        disagree = {
            block: (role, ROLE_BY_ROOT.get(block, block))
            for block, role in self._query_roles().items()
            if ROLE_BY_ROOT.get(block, block) != role
        }
        assert disagree == {}, f"same block, two role names: {disagree}"

    def test_the_inventory_names_every_block_the_query_probes(self):
        """A block left out of the map falls back to its slot name, silently."""
        from chemical_binding_inventory import ROLE_BY_ROOT

        missing = sorted(set(self._query_roles()) - set(ROLE_BY_ROOT))
        assert missing == [], f"not in ROLE_BY_ROOT, so named by fallback: {missing}"
