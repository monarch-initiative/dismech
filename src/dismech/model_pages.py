"""Generated pages for the models kept in ``models/<model_id>/`` (issue #13123).

A computational model is curated on a disorder or module entry, and the entry's
card says what the model is *for*: which nodes it links to, how faithfully, and
what it found. What a card cannot hold is the model itself: its rules and where
each one comes from, the scenarios and sweeps it was run under, the full result
tables, and how to run it. Each model whose files live in this repository gets
a page of its own for that, at ``pages/models/<model_id>.html``, plus an index.

Two kinds of model folder exist (see :mod:`dismech.model_registry`):

* **authored** (``spec.yaml`` + ``run.py`` + ``results.json``): rules written in
  this repository, each with provenance into ``kb/``. The page lists the rules
  and renders the committed results. When the folder also carries ``run.js``, a
  browser port held to exact parity with ``run.py`` by its own test, the page
  inlines it so a reader can replay the committed scenarios and run new ones.
* **dismech-perturb** (``config.yaml`` + SBML): the page lists the gene effects
  and renders the committed run from ``exports/model_runs/<model_id>.json``.

Pages are derived, like every other page under ``pages/``: they are written by
the page build (``render_all_disorders`` calls :func:`render_all_model_pages`)
and never committed from a hand-authored PR. Nothing here reruns a model; it
reads what the model's own tooling committed.

Usage::

    uv run python -m dismech.model_pages            # all model pages + index
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml

from dismech import model_registry
from dismech.export.utils import slugify
from dismech.perturb.results_export import load_results as load_model_run_results

MODEL_PAGES_DIR = Path("pages/models")
REPO_URL = "https://github.com/monarch-initiative/dismech"

#: Node-anchor prefix per entry kind, matching what render.py gives each page.
_NODE_ANCHOR_PREFIX = {
    "disorder": "pathophysiology",
    "module": "module-pathophysiology",
}


def _render():
    # Imported lazily: dismech.render imports this module from
    # render_all_disorders, and both need helpers from the other.
    from dismech import render

    return render


def _entry_page_href(kind: str, path: Path, entry: dict) -> str:
    """Relative href from pages/models/ to an entry's own page."""
    if kind == "module":
        return f"../modules/{path.stem}.html"
    return f"../disorders/{slugify(entry.get('name') or path.stem)}.html"


def _node_href(kind: str, page_href: str, node_name: str) -> str:
    anchor = _render()._make_anchor_id(_NODE_ANCHOR_PREFIX[kind], node_name)
    return f"{page_href}#{anchor}"


def collect_model_usage(
    disorders_dir: Path = Path("kb/disorders"),
    modules_dir: Path = Path("kb/modules"),
) -> dict[str, list[dict[str, Any]]]:
    """Every curated ``computational_models`` record, keyed by ``model_id``.

    One walk over disorders and modules. The documents come from the shared
    parse cache and are only read, never decorated.
    """
    render = _render()
    usage: dict[str, list[dict[str, Any]]] = {}
    sources = [("disorder", disorders_dir), ("module", modules_dir)]
    for kind, directory in sources:
        if not directory.exists():
            continue
        for path in sorted(directory.glob("*.yaml")):
            if path.name.endswith(".history.yaml"):
                continue
            entry = render.load_disorder_shared(path) or {}
            for model in entry.get("computational_models") or []:
                if not isinstance(model, dict) or not model.get("model_id"):
                    continue
                page_href = _entry_page_href(kind, path, entry)
                name = str(model.get("name") or model["model_id"])
                usage.setdefault(str(model["model_id"]), []).append(
                    {
                        "kind": kind,
                        "entry_name": entry.get("name") or path.stem,
                        "source_file": f"{directory.as_posix()}/{path.name}",
                        "page_href": page_href,
                        "card_href": page_href
                        + "#"
                        + render._make_anchor_id("computational-model", name),
                        "model": model,
                    }
                )
    return usage


