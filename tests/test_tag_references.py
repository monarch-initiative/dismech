"""Tests for `scripts/tag_references.py` tag insertion.

The script edits YAML as text to preserve formatting, so its correctness rests on
reading the two list styles a `tags:` value can be written in. It was the sole
writer of the slot until `ReferenceTagEnum` grew curator-applied values
(PatientOrganization, PatientCommunity), which is what made these paths
reachable on entries it did not write itself.

Both failure modes are covered here because both produced broken YAML on real
`kb/` files: writing a second `tags:` key into one mapping (the #8623
duplicate-key defect, where the loader keeps the last and existing tags vanish),
and appending a block item after a completed flow-style list (a hard parse
error).
"""

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]

_SPEC = importlib.util.spec_from_file_location(
    "tag_references", REPO_ROOT / "scripts" / "tag_references.py"
)
tag_references = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = tag_references
_SPEC.loader.exec_module(tag_references)


def _entry_lines(body: str) -> tuple[list[str], int, int]:
    """Split a `references:` document into (lines, entry_start, section_end)."""
    lines = body.split("\n")
    sec_start, sec_end = tag_references.find_references_section(lines)
    entry_start = tag_references.top_level_ref_ids(lines, sec_start, sec_end)[
        "PMID:20301616"
    ]
    return lines, entry_start, sec_end


def _add_tag(body: str, tag: str = "GeneReviews") -> str:
    lines, entry_start, sec_end = _entry_lines(body)
    return "\n".join(
        tag_references.add_tag_to_existing_entry(lines, entry_start, sec_end, tag)
    )


def _has_tag(body: str, tag: str = "GeneReviews") -> bool:
    lines, entry_start, sec_end = _entry_lines(body)
    return tag_references.has_tag_in_entry(lines, entry_start, sec_end, tag)


NO_TAGS = """references:
- reference: PMID:20301616
  title: "GeneReviews chapter"
"""

BLOCK_TAGS = """references:
- reference: PMID:20301616
  title: "GeneReviews chapter"
  tags:
  - PatientOrganization
"""

FLOW_TAGS = """references:
- reference: PMID:20301616
  title: "GeneReviews chapter"
  tags: [GeneReviews]
"""

FLOW_TAGS_OTHER = """references:
- reference: PMID:20301616
  title: "GeneReviews chapter"
  tags: [PatientOrganization]
"""

FLOW_TAGS_EMPTY = """references:
- reference: PMID:20301616
  title: "GeneReviews chapter"
  tags: []
"""


@pytest.mark.parametrize(
    "body", [NO_TAGS, BLOCK_TAGS, FLOW_TAGS_OTHER, FLOW_TAGS_EMPTY]
)
def test_adding_a_tag_leaves_parseable_yaml_with_one_tags_key(body):
    """Every insertion path yields valid YAML carrying a single `tags:` key."""
    result = _add_tag(body)
    doc = yaml.safe_load(result)  # raises on the flow-style append defect
    entry = doc["references"][0]
    assert "GeneReviews" in entry["tags"]
    # A second `tags:` key would be silently swallowed by the loader, so count
    # the text occurrences rather than trusting the parsed mapping.
    assert result.count("tags:") == 1


def test_existing_block_tags_are_preserved():
    """Appending to a block list keeps the tag already there."""
    doc = yaml.safe_load(_add_tag(BLOCK_TAGS))
    assert doc["references"][0]["tags"] == ["PatientOrganization", "GeneReviews"]


def test_existing_flow_tags_are_preserved_and_stay_flow_style():
    """A flow list is rewritten in place, not converted to block style."""
    result = _add_tag(FLOW_TAGS_OTHER)
    assert "  tags: [PatientOrganization, GeneReviews]" in result
    assert yaml.safe_load(result)["references"][0]["tags"] == [
        "PatientOrganization",
        "GeneReviews",
    ]


def test_flow_style_tag_is_detected_as_already_present():
    """`tags: [GeneReviews]` counts as tagged, so nothing is written.

    Reading only block items here is what made the script treat an already-tagged
    entry as untagged and then append into its completed list.
    """
    assert _has_tag(FLOW_TAGS) is True
    assert _has_tag(FLOW_TAGS_OTHER) is False
    assert _has_tag(BLOCK_TAGS, "PatientOrganization") is True
    assert _has_tag(NO_TAGS) is False


def test_flow_tag_items_parses_both_empty_and_populated_lists():
    assert tag_references.flow_tag_items("  tags: []") == []
    assert tag_references.flow_tag_items("  tags: [GeneReviews]") == ["GeneReviews"]
    assert tag_references.flow_tag_items('  tags: ["A", B]') == ["A", "B"]
    assert tag_references.flow_tag_items("  tags:") is None
    assert tag_references.flow_tag_items("  - GeneReviews") is None


def test_committed_flow_style_entries_are_left_alone(tmp_path):
    """The tagger is a no-op on the real `kb/` entries written in flow style.

    `Autosomal_Dominant_Charcot-Marie-Tooth_Disease_Type_2W.yaml` carries
    `tags: [GeneReviews]` on PMID:20301532 and is the file that reproduced the
    parse failure.
    """
    flow_files = [
        path
        for path in sorted((REPO_ROOT / "kb" / "disorders").glob("*.yaml"))
        if "tags: [" in path.read_text(encoding="utf-8")
    ]
    assert flow_files, "expected at least one flow-style `tags:` entry in kb/"

    for source in flow_files:
        target = tmp_path / source.name
        original = source.read_text(encoding="utf-8")
        target.write_text(original, encoding="utf-8")
        tag_references.tag_disorder_file(
            target, REPO_ROOT / "references_cache", dry_run=False
        )
        updated = target.read_text(encoding="utf-8")
        yaml.safe_load(updated)
        assert updated == original, f"{source.name} was rewritten"
