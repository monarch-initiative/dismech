"""Tests for the Orphanet disorder-disorder association / status-flag parsing.

Unlike ``tests/test_structured_sources.py``, this uses a small inline
``en_product1.xml`` fixture rather than the gitignored bulk Orphadata download,
so it always runs in CI. It locks down two things: the "Moved to"
deprecation/merge relation rendering (issue surfaced in PR #8707 review), and
the guard against an association side with no ``OrphaCode`` (which previously
crashed the ``## Related disorders`` sort key with ``int("")``).
"""

from __future__ import annotations

from pathlib import Path

import pytest

from dismech.structured_sources.orphanet import OrphanetSource

# Three disorders:
#   988  — survives; two other concepts were "Moved to" it.
#   2950 — deprecated ("Inactive" + "Deprecated entity" flags, one flag with an
#          empty Label that must be dropped), "Moved to" 988.
#   3332 — a second concept "Moved to" 988, to check multi-row sorting.
#   9999 — a "Referred to" association whose non-cycle side has no
#          <OrphaCode> child at all — must be dropped, not crash.
PRODUCT1_XML = """<?xml version="1.0" encoding="UTF-8"?>
<JDBOR date="2025-12-09 00:00:00" version="test">
  <DisorderList count="4">
    <Disorder id="1303">
      <OrphaCode>988</OrphaCode>
      <ExpertLink lang="en">http://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&amp;Expert=988</ExpertLink>
      <Name lang="en">Tibial hemimelia-polysyndactyly-triphalangeal thumb syndrome</Name>
      <DisorderFlagList count="1">
        <DisorderFlag id="475">
          <Value>1</Value>
          <Label></Label>
        </DisorderFlag>
      </DisorderFlagList>
      <SynonymList count="0"></SynonymList>
      <DisorderType id="21401"><Name lang="en">Malformation syndrome</Name></DisorderType>
      <DisorderGroup id="36547"><Name lang="en">Disorder</Name></DisorderGroup>
      <ExternalReferenceList count="0"></ExternalReferenceList>
      <DisorderDisorderAssociationList count="2">
        <DisorderDisorderAssociation>
          <TargetDisorder id="1303" cycle="true"/>
          <RootDisorder id="2662">
            <OrphaCode>2950</OrphaCode>
            <Name lang="en">Triphalangeal thumb-polysyndactyly syndrome</Name>
          </RootDisorder>
          <DisorderDisorderAssociationType id="21471"><Name lang="en">Moved to</Name></DisorderDisorderAssociationType>
        </DisorderDisorderAssociation>
        <DisorderDisorderAssociation>
          <TargetDisorder id="1303" cycle="true"/>
          <RootDisorder id="2956">
            <OrphaCode>3332</OrphaCode>
            <Name lang="en">Hypoplastic tibiae-postaxial polydactyly syndrome</Name>
          </RootDisorder>
          <DisorderDisorderAssociationType id="21471"><Name lang="en">Moved to</Name></DisorderDisorderAssociationType>
        </DisorderDisorderAssociation>
      </DisorderDisorderAssociationList>
      <SummaryInformationList count="0"></SummaryInformationList>
    </Disorder>
    <Disorder id="2662">
      <OrphaCode>2950</OrphaCode>
      <ExpertLink lang="en">http://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&amp;Expert=2950</ExpertLink>
      <Name lang="en">Triphalangeal thumb-polysyndactyly syndrome</Name>
      <DisorderFlagList count="3">
        <DisorderFlag id="495"><Value>8192</Value><Label>Inactive</Label></DisorderFlag>
        <DisorderFlag id="459"><Value>256</Value><Label>Deprecated entity</Label></DisorderFlag>
        <DisorderFlag id="475"><Value>1</Value><Label></Label></DisorderFlag>
      </DisorderFlagList>
      <SynonymList count="0"></SynonymList>
      <DisorderType id="21401"><Name lang="en">Malformation syndrome</Name></DisorderType>
      <DisorderGroup id="36547"><Name lang="en">Disorder</Name></DisorderGroup>
      <ExternalReferenceList count="0"></ExternalReferenceList>
      <DisorderDisorderAssociationList count="1">
        <DisorderDisorderAssociation>
          <TargetDisorder id="1303">
            <OrphaCode>988</OrphaCode>
            <Name lang="en">Tibial hemimelia-polysyndactyly-triphalangeal thumb syndrome</Name>
          </TargetDisorder>
          <RootDisorder id="2662" cycle="true"/>
          <DisorderDisorderAssociationType id="21471"><Name lang="en">Moved to</Name></DisorderDisorderAssociationType>
        </DisorderDisorderAssociation>
      </DisorderDisorderAssociationList>
      <SummaryInformationList count="0"></SummaryInformationList>
    </Disorder>
    <Disorder id="9999">
      <OrphaCode>9999</OrphaCode>
      <Name lang="en">Malformed-association test disorder</Name>
      <SynonymList count="0"></SynonymList>
      <DisorderType id="21401"><Name lang="en">Malformation syndrome</Name></DisorderType>
      <DisorderGroup id="36547"><Name lang="en">Disorder</Name></DisorderGroup>
      <ExternalReferenceList count="0"></ExternalReferenceList>
      <DisorderDisorderAssociationList count="1">
        <DisorderDisorderAssociation>
          <TargetDisorder id="9999" cycle="true"/>
          <RootDisorder id="424242"/>
          <DisorderDisorderAssociationType id="21471"><Name lang="en">Referred to</Name></DisorderDisorderAssociationType>
        </DisorderDisorderAssociation>
      </DisorderDisorderAssociationList>
      <SummaryInformationList count="0"></SummaryInformationList>
    </Disorder>
  </DisorderList>
</JDBOR>
"""


