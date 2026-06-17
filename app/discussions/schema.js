window.searchSchema = {
  "title": "Discussions Browser",
  "description": "Browse open questions, knowledge gaps, controversies, and other curation discussions across the dismech knowledge base",
  "searchPlaceholder": "Search discussions...",
  "recordIdField": "discussion_id",
  "searchableFields": [
    "name",
    "prompt",
    "rationale",
    "source_name",
    "attached_nodes",
    "attaches_to",
    "experiment_names",
    "evidence_refs"
  ],
  "fieldBoosts": {
    "name": 8,
    "prompt": 8,
    "source_name": 5,
    "attached_nodes": 3,
    "rationale": 2,
    "experiment_names": 1,
    "evidence_refs": 1
  },
  "facets": [
    {
      "field": "kind",
      "label": "Discussion Type",
      "type": "string"
    },
    {
      "field": "is_gap",
      "label": "Knowledge Gap?",
      "type": "string"
    },
    {
      "field": "status",
      "label": "Status",
      "type": "string"
    },
    {
      "field": "source_type",
      "label": "Source Type",
      "type": "string"
    },
    {
      "field": "has_experiments",
      "label": "Proposed Experiments",
      "type": "string"
    },
    {
      "field": "parents",
      "label": "Disease Class",
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
