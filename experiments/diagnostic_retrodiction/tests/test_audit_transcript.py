"""Unit tests for audit_transcript.py on synthetic transcripts.

Run: uv run pytest experiments/diagnostic_retrodiction/tests -q
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import audit_transcript as at  # noqa: E402

PACKET = {"11111111", "22222222"}


def line(role, *blocks):
    return json.dumps({"type": role, "message": {"role": role, "content": list(blocks)}})


def tool(name, **inp):
    return {"type": "tool_use", "id": "t", "name": name, "input": inp}


def text(t):
    return {"type": "text", "text": t}


def kinds(lines, leakage=(), exclude=()):
    return sorted(e.kind for e in at.audit(lines, PACKET, list(leakage), list(exclude)))


def test_clean_transcript_has_no_events():
    lines = [line("assistant", text("Reading the packet."), tool("Read", file_path="run/packet/packet.tsv")),
             line("user", {"type": "tool_result", "tool_use_id": "t", "content": "PMID:99999999 is in a file"}),
             line("assistant", text("Citing PMID:11111111 and PMID:22222222."))]
    assert kinds(lines) == []


def test_web_tools_and_codex_are_events():
    lines = [line("assistant", tool("WebSearch", query="x")), line("assistant", tool("WebFetch", url="u")),
             line("assistant", tool("mcp__codex__codex", prompt="p"))]
    assert kinds(lines) == ["WEB_TOOL", "WEB_TOOL", "WEB_TOOL"]


def test_network_and_inline_interpreter_commands():
    cmds = ["curl https://x", "wget x", "python3 -c 'import urllib'", "uv run python x.py # eutils",
            "node -e 'fetch()'"]
    lines = [line("assistant", tool("Bash", command=c)) for c in cmds]
    assert kinds(lines).count("NETWORK_COMMAND") == len(cmds)


def test_ordinary_bash_is_not_an_event():
    assert kinds([line("assistant", tool("Bash", command="just validate kb/disorders/X.yaml"))]) == []


def test_out_of_packet_pmid_in_tool_input_and_text():
    lines = [line("assistant", tool("Write", file_path="kb/disorders/X.yaml", content="reference: PMID:33333333")),
             line("assistant", text("see PMID 44444444"))]
    assert kinds(lines) == ["OUT_OF_PACKET_PMID", "OUT_OF_PACKET_PMID"]


def test_pmids_in_tool_results_are_not_scanned():
    lines = [line("user", {"type": "tool_result", "tool_use_id": "t", "content": "PMID:55555555"})]
    assert kinds(lines) == []


def test_excluded_paths():
    lines = [line("assistant", tool("Read", file_path="references_cache/PMID_1.md")),
             line("assistant", tool("Bash", command="cat references_cache/PMID_2.md"))]
    assert kinds(lines, exclude=["references_cache/**"]) == ["EXCLUDED_PATH", "EXCLUDED_PATH"]


def test_leakage_term_whole_word_and_nmo_alone_is_not_an_alarm():
    lines = [line("assistant", text("Neuromyelitis optica (NMO) affects the optic nerve."))]
    assert kinds(lines, leakage=["NMO-IgG", "AQP4"]) == []
    lines = [line("assistant", text("Propose testing NMO-IgG in serum."))]
    assert kinds(lines, leakage=["NMO-IgG"]) == ["LEAKAGE_TERM"]


def test_leakage_term_does_not_match_inside_longer_token():
    lines = [line("assistant", text("The AQP4x construct"))]
    assert kinds(lines, leakage=["AQP4"]) == []


def test_unicode_leakage_term():
    lines = [line("assistant", text("Measure Aβ42 in CSF"))]
    assert kinds(lines, leakage=["Aβ42"]) == ["LEAKAGE_TERM"]


def test_unparseable_line_is_an_event():
    assert kinds(["{not json"]) == ["UNPARSEABLE_LINE"]


def test_leakage_terms_read_only_in_packet_no(tmp_path):
    r = tmp_path / "r.yaml"
    r.write_text("leakage_terms:\n- {term: A, in_packet: 'yes'}\n- {term: B, in_packet: 'no'}\n", encoding="utf-8")
    assert at.leakage_terms(r) == ["B"]
