"""Exercise cache conflict repair against real Git histories.

The planner may write unreachable Git objects, but must preserve every branch's
content and leave the caller's refs, index, and working files untouched. These
fixtures are disposable repositories; no committed repository cache is changed.
"""

from __future__ import annotations

import importlib.util
import os
import re
import subprocess
import sys
from pathlib import Path

import pytest

_SPEC = importlib.util.spec_from_file_location(
    "repair_generated_cache_conflicts",
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "repair_generated_cache_conflicts.py",
)
repair = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = repair
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
try:
    _SPEC.loader.exec_module(repair)
finally:
    sys.path.pop(0)

LABEL_PATH = "cache/hp/terms.csv"
ENUM_PATH = "cache/enums/phenotypeterm_deadbeef0000.csv"
HEADER = "curie,label,retrieved_at\n"
STAMP = "2026-09-17T01:00:00"


def labels(*numbers: int) -> str:
    return HEADER + "".join(
        f"HP:{number:07d},Fixture label {number},{STAMP}\n" for number in numbers
    )


def members(*numbers: int) -> str:
    return "curie\n" + "".join(f"HP:{number:07d}\n" for number in numbers)


def git(path: Path, *args: str, input: bytes | None = None) -> bytes:
    return subprocess.run(
        ["git", "-C", str(path), *args],
        input=input,
        check=True,
        capture_output=True,
    ).stdout


def write(path: Path, name: str, content: str | None) -> None:
    target = path / name
    if content is None:
        target.unlink()
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")


def commit(path: Path, changes: dict[str, str | None], message: str) -> str:
    for name, content in changes.items():
        write(path, name, content)
    git(path, "add", "--", *changes)
    git(path, "commit", "-m", message)
    return git(path, "rev-parse", "HEAD").decode().strip()


@pytest.fixture
def repo(tmp_path: Path, monkeypatch) -> Path:
    version = subprocess.run(
        ["git", "--version"], check=True, capture_output=True, text=True
    ).stdout
    match = re.search(r"git version (\d+)\.(\d+)", version)
    if match is None or tuple(map(int, match.groups())) < (2, 38):
        pytest.skip(
            "cache merge planning requires Git >= 2.38 (merge-tree --write-tree)"
        )
    monkeypatch.setenv("GIT_CONFIG_GLOBAL", os.devnull)
    monkeypatch.setenv("GIT_CONFIG_NOSYSTEM", "1")
    monkeypatch.setenv("GIT_OPTIONAL_LOCKS", "0")
    for variable in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE"):
        monkeypatch.delenv(variable, raising=False)
    path = tmp_path / "repository"
    path.mkdir()
    git(path, "init", "--initial-branch=base")
    git(path, "config", "user.name", "Cache repair test")
    git(path, "config", "user.email", "cache-repair@example.invalid")
    git(path, "config", "commit.gpgsign", "false")
    git(path, "config", "core.hooksPath", str(tmp_path / "no-hooks"))
    git(path, "config", "core.fileMode", "true")
    return path


def diverge(
    repo: Path,
    ancestor: dict[str, str],
    head_changes: dict[str, str | None],
    base_changes: dict[str, str | None],
) -> tuple[str, str]:
    commit(repo, ancestor, "common ancestor")
    git(repo, "checkout", "-b", "pr")
    head = commit(repo, head_changes, "PR work")
    git(repo, "checkout", "base")
    base = commit(repo, base_changes, "base work")
    return head, base


def tree_file(repo: Path, tree: str, path: str) -> str:
    return git(repo, "show", f"{tree}:{path}").decode()


def caller_state(repo: Path) -> tuple[bytes, bytes, bytes, dict[str, bytes]]:
    return (
        git(repo, "symbolic-ref", "HEAD"),
        git(repo, "show-ref"),
        (repo / ".git" / "index").read_bytes(),
        {
            str(path.relative_to(repo)): path.read_bytes()
            for path in repo.rglob("*")
            if path.is_file() and ".git" not in path.relative_to(repo).parts
        },
    )


