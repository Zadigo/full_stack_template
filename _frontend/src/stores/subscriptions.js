import { lengthOfDict } from '../utils'

var subscriptionsModule = {
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
        chooseSubscription(state, payload) {
            state.selectedSubscription = payload
        }
    },

    getters: {
        hasSubscription(state) {
            return lengthOfDict(state.currentSubscription) > 0
        },
        hasSelectedSubscription(state) {
            return lengthOfDict(state.selectedSubscription) > 0
        }
    }
}

export default subscriptionsModule
