/**
 * Search ranking tests for the dismech browser app.
 *
 * These tests exercise the same MiniSearch configuration used in app/index.html
 * against the real app/data.js dataset, verifying that search results are ranked
 * sensibly (name matches first, prefix matches above substring, etc.).
 *
 * Run with: node --test tests/js/search_ranking.test.mjs
 */

import { describe, it, before } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import MiniSearch from 'minisearch';

const __dirname = dirname(fileURLToPath(import.meta.url));
const root = join(__dirname, '..', '..');

// ---------------------------------------------------------------------------
// Load data.js & schema.js the same way a browser would
// ---------------------------------------------------------------------------

function loadAppData() {
    const dataCode = readFileSync(join(root, 'app', 'data.js'), 'utf-8');
    // Extract JSON array from: window.searchData = [...];
    const jsonStr = dataCode
        .replace(/^window\.searchData\s*=\s*/, '')
        .replace(/;\s*window\.dispatchEvent\(.*\)\s*;?\s*$/, '')
        .trim();
    return JSON.parse(jsonStr);
}

function loadSchema() {
    const schemaCode = readFileSync(join(root, 'app', 'schema.js'), 'utf-8');
    const jsonStr = schemaCode
        .replace(/^window\.searchSchema\s*=\s*/, '')
        .replace(/;\s*window\.dispatchEvent\(.*\)\s*;?\s*$/, '')
        .trim();
    return JSON.parse(jsonStr);
}

// ---------------------------------------------------------------------------
// Recreate the exact same MiniSearch index as app/index.html
// ---------------------------------------------------------------------------

function buildIndex(data, schema) {
    const searchableFields = schema.searchableFields || [];

    const documents = data.map((record, idx) => {
        const doc = { _id: idx };
        for (const field of searchableFields) {
            const value = record[field];
            if (Array.isArray(value)) {
                doc[field] = value.join(' ');
            } else {
                doc[field] = value || '';
            }
        }
        return doc;
    });

    const miniSearch = new MiniSearch({
        fields: searchableFields,
        idField: '_id',
        storeFields: ['name'],
        tokenize: (text) =>
            text
                .toLowerCase()
                .split(/[\s\-_/,;:()]+/)
                .filter((t) => t.length > 1),
        searchOptions: {
            boost: schema.fieldBoosts || {},
            prefix: true,
            fuzzy: 0.2,
            combineWith: 'AND',
            weights: { fuzzy: 0.45, prefix: 0.75 },
        },
    });

    miniSearch.addAll(documents);
    return miniSearch;
}

// ---------------------------------------------------------------------------
// Search helper that mirrors filter() in app/index.html
// ---------------------------------------------------------------------------

function search(miniSearch, data, query) {
    const queryLower = query.toLowerCase().trim();
    const searchResults = miniSearch.search(query, {
        boostDocument: (_id, _term, storedFields) => {
            const nameLower = (storedFields?.name || '').toLowerCase();
            if (nameLower === queryLower) return 50;
            if (nameLower.startsWith(queryLower)) return 10;
            if (nameLower.includes(queryLower)) return 3;
            return 1;
        },
    });

    // Sort by score descending (MiniSearch already does this, but be explicit)
    searchResults.sort((a, b) => b.score - a.score);

    return searchResults.map((r) => ({
        name: data[r.id].name,
        score: r.score,
        id: r.id,
    }));
}

// ---------------------------------------------------------------------------
// Tests
// ---------------------------------------------------------------------------

let data, schema, miniSearch;

before(() => {
    data = loadAppData();
    schema = loadSchema();
    miniSearch = buildIndex(data, schema);
});

describe('search data loading', () => {
    it('loads a reasonable number of disorders', () => {
        assert.ok(data.length > 50, `Expected >50 disorders, got ${data.length}`);
    });

    it('schema has fieldBoosts configured', () => {
        assert.ok(schema.fieldBoosts, 'fieldBoosts missing from schema');
        assert.ok(schema.fieldBoosts.name > 1, 'name should be boosted');
    });
});

describe('exact name matches rank first', () => {
    const cases = [
        ['Asthma', 'Asthma'],
        ['Epilepsy', 'Epilepsy'],
        ['Crohn', 'Crohn Disease'],
        ['Sickle Cell Disease', 'Sickle Cell Disease'],
        ['Multiple Sclerosis', 'Multiple Sclerosis'],
    ];

    for (const [query, expectedFirst] of cases) {
        it(`"${query}" → "${expectedFirst}" is #1`, () => {
            const results = search(miniSearch, data, query);
            assert.ok(results.length > 0, `No results for "${query}"`);
            assert.equal(
                results[0].name,
                expectedFirst,
                `Expected "${expectedFirst}" first, got "${results[0].name}" (score: ${results[0].score})`
            );
        });
    }
});

describe('name prefix matches rank first', () => {
    const cases = [
        ['Parkinson', "Parkinson's Disease"],
        ['Marfan', 'Marfan Syndrome'],
        ['Huntington', "Huntington's Disease"],
        ['Cystic Fibrosis', 'Cystic Fibrosis'],
    ];

    for (const [query, expectedFirst] of cases) {
        it(`"${query}" → "${expectedFirst}" is #1`, () => {
            const results = search(miniSearch, data, query);
            assert.ok(results.length > 0, `No results for "${query}"`);
            assert.equal(
                results[0].name,
                expectedFirst,
                `Expected "${expectedFirst}" first, got "${results[0].name}" (score: ${results[0].score})`
            );
        });
    }
});