def test_additive_conflicts_preserve_both_branches_and_unrelated_code(repo: Path):
    original_code = "first = 0\n" + "# unchanged\n" * 10 + "last = 0\n"
    head, base = diverge(
        repo,
        {
            LABEL_PATH: labels(1),
            ENUM_PATH: members(1),
            "src/example.py": original_code,
            "src/removed_by_pr.py": "obsolete = True\n",
            "docs/removed_by_base.txt": "obsolete documentation\n",
        },
        {
            LABEL_PATH: labels(1, 2, 4),
            ENUM_PATH: members(1, 2, 4),
            "src/example.py": original_code.replace("first = 0", "first = 2"),
            "src/removed_by_pr.py": None,
            "docs/pr.txt": "PR-only content\n",
        },
        {
            LABEL_PATH: labels(1, 3, 4),
            ENUM_PATH: members(1, 3, 4),
            "src/example.py": original_code.replace("last = 0", "last = 3"),
            "docs/removed_by_base.txt": None,
            "docs/base.txt": "base-only content\n",
        },
    )
    before = caller_state(repo)

    plan = repair.build_merge(repair.GitRepo(repo), head, base)

    assert plan.head == head
    assert plan.base == base
    assert set(plan.paths) == {LABEL_PATH, ENUM_PATH}
    assert tree_file(repo, plan.tree, LABEL_PATH) == labels(1, 2, 3, 4)
    assert tree_file(repo, plan.tree, ENUM_PATH) == members(1, 2, 3, 4)
    assert tree_file(repo, plan.tree, "src/example.py") == original_code.replace(
        "first = 0", "first = 2"
    ).replace("last = 0", "last = 3")
    assert tree_file(repo, plan.tree, "docs/pr.txt") == "PR-only content\n"
    assert tree_file(repo, plan.tree, "docs/base.txt") == "base-only content\n"
    paths = set(
        git(repo, "ls-tree", "-r", "--name-only", plan.tree).decode().splitlines()
    )
    assert "src/removed_by_pr.py" not in paths
    assert "docs/removed_by_base.txt" not in paths
    assert caller_state(repo) == before


def test_mixed_python_and_cache_conflicts_refuse_the_entire_repair(repo: Path):
    head, base = diverge(
        repo,
        {LABEL_PATH: labels(1), "src/example.py": "answer = 0\n"},
        {LABEL_PATH: labels(1, 2), "src/example.py": "answer = 2\n"},
        {LABEL_PATH: labels(1, 3), "src/example.py": "answer = 3\n"},
    )
    before = caller_state(repo)
    with pytest.raises(repair.UnsafeMerge):
        repair.build_merge(repair.GitRepo(repo), head, base)
    assert caller_state(repo) == before


@pytest.mark.parametrize("field", ["label", "timestamp"])
def test_same_curie_with_different_data_is_not_arbitrarily_selected(repo: Path, field):
    head_rows = labels(1, 2)
    if field == "label":
        base_rows = head_rows.replace("Fixture label 2", "Different label")
    else:
        base_rows = labels(1) + "HP:0000002,Fixture label 2,2026-09-18T01:00:00\n"
    head, base = diverge(
        repo, {LABEL_PATH: labels(1)}, {LABEL_PATH: head_rows}, {LABEL_PATH: base_rows}
    )
    with pytest.raises(repair.UnsafeMerge):
        repair.build_merge(repair.GitRepo(repo), head, base)


@pytest.mark.parametrize("path,content", [(LABEL_PATH, labels), (ENUM_PATH, members)])
def test_deleted_rows_are_not_resurrected(repo: Path, path, content):
    head, base = diverge(
        repo,
        {path: content(1, 2)},
        {path: content(2, 3)},
        {path: content(1, 2, 4)},
    )
    with pytest.raises(repair.UnsafeMerge):
        repair.build_merge(repair.GitRepo(repo), head, base)