def _resolve_ref(ref: str, source: dict | None) -> dict[str, str | None]:
    """A spec's ``maps_to`` (``section#Name``) as display text plus a link.

    Pathophysiology nodes carry a known anchor on both page kinds; for other
    sections the link lands on the entry page without an anchor rather than
    guessing one.
    """
    text = str(ref)
    if source is None or "#" not in text:
        return {"text": text, "href": None}
    section, _, name = text.partition("#")
    if section == "pathophysiology" and name:
        return {
            "text": text,
            "href": _node_href(source["kind"], source["page_href"], name),
        }
    return {"text": text, "href": source["page_href"]}


def _rule_rows(block: Any, source: dict | None) -> list[dict[str, Any]]:
    rows = []
    for name, body in (block or {}).items():
        if not isinstance(body, dict):
            continue
        provenance = body.get("provenance")
        if isinstance(provenance, str):
            provenance = [provenance]
        # Interventions phrase their action as `effect:` (ABM) or
        # `inhibits: <node>` (Boolean), and their rationale as `detail:`.
        rule = body.get("rule") or body.get("effect")
        if not rule and body.get("inhibits"):
            rule = f"inhibits {body['inhibits']}"
        if not rule and body.get("acts_on"):
            rule = f"acts on {body['acts_on']}"
        rows.append(
            {
                "name": name,
                "rule": rule,
                "maps_to": _resolve_ref(body["maps_to"], source)
                if body.get("maps_to")
                else None,
                "provenance": provenance or [],
                "background_assumption": provenance == ["background_assumption"],
                "decision": body.get("decision") or body.get("detail"),
            }
        )
    return rows


def _input_rows(block: Any, source: dict | None) -> list[dict[str, Any]]:
    rows = []
    for name, body in (block or {}).items():
        body = body if isinstance(body, dict) else {}
        rows.append(
            {
                "name": name,
                "maps_to": _resolve_ref(body["maps_to"], source)
                if body.get("maps_to")
                else None,
                "default": body.get("default"),
                "range": body.get("range"),
                "description": body.get("description"),
            }
        )
    return rows


def _source_from_spec(spec: dict) -> dict | None:
    """The entry an authored spec names as its ``source_entry``."""
    path = Path(str(spec.get("source_entry") or ""))
    if not path.is_file():
        return None
    kind = "module" if path.parent.name == "modules" else "disorder"
    entry = _render().load_disorder_shared(path) or {}
    return {
        "kind": kind,
        "entry_name": entry.get("name") or path.stem,
        "source_file": path.as_posix(),
        "page_href": _entry_page_href(kind, path, entry),
    }


def _gene_effect_rows(config: dict) -> list[dict[str, Any]]:
    rows = []
    for gene, body in (config.get("gene_effects") or {}).items():
        if not isinstance(body, dict):
            continue
        rows.append(
            {
                "gene": gene,
                "parameter": body.get("parameter"),
                "effects": {
                    k: v
                    for k, v in body.items()
                    if k not in {"parameter", "description"}
                    and isinstance(v, (int, float))
                },
                "description": body.get("description"),
            }
        )
    return rows


