window.searchSchema = {
  "title": "Disorder Mechanisms Browser",
  "description": "Browse disease pathophysiology, phenotypes, and mechanisms",
  "searchPlaceholder": "Search disorders...",
  "recordIdField": "disease_id",
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
  "fieldBoosts": {
    "name": 10,
    "subtypes": 5,
    "genes": 4,
    "description": 3,
    "pathophysiology": 2,
    "phenotypes": 2,
    "treatments": 2,
    "cell_types": 1,
    "biological_processes": 1
  },
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
      "field": "phenotype_hpo_categories",
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
    },
    {
      "field": "causal_graph_edges",
      "label": "Causal Graph Edges",
      "type": "string"
    },
    {
      "field": "causal_graph_longest_path",
      "label": "Longest Causal Path",
      "type": "string"
    }
  ],
  "displayFields": [
    {
      "field": "name",
      "label": "Disorder",
      "type": "string",
      "primary": true,
      "decorators": [
        { "type": "thumbs", "field": "name_quality" }
      ]
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
  ],
  "curationFields": [
    {
      "field": "mechanism_confidence",
      "label": "Mechanism Confidence",
      "type": "rating",
      "min": 1,
      "max": 5
    },
    {
      "field": "evidence_strength",
      "label": "Evidence Strength",
      "type": "enum",
      "choices": ["low", "medium", "high"]
    },
    {
      "field": "needs_followup",
      "label": "Needs Follow-up",
      "type": "boolean"
    },
    {
      "field": "curation_notes",
      "label": "Curation Notes",
      "type": "textarea"
    }
  ],
  "curation": {
    "layout": "inline",
    "sections": [
      {
        "label": "Quick Review",
        "fields": ["mechanism_confidence", "evidence_strength", "needs_followup"]
      },
      {
        "label": "Notes",
        "fields": ["curation_notes"]
      }
    ]
  }
};

window.dispatchEvent(new Event('searchSchemaReady'));
