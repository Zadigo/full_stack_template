<template>
  <base-validation-card :button-name="'Reset password'" @validateAction="updatePassword">

    <transition name="alert-transition">
      <div v-if="!isValid" class="alert alert-danger">
        Passwords do not match
      </div>
    </transition>

    <div v-for="field in fields" :key="field.id" class="form-group mt-2">
      <label v-if="field.name==='password1'" :for="field.name" class="mt-3 mb-2">
        Enter your new password here. It should be different from your old password
        and should contain at least one.
      </label>
      <input :id="field.name" v-model="credentials[field.name]" :autocomplete="field.autocomplete" :placeholder="field.placeholder" :aria-label="field.aria" type="password" class="form-control">
    </div>

  </base-validation-card>
</template>

<script>
import { mapState } from 'pinia'
import BaseValidationCard from './BaseValidationCard.vue'
export default {
  components: { BaseValidationCard },
  data () {
    return {
      credentials: {},
      fields: [
        { id: 1, name: 'old_password', aria: 'Current password', autocomplete: 'current-password', placeholder: 'Current password' },
        { id: 2, name: 'password1', aria: 'New password', autocomplete: 'new-password', placeholder: 'New password' },
        { id: 3, name: 'password2', aria: 'New password', autocomplete: 'new-password', placeholder: 'New password' },
      ]
    }
  },

  computed: {
    ...mapState('profileModule', {
      userId: (state) => {
        return state.userDetails.id
      }
    }),
    
    isValid () {
      const { password1, password2 } = this.credentials
      if (password2 && password1 !== password2) {
        return false
      } else {
        return true
      }
    }
  },
  
  methods: {
    updatePassword () {
      this.$api.profile.changePassword(this.credentials)
      .then(() => {

      })
      .catch(() => {

      })
      // axios({
      //   method: 'post',
      //   url: 'http://127.0.0.1:8000/api/v1/change-password',
      //   data: this.credentials,
      //   headers: {
      //     'Content-Type': 'application/json',
      //     'Authorization': `Token ${this.$store.getters['authenticationModule/getToken']}`
      //   },
      //   withCredentials: true
      // })
      // .then((response) => {
      //   if (response.status === 200) {
      //     this.credentials = {}
      //   } else {
      //     console.log('Could not reset password')
      //   }
      // })
      // .error((error) => {
      //   console.log(error)
      // })
    }
  }
}
</script>

<style>
.alert-transition-enter-active,
.alert-transition-leave-active {
  transition: all .5s ease;
}

.alert-transition-enter,
.alert-transition-leave-to {
  opacity: 0;
  transform: scale(.95, .95);
}

.alert-transition-enter-to,
.alert-transition-leave {
  opacity: 1;
  transform: scale(1, 1);
}
</style>
