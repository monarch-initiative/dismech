"""The curated layer of gene pages: agent-written summaries kept honest by provedown.

A summary lives at ``kb/genes/curated/hgnc_<n>.md``. It is Markdown with YAML
frontmatter, and every statement a reader could check against the KB is a
provedown result span whose expression calls :mod:`dismech.genes.claims`::

    <span class="result" data-code="g.relationship('Cowden Syndrome')">untyped<span class="method"></span></span>

:func:`verify_summary` re-runs every span. A summary whose prose no longer
matches the KB fails, and the gene page shows it as stale rather than hiding it.

**The code in a summary is executed**, in-process, by provedown's Python
verifier. Summaries are written by agents and can merge through the
approve-then-merge path with no human in it, so before anything runs this
module checks that the document's code does exactly two things: import
``gene`` from :mod:`dismech.genes.claims` and bind its result, and, in each
claim, call one public :class:`~dismech.genes.claims.GeneClaims` method on
that result with literal arguments, optionally inside ``len(...)``. Anything
else (another import, an attribute chain such as ``g.slice.occurrences``, a
non-literal argument, SQL) is refused and nothing is executed.
"""

from __future__ import annotations

import ast
import re
from dataclasses import dataclass, field
from pathlib import Path

CURATED_DIR = Path("kb/genes/curated")

FILENAME_RE = re.compile(r"^hgnc_(?P<n>\d+)\.md$")


#: Frontmatter keys a summary must carry.
REQUIRED_FRONTMATTER = ("hgnc_id", "symbol", "status")

#: ``status`` values. DRAFT is agent-written and unreviewed; REVIEWED has had a
#: person read it. Neither says anything about verification, which is computed.
SUMMARY_STATUSES = ("DRAFT", "REVIEWED")

_ALLOWED_IMPORT = ("dismech.genes.claims", frozenset({"gene"}))
_ALLOWED_WRAPPERS = frozenset({"len"})


def curated_ids(curated_dir: Path = CURATED_DIR) -> set[str]:
    """HGNC ids that have a curated summary, read off the filenames.

    Two callers ask this and they have to agree. A summary forces a gene page
    (:func:`dismech.genes.render._has_page`), so :func:`.ingest.build_ingest`
    has to write that gene's HGNC identity row even when no KB entry names it —
    which is exactly the case for a gene curated *because* it causes no
    disease. Without the row the page renders titled with the bare CURIE and
    the claims API reports the gene as having no name.
    """
    return {
        f"hgnc:{m['n']}"
        for p in Path(curated_dir).glob("*.md")
        if (m := FILENAME_RE.match(p.name))
    }


class UnsafeSummaryError(ValueError):
    """The summary's code does something other than call the claims API."""


@dataclass
class SummaryResult:
    path: Path
    hgnc_id: str | None
    frontmatter: dict = field(default_factory=dict)
    passed: int = 0
    failed: int = 0
    errored: int = 0
    problems: list[str] = field(default_factory=list)
    #: (line, column) of each result span -> "pass" | "fail" | "error"
    span_status: dict[tuple[int, int], str] = field(default_factory=dict)
    verified: bool = False

    @property
    def claims(self) -> int:
        return self.passed + self.failed + self.errored

    @property
    def ok(self) -> bool:
        return (
            self.verified and not self.problems and not self.failed and not self.errored
        )

    @property
    def state(self) -> str:
        """``verified`` | ``stale`` | ``unverified`` (not run, or refused)."""
        if self.ok:
            return "verified"
        if self.verified and (self.failed or self.errored):
            return "stale"
        return "unverified"

    def line(self) -> str:
        return (
            f"{self.state.upper():10s} {self.path}  "
            f"pass={self.passed} fail={self.failed} error={self.errored}"
        )


# ---------------------------------------------------------------------------
# safety


