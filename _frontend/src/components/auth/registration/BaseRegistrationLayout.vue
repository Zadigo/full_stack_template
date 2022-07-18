<template>
  <div class="row justify-content-center">
    <div class="col-xl-5 col-md-8">
      
      <base-card class="mt-5">
        <transition-group name="general-transition">
          <div v-for="message in messages" :key="message.id" :class="message.type" class="alert alert-danger" role="alert">
            {{ message.content }}
          </div>
        </transition-group>

        <slot></slot>

        <template v-slot:cardFooter class="card-footer text-center">
          <button @click="$emit('startAuthentication')" :aria-label="buttonName" class="btn btn-primary" role="button">
            {{ buttonName }}
          </button>
        </template>
      </base-card>

      <slot name="registrationTexts"></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BaseRegistrationLayout',
  props: {
    buttonName: {
      type: String,
      default: 'Authenticate'
    }
  },

  computed: {
    messages() {
      return this.$store.getters['getMessagesFor']('auth')
    }
  }
}
</script>