describe('partial prefix queries rank the right disorder first', () => {
    const cases = [
        ['Parkin', "Parkinson's Disease"],
        ['22q', '22q11.2 Deletion Syndrome'],
        ['Achondro', 'Achondroplasia'],
    ];

    for (const [query, expectedFirst] of cases) {
        it(`"${query}" → "${expectedFirst}" is #1`, () => {
            const results = search(miniSearch, data, query);
            assert.ok(results.length > 0, `No results for "${query}"`);
            assert.equal(
                results[0].name,
                expectedFirst,
                `Expected "${expectedFirst}" first, got "${results[0].name}" (score: ${results[0].score})`
            );
        });
    }
});

describe('name field is boosted above other fields', () => {
    it('"BRCA" ranks BRCA-named disorder above others mentioning BRCA in genes', () => {
        const results = search(miniSearch, data, 'BRCA');
        assert.ok(results.length > 0, 'No results for "BRCA"');
        // The first result should have BRCA in its name
        assert.ok(
            results[0].name.includes('BRCA'),
            `Expected a BRCA-named disorder first, got "${results[0].name}"`
        );
    });

    it('"BRAF" ranks BRAF-named disorders at the top', () => {
        const results = search(miniSearch, data, 'BRAF');
        assert.ok(results.length > 0, 'No results for "BRAF"');
        assert.ok(
            results[0].name.includes('BRAF'),
            `Expected a BRAF-named disorder first, got "${results[0].name}"`
        );
    });

    it('"melanoma" ranks Melanoma-named disorders above others', () => {
        const results = search(miniSearch, data, 'melanoma');
        assert.ok(results.length > 0, 'No results for "melanoma"');
        const nameLower = results[0].name.toLowerCase();
        assert.ok(
            nameLower.includes('melanoma'),
            `Expected a melanoma-named disorder first, got "${results[0].name}"`
        );
    });
});

describe('multi-word queries', () => {
    it('"Lung Cancer" ranks lung cancer disorders at the top', () => {
        const results = search(miniSearch, data, 'Lung Cancer');
        assert.ok(results.length > 0, 'No results for "Lung Cancer"');
        const nameLower = results[0].name.toLowerCase();
        assert.ok(
            nameLower.includes('lung cancer'),
            `Expected a lung cancer disorder first, got "${results[0].name}"`
        );
    });

    it('"Sickle Cell" → Sickle Cell Disease is #1', () => {
        const results = search(miniSearch, data, 'Sickle Cell');
        assert.ok(results.length > 0, 'No results for "Sickle Cell"');
        assert.equal(results[0].name, 'Sickle Cell Disease');
    });

    it('"Type 2 Diabetes" → Type 2 Diabetes Mellitus is #1', () => {
        const results = search(miniSearch, data, 'Type 2 Diabetes');
        assert.ok(results.length > 0, 'No results for "Type 2 Diabetes"');
        assert.equal(results[0].name, 'Type 2 Diabetes Mellitus');
    });
});

describe('search returns results (no false negatives)', () => {
    const queries = [
        'asthma',
        'T cell',
        'neural crest',
        'dopamine',
        'fibrosis',
        'autoimmune',
    ];

    for (const query of queries) {
        it(`"${query}" returns at least one result`, () => {
            const results = search(miniSearch, data, query);
            assert.ok(
                results.length > 0,
                `Expected at least one result for "${query}"`
            );
        });
    }
});

describe('empty and edge-case queries', () => {
    it('empty string returns no results from MiniSearch', () => {
        const results = search(miniSearch, data, '');
        // Empty query goes to the else branch in filter(), returns all unscored
        // But our search() helper calls miniSearch.search('') which returns []
        assert.equal(results.length, 0);
    });

    it('single character returns no results (min token length = 2)', () => {
        const results = search(miniSearch, data, 'a');
        assert.equal(results.length, 0);
    });

    it('nonsense query returns no results', () => {
        const results = search(miniSearch, data, 'xyzzy12345');
        assert.equal(results.length, 0);
    });
});

describe('relevance ordering (name match > description match)', () => {
    it('"fibrosis" ranks Cystic Fibrosis far above disorders that only mention fibrosis in descriptions', () => {
        // "fibrosis" appears in many disorders' descriptions/phenotypes but
        // only Cystic Fibrosis and Primary Myelofibrosis have it in the name.
        // Name matches should score significantly higher.
        const results = search(miniSearch, data, 'fibrosis');
        assert.ok(results.length >= 5, `Expected many results for "fibrosis", got ${results.length}`);

        const cysticFibrosis = results.find((r) => r.name === 'Cystic Fibrosis');
        const nonNameMatches = results.filter(
            (r) => !r.name.toLowerCase().includes('fibrosis')
        );

        assert.ok(cysticFibrosis, '"Cystic Fibrosis" not found in results');
        assert.ok(nonNameMatches.length > 0, 'Expected results without fibrosis in name');

        // Name-containing match should score much higher than description-only match
        assert.ok(
            cysticFibrosis.score > nonNameMatches[0].score * 2,
            `Cystic Fibrosis score (${cysticFibrosis.score.toFixed(2)}) should be significantly ` +
                `higher than top non-name result (${nonNameMatches[0].name}: ${nonNameMatches[0].score.toFixed(2)})`
        );
    });

    it('"sclerosis" ranks Multiple Sclerosis above disorders only mentioning sclerosis in other fields', () => {
        const results = search(miniSearch, data, 'sclerosis');
        assert.ok(results.length >= 3, `Expected multiple results for "sclerosis", got ${results.length}`);

        // Multiple Sclerosis or Systemic Sclerosis should be at the top
        const topName = results[0].name.toLowerCase();
        assert.ok(
            topName.includes('sclerosis'),
            `Expected a sclerosis-named disorder first, got "${results[0].name}"`
        );
    });
});
