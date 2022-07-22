<template>
  <div class="card-body">
    <div class="row">
      <div class="col-12">
        <form @submit.prevent>
          <input v-model="loginCredentials.email" type="email" autocomplete="email" class="form-control p-2 my-2">
          <input v-model="loginCredentials.password" type="password" autocomplete="current-password" class="form-control p-2 my-2">

          <!-- Recaptcha -->
          <vue-recaptcha :sitekey="'1234'" :load-recaptcha-script="false" @verify="handleSuccess" @error="handleError" />
        </form>
      </div>

      <div class="col-12">
        <auth-navigation-vue />
      </div>

      <div class="col-12">
        <div id="google-button"></div>
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
import { getCurrentInstance } from 'vue'

import useAuthenticationComposable from '@/composables/authentication'
import useGoogleAuthentication from '../../../composables/socials'

import AuthNavigationVue from './AuthNavigation.vue'

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
    console.info(process.env)
    const instance = getCurrentInstance()
    const { load } = useGoogleAuthentication(instance, { clientId: '707231563844-e5cpkqrlt62gncmj6b84of5sml9lp8g9.apps.googleusercontent.com' })
    
    const { loginCredentials, responseData, authenticationErrors, login } = useAuthenticationComposable()
    function handleSuccess () {}
    function handleError (response) {
      response
    }
    return {
      load,
      // completeSignin,
      // authentifiedUser,

      loginCredentials,
      responseData,
      authenticationErrors,
      handleSuccess,
      handleError,
      login
    }
  },
  mounted () {
    this.load()
  }
}
</script>
