# Curated Statistical Phenotype Distributions

Curated phenotype-distribution collections go here, one YAML file per analysis
or import. They validate against
[`src/dismech/schema/phenotype_distribution.yaml`](../../src/dismech/schema/phenotype_distribution.yaml)
with target class `PhenotypeDistributionCollection`.

```bash
just validate-phenotype-distribution kb/phenotype_distributions/<file>.yaml
just validate-phenotype-distributions   # all, plus the worked examples
just phenodist-rebuild                  # render references_cache/PHENODIST_*.md
```

Only collections in **this** directory are rendered into `references_cache/`
and so become citable as `PHENODIST:<record_id>`. The worked examples under
`examples/phenotype_distributions/` carry synthetic numbers and are
deliberately excluded.

See [`docs/phenotype-distributions.md`](../../docs/phenotype-distributions.md)
for the curation guide.
