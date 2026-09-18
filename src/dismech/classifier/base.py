"""Provider-independent input and output for a single classification question."""

from dataclasses import dataclass
from typing import Any, Protocol


@dataclass(frozen=True)
class ClassificationTask:
    name: str
    version: str
    state: dict[str, Any]
    instructions: str
    criteria: dict[str, str]


@dataclass(frozen=True)
class Classification:
    label: str
    probabilities: dict[str, float]
    confidence: float
    model: str
    usage: dict[str, int]
    elapsed_seconds: float
    request_sha256: str


class Classifier(Protocol):
    def classify(self, task: ClassificationTask) -> Classification: ...
