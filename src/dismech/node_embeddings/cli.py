"""CLI for per-patho-event node embeddings.

Examples::

    # evaluate node embeddings against conforms_to links (default backend)
    dismech-node-embed evaluate

    # use OpenAI ada / 3-small (requires OPENAI_API_KEY)
    dismech-node-embed evaluate --backend openai:text-embedding-3-small

    # suggest conforms_to targets for unlabelled nodes
    dismech-node-embed suggest --threshold 0.6 --limit 30
"""

from __future__ import annotations

from pathlib import Path

import typer

from dismech.node_embeddings.embedders import available_backends, get_embedder
from dismech.node_embeddings.nodes import iter_nodes
from dismech.node_embeddings.similarity import (
    cosine_matrix,
    embed_nodes,
    group_cosine_summary,
    precision_at_k,
)

app = typer.Typer(help="Per-patho-event (pathophysiology node) embeddings.")

_KB = typer.Option("kb/disorders", "--kb-dir", help="Disorder YAML directory.")
_BACKEND = typer.Option(
    "model2vec", "--backend", help='Embedder spec "backend[:model]".'
)


@app.command("backends")
def backends() -> None:
    """List registered embedding backends."""
    for name in available_backends():
        typer.echo(name)


@app.command("evaluate")
def evaluate(
    kb_dir: str = _KB,
    backend: str = _BACKEND,
    ks: str = typer.Option("1,5,10", "--ks", help="Comma-separated precision@k cutoffs."),
) -> None:
    """Validate node embeddings against ``conforms_to`` links as ground truth."""
    nodes = list(iter_nodes(kb_dir))
    labelled = [n for n in nodes if n.conforms_to]
    typer.echo(f"nodes total      : {len(nodes)}")
    typer.echo(f"nodes labelled   : {len(labelled)}")
    typer.echo(f"distinct targets : {len({n.conforms_to for n in labelled})}")
    if len(labelled) < 2:
        raise typer.Exit(code=1)

    embedder = get_embedder(backend)
    typer.echo(f"embedder         : {embedder.name}")
    sim = cosine_matrix(embed_nodes(labelled, embedder))
    labels = [n.conforms_to for n in labelled]

    summary = group_cosine_summary(sim, labels)
    typer.echo(
        f"\ncosine same-module : {summary.same_mean:.3f} (n={summary.n_same})"
        f"\ncosine diff-module : {summary.diff_mean:.3f} (n={summary.n_diff})"
        f"\nseparation         : {summary.separation:.2f}x"
    )
    for k in (int(x) for x in ks.split(",")):
        p, nq = precision_at_k(sim, labels, k)
        typer.echo(f"precision@{k:<2}       : {p:.3f} (over {nq} queries)")


@app.command("suggest")
def suggest(
    kb_dir: str = _KB,
    backend: str = _BACKEND,
    threshold: float = typer.Option(0.6, "--threshold", help="Min cosine to suggest."),
    limit: int = typer.Option(30, "--limit", help="Max suggestions to print."),
    out: Path = typer.Option(None, "--out", help="Optional TSV output path."),
) -> None:
    """Suggest a ``conforms_to`` target for unlabelled nodes via nearest labelled node."""
    import numpy as np

    nodes = list(iter_nodes(kb_dir))
    labelled = [n for n in nodes if n.conforms_to]
    unlabelled = [n for n in nodes if not n.conforms_to]
    embedder = get_embedder(backend)

    lab_emb = embed_nodes(labelled, embedder)
    unl_emb = embed_nodes(unlabelled, embedder)
    lab_u = lab_emb / (np.linalg.norm(lab_emb, axis=1, keepdims=True) + 1e-9)
    unl_u = unl_emb / (np.linalg.norm(unl_emb, axis=1, keepdims=True) + 1e-9)
    sims = unl_u @ lab_u.T
    best = sims.argmax(axis=1)
    best_sim = sims[np.arange(len(unlabelled)), best]

    ranked = sorted(range(len(unlabelled)), key=lambda i: -best_sim[i])
    rows = []
    for i in ranked:
        if best_sim[i] < threshold:
            break
        nbr = labelled[best[i]]
        rows.append((f"{best_sim[i]:.3f}", nbr.conforms_to,
                     f"{unlabelled[i].disease}::{unlabelled[i].name}",
                     f"{nbr.disease}::{nbr.name}"))

    typer.echo(f"{len(rows)} suggestions >= {threshold} (showing {min(limit, len(rows))}):")
    for sim_s, target, src, nbr in rows[:limit]:
        typer.echo(f"  {sim_s}  {target}\n         {src}  ->  {nbr}")
    if out:
        out.write_text(
            "cosine\tsuggested_conforms_to\tnode\tnearest_labelled_node\n"
            + "\n".join("\t".join(r) for r in rows)
        )
        typer.echo(f"\nwrote {len(rows)} rows -> {out}")


def main() -> None:
    app()


if __name__ == "__main__":
    main()
