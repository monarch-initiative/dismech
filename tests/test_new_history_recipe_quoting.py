"""The `new-history` recipe must forward real positional arguments.

`just new-history` is the scaffolding entry point for history records, and two of
its options (`--summary`, `--details`) take free prose. A recipe body written as::

    uv run python scripts/new_history.py {{ARGS}}

pastes the *raw argument text* into the generated shell line, so every quote the
caller wrote is gone by the time the shell parses it. Three separate bug reports
came out of that one line:

* a multi-word value arrived as several arguments (``--summary "Create: Asthma"``
  became ``--summary Create: Asthma``) — issue #10148;
* an apostrophe in prose ("Bell's Palsy") aborted the recipe with
  ``Syntax error: Unterminated quoted string`` — issue #9784;
* ``$VAR``, backticks, ``;`` and ``&&`` in prose were interpreted by the shell
  rather than passed through — issue #10159.

Forwarding ``"$@"`` (enabled by ``set positional-arguments`` in the root
justfile) hands the script the argv the caller actually typed, fixing all three.
This test pins that so the recipe cannot quietly regress to interpolation.
"""

import re
from pathlib import Path

ROOT = Path(__file__).parent.parent


def _recipe_body(justfile: str, recipe: str) -> str:
    match = re.search(rf"(?m)^{re.escape(recipe)}:\n", justfile)
    assert match is not None, f"recipe {recipe!r} not found"
    body = justfile[match.end() :]
    # Recipe body ends at the first line that is not indented.
    lines: list[str] = []
    for line in body.split("\n"):
        if line and not line.startswith((" ", "\t")):
            break
        lines.append(line)
    return "\n".join(lines)


def test_new_history_forwards_positional_arguments() -> None:
    body = _recipe_body((ROOT / "project.justfile").read_text(), "new-history *ARGS")

    assert 'scripts/new_history.py "$@"' in body, (
        "new-history must forward real positional arguments so that quoted prose "
        "in --summary/--details survives; see issues #9784, #10148, #10159."
    )
    assert "{{ARGS}}" not in body, (
        "new-history must not interpolate {{ARGS}} as text: it discards the "
        "caller's quoting and re-splits prose in the shell."
    )


def test_root_justfile_enables_positional_arguments() -> None:
    """`"$@"` in a recipe only carries the caller's argv with this setting on."""
    assert "set positional-arguments := true" in (ROOT / "justfile").read_text()
