<template>
  <div class="row justify-content-center">
    <div class="col-xl-5 col-md-8">
      <b-card class="mt-5">
        <div v-for="(field, index) in fields" :key="field.id" :class="{ 'mt-2': index > 0 }" class="form-group">
          <label v-if="field.label !== null" :for="field.name" class="font-weight-bold">
            {{ field.label }}
            </label>
          <input v-model="credentials[field.name]" :type="field.type" :name="field.name" :id="field.name" :placeholder="field.placeholder" :autocomplete="field.autocomplete" class="form-control">
        </div>
        
        <p>By using {{ companyDetails.name }} you agree to our <router-link :to="{ name: 'terms_of_use' }" class="font-weight-bold">Terms of service</router-link> and our <router-link :to="{ name: 'terms_of_condition' }" class="font-weight-bold">Privacy policy</router-link></p>

        <p class="mt-3 mb-3">Already using {{ companyDetails.name }}? <router-link :to="{ name: 'signin' }">Login here</router-link></p>

        <!-- Submit button -->
        <div class="form-group text-center">
          <button @click.prevent="signupUser" :disabled="!isValid" type="submit" class="btn btn-primary">
            Sign up
          </button>
        </div>
      </b-card>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Signup',
  title () {
    return 'Signup'
  },
  data () {
    return {
      fields: [
        { id: 1, name: 'email', type: 'email', autocomplete: 'email', placeholder: 'Email', label: 'Email' },
        { id: 2, name: 'username', type: 'text', autocomplete: 'username', placeholder: 'Username', label: 'Username' },
        { id: 3, name: 'first_name', type: 'text', autocomplete: 'given-name', placeholder: 'Firstname', label: 'Firstname' },
        { id: 4, name: 'last_name', type: 'text', autocomplete: 'family-name', placeholder: 'Lastname', label: 'Lastname' },
        { id: 5, name: 'password1', type: 'password', autocomplete: 'new-password', placeholder: 'Password', label: 'Password' },
        { id: 6, name: 'password2', type: 'password', autocomplete: 'new-password', placeholder: 'Confirm password', label: null },
      ],
      credentials: {}
    }
  },
  computed: {
    isValid () {
      let { password1, password2 } = this.credentials
      if (password1 !== password2) {
        return false
      }
      return true
    }
  },
  methods: {
    signupUser () {
      this.$store.dispatch('authenticationModule/signUp', this.credentials)
    }
  }
}
</script>
