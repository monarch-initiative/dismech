"""Map model outputs to HP phenotype terms via thresholds."""

from dataclasses import dataclass

from dismech.perturb.simulate import PhenotypeThreshold


@dataclass
class ActivatedPhenotype:
    """A phenotype activated by model output exceeding a threshold."""

    hp_id: str
    hp_label: str
    severity: str
    value_description: str


def evaluate_phenotypes(
    result: dict[str, float],
    baseline: dict[str, float],
    thresholds: list[PhenotypeThreshold],
) -> list[ActivatedPhenotype]:
    """Evaluate which phenotypes are activated by comparing result to baseline.

    For "below" direction: compares ratio (result/baseline) against threshold.
    For "above" direction: compares absolute value against threshold.

    Args:
        result: Final variable values from perturbed simulation
        baseline: Final variable values from healthy baseline simulation
        thresholds: Phenotype threshold definitions

    Returns:
        List of activated phenotypes with severity
    """
    activated = []

    for pt in thresholds:
        var = pt.model_variable
        if var not in result or var not in baseline:
            continue

        val = result[var]
        base_val = baseline[var]

        if pt.direction == "below":
            ratio = val / base_val if base_val != 0 else 1.0
            if ratio < pt.threshold:
                severity = _determine_severity(ratio, pt.severity_scale, reverse=True)
                activated.append(
                    ActivatedPhenotype(
                        hp_id=pt.hp_id,
                        hp_label=pt.hp_label,
                        severity=severity,
                        value_description=f"{ratio:.2f}x baseline",
                    )
                )

        elif pt.direction == "above":
            if val > pt.threshold:
                severity = _determine_severity(val, pt.severity_scale, reverse=False)
                activated.append(
                    ActivatedPhenotype(
                        hp_id=pt.hp_id,
                        hp_label=pt.hp_label,
                        severity=severity,
                        value_description=f"{val:.1f}",
                    )
                )

    return activated


def _determine_severity(
    value: float,
    severity_scale: list[tuple[float, str]],
    reverse: bool = False,
) -> str:
    """Determine severity from a scale.

    For "above" thresholds (reverse=False): higher value = higher severity.
    For "below" thresholds (reverse=True): lower value = higher severity.
    """
    if not severity_scale:
        return "unknown"

    if reverse:
        # Lower value = higher severity; iterate from lowest threshold up,
        # return first (most severe) match
        for thresh, sev in sorted(severity_scale):
            if value < thresh:
                return sev
    else:
        # Higher value = higher severity; iterate from highest threshold down,
        # return first (most severe) match
        for thresh, sev in sorted(severity_scale, reverse=True):
            if value > thresh:
                return sev
    return "unknown"