def _check_code_block(code: str, bound: set[str]) -> None:
    try:
        tree = ast.parse(code, mode="exec")
    except SyntaxError as exc:
        raise UnsafeSummaryError(f"code cell does not parse: {exc}") from exc
    module, names = _ALLOWED_IMPORT
    for stmt in tree.body:
        if isinstance(stmt, ast.ImportFrom):
            imported = {alias.name for alias in stmt.names}
            if (
                stmt.module != module
                or not imported <= names
                or any(a.asname for a in stmt.names)
            ):
                raise UnsafeSummaryError(
                    f"only `from {module} import gene` is allowed, got `{ast.unparse(stmt)}`"
                )
            continue
        if (
            isinstance(stmt, ast.Assign)
            and len(stmt.targets) == 1
            and isinstance(stmt.targets[0], ast.Name)
            and isinstance(stmt.value, ast.Call)
            and isinstance(stmt.value.func, ast.Name)
            and stmt.value.func.id == "gene"
            and len(stmt.value.args) == 1
            and isinstance(stmt.value.args[0], ast.Constant)
            and isinstance(stmt.value.args[0].value, str)
            and not stmt.value.keywords
        ):
            bound.add(stmt.targets[0].id)
            continue
        raise UnsafeSummaryError(
            f"code cells may only import `gene` and bind `<name> = gene('hgnc:<n>')`, "
            f"got `{ast.unparse(stmt)}`"
        )


def claim_methods() -> frozenset[str]:
    """Public methods of :class:`dismech.genes.claims.GeneClaims`: all a claim may call."""
    import inspect

    from dismech.genes.claims import GeneClaims

    return frozenset(
        name
        for name, member in inspect.getmembers(GeneClaims, inspect.isfunction)
        if not name.startswith("_")
    )


def _is_literal(node: ast.AST) -> bool:
    return isinstance(node, ast.Constant) and isinstance(
        node.value, (str, int, float, bool, type(None))
    )


def _check_method_call(node: ast.AST, expression: str, bound: set[str]) -> None:
    """``<bound name>.<GeneClaims method>(<literals>, key=<literal>)`` and nothing else."""
    if not (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and isinstance(node.func.value, ast.Name)
        and node.func.value.id in bound
    ):
        raise UnsafeSummaryError(
            f"claim {expression!r} must be a method call on a gene, e.g. g.disorders('causative')"
        )
    if node.func.attr not in claim_methods():
        raise UnsafeSummaryError(
            f"claim {expression!r} calls {node.func.attr!r}, which is not a GeneClaims method"
        )
    arguments = [*node.args, *(k.value for k in node.keywords)]
    if any(k.arg is None for k in node.keywords) or not all(
        _is_literal(a) for a in arguments
    ):
        raise UnsafeSummaryError(
            f"claim {expression!r} may pass only literal arguments"
        )


def _check_expression(expression: str, bound: set[str]) -> None:
    """A claim is ``g.method(literals)``, optionally wrapped in ``len(...)``.

    The shape is checked exactly rather than by allowing node types, because a
    permissive walk admits ``g.slice.occurrences.clear()``: a call on a public
    attribute chain that mutates the cached KB index every later summary and
    page in the same build is computed from.
    """
    try:
        tree = ast.parse(expression, mode="eval")
    except SyntaxError as exc:
        raise UnsafeSummaryError(f"claim does not parse: {expression!r}") from exc
    body = tree.body
    if (
        isinstance(body, ast.Call)
        and isinstance(body.func, ast.Name)
        and body.func.id in _ALLOWED_WRAPPERS
    ):
        if len(body.args) != 1 or body.keywords:
            raise UnsafeSummaryError(f"claim {expression!r} wraps more than one call")
        body = body.args[0]
    _check_method_call(body, expression, bound)


def check_document_safety(document) -> None:
    """Raise :class:`UnsafeSummaryError` unless the provedown document only
    calls the claims API. ``document`` is a parsed provedown ``Document``."""
    from provedown.model import CodeBlock, CodeUse, ResultAssertion

    bound: set[str] = set()
    for event in document.events:
        language = getattr(event, "language", "python") or "python"
        if language.lower() not in {"python", "py"}:
            raise UnsafeSummaryError(
                f"only python claims are allowed, found {language!r}"
            )
        if isinstance(event, CodeBlock):
            _check_code_block(event.code, bound)
        elif isinstance(event, CodeUse):
            continue  # executes a named CodeBlock, which is checked where defined
        elif isinstance(event, ResultAssertion):
            if event.code.startswith("#"):
                raise UnsafeSummaryError(
                    "claims must be expressions, not named-code references"
                )
            _check_expression(event.code, bound)


# ---------------------------------------------------------------------------
# raw HTML

