<doc>
  Allows the use to change his passwords
</doc>

<template>
  <base-validation-card button-name="Reset password" @validate-action="update">
    <transition name="alert-transition">
      <div v-if="!isValid" class="alert alert-danger">
        Passwords do not match
      </div>
    </transition>

    <div v-for="field in getFields('password')" :key="field.id" class="form-group mt-2">
      <label v-if="field.name==='password1'" :for="field.name" class="mt-3 mb-2">
        Enter your new password here. It should be different from your old password
        and should contain at least one.
      </label>
      <input :id="field.name" v-model="credentials[field.name]" :autocomplete="field.autocomplete" :placeholder="field.placeholder" :aria-label="field.aria" type="password" class="form-control p-3">
    </div>
  </base-validation-card>
</template>

<script>
import BaseValidationCard from '@/layouts/BaseValidationCard.vue'

import useProfileComposable from '@/composables/profile'

export default {
  name: 'PasswordView',
  components: { BaseValidationCard },
  setup () {
    const { getFields } = useProfileComposable()
    return {
      getFields
    }
  },
  data () {
    return {
      credentials: {}
    }
  },

  computed: {
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
    async update () {
      try {
        // pass
      } catch (error) {
        error
      }
    }
  }
}
</script>

<style scoped>
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
