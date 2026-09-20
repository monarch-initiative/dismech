"""Export modules for dismech."""

from __future__ import annotations

from importlib import import_module

__all__ = [
    "BrowserExporter",
    "DiscussionsExporter",
    "PathographExporter",
    "Statement",
    "biological_process_to_edge",
    "build_inventory",
    "cell_type_to_edge",
    "disorder_to_cx2",
    "dump_cx2",
    "gene_to_edge",
    "kgx_transform",
    "location_to_edge",
    "phenotype_to_edge",
    "statements_for_edges",
    "statements_from_record",
    "treatment_to_edge",
    "upload_cx2_to_ndex",
]

_SYMBOL_TO_MODULE = {
    "BrowserExporter": "dismech.export.browser_export",
    "DiscussionsExporter": "dismech.export.discussions_export",
    "PathographExporter": "dismech.export.pathograph_export",
    "build_inventory": "dismech.export.disease_inventory",
    "disorder_to_cx2": "dismech.export.cx2_export",
    "dump_cx2": "dismech.export.cx2_export",
    "upload_cx2_to_ndex": "dismech.export.cx2_export",
    "kgx_transform": "dismech.export.kgx_export",
    "phenotype_to_edge": "dismech.export.kgx_export",
    "cell_type_to_edge": "dismech.export.kgx_export",
    "location_to_edge": "dismech.export.kgx_export",
    "biological_process_to_edge": "dismech.export.kgx_export",
    "treatment_to_edge": "dismech.export.kgx_export",
    "gene_to_edge": "dismech.export.kgx_export",
    "Statement": "dismech.export.sepio_export",
    "statements_for_edges": "dismech.export.sepio_export",
    "statements_from_record": "dismech.export.sepio_export",
}


def __getattr__(name: str):
    module_name = _SYMBOL_TO_MODULE.get(name)
    if module_name is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    module = import_module(module_name)
    return getattr(module, name)
