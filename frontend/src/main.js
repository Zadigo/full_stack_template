import { createApp, markRaw } from 'vue'
import App from './App.vue'

import 'bootstrap/dist/css/bootstrap.min.css'
import 'mdb-ui-kit/css/mdb.min.css'
import '@mdi/font/css/materialdesignicons.css'
import './plugins/fontawesome'
import router from './router'

import NavItemVue from './components/nav/NavItem.vue'
import { loadFonts, useMessagesPlugin } from './plugins'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { createLocalStorage, createVueSession } from './plugins/vue-storages'
import { createPinia } from 'pinia'
// import {  functions } from './plugins/vue-analytics/google'
// import { createGoogleAnalytics } from './plugins/vue-analytics/google'
// console.log(functions)
loadFonts()

const app = createApp(App)

const session = createVueSession()
const localstorage = createLocalStorage()
const pinia = createPinia()

pinia.use(useMessagesPlugin)

pinia.use((store) => {
  store.sessionStorage = markRaw(session)
  store.localstorage = markRaw(localstorage)
})

// const analytics = createGoogleAnalytics('some-tag', {
//   currency: 1
// })
console.log('test', session.retrieve(1))
app.use(router)
// app.use(analytics)
app.use(session)
app.use(localstorage)
app.use(pinia)
app.component('NavItemVue', NavItemVue)
app.component('FontAwesomeIcon', FontAwesomeIcon)
app.mount('#app')
