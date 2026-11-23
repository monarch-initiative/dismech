"""Three-valued judgments of a declared claim/evidence relationship."""

VERSION = "three-valued-v2"
CRITERIA = {
    "MATCH": "The selected excerpt adequately justifies the declared evidence relationship to the assessed claim or aspect.",
    "MISMATCH": "The selected excerpt clearly fails to justify that relationship, for example through unrelated evidence, an incompatible finding, or no support for the assessed qualifier.",
    "PARTIAL": "Relevant but incomplete, mixed, dependent on an unsettled contextual interpretation, or otherwise unsuitable for a firm MATCH or MISMATCH. Defer the judgment; limited study strength alone is not a reason to defer.",
}
INSTRUCTIONS = """Use three judgments: MATCH, MISMATCH, PARTIAL.
MATCH means adequate support for the declared relationship at the assessed scope.
MISMATCH means a clear failure of that relationship, such as irrelevant evidence,
a materially incompatible finding, or no support for an isolated qualifier.
PARTIAL is a deferral for relevant but incomplete, mixed or uncertain
support. A description supported in some substantive parts but missing others
can be PARTIAL even when one unsupported qualifier assessed alone is MISMATCH.
Use PARTIAL for a contextual inference whose adequacy remains unsettled. There
is no required subtype of PARTIAL; it is acceptable for many judgments to defer.
Ordinary background understanding may help interpret the excerpt. Support can
be distributed across its overall meaning without one decisive phrase. Mere
confidence that the claim is true elsewhere does not establish snippet support.
Judge each requested scope independently; do not infer a whole-claim result
from a subset of assessed fields. PARTIAL is an explicit assessment, not a
missing answer or a change to selected_evidence.supports/directness.

Assess whether the excerpt justifies the claim as worded, not the overall strength
of the research literature. A small sample, uncontrolled design, or call for future
work does not by itself require PARTIAL or MISMATCH, imply REFUTE or NO_EVIDENCE,
or make evidence INDIRECT. Such limitations can coexist with MATCH for a finding
accurately stated within the studied scope. Respect explicit author caveats when
they limit what the excerpt establishes: an association does not establish causation,
and a preliminary finding does not establish a universal or definitive conclusion.
Apply the usual coverage rules to overstatement: a partly supported composite can
be PARTIAL; an unsupported qualifier assessed alone is MISMATCH. A curator's
explanation is not independent evidence and cannot repair an overstated assertion.
"""
