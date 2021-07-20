<template>
  <div class="row justify-content-center">
    <div class="col-xl-5 col-md-8">
      <b-card class="mt-5">
        <transition-group name="general-transition">
          <div v-for="message in messages" :key="message.id" :class="message.type" class="alert alert-danger" role="alert">
            {{ message.content }}
          </div>
        </transition-group>

        <div class="form-group">
          <label class="font-weight-bold" for="email">Email</label>
          <input v-model="credentials['email']" type="email" class="form-control" id="email" autocomplete="email" placeholder="Email">
        </div>
        
        <div class="form-group mt-3">
          <label class="font-weight-bold" for="email">Password</label>
          <input v-model="credentials['password']" type="password" class="form-control" id="password" autocomplete="current-password" placeholder="Password">
        </div>

        <template class="text-center" #footer>
          <button @click="loginUser" class="btn btn-primary">
            Sign in to your account
          </button>
        </template>
      </b-card>

      <div class="col-md-12 col-xl-12 text-white">
        <p class="mt-3">Don't have an account? <router-link :to="{ name: 'signup' }" class="font-weight-bold text-muted">Get yours now</router-link></p>
        <p class="mt-3 mb-3">Forgot your password? <router-link :to="{ name: 'forgot' }" class="font-weight-bold text-muted">Send yourself a new one</router-link></p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Signin',
  title () {
    return 'Signin'
  },

  data() {
    return {
      credentials: {
        email: null,
        username: null,
        password: null
      },
      rememberMe: false
    }
  },

  // beforeRouteLeave (to, from, next) {
  //   next()
  // },

  computed: {
    messages() {
      return this.$store.getters['getMessagesFor']('auth')
    }
  },
  
  methods: {
    loginUser () {
      this.$store.dispatch('authenticationModule/login', this.credentials)
    }
  }
}
</script>
