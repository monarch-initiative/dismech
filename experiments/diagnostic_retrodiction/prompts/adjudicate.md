<!-- LLM adjudicator (DRAFT, to be frozen). Fresh call per (case, arm output), blind to arm identity:
     the arm name, replicate and run are never shown. Placeholders: {RUBRIC_T1}, {RUBRIC_T3},
     {CLINICAL_T1_ONLY}, {CANDIDATES}. -->
You are scoring proposed diagnostic tests against a fixed rubric. Judge each candidate only
against the rubric text below; do not use your own view of what the right test is.

Rubric, tier 1 (mechanism class): a candidate reaches T1 when the mechanism it relies on is this
class or a narrower case of it:
{RUBRIC_T1}

Rubric, tier 3 (discovery experiment): a candidate reaches T3 when the experiment it implies
(the specimen, the comparison groups and the measurement) matches this description in substance:
{RUBRIC_T3}

Analytes already in clinical use for this disease at the cutoff (a candidate naming one of these
is CLINICAL_T1_ONLY):
{CLINICAL_T1_ONLY}

Candidates (index: analyte | type | specimen | target | mechanism | rationale):
{CANDIDATES}

Return, for every candidate index, T1, T3 and CLINICAL_T1_ONLY as true or false.
