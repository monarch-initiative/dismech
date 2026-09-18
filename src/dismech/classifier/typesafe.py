"""TypeSafe HTTP adapter using the project's existing httpx dependency."""

import hashlib
import json
import math
import os
import time

import httpx

from dismech.classifier.base import Classification, ClassificationTask


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
        payload = {
            "model": self.model,
            "state": task.state,
            "questions": {
                task.name: {
                    "type": "choice",
                    "instructions": task.instructions,
                    "criteria": task.criteria,
                }
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
        answer = body["answers"][task.name]
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
        if not math.isclose(sum(probabilities.values()), 1, abs_tol=0.001):
            raise ValueError("TypeSafe probabilities do not sum to one")
        label = answer["choice"]
        if label not in probabilities or probabilities[label] < max(
            probabilities.values()
        ):
            raise ValueError("TypeSafe returned an inconsistent choice")
        return Classification(
            label=label,
            probabilities=probabilities,
            confidence=answer["confidence"],
            model=body["model"],
            usage=body["usage"],
            elapsed_seconds=round(time.monotonic() - start, 4),
            request_sha256=digest,
        )
