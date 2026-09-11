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
    return JSON.parse(extractWindowJson(dataCode, 'window.searchData = '));
}

function loadSchema() {
    const schemaCode = readFileSync(join(root, 'app', 'schema.js'), 'utf-8');
    return JSON.parse(extractWindowJson(schemaCode, 'window.searchSchema = '));
}

function extractWindowJson(code, prefix) {
    const normalized = code.replace(/\r\n/g, '\n').trim();
    if (!normalized.startsWith(prefix)) {
        throw new Error(`Expected content starting with "${prefix}"`);
    }

    const payload = normalized.slice(prefix.length).trimStart();
    const opener = payload[0];
    const closer = opener === '[' ? ']' : opener === '{' ? '}' : null;

    if (!closer) {
        throw new Error(`Expected JSON array/object after "${prefix}"`);
    }

    let depth = 0;
    let inString = false;
    let escaped = false;

    for (let i = 0; i < payload.length; i += 1) {
        const ch = payload[i];

        if (inString) {
            if (escaped) {
                escaped = false;
            } else if (ch === '\\') {
                escaped = true;
            } else if (ch === '"') {
                inString = false;
            }
            continue;
        }

        if (ch === '"') {
            inString = true;
            continue;
        }

        if (ch === opener) {
            depth += 1;
            continue;
        }

        if (ch === closer) {
            depth -= 1;
            if (depth === 0) {
                return payload.slice(0, i + 1);
            }
        }
    }

    throw new Error(`Could not find the end of the JSON payload for "${prefix}"`);
}

// ---------------------------------------------------------------------------
// Recreate the exact same MiniSearch index as app/index.html
// ---------------------------------------------------------------------------

