<template>
  <base-registration-layout @startAction="sendRequest" :buttonName="'Send me a password reset email'">
    <div class="form-group">
      <label class="font-weight-bold" for="email">Email</label>
      <input v-model="email" type="email" class="form-control" id="email" autocomplete="email" placeholder="Email">
    </div>

    <template v-slot:registrationTexts>
      <p class="mt-3 mb-3">Actually, I remember my password <router-link :to="{ name: 'signin' }" class="font-weight-bold">Login here</router-link></p>
    </template>
  </base-registration-layout>
</template>

<script>
import BaseRegistrationLayout from './BaseRegistrationLayout.vue'

import { isNull } from 'lodash'

export default {
  name: 'ForgotPassword',
  title () {
    return 'Forgot password'
  },
  components: {
    BaseRegistrationLayout
  },
  data () {
    return {
      email: null
    }
  },
  beforeRouteEnter (to, from, next) {
    next(vm => {
      if (vm.$store.getters['authenticationModule/isAuthenticated']) {
        return true
      } else {
        return 'profile_passwords'
      }
    })
  },
  computed: {
    hasEmail () {
      return isNull(this.email)
    }
  },
  methods: {
    sendRequest () {
      if (this._validateEmail(this.email)) {
        console.log('Requested email change')
        this.$router.push({ name: 'signin' })
      } else {
        console.error('Email is not valid')
      }
    }
  }
}
</script>