@pytest.mark.parametrize("deleted_side", ["head", "base"])
def test_deleted_file_is_not_resurrected(repo: Path, deleted_side):
    changes = [{LABEL_PATH: None}, {LABEL_PATH: labels(1, 2)}]
    if deleted_side == "base":
        changes.reverse()
    head, base = diverge(repo, {LABEL_PATH: labels(1)}, *changes)
    with pytest.raises(repair.UnsafeMerge):
        repair.build_merge(repair.GitRepo(repo), head, base)


@pytest.mark.parametrize("kind", ["executable", "symlink"])
def test_mode_or_type_changes_require_manual_resolution(repo: Path, kind):
    commit(repo, {LABEL_PATH: labels(1), "README.md": "fixture\n"}, "ancestor")
    git(repo, "checkout", "-b", "pr")
    target = repo / LABEL_PATH
    if kind == "executable":
        target.write_text(labels(1, 2), encoding="utf-8")
        target.chmod(0o755)
    else:
        target.unlink()
        target.symlink_to("../../README.md")
    git(repo, "add", "--", LABEL_PATH)
    git(repo, "commit", "-m", "change cache type or mode")
    head = git(repo, "rev-parse", "HEAD").decode().strip()
    git(repo, "checkout", "base")
    base = commit(repo, {LABEL_PATH: labels(1, 3)}, "add on base")
    with pytest.raises(repair.UnsafeMerge):
        repair.build_merge(repair.GitRepo(repo), head, base)


def test_rename_is_not_treated_as_an_additive_same_path_conflict(repo: Path):
    commit(repo, {LABEL_PATH: labels(*range(1, 15))}, "ancestor")
    git(repo, "checkout", "-b", "pr")
    git(repo, "mv", LABEL_PATH, "cache/hp/renamed.csv")
    head = commit(
        repo, {"cache/hp/renamed.csv": labels(*range(1, 15), 20)}, "rename on PR"
    )
    git(repo, "checkout", "base")
    base = commit(repo, {LABEL_PATH: labels(*range(1, 15), 30)}, "add on base")
    with pytest.raises(repair.UnsafeMerge):
        repair.build_merge(repair.GitRepo(repo), head, base)


@pytest.mark.parametrize(
    "unsupported",
    ["cache/hp/hierarchy.csv", "pages/disorders/Example.html", "app/data.js"],
)
def test_generated_directory_alone_does_not_make_a_conflict_safe(
    repo: Path, unsupported
):
    head, base = diverge(
        repo,
        {LABEL_PATH: labels(1), unsupported: "original\n"},
        {LABEL_PATH: labels(1, 2), unsupported: "PR version\n"},
        {LABEL_PATH: labels(1, 3), unsupported: "base version\n"},
    )
    with pytest.raises(repair.UnsafeMerge):
        repair.build_merge(repair.GitRepo(repo), head, base)


def test_add_add_cache_conflict_preserves_both_new_files_rows(repo: Path):
    head, base = diverge(
        repo,
        {"README.md": "fixture\n"},
        {LABEL_PATH: labels(1)},
        {LABEL_PATH: labels(2)},
    )
    plan = repair.build_merge(repair.GitRepo(repo), head, base)
    assert tree_file(repo, plan.tree, LABEL_PATH) == labels(1, 2)


def test_planning_preserves_dirty_worktree_staged_index_and_refs(repo: Path):
    head, base = diverge(
        repo,
        {LABEL_PATH: labels(1), "notes.txt": "committed\n"},
        {LABEL_PATH: labels(1, 2)},
        {LABEL_PATH: labels(1, 3)},
    )
    write(repo, "notes.txt", "staged work\n")
    git(repo, "add", "--", "notes.txt")
    write(repo, "notes.txt", "unstaged work after staging\n")
    write(repo, LABEL_PATH, "private unfinished cache changes\n")
    write(repo, "untracked.txt", "do not delete\n")
    before = caller_state(repo)

    first = repair.build_merge(repair.GitRepo(repo), head, base)
    second = repair.build_merge(repair.GitRepo(repo), head, base)

    assert first == second
    assert tree_file(repo, first.tree, LABEL_PATH) == labels(1, 2, 3)
    assert caller_state(repo) == before
    assert not (repo / ".git" / "MERGE_HEAD").exists()
    assert not (repo / ".git" / "index.lock").exists()


