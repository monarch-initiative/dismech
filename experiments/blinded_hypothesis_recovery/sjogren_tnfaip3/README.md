# Sjögren's disease: TNFAIP3 (A20)

## Reference hypothesis

From the Biomni Target Atlas (beta) TNFAIP3 profile for Sjögren's syndrome, viewed
2026-11-05. The profile's illustrated panel states:

- TNFAIP3 encodes A20, a ubiquitin-editing enzyme (deubiquitinase and ZnF4 E3 ligase
  domains) that terminates NF-κB signalling downstream of TNFR1, TLRs and the BCR.
- The coding variant rs2230926 (Phe127Cys) gives a hypomorphic A20 and raises the risk of
  Sjögren's disease with early-onset lymphoma (OR "up to ~6.0", PMID:30662920). TNFAIP3 is
  a genome-wide Sjögren's risk locus (Khatri 2022, Nat Commun; no PMID given).
- Knocking out A20 in salivary epithelial cells alone causes Sjögren's-like sialadenitis and
  hyposalivation in mice (PMID:30067782).
- 77% of Sjögren's-associated MALT lymphomas carry A20 loss of function (PMID:24159176).
- A20 upregulation restored salivation and reduced inflammation in the MRL/lpr model
  (PMID:26445930). Therapeutic direction: restore A20 activity or block NF-κB downstream.

None of these claims had been checked against the papers when this run was set up. They
were checked afterwards; see `reference_claims_check.md`.

## State of dismech at the start

`kb/disorders/Sjogrens_Syndrome.yaml` (commit `f3bb2dc0815`) carries no TNFAIP3 gene, no
A20 or NF-κB node, and none of the four PMIDs above. Neither existing deep-research report
for this disease (`research/Sjogrens_Syndrome-deep-research-falcon.md`,
`research/Sjogrens_Syndrome-deep-research-cyberian-codex.md`) mentions TNFAIP3.

## Prompts

Both runs use `../template.md` with the same `existing_mechanism.txt` and
`existing_genetics.txt`. They differ only in `focus`:

- `focus_blind.txt`: no direction.
- `focus_semi.txt`: asks for mechanisms that jointly explain epithelium-driven salivary
  inflammation and the raised MALT lymphoma risk, from germline loci or somatic lesions.

Neither prompt contains TNFAIP3, A20, NF-κB, ubiquitin, deubiquitinase, or any of the
reference PMIDs. `check_blinding.sh` checks that before a run.

## Scoring rubric (fixed before the runs)

For each report:

1. **Gene recovered**: TNFAIP3 / A20 named as a hypothesis. Record its rank.
2. **Mechanism recovered**: A20 described as a negative regulator of NF-κB, and its loss
   linked to inflammation.
3. **Both features linked**: the same hypothesis connects TNFAIP3 to the salivary gland
   pathology *and* to lymphoma.
4. **Evidence overlap**: which of the four reference PMIDs it cites, and which other papers
   it cites for the same claims.
5. **Direction**: whether it says to restore A20 or inhibit NF-κB downstream.
6. **Citation validity**: share of its PMIDs that resolve and whose abstract contains the
   quoted text (from the deep-research client's reference validation).

Also recorded, but not scored as recovery: hypotheses the provider proposes that neither
Biomni nor dismech has. These are leads for the curation pilot.
