#!/usr/bin/env python3
"""Verify bidirectional alignment between graphical abstracts and pathograph nodes.

Checks every KB YAML entry (`kb/modules/*.yaml`, `kb/disorders/*.yaml`,
`kb/groupings/*.yaml`, `kb/module_collections/*.yaml`) and project Markdown file
(`projects/*.md`) that declares a `graphical_abstract`:

1. **Image file exists**: `graphical_abstract.image_path` resolves to an existing
   committed file in the repository.
2. **Legend presence**: `graphical_abstract.legend` is non-empty and each non-TODO
   panel declares `panel`, `depicts`, and `attaches_to`.
3. **Forward FK resolution (`Legend ⊆ Entry`)**:
   - On KB YAML entries: every `attaches_to` reference on a non-TODO panel
     resolves against the entry via `dismech.entity_refs`.
   - On `projects/*.md`: every `<kind>#<slug>` reference in `attaches_to` on a
     non-TODO panel is declared in the project's own frontmatter list (`modules`,
     `diseases`, `groupings`, `drugs`, `phenotypes`).
4. **Reverse Pathograph Coverage (`Pathograph ⊆ Legend`)**:
   - On KB YAML entries (`kb/modules/`, `kb/disorders/`): every node that
     participates in the entry's pathograph (`pathophysiology#<name>`, plus any
     `treatments#<name>`, `experimental_models#<name>`, `animal_models#<name>`,
     or `computational_models#<name>` linked into the causal graph via
     `target_mechanisms` or `modeled_mechanisms`) must be referenced by at least
     one `legend[].attaches_to` item.
5. **Escape Hatch (`todo` / `panel: "TODO"`)**:
   - When a curator or agent edits an entry's pathograph without access to an
     image generation model, setting `todo: "<what to redraw>"` (or
     `panel: "TODO"`) on the affected `GraphicalAbstractPanel` (or at the top
     level of `graphical_abstract`) bypasses validation errors for that legend
     node and records an advisory redraw notice instead.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dismech.entity_refs import (
    canonical_kind,
    entity_ref_errors,
    is_graphical_abstract_todo,
    parse_entity_ref,
    resolve_entity_ref,
)


def _split_front_matter(text: str) -> dict:
    lines = text.replace("\r\n", "\n").split("\n")
    if not lines or lines[0].strip() != "---":
        return {}
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            data = yaml.safe_load("\n".join(lines[1:idx])) or {}
            return data if isinstance(data, dict) else {}
    return {}


def _expected_pathograph_refs(data: dict) -> list[str]:
    """Return canonical `<kind>#<name>` refs for all pathograph-participating nodes."""
    expected: list[str] = []
    for node in data.get("pathophysiology") or []:
        if isinstance(node, dict) and node.get("name"):
            expected.append(f"pathophysiology#{node['name']}")
    for tx in data.get("treatments") or []:
        if isinstance(tx, dict) and tx.get("name") and tx.get("target_mechanisms"):
            expected.append(f"treatments#{tx['name']}")
    for section in ("experimental_models", "animal_models", "computational_models"):
        for model in data.get(section) or []:
            if (
                isinstance(model, dict)
                and model.get("name")
                and model.get("modeled_mechanisms")
            ):
                expected.append(f"{section}#{model['name']}")
    return expected


def check_kb_entry(
    path: Path,
    data: dict,
    *,
    root: Path = ROOT,
    todos_out: list[str] | None = None,
) -> list[str]:
    ga = data.get("graphical_abstract")
    if not ga:
        return []
    errors: list[str] = []
    todos: list[str] = todos_out if todos_out is not None else []
    if not isinstance(ga, dict):
        return [
            f"{path}: graphical_abstract must be a structured mapping with image_path and legend"
        ]

    top_todo = is_graphical_abstract_todo(ga)
    if top_todo:
        todos.append(
            f"{path}: graphical_abstract.todo={ga.get('todo')!r} (whole-figure redraw pending)"
        )

    image_path = ga.get("image_path")
    if not image_path or not isinstance(image_path, str):
        errors.append(f"{path}: graphical_abstract.image_path is required")
    elif not (root / image_path).is_file():
        errors.append(
            f"{path}: graphical_abstract.image_path {image_path!r} does not exist on disk"
        )

    legend = ga.get("legend") or []
    if not isinstance(legend, list) or not legend:
        if top_todo:
            return errors
        errors.append(
            f"{path}: graphical_abstract.legend must be a non-empty list of panels"
        )
        return errors

    # 1. Forward FK check via entity_refs (automatically skips todo-marked panels)
    for err in entity_ref_errors(data):
        if err.startswith("graphical_abstract."):
            errors.append(f"{path}: {err}")

    # Collect canonicalized refs covered by the legend and inspect per-panel requirements
    covered_refs: set[str] = set()
    has_unattached_todo_panel = False
    for i, item in enumerate(legend):
        if not isinstance(item, dict):
            errors.append(f"{path}: graphical_abstract.legend[{i}] must be a mapping")
            continue
        panel_label = item.get("panel")
        if not panel_label or not isinstance(panel_label, str):
            errors.append(f"{path}: graphical_abstract.legend[{i}].panel is required")
        panel_is_todo = top_todo or is_graphical_abstract_todo(item)
        if panel_is_todo and not top_todo:
            todo_msg = item.get("todo") or panel_label
            todos.append(
                f"{path}: graphical_abstract.legend[{i}] ({panel_label!r}): {todo_msg}"
            )

        attaches = item.get("attaches_to") or []
        if not panel_is_todo:
            if not item.get("depicts") or not isinstance(item.get("depicts"), str):
                errors.append(
                    f"{path}: graphical_abstract.legend[{i}].depicts is required "
                    "(or set `todo` on the panel if awaiting figure redraw)"
                )
            if not isinstance(attaches, list) or not attaches:
                errors.append(
                    f"{path}: graphical_abstract.legend[{i}].attaches_to must be a non-empty list "
                    "(or set `todo` on the panel if awaiting figure redraw)"
                )
        else:
            if not attaches:
                has_unattached_todo_panel = True

        for ref in attaches if isinstance(attaches, list) else []:
            parsed = parse_entity_ref(ref)
            if parsed is not None:
                covered_refs.add(f"{canonical_kind(parsed.kind)}#{parsed.name}")
                if panel_is_todo and resolve_entity_ref(data, ref) is False:
                    todos.append(
                        f"{path}: graphical_abstract.legend[{i}].attaches_to={ref!r} "
                        "does not resolve (bypassed by panel TODO)"
                    )

    # 2. Reverse pathograph coverage check (Pathograph <= Legend)
    bypass_unmapped = top_todo or has_unattached_todo_panel
    for req_ref in _expected_pathograph_refs(data):
        if req_ref not in covered_refs:
            msg = (
                f"{path}: pathograph node {req_ref!r} is not covered by any "
                f"graphical_abstract.legend[].attaches_to entry"
            )
            if bypass_unmapped:
                todos.append(f"{msg} (bypassed by TODO)")
            else:
                errors.append(
                    f"{msg} (figure/pathograph out of sync; add a legend entry or "
                    "a `panel: TODO` / `todo:` escape-hatch entry)"
                )

    return errors


def check_project_file(
    path: Path,
    *,
    root: Path = ROOT,
    todos_out: list[str] | None = None,
) -> list[str]:
    meta = _split_front_matter(path.read_text(encoding="utf-8"))
    ga = meta.get("graphical_abstract")
    if not ga:
        return []
    errors: list[str] = []
    todos: list[str] = todos_out if todos_out is not None else []
    if not isinstance(ga, dict):
        return [
            f"{path}: graphical_abstract must be a structured mapping with image_path and legend"
        ]

    top_todo = is_graphical_abstract_todo(ga)
    if top_todo:
        todos.append(
            f"{path}: graphical_abstract.todo={ga.get('todo')!r} (whole-figure redraw pending)"
        )

    image_path = ga.get("image_path")
    if not image_path or not isinstance(image_path, str):
        errors.append(f"{path}: graphical_abstract.image_path is required")
    elif not (root / image_path).is_file():
        errors.append(
            f"{path}: graphical_abstract.image_path {image_path!r} does not exist on disk"
        )

    legend = ga.get("legend") or []
    if not isinstance(legend, list) or not legend:
        if top_todo:
            return errors
        errors.append(
            f"{path}: graphical_abstract.legend must be a non-empty list of panels"
        )
        return errors

    declared: dict[str, set[str]] = {}
    for kind in ("diseases", "modules", "groupings", "drugs", "phenotypes"):
        tokens: set[str] = set()
        for raw in meta.get(kind) or []:
            if isinstance(raw, str):
                tokens.add(raw.strip())
            elif isinstance(raw, dict):
                tok = raw.get("slug") or raw.get("name") or raw.get("id")
                if tok:
                    tokens.add(str(tok).strip())
        declared[kind] = tokens

    for i, item in enumerate(legend):
        if not isinstance(item, dict):
            errors.append(f"{path}: graphical_abstract.legend[{i}] must be a mapping")
            continue
        panel_label = item.get("panel")
        panel_is_todo = top_todo or is_graphical_abstract_todo(item)
        if panel_is_todo and not top_todo:
            todo_msg = item.get("todo") or panel_label
            todos.append(
                f"{path}: graphical_abstract.legend[{i}] ({panel_label!r}): {todo_msg}"
            )
        for ref in item.get("attaches_to") or []:
            parsed = parse_entity_ref(ref)
            if parsed is None:
                if panel_is_todo:
                    continue
                errors.append(
                    f"{path}: graphical_abstract.legend[{i}].attaches_to={ref!r} "
                    "must use <kind>#<slug> syntax"
                )
                continue
            if parsed.kind not in declared:
                if panel_is_todo:
                    continue
                errors.append(
                    f"{path}: graphical_abstract.legend[{i}] uses unknown project entity kind {parsed.kind!r}"
                )
                continue
            if parsed.name not in declared[parsed.kind]:
                msg = (
                    f"{path}: graphical_abstract.legend[{i}] references {ref!r}, "
                    f"which is not listed in project frontmatter `{parsed.kind}:`"
                )
                if panel_is_todo:
                    todos.append(f"{msg} (bypassed by panel TODO)")
                else:
                    errors.append(msg)

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="Optional files to check")
    parser.add_argument(
        "--list-todos",
        action="store_true",
        help="List all graphical abstract panels/entries marked with a redraw TODO",
    )
    parser.add_argument(
        "--fail-on-todo",
        action="store_true",
        help="Treat pending redraw TODOs as errors (exit 1)",
    )
    args = parser.parse_args()

    errors: list[str] = []
    todos: list[str] = []
    checked = 0

    if args.paths:
        candidates = [Path(p) for p in args.paths]
    else:
        candidates = (
            sorted((ROOT / "kb" / "modules").glob("*.yaml"))
            + sorted((ROOT / "kb" / "disorders").glob("*.yaml"))
            + sorted((ROOT / "kb" / "groupings").glob("*.yaml"))
            + sorted((ROOT / "kb" / "module_collections").glob("*.yaml"))
            + sorted((ROOT / "projects").glob("*.md"))
        )

    for path in candidates:
        if path.name.endswith(".history.yaml"):
            continue
        if path.suffix == ".md":
            meta = _split_front_matter(path.read_text(encoding="utf-8"))
            if meta.get("graphical_abstract"):
                checked += 1
                errors.extend(check_project_file(path, todos_out=todos))
        elif path.suffix in (".yaml", ".yml"):
            data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
            if isinstance(data, dict) and data.get("graphical_abstract"):
                checked += 1
                errors.extend(check_kb_entry(path, data, todos_out=todos))

    if args.list_todos:
        if todos:
            for item in todos:
                print(f"TODO: {item}")
            print(
                f"\nFound {len(todos)} pending graphical abstract redraw TODO(s) across {checked} entry/entries."
            )
        else:
            print(
                f"OK: 0 pending graphical abstract redraw TODOs across {checked} entry/entries."
            )
        return 1 if (todos and args.fail_on_todo) else 0

    if todos:
        for item in todos:
            print(f"ADVISORY [TODO]: {item}", file=sys.stderr)

    if errors or (todos and args.fail_on_todo):
        for err in errors:
            print(err, file=sys.stderr)
        total_err = len(errors) + (len(todos) if args.fail_on_todo else 0)
        print(
            f"\nFAILED: {total_err} graphical abstract sync error(s) across {checked} entry/entries.",
            file=sys.stderr,
        )
        return 1

    todo_suffix = f" ({len(todos)} pending redraw TODO(s) bypassed)" if todos else ""
    print(
        f"OK: {checked} graphical abstract(s) verified in sync with pathograph/frontmatter nodes{todo_suffix}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