#: The raw HTML a summary may contain: provedown's own markup plus the
#: disclosure wrapper. Everything else is written as Markdown, which the
#: renderer turns into HTML itself.
_ALLOWED_TAGS: dict[str, frozenset[str]] = {
    "span": frozenset({"class", "data-code", "data-compare", "data-tol", "tol"}),
    "code": frozenset({"name", "use"}),
    "pre": frozenset(),
    "details": frozenset(),
    "summary": frozenset(),
}
_ALLOWED_SPAN_CLASSES = frozenset({"result", "method"})
_LINK_TARGET_RE = re.compile(r"\]\(\s*<?([^)\s>]*)")
_SAFE_LINK_RE = re.compile(r"^(https?://|#|\.{0,2}/|[\w./-]+$)", re.IGNORECASE)


class _TagCollector:
    """Every start tag in a document, with its attributes, via the stdlib parser."""

    def __init__(self, text: str) -> None:
        from html.parser import HTMLParser

        self.tags: list[tuple[str, list[tuple[str, str | None]]]] = []
        collector = self

        class _Parser(HTMLParser):
            def handle_starttag(self, tag, attrs):
                collector.tags.append((tag, attrs))

            def handle_startendtag(self, tag, attrs):
                collector.tags.append((tag, attrs))

        _Parser(convert_charrefs=True).feed(text)


def html_problems(body: str) -> list[str]:
    """Raw HTML in a summary body that falls outside the allowlist.

    Summaries are agent-written and published, so a ``<script>`` or an event
    handler attribute would otherwise reach the gene page as live markup.
    """
    problems: list[str] = []
    for tag, attrs in _TagCollector(body).tags:
        allowed = _ALLOWED_TAGS.get(tag)
        if allowed is None:
            problems.append(f"raw HTML <{tag}> is not allowed; write Markdown instead")
            continue
        for name, value in attrs:
            if name not in allowed:
                problems.append(f"attribute {name!r} is not allowed on <{tag}>")
            elif (
                tag == "span" and name == "class" and value not in _ALLOWED_SPAN_CLASSES
            ):
                problems.append(f"<span class={value!r}> is not provedown markup")
    for target in _LINK_TARGET_RE.findall(body):
        if target and not _SAFE_LINK_RE.match(target):
            problems.append(
                f"link target {target!r} is not an http(s) or relative link"
            )
    return problems


# ---------------------------------------------------------------------------
# verification

#: Comparison policy for lists of names. provedown's built-in ``set`` policy
#: splits authored text on commas, and disease names and GO labels contain
#: commas ("Glioblastoma, IDH-Wildtype", "phosphatidylinositol-3,4,5-..."), so
#: summaries write lists separated by semicolons and use ``data-compare="names"``.
NAMES_POLICY = "names"


def _split_names(authored: str) -> set[str]:
    items = set()
    for part in authored.split(";"):
        part = part.strip()
        if part.startswith("and "):
            part = part[4:].strip()
        if part:
            items.add(part)
    return items


def _names_compare(authored, actual, attributes):
    from provedown.compare import ComparisonResult, stringify
    from provedown.report import Status

    del attributes
    if isinstance(actual, str):
        actual_set = _split_names(actual)
    elif isinstance(actual, (set, frozenset, list, tuple)):
        actual_set = {stringify(item) for item in actual}
    else:
        return ComparisonResult(
            Status.ERROR,
            "names comparison needs a collection",
            authored,
            stringify(actual),
        )
    expected = _split_names(authored)
    actual_text = "; ".join(sorted(actual_set, key=str.casefold))
    if expected == actual_set:
        return ComparisonResult(Status.PASS, "names match", authored, actual_text)
    missing = sorted(actual_set - expected)
    extra = sorted(expected - actual_set)
    detail = []
    if missing:
        detail.append(f"not mentioned: {missing}")
    if extra:
        detail.append(f"no longer true: {extra}")
    return ComparisonResult(Status.FAIL, "; ".join(detail), authored, actual_text)


def _comparators():
    from provedown.compare import default_comparators

    registry = default_comparators()
    registry.register(NAMES_POLICY, _names_compare)
    return registry


