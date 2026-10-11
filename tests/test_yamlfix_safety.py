"""Regression coverage for syntax-blind formatter rewrites (#12101, #9613)."""

import tomllib
from pathlib import Path

import pytest
import yaml
from yamlfix.model import YamlfixConfig

from scripts import check_block_scalar_comments as gate
from scripts import yamlfix_safe as hook

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def config():
    return YamlfixConfig(**tomllib.loads((ROOT / ".yamlfix.toml").read_text()))


@pytest.mark.parametrize("style", [">", ">-", ">+", "|", "|-", "|+", ">2-", "|2+"])
def test_comment_text_survives_formatting(tmp_path, config, style):
    path = tmp_path / "entry.yaml"
    source = f"snippet: {style}\n  While CACHE #3 participants\n  tested item #12.\nother: value\n"
    path.write_text(source)
    hook.format_file(path, config)
    assert yaml.safe_load(path.read_text()) == yaml.safe_load(source)
    assert "CACHE #3" in path.read_text()
    assert not hook.format_file(path, config)


@pytest.mark.parametrize("style", [">-", "|-"])
@pytest.mark.parametrize("ending", [": no", "- no", ": yes", ": on", ": off", ": NO"])
def test_boolean_prose_is_rejected_before_writing(tmp_path, config, style, ending):
    path = tmp_path / "entry.yaml"
    source = f"notes: {style}\n  The response is{ending}\n  according to the source.\n"
    path.write_text(source)
    with pytest.raises(ValueError, match="file left untouched"):
        hook.format_file(path, config)
    assert path.read_text() == source


def test_guard_also_catches_default_comment_rewrite(tmp_path):
    path = tmp_path / "entry.yaml"
    source = "snippet: >-\n  CACHE #3 participants\n"
    path.write_text(source)
    with pytest.raises(ValueError, match="parsed YAML data"):
        hook.format_file(path, YamlfixConfig())
    assert path.read_text() == source


def test_guard_rejects_loss_of_block_scalar_final_newline(tmp_path, config):
    # Another syntax-blind rewrite: yamlfix strips a significant final newline
    # when a clipped block scalar is the last value in the document.
    path = tmp_path / "entry.yaml"
    source = "notes: |\n  prose\n"
    path.write_text(source)
    with pytest.raises(ValueError, match="parsed YAML data"):
        hook.format_file(path, config)
    assert path.read_text() == source


def test_invalid_formatter_output_never_reaches_file(tmp_path, config, monkeypatch):
    path = tmp_path / "entry.yaml"
    source = "notes: prose\n"
    path.write_text(source)
    monkeypatch.setattr(hook, "fix_code", lambda *_: "notes: [unclosed\n")
    with pytest.raises(yaml.YAMLError):
        hook.format_file(path, config)
    assert path.read_text() == source


def test_quoted_workaround_and_real_boolean_formatting(tmp_path, config):
    path = tmp_path / "entry.yaml"
    source = 'notes: "CACHE #3: no"\nliteral: "response: no\\n"\nflag: True\n'
    path.write_text(source)
    assert hook.format_file(path, config)
    assert yaml.safe_load(path.read_text()) == yaml.safe_load(source)
    assert "flag: true" in path.read_text()
    assert not hook.format_file(path, config)


@pytest.mark.parametrize(
    ("before", "after"),
    [("x: true", "x: 1"), ("x: 1", "x: 1.0"), ('x: "a  b"', 'x: "a b"')],
)
def test_comparison_preserves_types_and_whitespace(before, after):
    assert hook.canonical_data(before) != hook.canonical_data(after)


def test_comparison_accepts_order_quoting_nan_and_aliases():
    assert hook.canonical_data("x: .nan\ny: &a [1, 2]\nz: *a") == hook.canonical_data(
        'z: &b [1, 2]\ny: *b\n"x": .NaN'
    )


def test_cli_processes_other_files_after_refusal(tmp_path, capsys):
    bad, good = tmp_path / "bad.yaml", tmp_path / "good.yaml"
    bad.write_text("notes: >-\n  response: no\n")
    original = bad.read_bytes()
    good.write_text("flag: True\n")
    args = ["-c", str(ROOT / ".yamlfix.toml"), str(bad), str(good)]
    assert hook.main(args) == 1
    assert bad.read_bytes() == original
    assert good.read_text() == "flag: true\n"
    assert str(bad) in capsys.readouterr().err
    assert hook.main(["-c", str(ROOT / ".yamlfix.toml"), str(good)]) == 0


