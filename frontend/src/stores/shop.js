var _ = require('lodash')
import products from '../data/products.json'

var cartModule = {
    // This sections deals with products
    // or items that the user has placed
    // in the cart of future payment
    state: () => ({
        cart: []
    }),

    mutations: {
        addToCart(state, payload) {
            var lastItem = _.last(state.cart)
            var id = 1
            if (lastItem !== undefined) {
                id = lastItem.id + 1
            }
            payload['id'] = id
            state.cart.push(payload)
        },

        emptyCart(state) {
            state.cart = []
        }
    },

    getters: {
        cartIsEmpty(state) {
            return state.cart.length === 0
        },

        numberOfItems(state) {
            return state.cart.length
        }
    }
}


var shopModule = {
    namespaced: true,

    state: () => ({
        // items: []
        items: products
    }),

    modules: {
        cartModule: cartModule
    },

    mutations: {
        newItem(state, item) {
            state.items.push(item)
        }
    },

    getters: {
        getProduct (state) {
            return (id) => {
                return _.find(state.items, ['id', id])
            }
        }
    }
}

export default shopModule
