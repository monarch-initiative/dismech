# Blinded hypothesis recovery

Can a deep-research provider independently arrive at a mechanistic hypothesis that
another system has already proposed, if it is not told what that hypothesis is?

Each run starts from a hypothesis found elsewhere (the "reference hypothesis"), and asks a
provider to propose missing mechanisms for the same disease using `template.md`. The prompt
gives the provider what the dismech entry already records, and never names the reference
hypothesis's gene, protein, pathway or citations. Two blinding levels are run:

- **blind**: no direction beyond "any part of the disease".
- **semi**: a hint at the level of clinical features the reference hypothesis explains,
  with no molecular content.

The scoring rubric is written into each run's `README.md` before the provider is called, so
the result cannot shape what counts as recovery.

| Run | Reference hypothesis | Source | Provider |
|---|---|---|---|
| [`sjogren_tnfaip3/`](sjogren_tnfaip3/) | TNFAIP3 (A20) loss-of-function drives sialadenitis and MALT lymphoma in Sjögren's disease | Biomni Target Atlas (beta) TNFAIP3 profile | OpenScientist |
