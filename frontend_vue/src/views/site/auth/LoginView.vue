<template>
  <div class="card-body">
    <div class="row">
      <div class="col-12">
        <form @submit.prevent>
          <input v-model="loginCredentials.email" type="email" autocomplete="email" class="form-control p-2 my-2">
          <input v-model="loginCredentials.password" type="password" autocomplete="current-password" class="form-control p-2 my-2">

          <!-- Recaptcha -->
          <!-- <vue-recaptcha :sitekey="'1234'" :load-recaptcha-script="false" @verify="handleSuccess" @error="handleError" /> -->
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
// import { VueRecaptcha } from 'vue-recaptcha'

import useAuthenticationComposable from '@/composables/authentication'

import AuthNavigationVue from './AuthNavigation.vue'
import { useAuthentication } from '@/store/authentication'

export default {
  name: 'LoginView',
  components: {
    AuthNavigationVue,
    // VueRecaptcha
  },
  emits: {
      submitted: () => true
  },
  setup() {
    const store = useAuthentication()
    const { loginCredentials, performLogin } = useAuthenticationComposable()

    // function handleSuccess () {}
    // function handleError (response) {
    //   response
    // }
    return {
      store,
      loginCredentials,
      // authenticationErrors,
      // handleSuccess,
      // handleError,
      performLogin
    }
  },
  methods: {
    completeLogin () {
      this.performLogin((response) => {
        this.store.loginUser(response.data)
        this.$session.create('auth', response.data)
        this.$router.push({ name: 'home_view' })
      }, (error) => {
        console.error(error)
      })
    }
  }
}
</script>
