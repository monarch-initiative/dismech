---
title: AOP EMOD Framework Alignment
status: IN_PROGRESS
description: >-
  Assess to what extent dismech's environmental-exposure and evidence model
  aligns with the Adverse Outcome Pathway framework & the expanded AOP Evidence Model (EMOD),
  with an eye towards identifying ways dismech might be expanded and enriched by incorporating AOPs,
  ways dismech might seed development of new AOPs, and ways that AOP EMOD might adopt evidence
  modeling approaches from dismech.
tags: [FRAMEWORK_ALIGNMENT, EVIDENCE, EXTERNAL_COLLABORATION, ENVIRONMENTAL_EXPOSURE, SCHEMA_EVOLUTION]
diseases:
  - Lead_Poisoning
---

# AOP EMOD Framework Alignment

## Scope

This project started with issue [#8309](https://github.com/monarch-initiative/dismech/issues/8309), which 
asked **to what extent** dismech's environmental-exposure and evidence modeling approaches align with the Adverse
Outcome Pathway (AOP) framework, including the AOP Evidence Model (EMOD) expansions. Iterative
refinement of the questions that need to be asked led to the content of this project document.
The project should be used to identify specific directions for dismech and AOP integration.

There are **two AOP reference categories** describing the AOP framework and the data classes on a conceptual level. 

| Reference category | What it is | Status |
|---|---|---|
| **AOP-Wiki v2.8 data model** | The current structure. The AOP Developer's Handbook presents it conceptually to humans; the bulk XML serializes it. | Stable, citable |
| **AOP EMOD** | Proposed computable version of the framework and expansion of v2.8, adding structure to fields that are currently free text. | In development; evolving with emergent use cases |

`Lead_Poisoning` is the pilot comparator entry used to ground the comparison
against a real dismech pathograph.


## What this page is

It records an inventory of schema comparisons. It does **not** decide adoption. Whether dismech should
sanction AOP-Wiki as a structured reference source or represent canonical AOPs as
modules are separate calls belonging in their own issues.

## How to read this record

**Stability is a property of individual constructs, not of either framework.** Both
models mix settled and experimental elements, so how firmly a claim can be stated
depends on which construct it describes — not on which side of the comparison it sits.

- **AOP side.** Settled: Key Event Components, deployed since AOP-Wiki Release 2.2,
  and the v2.8 serialization. Open: EMOD concepts are being adopted by the AOP
  community, but the details have not been endorsed by the OECD as the AOP standard
  and remain open to change.
- **dismech side.** Settled: `EvidenceItem` and `CausalEdge`, exercised across ~2000
  entries. Open: `biological_scale` is optional and barely populated, OBI assay
  grounding is unvalidated, and `inference.role` is an unbuilt proposal.
