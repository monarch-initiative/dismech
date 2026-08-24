"""Parser for the compact pathograph node-class tree.

``docs/superpowers/pathograph_node_classes.txt`` holds a candidate
classification of pathograph nodes as an indented plain-text tree whose leaves
are real ``(node name, disease)`` pairs from ``kb/disorders/``. The format was
written by hand because compactness is the point: the whole classification is
readable in one screen and a category can be added, moved, or argued with in a
single line. This module makes that text machine-readable without giving up the
compactness, so the tree can be checked in CI and converted to YAML/JSON when
the design settles.

Nothing in ``kb/`` or the schema depends on this. It is a design artifact.

Grammar
-------
Indentation is **exactly two spaces per level**; tabs are rejected. Blank lines
and lines whose first non-space character is ``#`` are ignored, so the prose
notes in the file stay where they are. Every other line is one of three things,
tested in this order:

``Node name  [Disease_Entry]``
    An **example**: a real pathophysiology node cited as a representative of
    the enclosing class. The separator is two or more spaces before ``[``, so a
    class name may itself contain single spaces.

``:key free text value``
    An **attribute** of the nearest enclosing node (class or example). Repeats
    accumulate, so a debundle proposal can carry several ``:split`` lines.

``CLASS NAME  -- optional gloss``
    A **class**. The gloss is separated by two or more spaces followed by
    ``--``, and is the human-readable definition of the class.

Class names must be unique among siblings, depth may increase by at most one
level per line, and an example may carry attributes but not class children.
"""

from __future__ import annotations

import json
import re
import sys
from collections.abc import Iterator
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

INDENT = 2

#: ``Node name  [Disease_Entry]`` -- two or more spaces, then a bracketed slug.
EXAMPLE_RE = re.compile(r"^(?P<node>.*?)\s{2,}\[(?P<disease>[^\[\]]+)\]$")
#: ``NAME  -- gloss`` -- two or more spaces, then a double dash.
GLOSS_RE = re.compile(r"^(?P<name>.*?)\s{2,}--\s*(?P<gloss>.*)$")
#: ``:key value`` -- key is a single bare word.
ATTR_RE = re.compile(r"^:(?P<key>[A-Za-z][\w-]*)\s*(?P<value>.*)$")


class ParseError(ValueError):
    """A node-class file could not be parsed. Carries the offending line."""

    def __init__(self, source: str, line: int, message: str) -> None:
        super().__init__(f"{source}:{line}: {message}")
        self.source = source
        self.line = line
        self.message = message


def _slug(name: str) -> str:
    """Derive a stable upper-snake identifier from a human class name."""
    return re.sub(r"[^A-Z0-9]+", "_", name.upper()).strip("_")


@dataclass
class Example:
    """A real ``(node, disease)`` pair cited under a class."""

    node: str
    disease: str
    line: int
    attributes: dict[str, list[str]] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        out: dict[str, Any] = {"node": self.node, "disease": self.disease}
        if self.attributes:
            out["attributes"] = {k: list(v) for k, v in self.attributes.items()}
        return out


@dataclass
class ClassNode:
    """One class in the tree, with its sub-classes and cited examples."""

    name: str
    line: int
    gloss: str | None = None
    children: list[ClassNode] = field(default_factory=list)
    examples: list[Example] = field(default_factory=list)
    attributes: dict[str, list[str]] = field(default_factory=dict)

    @property
    def id(self) -> str:
        """Upper-snake identifier, the candidate enum/class name."""
        return _slug(self.name)

    def to_dict(self) -> dict[str, Any]:
        out: dict[str, Any] = {"id": self.id, "name": self.name}
        if self.gloss:
            out["gloss"] = self.gloss
        if self.attributes:
            out["attributes"] = {k: list(v) for k, v in self.attributes.items()}
        if self.examples:
            out["examples"] = [e.to_dict() for e in self.examples]
        if self.children:
            out["children"] = [c.to_dict() for c in self.children]
        return out


def _add_attribute(target: ClassNode | Example, key: str, value: str) -> None:
    target.attributes.setdefault(key, []).append(value)


