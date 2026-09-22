"""TypeSafe HTTP adapter using the project's existing httpx dependency."""

from dataclasses import asdict
import hashlib
import json
import math
import os
import time

import httpx

from dismech.classifier.base import (
    Classification,
    ClassificationTask,
    ClassificationBatch,
    ChoiceAnswer,
)


class TypeSafeClassifier:
    def __init__(
        self,
        model: str = "jev-1.13.0",
        *,
        api_key: str | None = None,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        self.model = model
        self._key = api_key or os.environ.get("TYPESAFE_API_KEY")
        if not self._key:
            raise ValueError("Set TYPESAFE_API_KEY to run live classification")
        self._transport = transport

    def classify(self, task: ClassificationTask) -> Classification:
        batch = self.classify_many([task])
        return Classification(
            **asdict(batch.answers[task.name]),
            model=batch.model,
            usage=batch.usage,
            elapsed_seconds=batch.elapsed_seconds,
            request_sha256=batch.request_sha256,
        )

    def classify_many(self, tasks: list[ClassificationTask]) -> ClassificationBatch:
        """Ask independent questions about one shared state in one API request."""
        if not tasks or len({t.name for t in tasks}) != len(tasks):
            raise ValueError("Questions must have distinct names and not be empty")
        if any(t.state != tasks[0].state for t in tasks):
            raise ValueError("Batched questions must share the same state")
        payload = {
            "model": self.model,
            "state": tasks[0].state,
            "questions": {
                t.name: {
                    "type": "choice",
                    "instructions": t.instructions,
                    "criteria": t.criteria,
                }
                for t in tasks
            },
        }
        digest = hashlib.sha256(
            json.dumps(payload, sort_keys=True).encode()
        ).hexdigest()
        start = time.monotonic()
        with httpx.Client(timeout=60, transport=self._transport) as client:
            for attempt in range(3):
                response = client.post(
                    "https://api.typesafe.ai/v1/systemone",
                    json=payload,
                    headers={"Authorization": f"Bearer {self._key}"},
                )
                if response.status_code not in {429, 529} or attempt == 2:
                    break
                time.sleep(2**attempt)
            response.raise_for_status()
            body = response.json()
        if set(body["answers"]) != {t.name for t in tasks}:
            raise ValueError("TypeSafe returned unexpected questions")
        return ClassificationBatch(
            answers={t.name: self._answer(t, body["answers"][t.name]) for t in tasks},
            model=body["model"],
            usage=body["usage"],
            elapsed_seconds=round(time.monotonic() - start, 4),
            request_sha256=digest,
        )

    @staticmethod
    def _answer(task: ClassificationTask, answer: dict) -> ChoiceAnswer:
        probabilities = answer["probabilities"]
        if answer["type"] != "choice" or set(probabilities) != set(task.criteria):
            raise ValueError("TypeSafe returned unexpected classification options")
        values = list(probabilities.values()) + [answer["confidence"]]
        if any(
            isinstance(p, bool)
            or not isinstance(p, (int, float))
            or not math.isfinite(p)
            or not 0 <= p <= 1
            for p in values
        ):
            raise ValueError("TypeSafe returned invalid probabilities/confidence")
        # The service can round each probability to two decimal places. Allow
        # at most half a percentage point per rounded value, while retaining
        # the stricter check for responses carrying more precision. Preserve
        # the returned probabilities rather than silently renormalizing them.
        rounded = all(
            math.isclose(p, round(p, 2), rel_tol=0, abs_tol=1e-12)
            for p in probabilities.values()
        )
        tolerance = 0.005 * len(probabilities) + 1e-12 if rounded else 0.001
        if not math.isclose(
            sum(probabilities.values()), 1, rel_tol=0, abs_tol=tolerance
        ):
            raise ValueError("TypeSafe probabilities do not sum to one")
        label = answer["choice"]
        if label not in probabilities or probabilities[label] < max(
            probabilities.values()
        ):
            raise ValueError("TypeSafe returned an inconsistent choice")
        return ChoiceAnswer(label, probabilities, answer["confidence"])
