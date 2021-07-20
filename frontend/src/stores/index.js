import Vue from 'vue'
import Vuex from 'vuex'

// var _ = require('lodash')

// import Cookies from 'js-cookie'

// Modules
import { authenticationModule, profileModule } from './auth'
import subscriptionsModule from './subscriptions'
import Messages from './messages'

Vue.use(Vuex)

var store = new Vuex.Store({
    state: () => ({
        baseUrls: {
            api: 'http://127.0.0.1:8000/api/v1/'
        }
    }),

    modules: {
        authenticationModule,
        profileModule,
        Messages,
        
        // Optional
        subscriptionsModule,
        // shopModule
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