// These two mirror app/index.html (and its models/ and discussions/ siblings).
// `search config stays in sync across the browsers` below is what keeps the
// copies from drifting apart.
const SEARCH_TOKEN_SPLIT = /[\s\-_/,;:()'’]+/;

function nameBoost(queryLower, nameLower) {
    if (nameLower === queryLower) return 50;
    // Each name-match tier is scaled by how much of the name the query accounts
    // for, so a short canonical name outranks a long specific one that merely
    // starts the same way. The floors keep the tiers ordered by boost.
    const coverage = queryLower.length / nameLower.length;
    if (nameLower.startsWith(queryLower)) return Math.max(3, 30 * coverage);
    if (nameLower.includes(queryLower)) return 1 + 2 * coverage;
    return 1;
}

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
        tokenize: (text) => text.toLowerCase().split(SEARCH_TOKEN_SPLIT).filter((t) => t.length > 1),
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
        boostDocument: (_id, _term, storedFields) =>
            nameBoost(queryLower, (storedFields?.name || '').toLowerCase()),
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

    it('extracts JSON cleanly from generated wrapper code', () => {
        const wrapped = "window.searchData = [1,2,3];\r\nwindow.dispatchEvent(new Event('searchDataReady'));\nconsole.log('ignored');";
        assert.equal(extractWindowJson(wrapped, 'window.searchData = '), '[1,2,3]');
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
        ['Parkinson', ["Parkinson's Disease"]],
        ['Marfan', ['Marfan Syndrome']],
        ['Huntington', ["Huntington's Disease", 'Huntington Disease']],
        ['Cystic Fibrosis', ['Cystic Fibrosis']],
    ];

    for (const [query, expectedFirst] of cases) {
        it(`"${query}" ranks the expected disorder first`, () => {
            const results = search(miniSearch, data, query);
            assert.ok(results.length > 0, `No results for "${query}"`);
            assert.ok(
                expectedFirst.includes(results[0].name),
                `Expected one of ${JSON.stringify(expectedFirst)} first, got "${results[0].name}" (score: ${results[0].score})`
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

// ---------------------------------------------------------------------------
// Ranking rules, pinned against a fixture corpus
//
// The suites above run against the committed app/data.js, which is only
// refreshed by the generate-pages bot. On main it therefore lags the KB by
// however many disorders have been curated since the last page build, so a
// ranking regression introduced by a new entry stays invisible here and only
// surfaces later, in the bot's own PR. These cases use a fixture corpus
// instead, so they hold however stale the snapshot is.
//
// The corpus is a miniature of the real one: enough sibling entries sharing a
// stem for term frequencies to behave as they do at full size. A two-document
// fixture will not do — with that little text MiniSearch's own term weighting
// swamps the name boost, and the case stops measuring the rule it names.
// ---------------------------------------------------------------------------

const FIXTURE_CORPUS = [
    {
        name: "Parkinson's Disease",
        description:
            'A progressive neurodegenerative movement disorder with parkinsonism, rest tremor, rigidity and bradykinesia.',
    },
    {
        name: 'Parkinson Disease, Mitochondrial',
        description:
            'Maternally inherited parkinsonism caused by mitochondrial DNA variants; presents with parkinson features and parkinsonian gait.',
    },
    {
        name: 'PRKN-Related Juvenile Parkinson Disease',
        description:
            'Early-onset parkinsonism caused by biallelic PRKN variants; parkinsonian features with dystonia.',
    },
    {
        name: 'Infantile Parkinsonism-Dystonia',
        description: 'Dopamine transporter deficiency causing parkinsonism and dystonia in infancy.',
    },
    { name: 'Multiple Sclerosis', description: 'A demyelinating disease of the central nervous system.' },
    { name: 'Asthma', description: 'A chronic inflammatory airway disease with wheeze and reversible obstruction.' },
    { name: 'Marfan Syndrome', description: 'A connective tissue disorder caused by FBN1 variants.' },
    { name: 'Huntington Disease', description: 'A trinucleotide repeat neurodegenerative disorder with chorea.' },
];

describe('ranking rules (fixture corpus)', () => {
    let fixtureIndex;

    before(() => {
        fixtureIndex = buildIndex(FIXTURE_CORPUS, schema);
    });

    // Both of these fail on the pre-2026-08 configuration, where "Parkinson's"
    // was a single token (so "Parkinson" could only reach it as a downweighted
    // prefix match) and every prefix match got a flat boost regardless of how
    // much of the name the query accounted for.
    for (const query of ['Parkinson', 'Parkin']) {
        it(`"${query}" ranks the canonical entry above a longer same-prefix sibling`, () => {
            const results = search(fixtureIndex, FIXTURE_CORPUS, query);
            assert.ok(results.length > 0, `No results for "${query}"`);
            assert.equal(
                results[0].name,
                "Parkinson's Disease",
                `Expected "Parkinson's Disease" first, got "${results[0].name}" (score: ${results[0].score})`
            );
        });
    }

    it('an exact name match still wins outright', () => {
        const results = search(fixtureIndex, FIXTURE_CORPUS, 'Asthma');
        assert.equal(results[0].name, 'Asthma', `got "${results[0].name}"`);
    });
});

// ---------------------------------------------------------------------------
// Guards on the ranking rules themselves
// ---------------------------------------------------------------------------

describe('name boost tiers', () => {
    it('an exact name match outranks every other tier', () => {
        assert.equal(nameBoost('asthma', 'asthma'), 50);
    });

    it('a prefix match is always worth at least as much as any substring match', () => {
        // The floors are what make this hold: with startsWith/includes both
        // implying coverage <= 1, prefix lands in [3, 30] and substring in
        // (1, 3]. This bounds the *boost*, not the final rank — rank is this
        // boost times MiniSearch's own relevance, so a much richer substring
        // match can still finish ahead, as "Renal Agenesis" does.
        const query = 'agenesis';
        const prefixNames = [
            'agenesis of the corpus callosum with peripheral neuropathy',
            'agenesis',
            'agenesis of the kidney and lower urinary tract with a very long tail',
        ];
        const substringNames = ['renal agenesis', 'bilateral renal agenesis', 'x agenesis'];

        for (const name of prefixNames) {
            assert.ok(
                nameBoost(query, name) >= 3,
                `prefix match "${name}" scored ${nameBoost(query, name)}, expected >= 3`
            );
        }
        for (const name of substringNames) {
            assert.ok(
                nameBoost(query, name) <= 3,
                `substring match "${name}" scored ${nameBoost(query, name)}, expected <= 3`
            );
        }
    });

    it('a shorter name outranks a longer one with the same prefix', () => {
        assert.ok(nameBoost('parkinson', "parkinson's disease") > nameBoost('parkinson', 'parkinson disease, mitochondrial'));
        assert.ok(nameBoost('autism', 'autism spectrum disorder') > nameBoost('autism', 'autism, susceptibility to, x-linked 3'));
    });

    it('a name with no match at all gets no boost', () => {
        assert.equal(nameBoost('asthma', 'marfan syndrome'), 1);
    });
});

describe('search config stays in sync across the browsers', () => {
    // app/index.html, app/models/index.html and app/discussions/index.html each
    // carry their own copy of this MiniSearch configuration. The apostrophe bug
    // this suite now guards against was present in all three, and a "keep in
    // sync" comment is not a mechanism — this is.
    const BROWSERS = ['index.html', join('models', 'index.html'), join('discussions', 'index.html')];

    function extractSearchConfig(html) {
        const grab = (re) => {
            const found = html.match(re);
            assert.ok(found, `pattern ${re} not found`);
            return found.map((line) => line.trim().replace(/\s+/g, ' '));
        };
        return {
            tokenSplit: grab(/const SEARCH_TOKEN_SPLIT = .*/g),
            tokenize: grab(/tokenize: \(text\) =>.*/g),
            boostTiers: grab(/^ *(if \(nameLower|const coverage|return 1;).*/gm),
        };
    }

    const configs = BROWSERS.map((rel) => [rel, extractSearchConfig(readFileSync(join(root, 'app', rel), 'utf-8'))]);

    for (const [rel, config] of configs.slice(1)) {
        it(`app/${rel} matches app/index.html`, () => {
            assert.deepEqual(config, configs[0][1], `app/${rel} has drifted from app/index.html`);
        });
    }

    it('the browsers use the same token separators as this test', () => {
        const declared = configs[0][1].tokenSplit[0];
        assert.ok(
            declared.includes(SEARCH_TOKEN_SPLIT.source),
            `app/index.html declares ${declared}, this test uses /${SEARCH_TOKEN_SPLIT.source}/`
        );
    });

    it('the browsers use the same boost constants as this test', () => {
        // nameBoost() above is a transcription, not an import — the browsers are
        // standalone HTML with no module boundary to import across. Compare the
        // numbers so a retuned constant cannot land in one copy only.
        // In source order: the exact-match tier (50), the prefix tier (floor 3,
        // scale 30), the substring tier (base 1, scale 2), the no-match tier (1).
        const expected = ['50', '3', '30', '1', '2', '1'];
        const numbers = configs[0][1].boostTiers.join(' ').match(/\d+(\.\d+)?/g);
        assert.deepEqual(numbers, expected, `app/index.html: got ${JSON.stringify(numbers)}`);

        // ...and that nameBoost() above, which is a transcription of that same
        // logic, was retuned along with it. Without this the guard would stay
        // green while the transcription and the browsers drifted apart.
        const transcribed = nameBoost.toString().match(/\d+(\.\d+)?/g);
        assert.deepEqual(transcribed, expected, `nameBoost(): got ${JSON.stringify(transcribed)}`);
    });
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
