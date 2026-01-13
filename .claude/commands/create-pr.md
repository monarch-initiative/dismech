---
description: Create a pull request (PR) from some work
argument-hint: [DISORDER_NAME (optional)]
---

Create a pull request from work that you have done. Typically this is a new disease, but in some cases it may be QC improvements or enhancements to existing diseases.

ALWAYS make sure your work has been validated (see justfile for targets). Best efforts should be made to reach high compliance with guidelines, but we can always iterate

Generally a PR should be about a single disease. However, in some cases it makes sense to batch changes together. Use judgment.

What SHOULD be included in a PR

- the yaml file (kb/disorders/DISORDER.yaml)
- the deep research results for that disorder (if a new disorder is created)
- any publications added to the cache
- term cache changes

What should NOT be included

- derived browser files (e.g. app.js, HTML files); these are added later by a weekly job

## A note on schema extensions

Sometimes a PR involves extending the schema at the same time as using these new extensions. These should be flagged for review by @cmungall, and ideally discussed on an issue beforehand
