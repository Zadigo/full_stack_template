export default subscriptionsModule = {
    // This module deals with everything
    // related to the pricing page and
    // the user's actual subscription

    // This is kind of distinct from the
    // cart because it deals specifically
    // with services that require a subscription.
    // These items are thereafter placed in the
    // users cart once selected

    namespaced: true,
    state: () => ({
        currentSubscription: {},
        selectedSubscription: {},
    }),

    mutations: {
        selectSubscription(state, payload) {
            state.selectedSubscription = payload
        }
    },

    getters: {
        hasSubscription(state) {
            if (Object.keys(state.currentSubscription).length === 0) {
                return false
            } else {
                return true
            }
        },
        hasSelectedSubscription(state) {
            if (Object.keys(state.selectedSubscription).length === 0) {
                return false
            } else {
                return true
            }
        }
    }
}
