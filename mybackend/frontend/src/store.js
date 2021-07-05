import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from './routes'

// import products from './products.js'

// import Cookies from 'js-cookie'

var _ = require('lodash')


function urlJoin (url, path) {
    return new URL(path, url)
}


Vue.use(Vuex)


// var cartModule = {
//     // This sections deals with products
//     // or items that the user has placed
//     // in the cart of future payment
//     state: () => ({
//         cart: []
//     }),

//     mutations: {
//         addToCart(state, payload) {
//             var lastItem = _.last(state.cart)
//             var id = 1
//             if (lastItem !== undefined) {
//                 id = lastItem.id + 1
//             }
//             payload['id'] = id
//             state.cart.push(payload)
//         },
//         emptyCart(state) {
//             state.cart = []
//         }
//     },

//     getters: {
//         getCart(state) {
//             return state.cart
//         },
//         cartEmpty(state) {
//             return state.cart.length === 0
//         },
//         numberOfItems(state) {
//             return state.cart.length
//         }
//     }
// }


// var subscriptionsModule = {
//     // This module deals with everything
//     // related to the pricing page and
//     // the user's actual subscription

//     // This is kind of distinct from the
//     // cart because it deals specifically
//     // with services that require a subscription.
//     // These items are thereafter placed in the
//     // users cart once selected

//     namespaced: true,
//     state: () => ({
//         currentSubscription: {},
//         selectedSubscription: {},
//     }),

//     mutations: {
//         selectSubscription(state, payload) {
//             state.selectedSubscription = payload
//         }
//     },
    
//     getters: {
//         hasSubscription(state) {
//             if (Object.keys(state.currentSubscription).length === 0) {
//                 return false
//             } else {
//                 return true
//             }
//         },
//         hasSelectedSubscription(state) {
//             if (Object.keys(state.selectedSubscription).length === 0) {
//                 return false
//             } else {
//                 return true
//             }
//         }
//     }
// }


