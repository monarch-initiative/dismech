"""Shared corpus task routing, preserving each claim family's inference contract."""

from dismech.classifier.aspects import aspect_output_schema, aspect_prompt
from dismech.classifier.base import ClassificationTask
from dismech.classifier.edge_reading import (
    edge_claim_aspect_schema,
    edge_claim_task,
    edge_prompt,
)
from dismech.classifier.rubric import CRITERIA
from dismech.classifier.structured import structured_claim_task


def claim_state(claim):
    """Validate and copy model input; never resolve or rewrite an authored edge."""
    builder = edge_claim_task if "relationship" in claim else structured_claim_task
    return builder(claim).state


def tasks_for(claim):
    state = claim_state(claim)
    edge = "relationship" in claim
    prompt = edge_prompt() if edge else aspect_prompt()
    output = (
        edge_claim_aspect_schema(claim)
        if edge
        else aspect_output_schema(claim, fields=None)
    )
    return [
        ClassificationTask(
            name=path,
            version=prompt["version"],
            state=state,
            instructions=prompt["instructions"] + "\n" + spec["description"],
            # Match the benchmark's Choice options exactly for canonical edges.
            # Node questions retain their existing descriptions and cache keys.
            criteria={label: label for label in spec["enum"]}
            if edge
            else dict(CRITERIA),
        )
        for path, spec in output["properties"].items()
    ]
