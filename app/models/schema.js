window.searchSchema = {
  "title": "Computational Models Browser",
  "description": "Browse the computational and in-silico models curated across the dismech knowledge base — genome-scale metabolic reconstructions, ODE/kinetic models, Boolean networks, agent-based simulations, PBPK models, and ML models",
  "searchPlaceholder": "Search computational models...",
  "recordIdField": "model_key",
  "searchableFields": [
    "name",
    "description",
    "source_name",
    "model_type",
    "model_format",
    "model_software",
    "base_model",
    "model_id",
    "variables",
    "variable_ids",
    "variable_terms",
    "perturbations",
    "modeled_mechanisms",
    "findings",
    "evidence_refs",
    "notes"
  ],
  "fieldBoosts": {
    "name": 10,
    "source_name": 6,
    "model_software": 5,
    "model_type": 4,
    "model_id": 4,
    "perturbations": 4,
    "description": 3,
    "modeled_mechanisms": 3,
    "base_model": 3,
    "model_format": 2,
    "variables": 2,
    "variable_terms": 2,
    "findings": 1,
    "variable_ids": 1,
    "evidence_refs": 1,
    "notes": 1
  },
  "facets": [
    {
      "field": "model_type",
      "label": "Model Type",
      "type": "string"
    },
    {
      "field": "model_format",
      "label": "Exchange Format",
      "type": "string"
    },
    {
      "field": "model_software",
      "label": "Simulation Software",
      "type": "string"
    },
    {
      "field": "runnable",
      "label": "Runnable In-Repo",
      "type": "string"
    },
    {
      "field": "repository_host",
      "label": "Model Repository",
      "type": "string"
    },
    {
      "field": "source_type",
      "label": "Source Type",
      "type": "string"
    },
    {
      "field": "parents",
      "label": "Disease Class",
      "type": "array"
    },
    {
      "field": "perturbations",
      "label": "Perturbed Genes",
      "type": "array"
    },
    {
      "field": "source_name",
      "label": "Source Entry",
      "type": "string"
    }
  ]
};

window.dispatchEvent(new Event('searchSchemaReady'));
