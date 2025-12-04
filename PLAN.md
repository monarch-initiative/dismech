The goal for this repo is to be source for a disorder mechanisms database/knowledge database.

This will be a combo of

1. schema, in linkml
2. KB, in YAML

Using the latest linkml methods for validation. We will be inspired by ../ai-gene-review



# Step 1: seed KB from older repo

We will seed from the yaml file here

../dppkb/kb/dppkb.yaml

But make one file per disorder.

E.g.

kb/disorders/Antiphospholipid_Syndrome.yaml

We will also get the linkml schema from

../dppkb/kb/dppkb.yaml

put it here:

src/dismech/schema/dismech.yaml

Just overwrite this, it's a placeholder.

# Step 2: set up QC actions

Each yaml file should be validated with linkml-validate

You should read the docs for

- https://github.com/linkml/linkml-term-validator
- https://github.com/linkml/linkml-reference-validator


The ../ai-gene-review repo "seeded" the code for these, but we'll use the packages above

Always use `uv add` for dependencies

We'll use `just` as is standard for linkml now