@pytest.fixture()
def orphanet_source(tmp_path: Path) -> OrphanetSource:
    (tmp_path / "en_product1.xml").write_text(PRODUCT1_XML, encoding="utf-8")
    src = OrphanetSource(tmp_path)
    src.index()
    return src


def test_status_flags_drop_empty_labels(orphanet_source: OrphanetSource):
    idx = orphanet_source.index()
    assert idx["988"].status_flags == []
    assert idx["2950"].status_flags == ["Deprecated entity", "Inactive"]


def test_related_disorders_capture_moved_to(orphanet_source: OrphanetSource):
    idx = orphanet_source.index()
    rec_988 = idx["988"]
    assert len(rec_988.related_disorders) == 2
    codes = {(r[0], r[3]) for r in rec_988.related_disorders}
    assert codes == {("2950", "988"), ("3332", "988")}

    rec_2950 = idx["2950"]
    assert rec_2950.related_disorders == [
        ("2950", "Triphalangeal thumb-polysyndactyly syndrome", "Moved to", "988",
         "Tibial hemimelia-polysyndactyly-triphalangeal thumb syndrome")
    ]


def test_malformed_association_side_is_dropped_not_crashed(
    orphanet_source: OrphanetSource,
):
    """An association side lacking <OrphaCode> must be skipped, not raise.

    Regression test for the ``int("")`` crash in the ``## Related disorders``
    sort key when the non-cycle side of an association has no OrphaCode child.
    """
    idx = orphanet_source.index()
    assert idx["9999"].related_disorders == []
    # Rendering must not raise either — the bug reproduced during serialize().
    text = orphanet_source.serialize("9999").render()
    assert "## Related disorders" not in text


def test_serialize_renders_status_and_related_disorders_sections(
    orphanet_source: OrphanetSource,
):
    text_988 = orphanet_source.serialize("988").render()
    assert "## Related disorders" in text_988
    assert "| Root | Root Disorder | Relation | Target | Target Disorder |" in text_988
    assert (
        "| ORPHA:2950 | Triphalangeal thumb-polysyndactyly syndrome | Moved to | "
        "ORPHA:988 | Tibial hemimelia-polysyndactyly-triphalangeal thumb "
        "syndrome |"
    ) in text_988
    assert (
        "| ORPHA:3332 | Hypoplastic tibiae-postaxial polydactyly syndrome | "
        "Moved to | ORPHA:988 | Tibial hemimelia-polysyndactyly-triphalangeal "
        "thumb syndrome |"
    ) in text_988
    assert "**Status:**" not in text_988  # only the unlabeled flag present

    text_2950 = orphanet_source.serialize("2950").render()
    assert "**Status:** Deprecated entity; Inactive" in text_2950
    # The committed KB snippet quotes these two lines as one contiguous span
    # across the blank line between them (see ZRS-Related_Limb_Malformation.yaml's
    # ORPHA:2950 evidence item) -- pin the adjacency, not just each line in
    # isolation, so a renderer change that inserted a section between them
    # would be caught here instead of only at the next reference-validation run.
    assert (
        "**ORPHA:2950** — Triphalangeal thumb-polysyndactyly syndrome "
        "(Malformation syndrome, Disorder)\n\n"
        "**Status:** Deprecated entity; Inactive"
    ) in text_2950
    assert (
        "| ORPHA:2950 | Triphalangeal thumb-polysyndactyly syndrome | Moved to | "
        "ORPHA:988 | Tibial hemimelia-polysyndactyly-triphalangeal thumb "
        "syndrome |"
    ) in text_2950


def test_serialize_is_byte_deterministic(orphanet_source: OrphanetSource):
    for code in ["988", "2950", "9999"]:
        a = orphanet_source.serialize(code).render()
        b = orphanet_source.serialize(code).render()
        assert a == b, f"non-deterministic serialization for ORPHA:{code}"
