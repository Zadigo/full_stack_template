<template>
  <div class="card-body">
    <div class="row">
      <div class="col-12">
        <form @submit.prevent>
          <input v-model="loginCredentials.email" type="email" autocomplete="email" class="form-control p-2 my-2">
          <input v-model="loginCredentials.password" type="password" autocomplete="current-password" class="form-control p-2 my-2">

          <vue-recaptcha :sitekey="'1234'" :load-recaptcha-script="false" @verify="handleSuccess" @error="handleError" />
        </form>
      </div>

      <div class="col-12">
        <auth-navigation-vue />
      </div>
    </div>
  </div>

  <div class="card-footer">
    <button type="button" class="btn btn-primary" @click="completeLogin">
      Login
    </button>
  </div>
</template>

<script>
import { VueRecaptcha } from 'vue-recaptcha'
// import { getCurrentInstance } from 'vue'

import useAuthenticationComposable from '@/composables/authentication'
// import useGoogleAuthentication from '../../../composables/socials'

import AuthNavigationVue from './AuthNavigation.vue'
import { useScroll } from '@vueuse/core'

export default {
  name: 'LoginView',
  components: {
    AuthNavigationVue,
    VueRecaptcha
  },
  emits: {
      submitted: () => true
  },
  setup() {
    useScroll()
    // const instance = getCurrentInstance()
    // const { load } = useGoogleAuthentication({}, { clientId: '1345' })
    
    const { loginCredentials, responseData, authenticationErrors, login } = useAuthenticationComposable()
    function handleSuccess () {}
    function handleError (response) {
      response
    }
    return {
      // load,
      loginCredentials,
      responseData,
      authenticationErrors,
      handleSuccess,
      handleError,
      login
    }
  },
  // mounted () {
  //   this.load()
  // },
  methods: {
    async completeLogin() {
      this.login()
    }
  }
}
</script>
