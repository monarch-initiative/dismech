"""A full disk is reported as an environment error, not a content finding.

Regression cover for dismech#13119: the baseline gates extract ``kb/`` at
``origin/main`` into TMPDIR, and on a full disk they died with an ``OSError``
traceback that read like a content failure.
"""

import errno

import pytest

from dismech.disk_full import EXIT_DISK_FULL, is_disk_full, reports_disk_full
from scripts import (
    check_reference_titles,
    check_snippet_grading,
    check_snippet_length,
    check_title_snippets,
)


def _enospc(*_args, **_kwargs):
    raise OSError(errno.ENOSPC, "No space left on device", "/tmp/x/kb/disorders/A.yaml")


def test_is_disk_full_recognizes_enospc_and_quota():
    assert is_disk_full(OSError(errno.ENOSPC, "No space left on device"))
    assert is_disk_full(OSError(errno.EDQUOT, "Disk quota exceeded"))
    assert not is_disk_full(OSError(errno.EACCES, "Permission denied"))
    assert not is_disk_full(ValueError("not an OSError"))


def test_disk_full_exits_with_a_distinct_code_and_says_it_is_the_environment(capsys):
    @reports_disk_full("check-example")
    def main():
        _enospc()

    assert main() == EXIT_DISK_FULL
    assert EXIT_DISK_FULL not in (0, 1)
    err = capsys.readouterr().err
    assert "check-example: ENVIRONMENT ERROR, not a content finding" in err
    assert "/tmp/x/kb/disorders/A.yaml" in err


def test_other_os_errors_still_raise():
    @reports_disk_full("check-example")
    def main():
        raise OSError(errno.EACCES, "Permission denied")

    with pytest.raises(OSError):
        main()


def test_a_normal_result_passes_through():
    @reports_disk_full("check-example")
    def main(argv=None):
        return 1 if argv else 0

    assert main() == 0
    assert main(["x"]) == 1


@pytest.mark.parametrize(
    ("module", "gate"),
    [
        (check_snippet_length, "check-snippet-length"),
        (check_title_snippets, "check-title-snippets"),
        (check_reference_titles, "check-reference-titles"),
    ],
)
def test_baseline_gates_report_a_full_disk_during_extraction(
    module, gate, monkeypatch, capsys
):
    monkeypatch.setattr(module, "scan_repo", lambda *a, **k: [])
    monkeypatch.setattr(module, "baseline_from_ref", _enospc)

    assert module.main(["--against-ref", "origin/main"]) == EXIT_DISK_FULL
    assert f"{gate}: ENVIRONMENT ERROR" in capsys.readouterr().err


def test_snippet_grading_reports_a_full_disk_during_extraction(monkeypatch, capsys):
    module = check_snippet_grading
    monkeypatch.setattr(module, "collect_items", lambda *a, **k: [])
    monkeypatch.setattr(module, "baseline_from_ref", _enospc)

    assert module.main(["--against-ref", "origin/main"]) == EXIT_DISK_FULL
    assert "check-snippet-grading: ENVIRONMENT ERROR" in capsys.readouterr().err
