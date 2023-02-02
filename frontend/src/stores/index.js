import Vue from 'vue'
import Vuex from 'vuex'
// import Cookies from 'js-cookie'

// Modules
import { authenticationModule, profileModule } from './auth'
import subscriptionsModule from './subscriptions'
import notificationsModule from './messages'
import shopModule from './shop'

Vue.use(Vuex)

var store = new Vuex.Store({
    state: () => ({
    }),

    modules: {
        authenticationModule,
        profileModule,
        notificationsModule,
        
        // Optional
        subscriptionsModule,
        shopModule
    },

    getters: {
        getAuthenticationToken(state) {
            return state.authenticationModule.token
        }
    }
})


export default store