def test_clean_merge_does_not_create_a_branch_freshness_update(repo: Path):
    head, base = diverge(
        repo,
        {LABEL_PATH: labels(1), "README.md": "fixture\n"},
        {LABEL_PATH: labels(1, 2)},
        {"README.md": "updated on base\n"},
    )
    before = caller_state(repo)
    with pytest.raises(repair.UnsafeMerge):
        repair.build_merge(repair.GitRepo(repo), head, base)
    assert caller_state(repo) == before


@pytest.mark.parametrize("changed_side", ["head", "base"])
@pytest.mark.parametrize("change", ["modify", "delete", "add"])
def test_root_json_changes_refuse_before_merge_or_blob_reads(
    repo: Path, monkeypatch, changed_side, change
):
    # An ordinary synthetic JSON file exercises the protected path family;
    # the actual retired dataset cache is never opened, copied, or written.
    protected = "cache/legacy.json"
    ancestor = {LABEL_PATH: labels(1)}
    if change != "add":
        ancestor[protected] = '{"version": 1}\n'
    head_changes = {LABEL_PATH: labels(1, 2)}
    base_changes = {LABEL_PATH: labels(1, 3)}
    changed = head_changes if changed_side == "head" else base_changes
    changed[protected] = None if change == "delete" else '{"version": 2}\n'
    head, base = diverge(repo, ancestor, head_changes, base_changes)
    local = repair.GitRepo(repo)
    original_git = local.git

    def metadata_only(*args, **kwargs):
        assert "merge-tree" not in args, "protected changes reached merge-tree"
        assert "cat-file" not in args, "protected changes reached blob reads"
        return original_git(*args, **kwargs)

    monkeypatch.setattr(local, "git", metadata_only)
    before = caller_state(repo)
    with pytest.raises(repair.UnsafeMerge, match="protected cache"):
        repair.build_merge(local, head, base)
    assert caller_state(repo) == before


def test_case_collision_created_by_disjoint_additions_is_refused(repo: Path):
    head, base = diverge(
        repo,
        {LABEL_PATH: labels(1)},
        {LABEL_PATH: labels(1, 2), "docs/Example.txt": "PR content\n"},
        {LABEL_PATH: labels(1, 3), "docs/example.txt": "base content\n"},
    )
    with pytest.raises(repair.UnsafeMerge, match="case-colliding"):
        repair.build_merge(repair.GitRepo(repo), head, base)


def test_multiple_merge_bases_are_refused(repo: Path):
    ancestor = commit(repo, {LABEL_PATH: labels(1)}, "ancestor")
    git(repo, "checkout", "-b", "pr")
    left = commit(repo, {LABEL_PATH: labels(1, 2)}, "left")
    git(repo, "checkout", "base")
    right = commit(repo, {LABEL_PATH: labels(1, 3)}, "right")
    # Criss-cross merge commits share both independent ancestors. A recursive
    # virtual base could conceal deletion or replacement, so require a person.
    tree = git(repo, "rev-parse", f"{ancestor}^{{tree}}").decode().strip()
    head = (
        git(repo, "commit-tree", tree, "-p", left, "-p", right, input=b"left merge\n")
        .decode()
        .strip()
    )
    base = (
        git(repo, "commit-tree", tree, "-p", right, "-p", left, input=b"right merge\n")
        .decode()
        .strip()
    )
    with pytest.raises(repair.UnsafeMerge, match="exactly one merge base"):
        repair.build_merge(repair.GitRepo(repo), head, base)
