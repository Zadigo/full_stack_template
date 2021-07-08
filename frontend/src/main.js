import Vue from 'vue'
import App from './App.vue'
import router from './routes.js'
import store from './stores'

import BootstrapVue from 'bootstrap-vue'
import Buefy from 'buefy'
// import 'buefy/dist/buefy.css'


// Global components
import FieldsIterator from './components/FieldsIterator.vue'
import PrivacyText from './components/PrivacyText.vue'
import BannerCTA from './components/BannerCTA.vue'
import SmallFAQ from './components/SmallFAQ.vue'
import BaseJumbotron from './components/BaseJumbotron.vue'


// Mixins
// import TitleMixin from './titleMixin'
import globalMixins from './globalMixins'

// Plugins
import Stripe from './plugins/stripe'
// import Analytics from './plugins/analytics'
// import Api from './api'

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


new Vue({
  router,
  store,
  
  render: h => h(App),
}).$mount('#app')