// Module that contains all the getters
// actions and other state related to
// the user profile 
var profileModule = {
    state: () => ({
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
        changeAddress(state, payload) {
            var index = _.findIndex(state.updateUserDetails.addresses, ['id', payload.id])
            state.userDetails.addresses[index] = payload
        },

        initialUserDetails(state, payload) {
            // Updates some very specific user details
            // such as the firstname, the lastname and
            // the email address. P.S. Might also update
            // the date of birth
            _.forEach(Object.keys(payload.myuser), (key) => {
                // if (Object.keys(state.userDetails).includes(key)) {
                //     state.userDetails[key] = values[key]
                // }
                state.userDetails[key] = payload.myuser[key]
            })
            state.userDetails.addresses = payload.addresses
        },

        updateUserDetails(state, payload) {
            _.forEach(Object.keys(payload), (key) => {
                state.userDetails[key] = payload[key]
            })
        },

        chooseMainAddress(state, id) {
            // Let's the user choose a preferred address
            _.forEach(state.userDetails.addresses, (address) => {
                address['is_main'] = false
            })
            var address = _.find(state.userDetails.addresses, ['id', id])
            address.is_main = !address.is_main
        }
    },

    actions: {
        newAddress({ state, rootState }, payload) {
            axios({
                method: 'post',
                url: urlJoin(rootState.baseUrls.api, 'new-address').href,
                data: payload,
                responseType: 'json',
                headers: {
                    'Authorization': `Token ${state.token}`,
                    'Content-Type': 'application/json',
                },
                widthCredentials: true
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

        updateAddress({ commit, getters }, payload) {
            // Update an address by sending a request
            // to the backend in order to implement
            // the change
            axios({
                method: 'patch',
                url: `http://127.0.0.1:8000/api/v1/new-address`,
                responseType: 'json',
                data: payload,
                headers: {
                    'Authorization': `Token ${ getters.getAuthenticationToken }`,
                    'Content-Type': 'application/json',
                },
                withCredentials: true
            })
            .then((response) => {
                if (response.status >= 200) {
                    commit('changeAddress', response.data)
                }
            })
            .catch((error) => {
                console.log(error)
            })
        },

        deleteAddress(state) {
            state
        },

        // updatePersonalDetails({ dispatch, commit, getters, rootGetters }, payload) {
        updatePersonalDetails({ commit, getters }, payload) {
            // Updates details from the /details page such as
            // firstname, lastname and email
            axios({
                method: 'post',
                url: urlJoin(getters.getApiUrl, 'update-details').href,
                data: payload,
                responseType: 'json',
                headers: {
                    'Authorization': `Token ${ getters.getAuthenticationToken }`,
                    'Content-Type': 'application/json',
                },
                widthCredentials: true
            })
            .then((response) => {
                commit('updateUserDetails', response.data)
            })
            .catch((error) => {
                console.log(error)
            })
        }
    },

    getters: {
        getAddress: (state) => (id) => {
            // Returns a single address from the store
            return _.find(state.userDetails.addresses, ['id', id])
        },

        getUserFullName(state) {
            return `${state.userDetails.firstname} ${ state.userDetails.lastname }`
        }
    }
}


var authenticationModule = {
    namespaced: true,
    
    state: () => ({
        authenticated: false,
        admin: false,
        staff: false,
        token: null
    }),

    mutations: {
        performLogin(state, payload) {
            state.authenticated = true
            // Updates the state in the profileModule
            // with the initial values for the userDetail
            // state
            this.commit('initialUserDetails', payload.myuser)
            state.admin = payload.myuser.myuser.is_admin
            state.staff = payload.myuser.myuser.is_staff
            state.token = payload.token
            localStorage.setItem('ttk', state.token)
            router.push({ name: 'home' })
        },

        performLogout(state) {
            state.token = null
            state.admin = false
            state.staff = false
            state.authenticated = false
        }
    },

    actions: {
        login({ commit, rootState }, payload) {
            // Initiates a login request to Django
            let { email, username, password } = payload
            axios({
                method: 'post',
                url: urlJoin(rootState.baseUrls.api, 'login').href,
                responseType: 'json',
                data: { email: email, username: username, password: password},
                headers: {
                    'Content-Type': 'application/json'
                },
                withCredentials: true
            })
            .then((response) => {
                if (response.status >= 200) {
                    commit('performLogin', response.data)
                } else {
                    // TODO: Find a way to show message
                    console.error(response.data)
                }
            })
            .catch((error) => {
                console.log(error)
            })
        },

        logout({ state, commit, rootState }) {
            axios({
                url: urlJoin(rootState.baseUrls.api, 'logout'),
                method: 'post',
                headers: {
                    'Authorization': `Token ${state.token}`,
                    'Content-Type': 'application/json'
                },
                withCredentials: true
            })
            .then((response) => {
                commit('performLogout', response.data)
                router.push({ name: 'home' })
            })
            .catch((error) => {
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
        }
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

        // getAuthenticationToken (state) {
        //     return state.token
        // }
    }
}


// var itemsModule = {
//     namespaced: true,
//     state: () => ({
//         items: products
//     }),

//     mutations: {
//         newItem(state, item) {
//             state.items.push(item)
//         },
//         duplicateItems(state, payload) {
//             state
//             payload
//             // var lastItem = _.last(state.items)
//             // var products = _.filter(state.items, (item) => {
//             //     return payload.includes(item.id)
//             // })
//             // _.forEach(products, (product) => {
//             //     product['id'] = lastItem += 1
//             // })
//             // state.items.push(products)
//         },

//         activateItems (state, payload) {
//             state
//             payload
//         },

//         deactivateItems (state, payload) {
//             state,
//             payload
//         },

//         deleteItems (state, payload) {
//             var items = _.reject(state.items, (item) => {
//                 return payload.includes(item.id)
//             })
//             state.items = items
//         }
//     },

//     getters: {
//         getItems(state) {
//             return state.items
//         },
        
//         getItem: (state) => (id) => {
//             return _.find(state.items, { id: id })
//         }
//     }
// }


var store = new Vuex.Store({
    state: () => ({
        baseUrls: {
            api: 'http://127.0.0.1:8000/api/v1/'
        }
    }),

    modules: {
        // itemsModule: itemsModule,
        authenticationModule: authenticationModule,
        // subscriptionsModule: subscriptionsModule,
        // cartModule: cartModule,
        profileModule: profileModule
    },

    getters: {
        getAuthenticationToken(state) {
            return state.authenticationModule.token
        },
        getApiUrl(state) {
            return state.baseUrls.api
        }
    }
})


export default store
