<template>
  <base-registration-layout :button-name="'Sign up'" @startAuthentication="signupUser">

    <div v-for="(field, index) in fields" :key="field.id" :class="{ 'mt-2': index > 0 }" class="form-group">
      <label v-if="field.label !== null" :for="field.name" class="font-weight-bold">
        {{ field.label }}
      </label>

      <input :id="field.name" v-model="credentials[field.name]" :type="field.type" :name="field.name" :placeholder="field.placeholder" :autocomplete="field.autocomplete" class="form-control">
    </div>

    <p>
      By using {{ companyDetails.name }} you agree to
      our <router-link :to="{ name: 'terms_of_use' }" class="font-weight-bold">Terms of service</router-link>
      and our <router-link :to="{ name: 'terms_of_condition' }" class="font-weight-bold">Privacy policy</router-link>
    </p>

    <template v-slot:registrationTexts>
      <p class="mt-3 mb-3">Already using {{ companyDetails.name }}? <router-link :to="{ name: 'signin' }">Login here</router-link>
      </p>
    </template>

  </base-registration-layout>
</template>

<script>
import BaseRegistrationLayout from './BaseRegistrationLayout.vue'

export default {
  name: 'SignupView',
  title () {
    return 'Signup'
  },
  components: { BaseRegistrationLayout },

  data () {
    return {
      fields: [
        { id: 1, name: 'email', type: 'email', autocomplete: 'email', placeholder: 'Email', label: 'Email' },
        { id: 2, name: 'username', type: 'text', autocomplete: 'username', placeholder: 'Username', label: 'Username' },
        { id: 3, name: 'firstname', type: 'text', autocomplete: 'given-name', placeholder: 'Firstname', label: 'Firstname' },
        { id: 4, name: 'lastname', type: 'text', autocomplete: 'family-name', placeholder: 'Lastname', label: 'Lastname' },
        { id: 5, name: 'password1', type: 'password', autocomplete: 'new-password', placeholder: 'Password', label: 'Password' },
        { id: 6, name: 'password2', type: 'password', autocomplete: 'new-password', placeholder: 'Confirm password', label: null },
      ],
      credentials: {
        email: null,
        username: null,
        firstname: null,
        lastname: null,
        password1: null,
        password2: null
      }
    }
  },

  computed: {
    isValid () {
      const { password1, password2 } = this.credentials
      if (password1 !== password2) {
        return false
      }
      return true
    }
  },

  methods: {
    signupUser () {
      this.$api.auth.signup(this.credentials)
      .then(() => {
        this.$router.push({ name: 'signin' })
      })
      .catch((error) => {
        console.error(error)
      })
    }
  }
}
</script>
