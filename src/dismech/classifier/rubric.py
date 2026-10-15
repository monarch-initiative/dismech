"""Three-valued judgments of a declared claim/evidence relationship."""

VERSION = "three-valued-v1"
CRITERIA = {
    "MATCH": "The selected excerpt adequately justifies the declared evidence relationship to the assessed claim or aspect.",
    "MISMATCH": "The selected excerpt clearly fails to justify that relationship, for example through unrelated evidence, an incompatible finding, or no support for the assessed qualifier.",
    "PARTIAL": "Relevant but incomplete, weak, mixed, dependent on an unsettled contextual interpretation, or otherwise unsuitable for a firm MATCH or MISMATCH. Defer the judgment.",
}
INSTRUCTIONS = """Use three judgments: MATCH, MISMATCH, PARTIAL.
MATCH means adequate support for the declared relationship at the assessed scope.
MISMATCH means a clear failure of that relationship, such as irrelevant evidence,
a materially incompatible finding, or no support for an isolated qualifier.
PARTIAL is a deferral for relevant but incomplete, weak, mixed or uncertain
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
"""
