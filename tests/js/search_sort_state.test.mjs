import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const { reset, selectSort, sync } = require('../../app/search_sort_state.js');

describe('search sort state', () => {
    it('auto-switches to relevance and remembers the prior sort', () => {
        const state = { searchQuery: 'parkinson', sortBy: 'updated-desc' };

        sync(state);

        assert.equal(state.sortBy, 'relevance');
        assert.equal(state._preSortBy, 'updated-desc');
    });

    it('keeps a manual non-relevance sort during an active search', () => {
        const state = { searchQuery: 'parkinson', sortBy: 'name-asc' };

        sync(state);
        selectSort(state, 'updated-desc');
        sync(state);

        assert.equal(state.sortBy, 'updated-desc');
        assert.equal(state._preSortBy, 'name-asc');
        assert.equal(state._manualSearchSortOverride, true);
    });

    it('restores the pre-search sort when search clears without an override', () => {
        const state = { searchQuery: 'parkinson', sortBy: 'created-asc' };

        sync(state);
        state.searchQuery = '';
        sync(state);

        assert.equal(state.sortBy, 'created-asc');
        assert.equal(state._preSortBy, undefined);
        assert.equal(state._manualSearchSortOverride, undefined);
    });

    it('keeps the manual sort when search clears after an override', () => {
        const state = { searchQuery: 'parkinson', sortBy: 'name-asc' };

        sync(state);
        selectSort(state, 'updated-desc');
        state.searchQuery = '';
        sync(state);

        assert.equal(state.sortBy, 'updated-desc');
        assert.equal(state._preSortBy, undefined);
        assert.equal(state._manualSearchSortOverride, undefined);
    });

    it('reset preserves a manual override and clears search state', () => {
        const state = { searchQuery: 'parkinson', sortBy: 'name-desc' };

        sync(state);
        selectSort(state, 'updated-asc');
        reset(state, 'name-asc');

        assert.equal(state.searchQuery, '');
        assert.equal(state.sortBy, 'updated-asc');
        assert.equal(state._preSortBy, undefined);
        assert.equal(state._manualSearchSortOverride, undefined);
    });
});
