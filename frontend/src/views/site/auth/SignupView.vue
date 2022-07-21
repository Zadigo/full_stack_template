<template>
  <div class="card-body">
    <div class="row">
      <div class="col-12">
        <form @submit.prevent>
          <input v-model="signupCredentials.username" type="text" autocomplete="username" placeholder="Username" class="form-control p-2 my-2">
          <input v-model="signupCredentials.firstname" type="text" autocomplete="family-name" placeholder="Family name" class="form-control p-2 my-2">
          <input v-model="signupCredentials.lastname" type="text" autocomplete="given-name" placeholder="Given name" class="form-control p-2 my-2">
          <input v-model="signupCredentials.email" type="email" autocomplete="email" placeholder="Email" class="form-control p-2 my-2">
          <input v-model="signupCredentials.password1" type="password" autocomplete="new-password" placeholder="Password 1" class="form-control p-2 my-2">
          <input v-model="signupCredentials.password2" type="password" autocomplete="new-password" placeholder="Password 4" class="form-control p-2 my-2">
        </form>
      </div>

      <div class="col-12">
        <auth-navigation-vue />
      </div>
    </div>
  </div>

  <div class="card-footer">
    <button type="button" class="btn btn-primary" @click="completeSignup">
      Signup
    </button>
  </div>
</template>

<script>
import AuthNavigationVue from './AuthNavigation.vue'

import useAuthenticationComposable from '@/composables/authentication'

export default {
  name: 'LoginView',
  components: {
    AuthNavigationVue
  },
  setup () {
    const { signupCredentials, passwordsValid, signup } = useAuthenticationComposable()
    return {
      passwordsValid,
      signupCredentials,
      signup
    }
  },
  methods: {
    completeSignup () {
      this.signup()
    }
  }
}
</script>