def verify_summary(path: Path, *, execute: bool = True) -> SummaryResult:
    """Check a summary's frontmatter and safety, then (by default) run its claims."""
    from provedown.model import ResultAssertion
    from provedown.parser import parse_file
    from provedown.runner import verify_document
    from provedown.verifiers import VerificationContext

    path = Path(path)
    document = parse_file(path)
    frontmatter = dict(document.frontmatter or {})
    result = SummaryResult(
        path=path, hgnc_id=frontmatter.get("hgnc_id"), frontmatter=frontmatter
    )

    match = FILENAME_RE.match(path.name)
    for key in REQUIRED_FRONTMATTER:
        if not frontmatter.get(key):
            result.problems.append(f"frontmatter is missing `{key}`")
    if match is None:
        result.problems.append("file name must be hgnc_<n>.md")
    elif (
        frontmatter.get("hgnc_id")
        and str(frontmatter["hgnc_id"]).lower() != f"hgnc:{match['n']}"
    ):
        result.problems.append(
            f"frontmatter hgnc_id {frontmatter['hgnc_id']!r} does not match the file name"
        )
    if frontmatter.get("status") and frontmatter["status"] not in SUMMARY_STATUSES:
        result.problems.append(f"status must be one of {', '.join(SUMMARY_STATUSES)}")
    result.problems.extend(f"parser: {d}" for d in document.diagnostics)

    from dismech.frontmatter import split_frontmatter

    split = split_frontmatter(document.source)
    result.problems.extend(html_problems(split.body if split else document.source))

    spans = [e for e in document.events if isinstance(e, ResultAssertion)]
    if not spans:
        result.problems.append(
            "no provedown claims: nothing in this summary is checked"
        )
    try:
        check_document_safety(document)
    except UnsafeSummaryError as exc:
        result.problems.append(f"refused to execute: {exc}")
        return result
    if not execute or result.problems:
        return result

    report = verify_document(
        document,
        context=VerificationContext(cwd=path.parent, comparators=_comparators()),
        verifier_ids=["python-results"],
    )
    result.verified = True
    span_locations = {(s.location.line, s.location.column) for s in spans}
    for finding in report.findings:
        status = finding.status.value
        key = (finding.location.line, finding.location.column)
        if key in span_locations:
            result.span_status[key] = status
            if status == "pass":
                result.passed += 1
            elif status == "fail":
                result.failed += 1
                result.problems.append(
                    f"line {key[0]}: says {finding.expected!r}, KB now gives {finding.actual!r}"
                )
            elif status == "error":
                result.errored += 1
                result.problems.append(f"line {key[0]}: {finding.message}")
        elif status == "error":
            result.errored += 1
            result.problems.append(f"line {finding.location.line}: {finding.message}")
    return result


# ---------------------------------------------------------------------------
# rendering helpers

_CODE_DETAILS_RE = re.compile(
    r"<details>\s*<summary>[^<]*</summary>\s*<pre><code.*?</code></pre>\s*</details>",
    re.DOTALL,
)
_PRE_CODE_RE = re.compile(r"<pre><code.*?</code></pre>", re.DOTALL)
_CODE_USE_RE = re.compile(r"<code\s+use=\"[^\"]*\"\s*/>")
_SPAN_OPEN_RE = re.compile(r'<span class="result"')
_METHOD_RE = re.compile(r'<span class="method"></span>')


def summary_body_html(path: Path, result: SummaryResult) -> str:
    """The summary's prose as HTML, code cells removed, each claim tagged with
    its verification status (``claim-pass`` / ``claim-fail`` / ``claim-error``,
    or ``claim-unchecked`` when verification did not run)."""
    import markdown as markdown_lib

    from dismech.frontmatter import split_frontmatter

    text = Path(path).read_text(encoding="utf-8")
    split = split_frontmatter(text)
    body = split.body if split else text
    if html_problems(body):
        # Never publish markup the allowlist refused; show the source instead.
        import html

        return f"<pre>{html.escape(body)}</pre>"
    offset_lines = text[: len(text) - len(body)].count("\n")

    # Tag spans by their (line, column) in the original file before anything moves.
    pieces: list[str] = []
    last = 0
    for match in _SPAN_OPEN_RE.finditer(body):
        line = offset_lines + body.count("\n", 0, match.start()) + 1
        column = match.start() - (body.rfind("\n", 0, match.start()) + 1) + 1
        status = result.span_status.get((line, column), "unchecked")
        pieces.append(body[last : match.start()])
        pieces.append(f'<span class="result claim-{status}"')
        last = match.end()
    pieces.append(body[last:])
    body = "".join(pieces)

    body = _CODE_DETAILS_RE.sub("", body)
    body = _PRE_CODE_RE.sub("", body)
    body = _CODE_USE_RE.sub("", body)
    body = _METHOD_RE.sub("", body)
    md = markdown_lib.Markdown(extensions=["tables"])
    return md.convert(body)