def parse_text(text: str, *, source: str = "<text>") -> list[ClassNode]:
    """Parse node-class text into a forest of :class:`ClassNode` roots.

    Raises :class:`ParseError` with a line number on any grammar violation.
    """
    roots: list[ClassNode] = []
    # stack[d] is the class opened at depth d; examples are tracked separately
    # so an attribute line can attach to whichever was most recently opened.
    stack: list[ClassNode] = []
    last_at_depth: dict[int, ClassNode | Example] = {}

    for lineno, raw in enumerate(text.splitlines(), start=1):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if "\t" in raw[: len(raw) - len(raw.lstrip())]:
            raise ParseError(source, lineno, "tab in indentation; use spaces")

        spaces = len(raw) - len(raw.lstrip(" "))
        if spaces % INDENT:
            raise ParseError(
                source, lineno, f"indent {spaces} is not a multiple of {INDENT}"
            )
        depth = spaces // INDENT
        content = raw.strip()

        attr = ATTR_RE.match(content)
        if attr:
            owner = last_at_depth.get(depth - 1)
            if owner is None:
                raise ParseError(
                    source, lineno, "attribute line has no enclosing node"
                )
            _add_attribute(owner, attr.group("key"), attr.group("value").strip())
            continue

        example = EXAMPLE_RE.match(content)
        if example:
            # Guarded before the generic depth check so an example with no open
            # class reports what is actually wrong with it.
            if depth == 0 or depth > len(stack):
                raise ParseError(source, lineno, "example outside any class")
            parent = stack[depth - 1]
            ex = Example(
                node=example.group("node").strip(),
                disease=example.group("disease").strip(),
                line=lineno,
            )
            parent.examples.append(ex)
            last_at_depth[depth] = ex
            # An example opens no class scope; drop anything deeper.
            del stack[depth:]
            continue

        if depth > len(stack):
            if not stack:
                raise ParseError(
                    source, lineno, "indented line before any class"
                )
            raise ParseError(
                source,
                lineno,
                f"indent jumps from depth {len(stack) - 1} to {depth}; "
                "increase by one level at a time",
            )

        gloss_match = GLOSS_RE.match(content)
        name = (gloss_match.group("name") if gloss_match else content).strip()
        gloss = gloss_match.group("gloss").strip() if gloss_match else None
        if not name:
            raise ParseError(source, lineno, "class line has an empty name")

        node = ClassNode(name=name, line=lineno, gloss=gloss)
        siblings = roots if depth == 0 else stack[depth - 1].children
        if any(s.name == node.name for s in siblings):
            raise ParseError(
                source, lineno, f"duplicate sibling class name {node.name!r}"
            )
        siblings.append(node)
        del stack[depth:]
        stack.append(node)
        last_at_depth[depth] = node

    return roots


def parse_file(path: str | Path) -> list[ClassNode]:
    """Parse a node-class file from disk."""
    p = Path(path)
    return parse_text(p.read_text(encoding="utf-8"), source=str(p))


def iter_classes(
    roots: list[ClassNode], _trail: tuple[str, ...] = ()
) -> Iterator[tuple[tuple[str, ...], ClassNode]]:
    """Yield ``(path, node)`` for every class, depth-first."""
    for node in roots:
        trail = _trail + (node.name,)
        yield trail, node
        yield from iter_classes(node.children, trail)


def iter_examples(roots: list[ClassNode]) -> Iterator[tuple[tuple[str, ...], Example]]:
    """Yield ``(class path, example)`` for every cited example."""
    for trail, node in iter_classes(roots):
        for ex in node.examples:
            yield trail, ex


def to_dict(roots: list[ClassNode]) -> dict[str, Any]:
    """Serialize the forest to a plain dict, ready for YAML or JSON."""
    return {"classes": [r.to_dict() for r in roots]}


def render_text(roots: list[ClassNode]) -> str:
    """Render the forest back to the compact text form (round-trips)."""
    lines: list[str] = []

    def emit_attrs(owner: ClassNode | Example, depth: int) -> None:
        pad = " " * (INDENT * depth)
        for key, values in owner.attributes.items():
            for value in values:
                lines.append(f"{pad}:{key} {value}".rstrip())

    def walk(node: ClassNode, depth: int) -> None:
        pad = " " * (INDENT * depth)
        lines.append(f"{pad}{node.name}  -- {node.gloss}" if node.gloss else f"{pad}{node.name}")
        emit_attrs(node, depth + 1)
        for ex in node.examples:
            lines.append(f"{pad}{' ' * INDENT}{ex.node}  [{ex.disease}]")
            emit_attrs(ex, depth + 2)
        for child in node.children:
            walk(child, depth + 1)

    for root in roots:
        walk(root, 0)
        lines.append("")
    return "\n".join(lines).rstrip("\n") + "\n"


