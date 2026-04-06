"""Export modules for dismech."""

from __future__ import annotations

from importlib import import_module

__all__ = [
    "BrowserExporter",
    "disorder_to_cx2",
    "dump_cx2",
    "upload_cx2_to_ndex",
    "kgx_transform",
    "phenotype_to_edge",
    "cell_type_to_edge",
    "location_to_edge",
    "biological_process_to_edge",
    "treatment_to_edge",
    "gene_to_edge",
]

_SYMBOL_TO_MODULE = {
    "BrowserExporter": "dismech.export.browser_export",
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
}


def __getattr__(name: str):
    module_name = _SYMBOL_TO_MODULE.get(name)
    if module_name is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    module = import_module(module_name)
    return getattr(module, name)
