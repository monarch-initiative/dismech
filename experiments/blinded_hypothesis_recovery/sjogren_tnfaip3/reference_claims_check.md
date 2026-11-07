# Reference hypothesis: claims checked against the cited papers

Each claim in the Biomni TNFAIP3 panel was compared with the text of the paper it cites,
as fetched into `references_cache/` by `just fetch-reference`.

| Claim in the panel | Cited | What the paper says | Verdict |
|---|---|---|---|
| rs2230926 raises Sjögren's and early lymphoma risk, OR up to ~6.0 | PMID:30662920 (Greek cohort, 327 SS patients, 91 with lymphoma, 448 controls) | The variant is more common in SS with and without lymphoma than in controls. OR 6.0 (95% CI 1.8–19.8) applies only to SS-lymphoma patients with disease onset at age 40 or younger (18.2% vs 3.6%). | Accurate, but the 6.0 comes from the smallest subgroup and has a wide interval. The larger French cohort (PMID:24159176) gives OR 3.36 for SS with lymphoma. |
| Knocking out A20 in salivary epithelial cells alone causes Sjögren's-like sialadenitis and hyposalivation in mice | PMID:30067782 | A20 knocked out in keratin-14+ epithelial cells. Glands show raised IFNγ, TNFα, IL-6, CXCL10 and CXCL13, and stimulated saliva volume and mucin 10 fall. | Accurate. Mouse evidence (`MODEL_ORGANISM`). |
| 77% of Sjögren's-associated MALT lymphomas carry A20 loss of function | PMID:24159176 | 12 of 20 patients with paired germline and tumour sequence had functional A20 abnormalities (6 germline, 5 tumour, 1 both); "even higher (77%) among pSS patients with mucosa-associated lymphoid tissue lymphoma". | Accurate, but the abnormalities are germline or somatic and the subgroup is small (the abstract gives no denominator for the 77%). |
| A20 upregulation restored salivation and reduced inflammation in the MRL/lpr Sjögren's model | PMID:26445930 | The intervention is low-intensity pulsed ultrasound (LIPUS). LIPUS raised A20 mRNA in cultured human salivary cell lines after TNF-α or IL-1β stimulation. Separately, LIPUS raised salivary flow and AQP5 and reduced gland inflammation in MRL/lpr mice. | **Overstated.** The paper does not show that A20 upregulation caused the in vivo rescue. A20 was measured in vitro and the treatment was ultrasound. The panel turns an association across two experiments into a causal therapeutic result. |
| TNFAIP3 is a genome-wide Sjögren's risk locus | "Khatri 2022, Nat Commun" (no PMID; resolved to PMID:35896530) | TNFAIP3 is one of ten novel genome-wide significant regions in European-ancestry Sjögren's cases. The signal peaks at rs61117627 near the gene's 3' end; rs10499197 and rs58915141 sit in an upstream enhancer and are TNFAIP3 eQTLs in immune cells. | Accurate. Note the GWAS signal is noncoding regulatory variation, a different allele from the coding rs2230926 the panel puts beside it. |

Summary: the backbone of the hypothesis (A20 restrains NF-κB; loss in epithelium is enough
to cause gland dysfunction in mice; germline and somatic A20 lesions accompany Sjögren's
lymphoma) is supported by its citations. The therapeutic panel's rescue claim is not.
