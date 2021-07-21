import axios from 'axios'
import router from '../router/index'
import { isNull } from 'lodash'
// import TestAxios from '../axiosConfig'

var _ = require('lodash')

// Main store elements for all the application.
// Contains a basic profile and authentication
// module

function urlJoin(url, path) {
    return new URL(path, url)
}


var profileModule = {
    // Module that contains all the getters
    // actions and other state related to
    // the user profile 
    namespaced: true, 
    state: () => ({
        userDetails: {
            id: null,
            firstname: null,
            lastname: null,
            email: null,
            payments: [],
            addresses: []
        },
        hasUserDetails: false
    }),

    mutations: {
        changeAddress(state, payload) {
            var index = _.findIndex(state.userDetails.addresses, ['id', payload.id])
            state.userDetails.addresses[index] = payload
        },

        initialUserDetails(state, payload) {
            // Updates some very specific user details
            // such as the firstname, the lastname and
            // the email address. P.S. Might also update
            // the date of birth
            _.forEach(Object.keys(payload.myuser), (key) => {
                state.userDetails[key] = payload.myuser[key]
            })
            state.userDetails.addresses = payload.addresses
            state.hasUserDetails = true
        },

        updateUserDetails(state, payload) {
            _.forEach(Object.keys(payload), (key) => {
                state.userDetails[key] = payload[key]
            })
            state.hasUserDetails = true
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
        newAddress({ state }, response) {
            state.userDetails.addresses.push(response.data)
            // axios({
            //     method: 'post',
            //     url: urlJoin(rootState.baseUrls.api, 'new-address').href,
            //     data: payload,
            //     responseType: 'json',
            //     headers: {
            //         'Authorization': `Token ${rootGetters.getAuthenticationToken}`,
            //         'Content-Type': 'application/json',
            //     },
            //     widthCredentials: true
            // })
            // .then((response) => {
            //     if (response.status >= 200 | response.status <= 201) {
            //         state.userDetails.addresses.push(response.data)
            //     } else {
            //         console.log(response.data)
            //     }
            // })
            // .catch((error) => {
            //     console.log(error)
            // })
        },

        updateAddress({ commit }, response) {
            commit('changeAddress', response.data)
            // Update an address by sending a request
            // to the backend in order to implement
            // the change
            // axios({
            //     method: 'post',
            //     url: `http://127.0.0.1:8000/api/v1/new-address`,
            //     responseType: 'json',
            //     data: payload,
            //     headers: {
            //         'Authorization': `Token ${rootGetters.getAuthenticationToken}`,
            //         'Content-Type': 'application/json',
            //     },
            //     withCredentials: true
            // })
            // .then((response) => {
            //     if (response.status >= 200) {
            //         commit('changeAddress', response.data)
            //     }
            // })
            // .catch((error) => {
            //     console.log(error)
            // })
        },

        deleteAddress(state, id) {
            var itemId = _.findIndex(state.userDetails.addresses, ['id', id])
            state.userDetails.addresses.splice(itemId, 1)
        },

        // updatePersonalDetails({ dispatch, commit, getters, rootGetters }, payload) {
        updatePersonalDetails({ commit }, returnData) {
            commit('updateUserDetails', returnData.response.data)
            // Updates details from the /details page such as
            // firstname, lastname and email
            // axios({
            //     method: 'post',
            //     url: urlJoin(rootGetters.getApiUrl, 'update-details').href,
            //     data: payload,
            //     responseType: 'json',
            //     headers: {
            //         'Authorization': `Token ${rootGetters.getAuthenticationToken}`,
            //         'Content-Type': 'application/json',
            //     },
            //     widthCredentials: true
            // })
            // .then((response) => {
            //     commit('updateUserDetails', response.data)
            // })
            // .catch((error) => {
            //     console.log(error)
            // })
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
        token: null,
        active: true,
    }),

    mutations: {
        performLogin(state, payload) {
            let { token, details } = payload
            state.authenticated = true
            // Updates the state in the profileModule
            // with the initial values in the userDetails state
            this.commit('profileModule/initialUserDetails', details)

            state.admin = details.myuser.is_admin
            state.staff = details.myuser.is_staff
            state.active = details.myuser.is_active

            state.token = token
            localStorage.setItem('ttk', state.token)
        },

        performLogout(state) {
            localStorage.removeItem('ttk')
            state.token = null
            state.admin = false
            state.staff = false
            state.active = false
            state.authenticated = false
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
            // axios({
            //     method: 'post',
            //     url: urlJoin(rootState.baseUrls.api, 'login').href,
            //     responseType: 'json',
            //     data: { email: email, username: username, password: password},
            //     headers: {
            //         'Content-Type': 'application/json'
            //     },
            //     withCredentials: true
            // })
            // .then((response) => {
            //     if (response.status >= 200) {
            //         commit('performLogin', response.data)
            //     } else {
            //         // TODO: Find a way to show message
            //         console.error(response.data)
            //     }
            // })
            // .catch((error) => {
            //     var msg = { app: 'auth', content: "Nous n'avons pas pu vous vous connecter" }
            //     dispatch('newDangerMessage', msg, { root: true })
            //     console.log(error)
            // })
        },

        // logout({ state, commit, rootState }) {
        logout({ commit }, response) {
            // axios({
            //     url: urlJoin(rootState.baseUrls.api, 'logout').href,
            //     method: 'post',
            //     headers: {
            //         'Authorization': `Token ${state.token}`,
            //         'Content-Type': 'application/json'
            //     },
            //     withCredentials: true
            // })
            // .then((response) => {
            //     commit('performLogout', response.data)
            //     router.push({ name: 'home' })
            // })
            // .catch((error) => {
            //     console.log(error)
            // })
            commit('performLogout', response)
        },

        signUp({ rootState }, payload) {
            let { email, password1, password2 } = payload

            if (isNull(email) && isNull(password1) && isNull(password2)) {
                console.error('No or not enough credentials entered')
                return false
            }

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
            const currentToken = localStorage.getItem('ttk')
            console.log('Local storage token', currentToken)
            if (!_.isNull(currentToken)) {
                state.token = currentToken
                return true
            }
            // return state.authenticated && !_.isNull(state.token)
            return state.authenticated
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
