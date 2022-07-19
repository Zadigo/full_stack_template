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

        <template #cardFooter>
          <div class="card-footer text-center">
            <button :aria-label="buttonName" type="button" class="btn btn-primary" @click="$emit('start-authentication')">
              {{ buttonName }}
            </button>
          </div>
        </template>
      </base-card>

      <slot name="registrationTexts"></slot>
    </div>
  </div>
</template>

<script>
import { useAuthentication } from '@/store/authentication'
import { storeToRefs } from 'pinia'

export default {
  name: 'BaseRegistrationLayout',
  props: {
    buttonName: {
      type: String,
      default: 'Authenticate'
    }
  },
  emits: {
    'start-authentication': () => true
  },
  setup () {
    const store = useAuthentication()
    const { messages } = storeToRefs(store)
    return {
      messages
    }
  }
}
</script>
