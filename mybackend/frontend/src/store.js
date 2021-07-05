import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from './routes'
// import Cookies from 'js-cookie'

// Modules
// import shopModule from './stores/shop'


var _ = require('lodash')


function urlJoin (url, path) {
    return new URL(path, url)
}


Vue.use(Vuex)


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


var store = new Vuex.Store({
    state: () => ({
        baseUrls: {
            api: 'http://127.0.0.1:8000/api/v1/'
        }
    }),

    modules: {
        authenticationModule: authenticationModule,
        profileModule: profileModule,

        // Optional
        // shopModule: shopModule
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
