import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './stores'

import BootstrapVue from 'bootstrap-vue'
import Buefy from 'buefy'

// CSS
// require('buefy/dist/buefy.css')
require('../node_modules/bootstrap/dist/css/bootstrap.css')
require('./assets/style.css')
require('./assets/admin.css')

// Font awesome
import { library } from '@fortawesome/fontawesome-svg-core'
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

// Global components
import FieldsIterator from './components/FieldsIterator.vue'
import PrivacyText from './components/PrivacyText.vue'
import BannerCTA from './components/BannerCTA.vue'
import SmallFAQ from './components/SmallFAQ.vue'
import BaseJumbotron from './components/BaseJumbotron.vue'


// Mixins
import globalMixins from './globalMixins'

// Plugins
import Stripe from './plugins/stripe'

// Font awesome
library.add(faUserSecret)


Vue.config.productionTip = false


// Mixins
// Vue.mixin(TitleMixin)
Vue.mixin(globalMixins)


// Plugins
// Vue.use(Api)
// Vue.use(Analytics)
Vue.use(BootstrapVue)
Vue.use(Stripe)
Vue.use(Buefy)


// Components
Vue.component('fields-iterator', FieldsIterator)
Vue.component('privacy-text', PrivacyText)
Vue.component('banner-cta', BannerCTA)
Vue.component('small-faq', SmallFAQ)
Vue.component('base-jumbotron', BaseJumbotron)

Vue.component('font-awesome-icon', FontAwesomeIcon)


new Vue({
  router,
  store,
  
  render: h => h(App),
}).$mount('#app')