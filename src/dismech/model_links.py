"""Iteration over every ``ModelMechanismLink`` in an entry, wherever it sits.

A ``ModelMechanismLink`` -- the object carrying ``target``, ``relationship``,
``fidelity``, ``model_scale``, ``limitations``, ``divergences`` and ``readouts``
-- reaches the pathograph from four places, not three:

* the three top-level model sections, ``experimental_models``,
  ``animal_models`` and ``computational_models``; and
* ``model_systems`` on a *proposed* experiment, under
  ``discussions[].proposed_experiments[]`` and on that experiment's
  ``controls[]``.

The fourth was invisible to every check. ``tests/test_data.py`` and
``scripts/model_scale_audit.py`` each walked only the top-level sections, so a
link declared inside a proposed experiment skipped the divergence, scale,
readout-target and caveat gates entirely -- `just model-scale-audit` reported
``model->mechanism links: 0`` for an entry that had one. The first such link
(``Prolidase_Deficiency``, dismech#13375) passed those checks when they were
applied by hand, but nothing would have caught the next one.

This module exists so the two walks cannot disagree again, for the same reason
``entity_refs`` is the single place that resolves a hash-anchor reference: two
independent resolvers for one grammar is how the gap above happened.

``path_prefix`` is the dotted location of the list the model sits in, so a
caller can build a precise location by appending ``[i]`` -- for a top-level
model it is just the section name, and for a proposed experiment it is the full
route to the ``model_systems`` list. Existing callers formatted
``f"{section}[{i}].modeled_mechanisms[{j}]"``, which keeps working unchanged and
now yields a correct deep path.
"""

from __future__ import annotations

from collections.abc import Iterator
from typing import Any, NamedTuple

__all__ = [
    "MODEL_SECTIONS",
    "ModelLinkSite",
    "iter_model_links",
]

#: The three top-level sections whose entries carry ``modeled_mechanisms``.
MODEL_SECTIONS: tuple[str, ...] = (
    "experimental_models",
    "animal_models",
    "computational_models",
)


class ModelLinkSite(NamedTuple):
    """One ``ModelMechanismLink`` plus where it was found.

    ``path_prefix`` names the list holding the model (``"animal_models"``, or
    ``"discussions[0].proposed_experiments[1].model_systems"``), ``model_index``
    its position in that list, and ``link_index`` the link's position in the
    model's ``modeled_mechanisms``. ``proposed`` is True for a model system that
    exists only inside a proposed experiment -- it has not been run, so a caller
    that reports on curated evidence can skip it while a caller that validates
    structure does not.
    """

    path_prefix: str
    model_index: int
    link_index: int
    model: dict
    link: dict
    proposed: bool


def _links_in_models(
    models: Any, path_prefix: str, *, proposed: bool
) -> Iterator[ModelLinkSite]:
    """Yield each link across a list of models sharing one ``path_prefix``."""
    if not isinstance(models, list):
        return
    for model_index, model in enumerate(models):
        if not isinstance(model, dict):
            continue
        links = model.get("modeled_mechanisms")
        if not isinstance(links, list):
            continue
        for link_index, link in enumerate(links):
            if isinstance(link, dict):
                yield ModelLinkSite(
                    path_prefix, model_index, link_index, model, link, proposed
                )


def iter_model_links(
    data: Any, *, include_proposed: bool = True
) -> Iterator[ModelLinkSite]:
    """Yield every ``ModelMechanismLink`` in a loaded entry.

    Top-level model sections come first, in ``MODEL_SECTIONS`` order, then the
    model systems of each proposed experiment. Set ``include_proposed`` False to
    restrict to curated models -- appropriate for a report about models that
    exist, not for a structural check.
    """
    if not isinstance(data, dict):
        return

    for section in MODEL_SECTIONS:
        yield from _links_in_models(data.get(section), section, proposed=False)

    if not include_proposed:
        return

    discussions = data.get("discussions")
    if not isinstance(discussions, list):
        return
    for d_index, discussion in enumerate(discussions):
        if not isinstance(discussion, dict):
            continue
        experiments = discussion.get("proposed_experiments")
        if not isinstance(experiments, list):
            continue
        for e_index, experiment in enumerate(experiments):
            if not isinstance(experiment, dict):
                continue
            base = f"discussions[{d_index}].proposed_experiments[{e_index}]"
            yield from _links_in_models(
                experiment.get("model_systems"),
                f"{base}.model_systems",
                proposed=True,
            )
            controls = experiment.get("controls")
            if not isinstance(controls, list):
                continue
            for c_index, control in enumerate(controls):
                if not isinstance(control, dict):
                    continue
                yield from _links_in_models(
                    control.get("model_systems"),
                    f"{base}.controls[{c_index}].model_systems",
                    proposed=True,
                )
