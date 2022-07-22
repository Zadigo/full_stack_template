import { createApp, toRaw } from 'vue'
import App from './App.vue'

import '@mdi/font/css/materialdesignicons.css'
import './plugins/fontawesome'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'mdb-ui-kit/css/mdb.min.css'

// import NavItemVue from './components/nav/NavItem.vue'
import { loadFonts } from './plugins'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { createLocalStorage, createVueSession } from './plugins/vue-storages'
import { createPinia } from 'pinia'
import { createAxios } from './plugins/axios'
import router from './router'
import i18n from './i18n'
import messagesPlugin from '@/store/messages'
// import {  functions } from './plugins/vue-analytics/google'
// import { createGoogleAnalytics } from './plugins/vue-analytics/google'

loadFonts()

const app = createApp(App)

const session = createVueSession()
const localstorage = createLocalStorage()
const pinia = createPinia()

pinia.use(messagesPlugin)

pinia.use(({ store }) => {
  store.router = toRaw(router)
  store.session = toRaw(session)
  store.localstorage = toRaw(localstorage)
})

// const analytics = createGoogleAnalytics('some-tag', {
//   currency: 1
// })
// console.log('test', session.retrieve(1))
app.use(router)
// app.use(analytics)
app.use(session)
app.use(localstorage)
app.use(pinia)
app.use(i18n)
app.use(createAxios())
// app.component('NavItemVue', NavItemVue)
app.component('FontAwesomeIcon', FontAwesomeIcon)
app.mount('#app')
