import Vue from 'vue'
import App from './App.vue'
import router from './routes.js'
import store from './store.js'
import BootstrapVue from 'bootstrap-vue'

// Global components
import FieldsIterator from './components/FieldsIterator.vue'
import PrivacyText from './components/PrivacyText.vue'
import BannerCTA from './components/BannerCTA.vue'
import SmallFAQ from './components/SmallFAQ.vue'

// Mixins
import TitleMixin from './titleMixin'
import globalMixins from './globalMixins'

// Plugins
// import projectPlugins from './projectPlugins'
import Stripe from './plugins/stripe'

Vue.config.productionTip = false

Vue.mixin(TitleMixin)
Vue.mixin(globalMixins)

Vue.use(BootstrapVue)
// Vue.use(projectPlugins)
Vue.use(Stripe)

Vue.component('fields-iterator', FieldsIterator)
Vue.component('privacy-text', PrivacyText)
Vue.component('banner-cta', BannerCTA)
Vue.component('small-faq', SmallFAQ)

new Vue({
  router,
  store,
  
  render: h => h(App),
}).$mount('#app')