def build_model_context(
    folder: Path,
    usage: list[dict[str, Any]],
    *,
    model_runs_dir: Path | None = None,
) -> dict[str, Any]:
    """Everything the model page renders, for one ``models/<model_id>/`` folder."""
    render = _render()
    model_id = folder.name
    spec_path = folder / model_registry.SPEC_NAME
    config_path = folder / model_registry.CONFIG_NAME
    curated = usage[0]["model"] if usage else {}

    files = sorted(
        p.name for p in folder.iterdir() if p.is_file() and not p.name.startswith(".")
    )
    ctx: dict[str, Any] = {
        "model_id": model_id,
        "folder": f"models/{model_id}",
        "folder_url": f"{REPO_URL}/tree/main/models/{model_id}",
        "files": [
            {"name": name, "url": f"{REPO_URL}/blob/main/models/{model_id}/{name}"}
            for name in files
        ],
        "usage": usage,
        "curated": curated,
        "name": curated.get("name") or model_id,
        "description": curated.get("description"),
        "model_type": curated.get("model_type"),
        "model_format": curated.get("model_format"),
        "model_software": curated.get("model_software"),
    }

    if spec_path.is_file():
        spec = yaml.safe_load(spec_path.read_text()) or {}
        results_path = folder / model_registry.RESULTS_NAME
        results = json.loads(results_path.read_text()) if results_path.is_file() else {}
        source = _source_from_spec(spec)
        browser_js_path = folder / model_registry.BROWSER_RUNNER_NAME
        browser_js = browser_js_path.read_text() if browser_js_path.is_file() else None
        if browser_js is not None and "</script" in browser_js.lower():
            raise ValueError(f"{browser_js_path} cannot be inlined: contains </script")
        ctx.update(
            {
                "kind": "authored",
                "name": spec.get("name") or ctx["name"],
                "formalism": spec.get("formalism"),
                "seed": spec.get("seed"),
                "source": source,
                "spec": spec,
                "results": results,
                "inputs": _input_rows(spec.get("inputs"), source),
                "interventions": _rule_rows(spec.get("interventions"), source),
                "rules": _rule_rows(spec.get("rules"), source),
                "outputs": _rule_rows(spec.get("outputs"), source),
                "browser_runner_js": browser_js,
                # The column viewer reads the spec's domain and cohort geometry,
                # so it is offered only for a spec that has that shape.
                "column_viewer": browser_js is not None
                and isinstance(spec.get("domain"), dict)
                and isinstance(spec.get("cohorts"), dict),
                "run_commands": [
                    f"uv run python models/{model_id}/run.py --print",
                    f"uv run python models/{model_id}/run.py --check",
                    f"uv run python models/{model_id}/run.py",
                ],
            }
        )
    elif config_path.is_file():
        config = yaml.safe_load(config_path.read_text()) or {}
        run = load_model_run_results(model_id, model_runs_dir or render.MODEL_RUNS_DIR)
        source = usage[0] if usage else None
        if run and source:
            for scenario in run.get("scenarios") or []:
                root = scenario.get("causal_root")
                if root:
                    scenario["_causal_root_href"] = _node_href(
                        source["kind"], source["page_href"], str(root)
                    )
        entry_files = [u["source_file"] for u in usage] or ["kb/disorders/<Entry>.yaml"]
        ctx.update(
            {
                "kind": "perturb",
                "source": source,
                "config": config,
                "gene_effects": _gene_effect_rows(config),
                "run": run,
                "run_commands": [
                    f"uv run python -m dismech.perturb {entry_files[0]} --all",
                    f"just gen-model-results --id {model_id}",
                ],
            }
        )
    else:
        ctx["kind"] = "unknown"
    return ctx


def _environment():
    render = _render()
    env = render._get_shared_env(str(Path(render.__file__).parent / "templates"))
    env.filters["curie_to_url"] = render.curie_to_url
    return env


def render_model_page(ctx: dict[str, Any], output_path: Path) -> Path:
    html = _environment().get_template("model_page.html.j2").render(m=ctx)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html)
    return output_path


def render_model_index(contexts: list[dict[str, Any]], output_path: Path) -> Path:
    html = _environment().get_template("model_index.html.j2").render(models=contexts)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html)
    return output_path


def render_all_model_pages(
    models_dir: Path = model_registry.MODELS_DIR,
    output_dir: Path = MODEL_PAGES_DIR,
    *,
    disorders_dir: Path = Path("kb/disorders"),
    modules_dir: Path = Path("kb/modules"),
) -> list[Path]:
    """Render one page per model folder, plus ``index.html``; prune the rest."""
    if not models_dir.exists():
        return []
    usage = collect_model_usage(disorders_dir, modules_dir)
    contexts = []
    written: list[Path] = []
    for folder in model_registry.iter_model_dirs(models_dir):
        ctx = build_model_context(folder, usage.get(folder.name, []))
        contexts.append(ctx)
        written.append(render_model_page(ctx, output_dir / f"{folder.name}.html"))
        print(f"Rendered model: {folder.name} -> {written[-1]}")
    written.append(render_model_index(contexts, output_dir / "index.html"))
    _render()._prune_orphan_pages(output_dir, written, label="model")
    return written


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--models-dir", default=str(model_registry.MODELS_DIR))
    parser.add_argument("--output", "-o", default=str(MODEL_PAGES_DIR))
    args = parser.parse_args(argv)
    written = render_all_model_pages(Path(args.models_dir), Path(args.output))
    print(f"Generated {len(written)} model pages in {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
