var _ = require('lodash')

var profileModule = {
    // Module that contains all the getters
    // actions and other state related to
    // the user profile 
    namespaced: true, 
    state: () => ({
        userDetails: {
            id: null,
            customer_id: null,
            myuser: {
                firstname: null,
                lastname: null,
                email: null,
                payments: [],
                is_active: false,
                is_admin: false,
                is_staff: false
            },
            addresses: []
        },
        hasUserDetails: false
    }),

    mutations: {
        updateUserDetails(state, payload) {
            // Update userDetails with the
            // user's data
            state.userDetails = payload
            state.hasUserDetails = true
        },

        changeAddress(state, payload) {
            var index = _.findIndex(state.userDetails.addresses, ['id', payload.id])
            state.userDetails.addresses[index] = payload
        },

        chooseMainAddress(state, id) {
            // Let's the user choose a preferred address
            _.forEach(state.userDetails.addresses, (address) => {
                address['is_main'] = false
            })
            var address = _.find(state.userDetails.addresses, ['id', id])
            address.is_main = !address.is_main
        },

        performDeleteAddress(state, addressIndex) {
            state.userDetails.addresses.splice(addressIndex, 1)
        }
    },

    actions: {
        newAddress({ state }, response) {
            state.userDetails.addresses.push(response.data)
        },

        updateAddress({ commit }, response) {
            commit('changeAddress', response.data)
        },

        deleteAddress({ state, commit }, addressId) {
            var addressIndex = _.findIndex(state.userDetails.addresses, ['id', addressId])
            commit('performDeleteAddress', addressIndex)
        },

        // updatePersonalDetails({ dispatch, commit, getters, rootGetters }, payload) {
        updatePersonalDetails({ commit }, response) {
            commit('updateUserDetails', response.data)
        }
    },

    getters: {
        getAddress: (state) => (id) => {
            // Returns a single address from the store
            return _.find(state.userDetails.addresses, ['id', id])
        },

        getUserFullName(state) {
            // Returns the full lastname and fistname
            return `${state.userDetails.myuser.firstname} ${state.userDetails.myuser.lastname}`
        }
    }
}


var authenticationModule = {
    namespaced: true,
    
    state: () => ({
        authenticated: false,
        admin: false,
        staff: false,
        active: true,
        token: null,
    }),

    mutations: {
        performLogin(state, payload) {
            let { token, details } = payload
            state.authenticated = true
            
            state.admin = details.myuser.is_admin
            state.staff = details.myuser.is_staff
            state.active = details.myuser.is_active
            
            state.token = token
            localStorage.setItem('ttk', state.token)
            this.commit('profileModule/updateUserDetails', details)
        },

        performLogout(state) {
            state.token = null
            state.admin = false
            state.staff = false
            state.active = false
            state.authenticated = false
            localStorage.removeItem('ttk')
        }
    },

    actions: {
        login({ commit }, response) {
            // Login a user and get their details
            // for userDetails
            commit('performLogin', response.data)
        },

        logout({ commit }) {
            // Logout a user and clear all their
            // details in userDetails
            commit('performLogout')
        }
    },

    getters: {
        isAuthenticated(state) {
            // If we have both token and authentication on
            // the state, consider them authenticated
            if (!_.isNull(state.token) & state.authenticated) {
                return true
            }

            // If the user has already been logged in
            // with a token that was stored in the local storage
            // keep the current state as logged in
            const currentToken = localStorage.getItem('ttk')

            if (_.isNull(currentToken)) {
                return false
            } else {
                if (!state.authenticated) {
                    return false
                } else {
                    state.token = currentToken
                    return true
                }
            }
        },

        isAdmin(state) {
            return state.admin
        }
    }
}

export {
    profileModule,
    authenticationModule
}
