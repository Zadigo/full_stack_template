<template>
  <div class="row justify-content-center">
    <div class="col-md-8 col-xl-5">
      <b-card class="mt-5">
        <b-card-body>
          <div class="form-group">
            <label class="font-weight-bold" for="email">Email</label>
            <input v-model="email" type="email" class="form-control" id="email" autocomplete="email" placeholder="Email">
          </div>
        </b-card-body>

        <b-card-footer class="text-center">
          <button @click="sendRequest" :disabled="hasEmail" type="submit" class="btn btn-primary">
            Send me a password reset email
          </button>
        </b-card-footer>
      </b-card>
    </div>

    <div class="col-md-12 col-xl-12">
      <p class="mt-3 mb-3">Actually, I remember my password <router-link :to="{ name: 'signin' }" class="font-weight-bold">Login here</router-link></p>
    </div>
  </div>
</template>

<script>
import { isNull } from 'lodash'

export default {
  name: 'ForgotPassword',
  title () {
    return 'Forgot password'
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
