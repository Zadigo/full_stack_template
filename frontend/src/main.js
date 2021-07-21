import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './stores'

import BootstrapVue from 'bootstrap-vue'
import Buefy from 'buefy'

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
import BaseSmallFAQ from './components/BaseSmallFAQ.vue'
import BaseJumbotron from './components/BaseJumbotron.vue'
import BaseCard from './components/BaseCard.vue'


// Mixins
import globalMixins from './globalMixins'
import formFields from './mixins/formFields'

// Plugins
import Stripe from './plugins/stripe'
import Api from './plugins/api'

// Font awesome
library.add(faTrash)
library.add(faPen)
library.add(faCheck)


Vue.config.productionTip = false


// Mixins
// Vue.mixin(TitleMixin)
Vue.mixin(globalMixins)
Vue.mixin(formFields)


// Plugins
Vue.use(Api)
// Vue.use(Analytics)
Vue.use(BootstrapVue)
Vue.use(Stripe)
Vue.use(Buefy)


// Components
Vue.component('fields-iterator', FieldsIterator)
Vue.component('base-privacy-text', BasePrivacyText)
Vue.component('base-secondary-cta', BaseSecondaryCTA)
Vue.component('base-small-faq', BaseSmallFAQ)
Vue.component('base-jumbotron', BaseJumbotron)
Vue.component('base-card', BaseCard)

Vue.component('font-awesome-icon', FontAwesomeIcon)


new Vue({
  router,
  store,
  
  render: h => h(App),
}).$mount('#app')
