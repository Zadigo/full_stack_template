import { createApp } from 'vue'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { createPinia } from 'pinia'
import { createHead } from 'unhead'

import App from './App.vue'
import router from './router'

import './style.scss'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'mdb-ui-kit/css/mdb.min.css'
import installPlugins from './plugins'

const app = createApp(App)

const pinia = createPinia()

createHead()

app.use(installPlugins())
app.use(router)
app.use(pinia)
app.component('FontAwesomeIcon', FontAwesomeIcon)
app.mount('#app')
