(function (root, factory) {
    const api = factory();
    if (typeof module === 'object' && module.exports) {
        module.exports = api;
    }
    root.SearchSortState = api;
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
    function sync(state) {
        if (!state.searchQuery) {
            if (state._preSortBy !== undefined) {
                if (!state._manualSearchSortOverride) {
                    state.sortBy = state._preSortBy;
                }
                delete state._preSortBy;
            }
            delete state._manualSearchSortOverride;
            return state;
        }

        if (state._preSortBy === undefined) {
            state._preSortBy = state.sortBy;
        }
        if (!state._manualSearchSortOverride) {
            state.sortBy = 'relevance';
        }
        return state;
    }

    function selectSort(state, nextSort) {
        state.sortBy = nextSort;
        if (state.searchQuery) {
            state._manualSearchSortOverride = nextSort !== 'relevance';
        } else {
            delete state._manualSearchSortOverride;
        }
        return state;
    }

    function reset(state, fallbackSort) {
        state.searchQuery = '';
        state.sortBy = state._manualSearchSortOverride
            ? state.sortBy
            : state._preSortBy || fallbackSort;
        delete state._preSortBy;
        delete state._manualSearchSortOverride;
        return state;
    }

    return { reset, selectSort, sync };
});