def verify_examples(
    roots: list[ClassNode], kb_dirs: list[Path]
) -> list[str]:
    """Check every example resolves to a real pathophysiology node in ``kb/``.

    This is the check that was being run by hand while the tree was drafted: a
    class tree whose leaves have drifted from the knowledge base is worse than
    no tree, because it looks grounded. Returns a list of human-readable
    problems; empty means every example resolved.
    """
    from dismech.yaml_io import safe_load

    known: set[tuple[str, str]] = set()
    diseases: set[str] = set()
    for kb_dir in kb_dirs:
        for path in sorted(kb_dir.glob("*.yaml")):
            diseases.add(path.stem)
            try:
                data = safe_load(path.read_text(encoding="utf-8"))
            except Exception:  # a malformed KB file is not this check's business
                continue
            for node in (data or {}).get("pathophysiology") or []:
                name = node.get("name")
                if name:
                    known.add((str(name), path.stem))

    problems: list[str] = []
    for trail, ex in iter_examples(roots):
        if (ex.node, ex.disease) in known:
            continue
        where = " > ".join(trail)
        if ex.disease not in diseases:
            problems.append(
                f"line {ex.line}: no such entry {ex.disease!r} ({where})"
            )
        else:
            problems.append(
                f"line {ex.line}: {ex.disease} has no pathophysiology node "
                f"named {ex.node!r} ({where})"
            )
    return problems


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(
        prog="python -m dismech.node_classes",
        description="Parse and check the compact pathograph node-class tree.",
    )
    parser.add_argument(
        "path",
        nargs="?",
        default="docs/superpowers/pathograph_node_classes.txt",
        help="node-class text file (default: %(default)s)",
    )
    parser.add_argument(
        "--format",
        choices=("check", "yaml", "json", "text", "summary"),
        default="check",
        help="output format; 'check' parses and reports nothing on success",
    )
    parser.add_argument(
        "--verify-kb",
        action="store_true",
        help="also check every example resolves in kb/ (slow: parses the KB)",
    )
    parser.add_argument(
        "--kb-dir",
        action="append",
        default=None,
        help="KB directory to verify against (repeatable; "
        "default: kb/disorders and kb/modules)",
    )
    args = parser.parse_args(argv)

    try:
        roots = parse_file(args.path)
    except ParseError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    problems: list[str] = []
    if args.verify_kb:
        kb_dirs = [Path(d) for d in (args.kb_dir or ["kb/disorders", "kb/modules"])]
        missing = [d for d in kb_dirs if not d.is_dir()]
        if missing:
            print(
                "error: not a directory: " + ", ".join(str(d) for d in missing),
                file=sys.stderr,
            )
            return 2
        problems = verify_examples(roots, kb_dirs)

    if args.format == "json":
        print(json.dumps(to_dict(roots), indent=2))
    elif args.format == "yaml":
        import yaml

        print(yaml.safe_dump(to_dict(roots), sort_keys=False, width=100), end="")
    elif args.format == "text":
        print(render_text(roots), end="")
    elif args.format == "summary":
        classes = list(iter_classes(roots))
        examples = list(iter_examples(roots))
        print(f"{len(roots)} top-level classes, {len(classes)} classes total")
        print(f"{len(examples)} examples across {len({e.disease for _, e in examples})} entries")
        for trail, node in classes:
            if len(trail) == 1:
                n = sum(1 for t, _ in examples if t[0] == node.name)
                print(f"  {node.id:30s} {n:4d} examples")

    for problem in problems:
        print(f"{args.path}:{problem}", file=sys.stderr)
    if problems:
        print(f"error: {len(problems)} unresolved examples", file=sys.stderr)
        return 1
    if args.format == "check":
        classes = sum(1 for _ in iter_classes(roots))
        examples = sum(1 for _ in iter_examples(roots))
        suffix = ", all examples resolved in kb/" if args.verify_kb else ""
        print(f"ok: {classes} classes, {examples} examples{suffix}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
