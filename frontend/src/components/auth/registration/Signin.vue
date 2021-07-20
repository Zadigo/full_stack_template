<template>
  <base-layout @startAuthentication="loginUser" :buttonName="'Sign in to your account'">
    <div class="form-group">
      <label class="font-weight-bold" for="email">Email</label>
      <input v-model="credentials['email']" type="email" class="form-control" id="email" autocomplete="email" placeholder="Email">
    </div>
    
    <div class="form-group mt-3">
      <label class="font-weight-bold" for="email">Password</label>
      <input v-model="credentials['password']" type="password" class="form-control" id="password" autocomplete="current-password" placeholder="Password">
    </div>

    <template v-slot:registrationTexts>
      <div class="col-md-12 col-xl-12 text-white">
        <p class="mt-3">Don't have an account? <router-link :to="{ name: 'signup' }" class="font-weight-bold text-muted">Get yours now</router-link></p>
        <p class="mt-3 mb-3">Forgot your password? <router-link :to="{ name: 'forgot' }" class="font-weight-bold text-muted">Send yourself a new one</router-link></p>
      </div>
    </template>
  </base-layout>
</template>

<script>
import BaseLayout from './BaseLayout.vue'

import { mapActions } from 'vuex'
// import formFields from '../../../data/fields.json'

export default {
  name: 'Signin',
  title () {
    return 'Signin'
  },
  components: {
    BaseLayout
  },

  data() {
    return {
      credentials: {
        email: null,
        username: null,
        password: null
      },
      // fields: formFields.authentication.signin,
      rememberMe: false
    }
  },

  // beforeRouteLeave (to, from, next) {
  //   next()
  // },

  methods: {
    ...mapActions('authenticationModule', [
      'login'
    ]),
    loginUser () {
      // this.$store.dispatch('authenticationModule/login', this.credentials)
      this.login(this.credentials)
    },

    setCredentials(payload) {
      console.log(payload)
      // this.credentials[payload[0]] = payload[1]
    }
  }
}
</script>
