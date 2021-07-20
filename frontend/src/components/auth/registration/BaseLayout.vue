<template>
  <div class="row justify-content-center">
    <div class="col-xl-5 col-md-8">
      <b-card class="mt-5">
        <transition-group name="general-transition">
          <div v-for="message in messages" :key="message.id" :class="message.type" class="alert alert-danger" role="alert">
            {{ message.content }}
          </div>
        </transition-group>

        <slot></slot>

        <template class="text-center" #footer>
          <button @click="$emit('startAuthentication')" class="btn btn-primary">
            {{ buttonName }}
          </button>
        </template>
      </b-card>

      <slot name="registrationTexts"></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BaseLayout',
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
