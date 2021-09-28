import Vue from 'vue'
import App from './App.vue'

// Router / Store
import router from './router'
import store from './stores'

// CSS
require('buefy/dist/buefy.css')
require('../node_modules/bootstrap/dist/css/bootstrap.css')
require('./assets/style.css')
require('./assets/admin.css')

// Font awesome
import { library } from '@fortawesome/fontawesome-svg-core'
import { faTrash, faPen, faCheck } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

// Global components
import FieldsIterator from './components/FieldsIterator.vue'
import BasePrivacyText from './components/BasePrivacyText.vue'
import BaseSecondaryCTA from './components/BaseSecondaryCTA.vue'

import BaseSmallFAQ from './components/layouts/BaseSmallFAQ.vue'
import BaseJumbotron from './components/layouts/BaseJumbotron.vue'
import BaseCard from './components/layouts/BaseCard.vue'

// Mixins
import globalMixin from './mixins'
import formMixin from './mixins/form'

// Plugins
import Stripe from './plugins/stripe'
import Api from './plugins/api'
// import vuetify from './plugins/vuetify'
import BootstrapVue from 'bootstrap-vue'
import Buefy from 'buefy'

// Font awesome
library.add(faTrash)
library.add(faPen)
library.add(faCheck)

// Mixins
Vue.mixin(globalMixin)
Vue.mixin(formMixin)

// Plugins
Vue.use(Api)
Vue.use(BootstrapVue)
Vue.use(Stripe)
Vue.use(Buefy)
// Vue.use(Analytics)

// Components
Vue.component('fields-iterator', FieldsIterator)
Vue.component('base-privacy-text', BasePrivacyText)
Vue.component('base-secondary-cta', BaseSecondaryCTA)
Vue.component('base-small-faq', BaseSmallFAQ)
Vue.component('base-jumbotron', BaseJumbotron)
Vue.component('base-card', BaseCard)
Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  // vuetify,
  
  render: h => h(App),
}).$mount('#app')
