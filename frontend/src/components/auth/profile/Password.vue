<template>
  <div class="card">
    <div class="card-body">
      <transition name="alert-transition">
        <div v-if="!isValid" class="alert alert-danger">
          Passwords do not match
        </div>
      </transition>
      
      <div v-for="field in fields" :key="field.id" class="form-group mt-2">
        <label v-if="field.name==='password1'" :for="field.name" class="mt-3 mb-2">Enter your new password here. It should be something and another thing and that.</label>
        <input v-model="credentials[field.name]" :id="field.name" :autocomplete='field.autocomplete' :placeholder="field.placeholder" :aria-label="field.aria" type="password" class="form-control">
      </div>
    </div>

    <div class="card-footer bg-white text-right">
      <button @click="updatePassword" class="btn btn-primary">
        <i class="fa fa-check-mark"></i>
        Validate
      </button>
    </div>
  </div>
</template>

<script>
export default {
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
    isValid () {
      let { password1, password2 } = this.credentials
      if (password2 !== undefined && password1 !== password2) {
        return false
      } else {
        return true
      }
    }
  },
  methods: {
    updatePassword () {
      this.credentials = {}
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
