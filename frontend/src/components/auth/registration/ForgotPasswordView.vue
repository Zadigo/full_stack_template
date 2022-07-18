<template>
  <base-registration-layout :button-name="'Send me a password reset email'" @startAuthentication="sendRequest">
    <div class="form-group">
      <label class="font-weight-bold" for="email">Email</label>
      <input id="email" v-model="email" type="email" class="form-control" autocomplete="email" placeholder="Email">
    </div>

    <template v-slot:registrationTexts>
      <p class="mt-3 mb-3">
        Actually, I remember my password <router-link :to="{ name: 'signin' }" class="font-weight-bold">Login here</router-link>
      </p>
    </template>
  </base-registration-layout>
</template>

<script>
import { isNull } from 'lodash'

import BaseRegistrationLayout from './BaseRegistrationLayout.vue'

export default {
  name: 'ForgotPasswordView',
  title () {
    return 'Forgot password'
  },
  components: {
    BaseRegistrationLayout
  },
  beforeRouteEnter (to, from, next) {
    // If the user is authenticated then return the
    // page on the profile where an authenticated user
    // can modify there password
    next(vm => {
      if (vm.$store.getters['authenticationModule/isAuthenticated']) {
        return true
      } else {
        return 'profile_passwords'
      }
    })
  },
  data () {
    return {
      email: null
    }
  },
  computed: {
    hasEmail () {
      return isNull(this.email)
    }
  },
  methods: {
    sendRequest () {
      this.$api.auth.forgotPassword(this.email)
      .then(() => {
        // pass
      })
      .catch((error) => {
        this.$store.dispatch('newDangerMessage', {
          app: 'auth',
          content: error.response.data,
          title: null
        })
      })
    }
  }
}
</script>
