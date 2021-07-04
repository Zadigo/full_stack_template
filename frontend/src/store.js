import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from './routes'

import products from './products.js'

import Cookies from 'js-cookie'

var _ = require('lodash')


function urlJoin (url, path) {
    return new URL(path, url)
}



Vue.use(Vuex)

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
        getCart(state) {
            return state.cart
        },
        cartEmpty(state) {
            return state.cart.length === 0
        },
        numberOfItems(state) {
            return state.cart.length
        }
    }
}

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
    },
    actions: {
        
    }
}

var authenticationModule = {
    namespaced: true,
    state: () => ({
        authenticated: false,
        admin: false,
        staff: false,
        token: null,
        userDetails: {
            id: null,
            firstname: null,
            lastname: null,
            email: null,
            payments: [],
            addresses: []
        }
    }),
    mutations: {
        performLogin(state, payload) {
            state.authenticated = true
            this.commit('authenticationModule/updateUserDetails', payload.myuser)
            state.admin = payload.myuser.is_admin
            state.staff = payload.myuser.is_staff
            state.token = payload.token
            localStorage.setItem('ttk', state.token)
        },
        performLogout (state) {
            state.token = null
            state.authenticated = false
            state.userDetails = {
                firstname: null,
                lastname: null,
                email: null,
                payments: [],
                addresses: []
            }
        },
        updateUserDetails(state, values) {
            // Updates some very specific user details
            // such as the firstname, the lastname and
            // the email address. P.S. Might also update
            // the date of birth
            _.forEach(Object.keys(values), (key) => {
                // if (Object.keys(state.userDetails).includes(key)) {
                //     state.userDetails[key] = values[key]
                // }
                state.userDetails[key] = values[key]
            })
        },
        addNewCreditCard (state, values) {
            // The front end should request adding a new
            // card to Stripe and then return a token to be used
            // in the app overall
            values
            var id = 1
            var lastCard = _.last(state.payments)
            if (lastCard !== undefined) {
                id = lastCard.id + 1
            }
            state.userDetails.payments.push({ id: id, token: 'cc-dnfozienoz' })
        },
        deleteCreditCard (state, id) {
            var paymentsCopy = [...state.userDetails.payments]
            var cardIndex = _.findIndex(paymentsCopy, ['id', id])
            if (cardIndex !== undefined) {
                paymentsCopy.splice(0, cardIndex)
                state.userDetails.payments = paymentsCopy
            }
        },
        deleteAddress (state) {
            state
        },
        mainAddress (state, id) {
            // Let's the user select a preferred address
            _.forEach(state.userDetails.addresses, (address) => {
                address['is_main'] = false
            })
            var address = _.find(state.userDetails.addresses, ['id', id])
            address.is_main = !address.is_main
        }
    },
    actions: {
        login({ commit, rootState }, payload) {
            // Initiates a login request to Django
            let { email, username, password } = payload
            var requestUrl = urlJoin(rootState.baseUrls.api, 'login')
            axios({
                method: 'post',
                url: requestUrl.href,
                data: { email: email, username: username, password: password},
                headers: {
                    'Content-Type': 'application/json'
                },
                withCredentials: true
            })
            .then((response) => {
                if (response.status === 200) {
                    commit('performLogin', response.data)
                    router.push({ name: 'home' })
                } else {
                    // TODO: Find a way to show message
                    console.error(response.data)
                }
            })
            .catch((error) => {
                console.log(error)
            })
        },
        logout({ commit, rootState }) {
            axios({
                url: urlJoin(rootState.baseUrls.api, 'logout'),
                method: 'post',
                data: null,
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then((response) => {
                response.data
                commit('performLogout')
                router.push({ name: 'home' })
            })
            .error((error) => {
                console.log(error)
            })
        },
        signUp({ rootState }, payload) {
            let { password1, password2 } = payload
            password1, password2
            axios({
                method: 'post',
                url: urlJoin(rootState.baseUrls.api, 'signup'),
                data: payload,
                headers: {
                    'Content-Type': 'application/json'
                },
                withCredentials: true
            })
            .then((response) => {
                if (response.status >= 200 && response.status <= 201) {
                    router.push({ name: 'signin' })
                } else {
                    console.log(response.data)
                }
            })
            .catch((error) => {
                console.log(error)
            })
        },
        newAddress({ state, rootState }, payload) {
            axios({
                method: 'post',
                url: urlJoin(rootState.baseUrls.api, 'new-address'),
                data: payload,
                headers: {
                    'Authorization': `Token ${state.token}`,
                    'Content-Type': 'application/json',
                    'X-CSRFToken': Cookies.get('csrftoken')
                }
            })
            .then((response) => {
                if (response.status >= 200 | response.status <= 201) {
                    state.userDetails.addresses.push(response.data)
                } else {
                    console.log(response.data)
                }
            })
            .catch((error) => {
                console.log(error)
            })
        },

    },
    getters: {
        isAuthenticated(state) {
            // If the user has already been logged in
            // with a token that was stored in the local storage
            // keep the current state as logged in
            // const currentToken = localStorage.getItem('ttk')
            // if (currentToken !== undefined) {
            //     return true
            // }
            return state.authenticated && state.token !== null
        },
        isAdmin(state) {
            return state.admin
        },
        userFullName (state) {
            return `${state.userDetails.firstname} ${state.userDetails.lastname}`
        },
        userFirstName (state) {
            return state.userDetails.firstname
        },
        getUserDetails (state) {
            return state.userDetails
        },
        getPaymentMethods (state) {
            return state.userDetails.payments
        },
        getUserAddresses (state) {
            return state.userDetails.addresses
        },
        getAuthenticationToken (state) {
            return state.token
        },
        getToken(state) {
            return state.token
        },
        hasPaymentMethods (state) {
            return state.userDetails.payments.length > 0
        }
    }
}

var itemsModule = {
    namespaced: true,
    state: () => ({
        items: products
    }),
    mutations: {
        newItem(state, item) {
            state.items.push(item)
        },
        duplicateItems(state, payload) {
            state
            payload
            // var lastItem = _.last(state.items)
            // var products = _.filter(state.items, (item) => {
            //     return payload.includes(item.id)
            // })
            // _.forEach(products, (product) => {
            //     product['id'] = lastItem += 1
            // })
            // state.items.push(products)
        },
        activateItems (state, payload) {
            state
            payload
        },
        deactivateItems (state, payload) {
            state,
            payload
        },
        deleteItems (state, payload) {
            var items = _.reject(state.items, (item) => {
                return payload.includes(item.id)
            })
            state.items = items
        }
    },
    getters: {
        getItems(state) {
            return state.items
        },
        getItem: (state) => (id) => {
            return _.find(state.items, { id: id })
        }
    }
}

var store = new Vuex.Store({
    state: () => ({
        baseUrls: {
            api: 'http://127.0.0.1:8000/api/v1/'
        }
    }),
    modules: {
        itemsModule: itemsModule,
        authenticationModule: authenticationModule,
        subscriptionsModule: subscriptionsModule,
        cartModule: cartModule
    }
})

export default store
