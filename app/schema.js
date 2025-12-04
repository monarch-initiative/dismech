window.searchSchema = {
  "title": "Disorder Mechanisms Browser",
  "description": "Browse disease pathophysiology, phenotypes, and mechanisms",
  "searchPlaceholder": "Search disorders...",
  "searchableFields": [
    "name",
    "description",
    "pathophysiology",
    "phenotypes",
    "cell_types",
    "biological_processes",
    "genes",
    "treatments",
    "subtypes"
  ],
  "facets": [
    {
      "field": "category",
      "label": "Category",
      "type": "string"
    },
    {
      "field": "parents",
      "label": "Disease Class",
      "type": "array"
    },
    {
      "field": "phenotype_categories",
      "label": "Phenotype Systems",
      "type": "array"
    },
    {
      "field": "cell_types",
      "label": "Cell Types",
      "type": "array"
    },
    {
      "field": "genes",
      "label": "Associated Genes",
      "type": "array"
    },
    {
      "field": "treatments",
      "label": "Treatments",
      "type": "array"
    },
    {
      "field": "environmental",
      "label": "Environmental Factors",
      "type": "array"
    },
    {
      "field": "biochemical",
      "label": "Biochemical Markers",
      "type": "array"
    }
  ],
  "displayFields": [
    {
      "field": "name",
      "label": "Disorder",
      "type": "string",
      "primary": true
    },
    {
      "field": "disease_id",
      "label": "MONDO ID",
      "type": "curie"
    },
    {
      "field": "category",
      "label": "Category",
      "type": "string"
    },
    {
      "field": "description",
      "label": "Description",
      "type": "string"
    },
    {
      "field": "pathophysiology",
      "label": "Pathophysiology",
      "type": "array"
    },
    {
      "field": "phenotypes",
      "label": "Phenotypes",
      "type": "array"
    },
    {
      "field": "cell_types",
      "label": "Cell Types",
      "type": "array"
    },
    {
      "field": "genes",
      "label": "Associated Genes",
      "type": "array"
    },
    {
      "field": "treatments",
      "label": "Treatments",
      "type": "array"
    },
    {
      "field": "source_file",
      "label": "Source",
      "type": "url",
      "urlPrefix": "https://github.com/monarch-initiative/dismech/blob/main/kb/disorders/"
    }
  ]
};

window.dispatchEvent(new Event('searchSchemaReady'));
