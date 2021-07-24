// Main store elements for all the application.
// Contains a basic profile and authentication
// module
// import axios from 'axios'
// import router from '../router/index'
// function urlJoin(url, path) {
//     return new URL(path, url)
// }


import { isNull } from 'lodash'

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
        // initialUserDetails(state, payload) {
        //     // Updates some very specific user details
        //     // such as the firstname, the lastname and
        //     // the email address. P.S. Might also update
        //     // the date of birth
        //     _.forEach(Object.keys(payload.myuser), (key) => {
        //         state.userDetails[key] = payload.myuser[key]
        //     })
        //     state.userDetails.addresses = payload.addresses
        //     state.hasUserDetails = true
        // },

        updateUserDetails(state, payload) {
            // _.forEach(Object.keys(payload), (key) => {
            //     state.userDetails[key] = payload[key]
            // })
            // state.hasUserDetails = true
            state.userDetails = payload
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
            // Updates the state in the profileModule
            // with the initial values in the userDetails state
            this.commit('profileModule/updateUserDetails', details)

            state.admin = details.myuser.is_admin
            state.staff = details.myuser.is_staff
            state.active = details.myuser.is_active

            state.token = token
            localStorage.setItem('ttk', state.token)
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
            // Initiates a login request to Django
            // let { email, username, password } = payload
            
            // When a person just presses the button without
            // entering anykind of credentials, we should
            // not be continuing the process
            // if (isNull(email) | isNull(username) && isNull(password)) {
            //     console.error('No crendentials entered')
            //     return false
            // }
            commit('performLogin', response.data)
        },

        // logout({ state, commit, rootState }) {
        logout({ commit }) {
            commit('performLogout')
        },

        signUp({ rootState }, payload) {
            let { email, password1, password2 } = payload

            if (isNull(email) && isNull(password1) && isNull(password2)) {
                console.error('No or not enough credentials entered')
                return false
            }
            rootState
            // axios({
            //     method: 'post',
            //     url: urlJoin(rootState.baseUrls.api, 'signup'),
            //     data: payload,
            //     headers: {
            //         'Content-Type': 'application/json'
            //     },
            //     withCredentials: true
            // })
            // .then((response) => {
            //     if (response.status >= 200 && response.status <= 201) {
            //         router.push({ name: 'signin' })
            //     } else {
            //         console.log(response.data)
            //     }
            // })
            // .catch((error) => {
            //     console.log(error)
            // })
        }
    },

    getters: {
        isAuthenticated(state) {
            // If the user has already been logged in
            // with a token that was stored in the local storage
            // keep the current state as logged in
            const currentToken = localStorage.getItem('ttk')

            if (_.isNull(currentToken)) {
                // return state.authenticated && !_.isNull(state.token)
                return state.authenticated
            } else {
                state.token = currentToken
                return true
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
