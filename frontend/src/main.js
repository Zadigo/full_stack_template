import { createApp, toRaw } from 'vue'
import App from './App.vue'

import './plugins/fontawesome'
import '@mdi/font/css/materialdesignicons.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'mdb-ui-kit/css/mdb.min.css'

<<<<<<< HEAD
// CSS
// require('buefy/dist/buefy.css')
require('../node_modules/bootstrap/dist/css/bootstrap.css')
require('./assets/style.css')
require('./assets/admin.css')
// require('')

// Font awesome
import { library } from '@fortawesome/fontawesome-svg-core'
import { faTrash, faPen, faCheck, faStar, faSearch } from '@fortawesome/free-solid-svg-icons'
=======
import { loadFonts } from './plugins'
>>>>>>> 29457371f93f9f58670a2a9fcba37192e4692f09
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

<<<<<<< HEAD
// Plugins
import Stripe from './plugins/stripe'
import Api from './plugins/api'
import BootstrapVue from 'bootstrap-vue'
import vuetify from './plugins/vuetify'
// import Buefy from 'buefy'

// Font awesome
library.add(faTrash)
library.add(faPen)
library.add(faCheck)
library.add(faStar)
library.add(faSearch)

// Mixins
Vue.mixin(globalMixin)
Vue.mixin(formMixin)

// Plugins
Vue.use(Api)
Vue.use(BootstrapVue)
Vue.use(Stripe)
// Vue.use(Buefy)
// Vue.use(Analytics)

// Components
Vue.component('fields-iterator', FieldsIterator)
Vue.component('base-privacy-text', BasePrivacyText)
Vue.component('base-secondary-cta', BaseSecondaryCTA)
Vue.component('base-small-faq', BaseSmallFAQ)
Vue.component('base-jumbotron', BaseJumbotron)
Vue.component('base-card', BaseCard)
Vue.component('base-hero', BaseHero)
Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,

  render: h => h(App),
}).$mount('#app')
=======
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
app.component('FontAwesomeIcon', FontAwesomeIcon)
app.mount('#app')
>>>>>>> 29457371f93f9f58670a2a9fcba37192e4692f09