@pytest.mark.parametrize("style", [">", ">-", ">+", "|", "|-", "|+", ">2-", "|2+"])
def test_gate_finds_only_block_content(style):
    source = (
        "# actual comment  # 12\n"
        'quoted: "CACHE  # 3"\n'
        f"items:\n- text: {style}  # 3 in header\n"
        "    CACHE  # 3 participants\n"
        "    continued\n"
        "  other: fine  # 12 real comment\n"
    )
    assert gate.find_corruption(source) == [5]


def test_gate_does_not_guess_blocks_inside_multiline_quotes():
    assert gate.find_corruption('text: "fake: >-\n  CACHE  # 3"\n') == []
    assert gate.find_corruption("text: >-\n  CACHE #3\n  issue #12101\n") == []


def test_gate_handles_unicode_blank_lines_and_multiple_documents():
    source = (
        "name: β\ntext: |+\n  first\n\n  CACHE  # 3\n---\ntext: >-\n  issue  # 12\n"
    )
    assert gate.find_corruption(source) == [5, 8]


def test_gate_cli_default_tree_and_failures(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(gate, "ROOT", tmp_path)
    baseline = tmp_path / "baseline.txt"
    baseline.write_text("")
    monkeypatch.setattr(gate, "BASELINE", baseline)
    kb = tmp_path / "kb" / "modules"
    kb.mkdir(parents=True)
    entry = kb / "entry.yml"
    entry.write_text("notes: >-\n  CACHE  # 3\n")
    assert gate.main([]) == 1
    assert "1 suspicious line(s) in 1 of 1" in capsys.readouterr().out
    entry.write_text("notes: >-\n  CACHE #3\n")
    assert gate.main([]) == 0
    entry.write_text("x: [unclosed\n")
    assert gate.main([]) == 1
    assert "could not check" in capsys.readouterr().err
    entry.unlink()
    assert gate.main([str(entry)]) == 1


def test_baseline_counts_copies_and_only_shrinks(tmp_path, monkeypatch):
    monkeypatch.setattr(gate, "ROOT", tmp_path)
    baseline = tmp_path / "baseline.txt"
    monkeypatch.setattr(gate, "BASELINE", baseline)
    kb = tmp_path / "kb"
    kb.mkdir()
    entry = kb / "entry.yaml"
    source = "notes: >-\n  CACHE  # 3\n"
    entry.write_text(source)
    key = ("kb/entry.yaml", "CACHE  # 3")
    gate.write_baseline(baseline, gate.Counter({key: 1}))
    assert gate.main([]) == 0
    assert gate.main(["--strict"]) == 1
    # Moving a line is harmless, duplicating it or copying to another file is new.
    entry.write_text("# heading\n" + source)
    assert gate.main([]) == 0
    entry.write_text(source + "  CACHE  # 3\n")
    assert gate.main(["--update-baseline"]) == 1
    assert gate.read_baseline(baseline)[key] == 1
    entry.write_text(source)
    copy = kb / "copy.yaml"
    copy.write_text(source)
    assert gate.main(["--update-baseline"]) == 1
    assert len(gate.read_baseline(baseline)) == 1
    copy.unlink()
    entry.write_text("notes: clean\n")
    assert gate.main(["--update-baseline"]) == 0
    assert not gate.read_baseline(baseline)
    entry.write_text(source)
    assert gate.main([]) == 1


def test_baseline_update_refuses_partial_or_invalid_scan(tmp_path, monkeypatch):
    monkeypatch.setattr(gate, "ROOT", tmp_path)
    baseline = tmp_path / "baseline.txt"
    baseline.write_text('["kb/entry.yaml", "CACHE  # 3", 1]\n')
    monkeypatch.setattr(gate, "BASELINE", baseline)
    original = baseline.read_bytes()
    with pytest.raises(SystemExit):
        gate.main(["--update-baseline", "kb/entry.yaml"])
    kb = tmp_path / "kb"
    kb.mkdir()
    (kb / "bad.yaml").write_text("x: [unclosed\n")
    assert gate.main(["--update-baseline"]) == 1
    assert baseline.read_bytes() == original
    baseline.unlink()
    assert gate.main([]) == 1


@pytest.mark.ci_step_twin("scripts/check_block_scalar_comments.py")
def test_committed_kb_has_no_new_block_scalar_corruption():
    assert gate.main([]) == 0


def test_hook_pin_and_entry_match_tested_formatter():
    from importlib.metadata import version

    config = yaml.safe_load((ROOT / ".pre-commit-config.yaml").read_text())
    repo = next(repo for repo in config["repos"] if repo["repo"].endswith("/yamlfix"))
    assert repo["rev"] == version("yamlfix")
    assert repo["hooks"][0]["entry"] == "python scripts/yamlfix_safe.py"
